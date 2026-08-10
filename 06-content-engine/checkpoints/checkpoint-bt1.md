# Checkpoint TH1 — Content angle (GV/TA)

## Expected state

- [ ] Agent đã đọc cả `product-brief-sunrise-kids.md` và `chan-dung-khach-hang.md`.
- [ ] Workspace có `content-angles.json`.
- [ ] Có `brief_id`, `brief_title`, `personas_covered`, 5 angle.
- [ ] `chan_dung` của mỗi angle là mã có thật trong file chân dung (PH1/PH2/PH3).
- [ ] `personas_covered` có từ 2 mã trở lên.
- [ ] `muc_tieu` là token viết hoa: AWARENESS / TRUST / EDUCATION / OBJECTION / CONVERSION.
- [ ] Chưa viết bài đăng nào.

## Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Agent tự nghĩ ra nhóm khách hàng mới | `Trường chan_dung phải là mã có trong chan-dung-khach-hang.md. Đọc lại file đó và sửa cả 5 angle.` |
| Cả 5 angle dồn vào một chân dung | `5 angle này chỉ nhắm một người. Viết lại để phủ ít nhất 2 chân dung khác nhau, rồi cập nhật personas_covered.` |
| `muc_tieu` viết tiếng Việt hoặc sai chính tả | `muc_tieu chỉ nhận đúng 5 giá trị viết hoa không dấu: AWARENESS, TRUST, EDUCATION, OBJECTION, CONVERSION. Sửa lại rồi validate.` |
| Agent chỉ in ra chat, không ghi file | `Ghi kết quả thật ra file content-angles.json trong workspace rồi đọc lại file để xác nhận.` |
| Angle chung chung, cái nào cũng như cái nào | `Mỗi angle phải nêu được một góc khác nhau. Angle nào trùng ý thì thay bằng góc mới bám vào một pain khác trong brief.` |
| Angle bịa học phí / ưu đãi | `Brief cố tình không có học phí, ưu đãi, ngày khai giảng. Bỏ mọi con số em tự thêm.` |
| Kẹt quá thời gian | Dùng `fallback-inputs/content-angles-bt1-sample-output.json` để tiếp tục TH2. |

## Kiểm nhanh

```bash
python giao_trinh/scripts/validate-b6-artifacts.py <thư-mục-của-học-viên>
```
