# Prompt TH4B — Build app hỗ trợ (frontend gọi thẳng webhook n8n)

> App là một file HTML tĩnh, mở trực tiếp bằng double-click hoặc `file://` là chạy — không cần dev
> server, không thư viện ngoài (không CDN). Toàn bộ logic nghiệp vụ nằm ở n8n (TH4A); app chỉ gọi
> webhook và hiển thị kết quả.

```text
BỐI CẢNH:
Content/Video Engine đã được đặc tả và validate ở TH4A, workflow n8n đã activate với các webhook
POST: `/b7/plan`, `/b7/generate-image`, `/b7/generate-clip`, `/b7/assemble`. Hãy build một app hỗ
trợ để vận hành trực quan. App là lớp hỗ trợ, phải bảo toàn engine-spec và data contract — không tự
đổi node, schema, số scene hay approval gate.

INPUT PHẢI ĐỌC:
- engine-spec.json và engine-spec.schema.json
- Ba schema nghiệp vụ
- Ba artifact mẫu
- media-run-log.json
- Bốn webhook URL từ TH4A (dán vào phần Cấu hình của app)

YÊU CẦU:
1. Một file HTML/CSS/JS duy nhất, không framework, không CDN. Có phần Cấu hình ở đầu trang để dán
   4 webhook URL — phần này đứng NGOÀI wizard (cấu hình một lần, không phải một bước).
2. Giao diện là **wizard step-by-step 4 bước**, không phải một trang dài cuộn hết mọi thứ: một
   thanh chỉ số bước ở trên (1-2-3-4, đánh dấu bước đã xong/đang làm/chưa tới); mỗi lúc chỉ hiện
   ĐÚNG MỘT bước; mỗi bước có nút "Quay lại" (trừ bước 1) và một nút hành động chính tiến sang bước
   sau. Quay lại chỉ để XEM lại bước trước, không tự động xoá dữ liệu; chỉ khi người dùng chủ động
   bấm lại nút sinh-kế-hoạch sau khi đã có tiến độ ở bước sau mới cảnh báo (confirm) vì việc đó sẽ
   ghi đè toàn bộ tiến độ.
3. Bước 1 — Nhập kịch bản: CHỈ có ô "Tiêu đề" và textarea dán kịch bản HOOK/PROBLEM/SOLUTION/CTA
   (viết tay). KHÔNG có lựa chọn nguồn B6_APPROVED/MANUAL, không có ô project_id/platform/aspect_ratio
   cho người dùng chỉnh — `platform` cố định "TIKTOK", `aspect_ratio` cố định "9:16" (cả khoá chỉ dạy
   TikTok dọc), `project_id` tự sinh từ Tiêu đề (slugify + hậu tố thời gian), `source_mode` luôn gửi
   cố định "MANUAL" trong payload gọi `/b7/plan`. B7 không tự đọc trạng thái Approved của Buổi 6 —
   việc đó đã xử lý đúng chỗ ở prompt TH1/TH2 (Coding Agent), không phải trách nhiệm của app này; nếu
   học viên có kịch bản đã duyệt ở B6, chỉ cần copy nội dung vào đúng ô textarea.
4. Nút chính ở bước 1 gọi `/b7/plan` → nhận về video_script + storyboard (có voice_bible) +
   video_plan (mỗi clip có dialogue/video_prompt/negative_prompt/duration_seconds), rồi tự chuyển
   sang bước 2.
5. Bước 2 — Script Review: liệt kê từng clip với dialogue, video_prompt, negative_prompt và
   voice_bible dùng chung; có nút "Duyệt kịch bản — Tiếp theo". Trước khi bấm duyệt, mọi hành động
   sinh ảnh/video ở các bước sau phải bị khoá (disable) ở UI. `/b7/generate-image` phải được n8n tự
   chặn (trả lỗi) nếu gọi khi kịch bản chưa duyệt — đây là cổng chặn kép: app khoá nút, n8n khoá luôn
   ở backend, không chỉ tin JS phía client. Bấm nút này chuyển sang bước 3.
6. Bước 3 — Ảnh & Clip: lưới card, mỗi card một scene (6–9 card). Mỗi card có nút "Sinh ảnh" gọi
   `/b7/generate-image`, hiện ảnh trả về, rồi nút Duyệt/Cần sửa cho card đó (trạng thái lưu ở client,
   không cần webhook riêng). Chỉ card đã Duyệt mới hiện được nút "Sinh clip", gọi `/b7/generate-clip`
   với đúng video_prompt/negative_prompt/duration_seconds của clip đó lấy từ video_plan (không tự
   đổi); `/b7/generate-clip` phải bị n8n chặn nếu frame chưa duyệt. Nút "Tiếp theo — Ghép video" ở
   cuối bước 3 chỉ bật khi ĐỦ clip APPROVED cho mọi scene cần dùng. API trả asset thành công chỉ đưa
   clip sang NEEDS_REVIEW, không tự coi là đã duyệt.
7. Trạng thái busy/lỗi của TỪNG card ở bước 3 phải lưu trong một object state riêng theo id (vd
   `state.busyFrames[frameId]`, `state.errFrames[frameId]`), không lưu bằng cách gắn class CSS trực
   tiếp lên node DOM. Hàm render danh sách card phải build lại toàn bộ lưới TỪ state mỗi lần gọi —
   nghĩa là khi một card khác được thao tác (và gọi lại hàm render), card đang chạy vẫn phải tiếp tục
   hiện đúng spinner/khoá nút của nó vì trạng thái đọc lại từ state, không bị mất khi DOM bị dựng lại.
   Đây là lỗi thật đã gặp: nếu chỉ toggle class DOM, lần render tiếp theo do card khác kích hoạt sẽ
   xoá mất spinner của card đang chạy, khiến người dùng tưởng nó dừng và bấm sinh lại — sinh trùng.
8. Trước bước ghép, mỗi clip có khu vực Clip Review riêng: phát video có tiếng, hiển thị scene/frame/
   clip ID và cho chọn `APPROVED`, `NEEDS_RETRY`, `REJECTED`. Retry giữ ID, tăng retry_count và lưu
   reviewer note; clip rejected không được gửi sang assemble.
9. Bước 4 — Ghép video: nút "Ghép video cuối" gọi `/b7/assemble` với danh sách clip_urls theo đúng
   thứ tự scene, hiện video/link kết quả.
10. Preview ảnh và video ngay trong trang; audio bật mặc định, có nút mute ở trình phát — không tắt
   audio bằng cách sửa request lên model.
11. Các trạng thái IDLE/RUNNING/SUCCESS/ERROR trên mỗi card phải phản ánh đúng response thật của
    webhook, không tự đặt SUCCESS khi chưa nhận được asset ref thật.
12. Không hardcode API key nào trong app — mọi API key nằm ở credential trong n8n, app chỉ giữ 4
    webhook URL.
13. Chạy test 2 scene thật qua UI (không phải gọi thẳng webhook bằng script), đi đúng 4 bước của
    wizard từ đầu tới cuối. Báo bằng chứng: ảnh chụp màn hình từng bước, console không có lỗi JS, và
    chuỗi reference input → script_approved → frame ref → clip ref. Nếu không chạy được, ghi lỗi
    thật và bước sửa ngắn, cụ thể — không tuyên bố hoàn thành chỉ vì giao diện render đẹp.

TIÊU CHUẨN BÀN GIAO:
- File app + master prompt đã dùng.
- Kết quả runtime thật (ảnh chụp màn hình 2 scene) và known limitations.
- Không tuyên bố hoàn thành nếu chưa bấm thật qua UI.
```
