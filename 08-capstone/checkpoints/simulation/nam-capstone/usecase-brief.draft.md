# Usecase Brief — Sắp lịch họp phòng hành chính (Nam)

## [BẮT BUỘC] Bài toán
Phòng HC 6 người, mỗi tuần nhận ~15 yêu cầu đặt phòng họp qua Zalo + sổ giấy. Nam tự đối lịch, tránh đụng giờ, xác nhận lại. Mỗi tuần mất ~3 giờ, hay bị đặt trùng giờ.

## [BẮT BUỘC] Người dùng
Người gửi: nhân viên các phòng. Người xử lý: Nam (HC). Người nhận output: người đặt + Nam.

## [BẮT BUỘC] Input hàng ngày
Tin nhắn Zalo "họp phòng A, 12 người, thứ 4 buổi sáng, đăng ký máy chiếu". ~15 tin/tuần.

## [BẮT BUỘC] Output mong muốn
Lịch tuần dạng bảng: phòng, khung giờ, người đặt, thiết bị. Xác nhận/trả lời đổi giờ.

## [BẮT BUỘC] Quy trình xử lý (tách theo loại bước)
1. (Cứng) Trích: phòng, ngày, giờ, số người, thiết bị.
2. (Cứng) Đối chiếu lịch trống: trùng hay không.
3. (AI phán đoán) Tin mơ hồ ("buổi sáng") → đề xuất khung cụ thể.
4. (Người duyệt) Nam xác nhận cuối (HITL).
5. (Cứng) Cập nhật lịch + trả lời.

## [BẮT BUỘC] Tiêu chí thành công (đo được)
- Đặt phòng nhanh hơn
- Ít bị trùng lịch hơn
