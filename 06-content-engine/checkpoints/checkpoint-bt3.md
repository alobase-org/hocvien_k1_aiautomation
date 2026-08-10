# Checkpoint TH3 — Seeding + image brief + prompt ảnh (GV/TA)

## Expected state

- [ ] Agent đã đọc `content-draft.json`, seeding bám đúng bài đã viết.
- [ ] Workspace có `content-assets.json`.
- [ ] `brief_id` và `source_angle_id` khớp hai lớp trước.
- [ ] Đủ 5 seeding, `vai_tro` dùng token ASK / RELATE / EXPERIENCE / CONDITION / CTA_NUDGE.
- [ ] Có ít nhất 2 câu hỏi thật mà page trả lời được.
- [ ] `image_brief` đủ 9 mục, `khong_duoc_xuat_hien` không rỗng và có ràng buộc về mặt trẻ em.
- [ ] `image_prompt` viết tiếng Anh, **không chứa chữ cần hiển thị trên ảnh**.

## Vì sao image_prompt cấm chữ

Model sinh ảnh viết sai chính tả tiếng Việt gần như chắc chắn. Chữ chèn sau bằng Canva.
Prompt phải có `no text` và `no children / no human faces` — lớp 3 của workflow sẽ gửi thẳng chuỗi này đi sinh ảnh.

## Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Seeding toàn lời khen | `Bỏ hết câu khen. Seeding là người đọc thật đang hỏi hoặc kể, không phải người của trung tâm.` |
| 5 seeding cùng một giọng | `Viết lại: 2 câu hỏi, 1 câu kể trải nghiệm, 1 câu đồng cảnh, 1 câu hỏi điều kiện. Mỗi câu một người khác nhau nói.` |
| `vai_tro` viết tiếng Việt | `vai_tro chỉ nhận: ASK, RELATE, EXPERIENCE, CONDITION, CTA_NUDGE. Sửa rồi validate.` |
| Seeding nêu tên đối thủ, bịa ưu đãi | `Bỏ tên trung tâm khác và mọi ưu đãi. So sánh thì kể bằng trải nghiệm, không nêu tên.` |
| Image brief thiếu mục | `Bổ sung đủ 9 mục: mục tiêu, thông điệp chính, đối tượng, kênh, tỷ lệ, phong cách, bố cục, chữ trên ảnh, không được xuất hiện.` |
| Quên mục cấm | `Thêm khong_duoc_xuat_hien: mặt trẻ em, bảng điểm, logo bên khác, chữ tiếng Anh.` |
| `image_prompt` có chữ tiếng Việt trong ảnh | `Bỏ mọi chữ khỏi image_prompt, thêm "no text or lettering of any kind". Chữ sẽ chèn bằng Canva sau.` |
| `image_prompt` viết tiếng Việt | `Viết image_prompt bằng tiếng Anh — node sinh ảnh nhận tiếng Anh cho kết quả ổn định hơn.` |
| Kẹt quá thời gian | Dùng `checkpoints/content-assets-sample.json` để tiếp tục TH4. |
