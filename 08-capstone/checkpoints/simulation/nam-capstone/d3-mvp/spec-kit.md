# Spec Kit — MVP Booking Helper (Nam)

## PRD rút gọn
- **Mục tiêu 1 câu:** Web app dán 1 tin đặt phòng → biết ngay xác nhận/trùng/đề xuất khung, kèm câu trả lời soạn sẵn.
- **Phạm vi MVP:** (1) textarea dán tin; (2) nhập lịch tuần hiện có (đã pre-fill theo kb); (3) nút Kiểm tra — rule cứng local; (4) kết quả + reply draft copy được.
- **Ngoài phạm vi:** cập nhật lịch thật, gửi Zalo, nhiều tuần, đăng nhập.

## User stories
1. Với tư cách nhân viên HC, tôi muốn dán tin đặt phòng và thấy ngay có trùng không, để trả lời người đặt trong vài phút.
2. Với tư cách nhân viên HC, tôi muốn app đề xuất 2 khung trống khi khách ghi "buổi sáng", để khách tự chọn thay vì tôi gọi hỏi lại.
3. Với tư cách nhân viên HC, tôi muốn copy câu trả lời soạn sẵn, để chỉ duyệt và gửi.

## Test scenarios
| # | Kịch bản | Bước | Kỳ vọng |
|---|----------|------|---------|
| 1 | Không trùng | Dán tin P301 20/08 9:00-10:30 (8 người) → Kiểm tra | XAC_NHAN |
| 2 | Trùng khung | Dán tin P301 19/08 9:00-10:30 → Kiểm tra | TU_CHOI + trích dòng lịch Mỹ Linh |
| 3 | Trùng giao-khung (DỮ LIỆU LẠI) | Dán tin P301 19/08 10:00-11:00 (giao 30' với 9:00-10:30) | TU_CHOI — giao khung cũng là trùng |
| 4 | Mơ hồ buổi sáng | "P302 sáng 21/08 15 người" | DE_XUAT_KHUNG_KHAC ≥2 khung, không tự chọn |

## Ràng buộc kỹ thuật
1 file index.html, rule cứng JS, lịch tuần pre-fill, không API ngoài.

## MVP xong khi
4 scenario PASS + copy reply hoạt động.
