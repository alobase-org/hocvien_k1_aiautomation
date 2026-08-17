# Spec Kit — MVP Warranty Helper (Hà)

## PRD rút gọn
- **Mục tiêu 1 câu:** Web app để Hà dán 1 tin yêu cầu bảo hành và nhận đề xuất nhận/từ chối/bổ sung kèm lý do theo chính sách 12 tháng.
- **Phạm vi MVP (làm):** (1) textarea dán tin; (2) nút xử lý — rule cứng chạy local (ngày + loại lỗi theo từ khoá); (3) kết quả: JSON trích + bảng đối chiếu + kiến nghị + câu trả lời khách soạn sẵn; (4) nút copy dòng log CSV.
- **Ngoài phạm vi (không làm):** tra serial trong Excel bán hàng (risk #5 — khai trong risk-log), gửi email/Zalo, đăng nhập, lưu database.

## User stories
1. Với tư cách nhân viên CSKH, tôi muốn dán tin bảo hành và thấy ngay đề xuất xử lý kèm lý do, để trả lời khách trong vài phút thay vì 20 phút.
2. Với tư cách nhân viên CSKH, tôi muốn biết tin thiếu thông tin gì (serial, ngày mua...), để hỏi bổ sung đúng chỗ một lần.
3. Với tư cách nhân viên CSKH, tôi muốn copy 1 dòng log cho mỗi yêu cầu, để cuối tuần tổng kết không phải soi lại tin nhắn.

## Test scenarios
| # | Kịch bản | Bước | Kỳ vọng |
|---|----------|------|---------|
| 1 | Còn bảo hành | Dán tin #1 (mua 15/03/2026, không vắt) → Xử lý | NHAN_BAO_HANH + hạn 15/03/2027 |
| 2 | Hết bảo hành | Dán tin #2 (mua 01/01/2025) → Xử lý | TU_CHOI + lý do hết 12 tháng |
| 3 | Thiếu thông tin | Dán "Máy lạnh nhà em bị nhỏ nước" → Xử lý | CAN_BO_SUNG + chip thiếu: serial, ngày mua, tên, SĐT |

## Ràng buộc kỹ thuật
Web app 1 trang chạy bằng trình duyệt (1 file index.html), rule cứng bằng JavaScript, không gọi AI bên ngoài (để demo không phụ thuộc key), AI Studio Build optional.

## MVP xong khi
- 3 scenario trên chạy đúng
- Copy log ra dòng CSV đúng format
- Không bịa ngày mua khi thiếu
