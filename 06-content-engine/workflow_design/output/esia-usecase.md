# ESIA Use-case — Content Engine (B6)

> Use-case cốt lõi cho workflow_design package. Đây là nền để Track A (build đúng use-case) và Track B (HV customize) móc vào.

## Use-case chính (GV demo + Track A)

**"Content Engine — Sunrise Kids"** — trung tâm Anh ngữ trẻ em (6-11 tuổi), 2 cơ sở (Gò Vấp, Tân Bình), marketing 1 người kiêm nhiệm. Chuỗi 4 bài tập TH1→TH2→TH3→TH4 (`../../lab.md`), mỗi TH output = input TH sau, chạy trong cùng 1 phiên chat để Agent giữ context.

- File nguồn: `../../templates/product-brief-sunrise-kids.md`, `chan-dung-khach-hang.md`, `brand-voice.md`, `channel-format-spec.md` (synthetic, zero PII thật).
- Kỳ vọng Agent: `content-angles.json` → `content-draft.json` → `content-assets.json` kế thừa đúng `brief_id`/`source_angle_id`/`chan_dung` xuyên suốt, đủ schema PASS; TH4 đóng gói thành n8n 4 lớp + App duyệt chạy end-to-end, dừng ở `Approved`.

## Use-case nghiệm thu — KHÔNG có holdout riêng (khác B4, ghi rõ để không giả vờ)

Buổi 4 (Contract Review) có 1 hợp đồng holdout riêng (`contract-holdout.docx`) để GV nghiệm thu độc lập với dữ liệu HV chưa từng thấy. **Buổi 6 không có cơ chế này** — theo `checkpoint-bt4.md` mục "Nghiệm thu cuối buổi", GV chạy lại chính engine trên **cùng brief Sunrise Kids** đã dùng suốt buổi, kiểm workflow sinh nội dung mới + app hiện đúng + Approved ghi vào `Content_Queue`/`Publish_Log`. Đây là khác biệt thật giữa 2 buổi, không phải thiếu sót của package này.

## Use-case Track B (HV customize — bài tập về nhà)

Theo `../../prompts/custom-input-prompt.md`: HV tự viết `product-brief.md` + `chan-dung.md` + `brand-voice.md` cho sản phẩm/dịch vụ thật của mình (AI không biết doanh nghiệp HV, phần này bắt buộc người viết). Chạy lại engine, tạo ≥3 bài đã duyệt, ghi lại chỗ AI làm tốt/chỗ phải sửa tay nhiều nhất.

**Nguyên tắc (tương đương BR-06 của B4):** cấu trúc engine (3 JSON schema + 4 lớp n8n + App duyệt dừng ở Approved) **KHÔNG đổi** — chỉ đổi nguyên liệu đầu vào (brief/chân dung/brand-voice) và danh sách "8 điều cấm" theo ngành. Ba chỗ tuyệt đối không đụng khi customize (`custom-input-prompt.md` "Ba chỗ đừng đụng"):

1. Ba JSON Schema — hợp đồng giữa Coding Agent, n8n và app; sửa 1 bên phải sửa theo cả 3.
2. Status dừng ở `Approved` — cố ý không có `Published`.
3. Luật không bịa số liệu — thiếu thì `[cần bổ sung]`.

Track B mở rộng thêm 2 hướng tùy nhu cầu: đổi kênh đăng (`custom-input-prompt.md` Prompt 2 — LinkedIn/Blog SEO/Zalo OA/Email/Instagram, cần sửa đồng bộ schema+prompt lớp 2+app) hoặc chạy nhiều brief cùng lúc (Prompt 3 — hiện chưa làm, xem gap ở `03-hardening.md` mục "scalable = thiếu").

## 8 điều cấm — checklist brand-voice (rút gọn, tương đương "8 điều khoản bắt buộc" của B4)

Từ `../../templates/brand-voice.md` — chặn cứng, vi phạm bất kỳ mục nào thì trả về sửa, không duyệt:

1. Cam kết kết quả ("giỏi sau 3 tháng", "chắc chắn nói được")
2. Nội dung luyện thi/chứng chỉ/điểm số
3. Hù doạ phụ huynh ("con bạn đang tụt lại")
4. Nêu đích danh trung tâm đối thủ
5. Số liệu không có trong brief (học phí, ưu đãi, ngày khai giảng) → `[cần bổ sung]`
6. Ảnh trẻ em thật chưa có phụ huynh đồng ý bằng văn bản
7. Câu tuyệt đối ("tốt nhất", "số một", "duy nhất")
8. Quá 2 emoji một bài

> Khác B4 (JIT dạy 8 điều khoản, Agent thật rà 12 tiêu chí trong `checklist-rui-ro.json`): ở B6, 8 điều cấm này chính là toàn bộ checklist thật (`brand-voice.md`), không phải subset của bộ lớn hơn — vì brand-voice được dán trực tiếp vào prompt TH2/TH3 và quét lại ở App duyệt (TH4b), không có tầng checklist riêng nào khác.
