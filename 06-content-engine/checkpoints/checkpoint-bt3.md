# Checkpoint TH3 — Seeding + image brief + prompt ảnh (GV/TA)

## Expected state

- [ ] Agent đã đọc `content-draft.json`, seeding bám đúng bài đã viết.
- [ ] Workspace có `content-assets.json`.
- [ ] `brief_id` và `source_angle_id` khớp hai lớp trước.
- [ ] Đủ 5 seeding, `vai_tro` dùng token ASK / RELATE / EXPERIENCE / CONDITION / CTA_NUDGE.
- [ ] Có ít nhất 2 câu hỏi thật mà page trả lời được.
- [ ] `image_brief` đủ 9 mục, `khong_duoc_xuat_hien` không rỗng (điều thật sự không muốn thấy — không bắt buộc phải về trẻ em, ảnh AI sinh được phép có người/trẻ em để tăng độ thu hút).
- [ ] `image_prompt` viết tiếng Anh, **được phép có tối đa 1 dòng tiêu đề/CTA ngắn (≤8 từ) bằng tiếng Việt**, ghi đúng nguyên văn trong prompt, khớp `chu_tren_anh`. Nội dung dài hơn thì để trống, không đưa vào ảnh.

## Vì sao image_prompt được phép có chữ ngắn (đổi hướng 2026-08-09)

Trước đây cấm hoàn toàn vì giả định "model sinh ảnh viết sai chính tả tiếng Việt gần như chắc chắn" — **giả định này đã sai với model hiện tại** (`nano-banana-pro` qua GeminiGen.ai). Test thật: model render đúng 100% dấu tiếng Việt với các cụm từ như "Học thử miễn phí", "Gò Vấp & Tân Bình". Nên giờ cho phép TỐI ĐA 1 dòng tiêu đề/CTA ngắn (≤8 từ) hiển thị thẳng trong ảnh, không cần chờ Canva chèn sau. Nội dung dài (đoạn văn, danh sách) vẫn để trống — model chưa đủ tin cậy để đặt nhiều chữ đúng vị trí.

**Rủi ro còn lại, đã xác nhận có thật:** dù chính tả đúng, model đôi khi tự **lặp thừa một phần chữ** (ví dụ vẽ "Tiếng Anh" rồi lại vẽ "Tiếng Anh tự nhiên cho bé" ngay bên dưới) — đây là lý do Lớp 3b — Judge ảnh (`prompts/judge-extension-prompt.md`) vẫn giữ nguyên, chỉ đổi câu hỏi chấm từ "có chữ không" sang "chữ có đúng — không thiếu/thừa/lặp — so với dự kiến không".

Ảnh có người/trẻ em KHÔNG bị cấm — đây là ảnh AI sinh hoàn toàn, không tham chiếu ai thật nên
không phát sinh vấn đề quyền riêng tư (khác hẳn việc quay video thật ở TH2, nơi vẫn cấm quay
mặt trẻ em thật vì đó là footage thật, chưa có consent).

**Về ethnicity và tuổi (2026-08-09):** nếu ảnh có học sinh, mô tả rõ là trẻ em người Việt Nam
— đúng đối tượng thật. Nếu có giáo viên, được phép mô tả là người nước ngoài — đúng mô hình
"giáo viên bản ngữ" của brief; trợ giảng (nếu có) là người Việt. **TUYỆT ĐỐI không đưa ước
lượng tuổi trẻ em vào `khong_duoc_xuat_hien`** (vd "trẻ dưới 6 tuổi") — vision model đoán tuổi
qua ảnh tĩnh không đáng tin, test thật từng đoán nhầm 8-9 tuổi thành 4-5 tuổi rồi chặn oan một
ảnh đạt. Việc kiểm tuổi để người duyệt tự nhìn ở App, không phải điều kiện chặn tự động.

## Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Seeding toàn lời khen | `Bỏ hết câu khen. Seeding là người đọc thật đang hỏi hoặc kể, không phải người của trung tâm.` |
| 5 seeding cùng một giọng | `Viết lại: 2 câu hỏi, 1 câu kể trải nghiệm, 1 câu đồng cảnh, 1 câu hỏi điều kiện. Mỗi câu một người khác nhau nói.` |
| `vai_tro` viết tiếng Việt | `vai_tro chỉ nhận: ASK, RELATE, EXPERIENCE, CONDITION, CTA_NUDGE. Sửa rồi validate.` |
| Seeding nêu tên đối thủ, bịa ưu đãi | `Bỏ tên trung tâm khác và mọi ưu đãi. So sánh thì kể bằng trải nghiệm, không nêu tên.` |
| Image brief thiếu mục | `Bổ sung đủ 9 mục: mục tiêu, thông điệp chính, đối tượng, kênh, tỷ lệ, phong cách, bố cục, chữ trên ảnh, không được xuất hiện.` |
| Quên mục cấm | `Thêm khong_duoc_xuat_hien: bảng điểm, logo bên khác, chữ tiếng Anh, số điện thoại giả.` |
| `image_prompt` nhồi cả đoạn văn dài vào ảnh | `Chỉ giữ tối đa 1 dòng tiêu đề/CTA ngắn (≤8 từ) trong image_prompt, khớp chu_tren_anh. Nội dung dài để trống, chèn sau bằng Canva.` |
| `image_prompt` viết tiếng Việt | `Viết image_prompt bằng tiếng Anh — node sinh ảnh nhận tiếng Anh cho kết quả ổn định hơn.` |
| Kẹt quá thời gian | Dùng `checkpoints/content-assets-sample.json` để tiếp tục TH4. |
