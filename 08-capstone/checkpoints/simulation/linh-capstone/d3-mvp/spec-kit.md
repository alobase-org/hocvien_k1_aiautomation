# Spec Kit — MVP Recon Helper (Linh)

## PRD rút gọn
- **Mục tiêu 1 câu:** Web app dán 2 cột công nợ (nội bộ, sao kê) và nhận bảng đối chiếu + phân loại lệch + email draft.
- **Phạm vi MVP:** (1) 2 textarea dán CSV; (2) nút Đối chiếu — ghép so_dh, rule cứng chạy local; (3) bảng kết quả khớp/lệch + nguyên nhân; (4) copy email draft.
- **Ngoài phạm vi:** đọc file excel thật (dán text), gửi email, đăng nhập, lưu database.

## User stories
1. Với tư cách kế toán công nợ, tôi muốn dán 2 bảng và thấy ngay dòng nào lệch bao nhiêu, để không đối chiếu tay 1,5 ngày mỗi tháng.
2. Với tư cách kế toán công nợ, tôi muốn biết nguyên nhân đề xuất của mỗi dòng lệch, để email đại lý đúng vấn đề lần đầu.
3. Với tư cách kế toán công nợ, tôi muốn copy email draft per đại lý, để chỉ duyệt và gửi.

## Test scenarios
| # | Kịch bản | Bước | Kỳ vọng |
|---|----------|------|---------|
| 1 | Khớp hoàn toàn | Dán 2 bảng 3 dòng giống hệt → Đối chiếu | 3 KHỚP, 0 lệch |
| 2 | Lệch chiết khấu | DH001 nội bộ 12.500.000 / sao kê 12.000.000 | LỆCH 500.000 → CHIET_KHAU_CHUA_GHI |
| 3 | Dữ liệu lạ (bắt buộc) | Một dòng sao kê trống số tiền; số tiền có "12.500.000đ" kèm chữ | Không crash; THIEU_DON; bỏ "đ" vẫn tính đúng |

## Ràng buộc kỹ thuật
1 file index.html, rule cứng JS, không API ngoài.

## MVP xong khi
3 scenario PASS + copy draft hoạt động + xử lý được dấu chấm nghìn.
