# W6 — Leadership Deck 30 ngày (CRAFT)

> Input: W2-W3-W4. Adapt từ `v2.0-workflow-mindset/Output_B7/06-leadership-deck.md`, hiệu chỉnh theo chi tiết thật của `../../lab.md`/`checkpoint-bt1..4.md` và đánh giá trung thực ở `03-hardening.md`.
>
> **Lưu ý minh bạch (đọc trước khi dùng deck này):** Slide 8 dưới đây bắt buộc lồng đề xuất đào tạo K1 AI Automation của Alobase — đây là quy tắc của skill sinh tài liệu (`vibe-workflow-design-orchestrator`), không phải phân tích ROI trung lập tuyệt đối. Dùng deck này trong lớp như **ví dụ mẫu** về cách trình bày pitch cho lãnh đạo; nếu dùng thật ở nơi khác, nên tách rời phần đào tạo khỏi phần phân tích kỹ thuật. Số liệu ở Slide 4 là **kỳ vọng, chưa phải số đã đo** — package này chưa có lần chạy pilot thật ngoài giờ lab.

---

# Đề xuất Triển khai AI Automation: Cỗ máy dựng video ngắn — Tham mưu 30 ngày

---

## Slide 1: Cover

**Đề xuất triển khai AI Automation: Cỗ máy dựng video ngắn**
Tham mưu 30 ngày — Bộ phận Marketing

- Áp dụng cho: video ngắn TikTok/Reels 45–60 giây, dựng từ kịch bản đã duyệt (nối tiếp Content Engine Buổi 6)
- Người trình bày: [Tên] — Trưởng bộ phận Marketing

![Before/After](05-workflow-before-after.png)
> 🖼️ *Visual:* dùng làm nền mờ khi trình chiếu thật — xem prompt gốc ở `05-image-prompt.md`.

---

## Slide 2: Vấn đề — có kịch bản, nhưng không dựng được video

- Sau khi đã có cỗ máy nội dung (Buổi 6), **kịch bản không còn thiếu — thiếu là video**. Không có người quay chuyên trách, không có diễn viên, không được dùng hình ảnh học viên/trẻ em thật.
- **Đốt tiền mù:** cách làm tự phát hiện nay là gõ thẳng prompt vào công cụ sinh video rồi xem ra gì. Retry 4–6 lần mỗi cảnh là chuyện thường, không ai đếm đã tốn bao nhiêu.
- **Ghép lại không ra một video:** mỗi cảnh sinh ra một nhân vật, một bối cảnh, một tông màu khác nhau — vì bỏ qua hẳn khâu storyboard trong quy trình gốc (`../../luong-nghiep-vu.md` bước 2).
- **Phát hiện lỗi quá muộn:** lời thoại đọc không kịp trong cảnh ngắn chỉ lộ ra khi đã dựng xong hết.
- **Kết quả thật:** phần lớn video bỏ dở giữa chừng.

> *Thuật ngữ:* **Credit** = đơn vị tính tiền của công cụ sinh ảnh/video. Dựng một clip tốn nhiều credit hơn sinh một ảnh rất nhiều lần.

---

## Slide 3: Quy trình mới — xem trước bằng ảnh, rồi mới tiêu tiền

| Lớp | Làm gì | Ai làm |
|---|---|---|
| 1. Nền móng | Hai đường đầu vào (B6_APPROVED/MANUAL) về cùng một cấu trúc; ID nối xuyên suốt | Hệ thống |
| 2. Chia cảnh | Kịch bản → 6–9 cảnh có thời lượng; style bible giữ nhân vật/bối cảnh thống nhất | AI |
| 3. Storyboard | Sinh ảnh cho từng cảnh — xem trước cả video bằng ảnh tĩnh | AI |
| 4. Duyệt & dựng | **Con người duyệt từng ảnh**, rồi hệ thống mới dựng clip có tiếng | **Marketing** |

**Thay đổi cốt lõi — một câu:** *Trước đây tiêu tiền rồi mới biết sai. Bây giờ nhìn thấy sai từ lúc còn là ảnh.*

![System architecture](05-workflow-system-architecture.png)
> 🖼️ *Visual:* sơ đồ node chính xác từng bước — dán `04-mermaid.mmd` vào mermaid.live.
> *Thuật ngữ:* **Storyboard** = bộ ảnh phác từng cảnh, giống truyện tranh, để hình dung video trước khi dựng.

---

## Slide 4: Lợi ích kỳ vọng (chưa phải số đã đo)

| Chỉ số | Trước (as-is) | Sau (kỳ vọng, to-be) |
|---|---|---|
| Video hoàn thành/tuần | ~0–1 (phần lớn bỏ dở) | **2–3 video** — `[cần đo]` |
| Thời gian từ kịch bản tới video | Không hoàn thành được | **~2 giờ/video** — `[cần đo sau 3 video đầu]` |
| Credit lãng phí | Không ai đếm | Giảm nhờ duyệt ảnh trước + canary 2 scene — `[cần đo]` |
| Số lần dựng lại vì lệch phong cách | 4–6 lần/cảnh | Gần 0 nhờ style bible dùng chung |
| Truy vết clip nào từ đâu | Không có | 100% theo thiết kế — ID nối `project→scene→frame→clip` |

> ⚠️ Mọi số có nhãn `[cần đo]` là ước tính, chưa pilot thật. Sổ chi phí trong 30 ngày đầu là để có con số thật cho lần duyệt ngân sách sau.

---

## Slide 5: Vì sao lãnh đạo có thể yên tâm — đánh giá trung thực

- **Cổng cứng chặn chi phí:** ảnh chưa được người duyệt thì không có đường nào dựng thành clip. Cộng canary 2 scene trước khi chạy cả loạt, báo trước số lượt dự kiến mỗi lần chạy.
- **Một clip lỗi không làm hỏng cả buổi:** mỗi clip có trạng thái và số lần thử riêng; cảnh đã xong giữ nguyên.
- **Nhật ký & sổ chi phí theo thiết kế:** có trường `runtime_evidence` bắt buộc — không có bằng chứng thì không được ghi "chạy thành công".
- **Con người quyết định (HITL):** người duyệt từng ảnh và nghe từng clip. AI không được tự duyệt.
- **Chưa test thật (nói thẳng, xem `03-hardening.md`):** package này mới dừng ở thiết kế + checklist thủ công tại lớp; chưa có lần chạy pilot thật ngoài giờ để xác nhận 6/6 thuộc tính tin cậy — tự đánh giá hiện tại là 2 đạt / 4 một phần.

> 🔒 **Ba cam kết cứng:** không clone mặt/giọng người thật khi chưa có văn bản đồng ý · không dùng logo/nhạc/hình thiếu quyền · không bịa số liệu hay cam kết hiệu suất trong lời thoại.

---

## Slide 6: Lộ trình 30 ngày — đóng gap trước khi coi là production-ready

| Tuần | Mục tiêu | Kết quả bàn giao |
|---|---|---|
| Tuần 1 | Nền móng — dựng cấu trúc dữ liệu, style bible, chia thử 1 kịch bản thành 6–9 cảnh, validate 3 schema trên instance thật | 3 schema + 3 mẫu PASS; 1 kịch bản đã chia cảnh |
| Tuần 2 | Storyboard — sinh ảnh toàn bộ cảnh, dựng app duyệt ảnh, chạy canary 2 scene trên instance thật | Bộ ảnh storyboard đầy đủ; app duyệt từng khung hình; kết quả canary thật |
| Tuần 3 | Chạy thử có kiểm soát — batch 6–9 cảnh sau khi canary PASS, ghi số credit thật | 1 video hoàn chỉnh + `media-run-log.json` thật + số credit thật đã tốn |
| Tuần 4 | Vận hành + đóng gói — chạy thêm 2–3 video, chốt `engine-spec.json`, viết lại `03-hardening.md` với bằng chứng chạy thật | Báo cáo 30 ngày: sản lượng, credit/video, lỗi hay gặp |

**Ngoài phạm vi 30 ngày này** (đã cắt khỏi to-be ở `02-as-is-tobe.md`): ghép clip + chèn chữ + đăng tự động (bước 6), đo lường hiệu quả sau đăng (bước 7) — chỉ xem xét sau khi Tuần 4 đạt và có số credit thật.

---

## Slide 7: Rủi ro & cách giảm thiểu

| # | Rủi ro | Cách xử lý |
|---|---|---|
| 1 | Chi phí credit vượt dự tính | Duyệt ảnh trước (rẻ hơn clip nhiều lần) + canary 2 scene + báo trước số lượt mỗi lần chạy + sổ chi phí theo cảnh. Vượt dự kiến ở Tuần 3 → dừng ở quy mô hiện tại. |
| 2 | Rủi ro quyền hình ảnh và giọng nói | Cấm tuyệt đối clone mặt/giọng người thật khi chưa có văn bản đồng ý; không logo bên thứ ba; nhạc nền phải có license. Kiểm ở khâu duyệt ảnh và duyệt clip. |
| 3 | Báo cáo "đã chạy" trong khi mới có giao diện | `runtime_evidence` bắt buộc trong run log; thiếu bằng chứng → trạng thái không được ghi `SUCCESS`. Đây là chỗ dễ tự lừa mình nhất khi làm với AI (xem `03-hardening.md` §3). |

---

## Slide 8: Nguồn lực triển khai & phát triển năng lực nội bộ

- **Nhân sự dự án:** 2 nhân viên content hiện tại (không tuyển thêm người quay dựng) + 1 người duyệt ảnh/clip (~30 phút/video).
- **Công cụ:** n8n hoặc Coding Agent (tự vận hành nội bộ) · công cụ sinh ảnh và sinh video có tiếng · công cụ dựng để ghép/chèn chữ.
- **Ngân sách công nghệ:** credit sinh ảnh + video — mức cụ thể `[cần đo]` sau Tuần 3, chưa có số đo.
- **Đề xuất phát triển năng lực nội bộ:** *(phần dưới đây là ví dụ mẫu trong tài liệu giảng dạy về cách lồng đề xuất đào tạo vào một bài pitch lãnh đạo — xem lưu ý minh bạch đầu file)*
  - Cử nhân sự tham gia khoá học AI Automation K1 do Alobase tổ chức để học cách thiết kế cổng chặn chi phí, trạng thái từng clip, và kỷ luật báo cáo runtime — không chỉ "gọi được công cụ sinh video".
  - Tầm nhìn dài hạn: `engine-spec.json` độc lập công cụ — công cụ sinh video sẽ còn đổi liên tục, bản mô tả engine thì không.

---

## Slide 9: Quyết định cần phê duyệt

1. **Phê duyệt pilot 30 ngày:** theo lộ trình 4 tuần ở Slide 6, mục tiêu 1 video hoàn chỉnh trong Tuần 3 kèm số liệu chi phí thật.
2. **Phê duyệt hạn mức credit** cho 30 ngày và **chỉ định người duyệt ảnh/clip** — không có người này, cổng chặn chi phí không hoạt động.
3. **Duyệt thời gian đóng gap kỹ thuật:** cho phép dành Tuần 1-2 để validate 3 schema + canary trên instance thật, trước khi coi hệ thống là production-ready.
4. **Quyết định riêng, không gộp vào pilot này:** có mở rộng sang ghép/chèn chữ/đăng tự động và đo lường hiệu quả (bước 6/7 đã cắt khỏi phạm vi) ở giai đoạn kế tiếp hay không — chỉ xem xét sau khi Tuần 4 đạt.

> 🔒 **Cam kết đi kèm:** hệ thống không tự đăng video. Mọi video ra khỏi quy trình đều có một người thật đã xem ảnh, nghe clip và ký duyệt.
