# Usecase Brief — Xử lý yêu cầu bảo hành khách gửi qua email/Zalo

> Học viên: Nguyễn Thị Hà · CSKH Điện Lạnh Gia Phúc (dữ liệu mô phỏng) · Buổi 8 TH1, 18/08/2026

## [BẮT BUỘC] Bài toán
Khách gửi yêu cầu bảo hành (bảo trì/sửa máy giặt, máy lạnh, nồi chiên...) qua email cs@giaphuc.vn và Zalo OA. Hiện Hà tự đọc từng tin, tra số serial trong file Excel bán hàng, check chính sách bảo hành (12 tháng, loại lỗi), rồi trả lời hẹn lịch. Trung bình 10 yêu cầu/tuần, mỗi cái 20 phút, hay trả lời trễ cuối ngày và bỏ sót tin Zalo.

## [BẮT BUỘC] Người dùng
Người gửi: khách đã mua máy. Người xử lý: Hà (đề xuất), trưởng nhóm kỹ thuật duyệt lịch sửa. Người nhận output: khách (trả lời tự động) + Hà + kỹ thuật (yêu cầu sửa có đủ thông tin).

## [BẮT BUỘC] Input hàng ngày
Tin nhắn/email yêu cầu bảo hành dạng tự nhiên: tên khách, SĐT, loại máy, sự cố, ngày mua (khách có thể nhớ sai). ~10 tin/tuần. Ví dụ: "Máy giặt Electrolux em mua tháng 3 giờ không vắt, bảo hành giúp em, 0900.000.012, Mỹ Dung".

## [BẮT BUỘC] Output mong muốn
File `warranty-requests/de-xuat-YYYY-MM-DD.md`: trích thông tin + kết quả check chính sách + đề xuất (nhận bảo hành / từ chối / cần thêm thông tin) + lịch sửa đề xuất. Kèm `warranty-log.csv` 1 dòng/yêu cầu (ngày, khách, máy, trong bảo hành?, đề xuất).

## [BẮT BUỘC] Quy trình xử lý (tách theo loại bước)
1. (Quy tắc cứng) Trích: tên, SĐT, loại máy, sự cố, ngày mua.
2. (Cứng) Check: ngày mua + 12 tháng? loại lỗi thuộc bảo hành (lỗi máy) hay do sử dụng (rơ mỡ, vỡ nhựa)?
3. (AI phán đoán) Đọc mô tả sự cố → phân loại lỗi máy/do người dùng/thiếu thông tin.
4. (Người duyệt) Kỹ thuật duyệt lịch sửa (HITL).
5. (Cứng) Trả lời khách + ghi log.

## [BẮT BUỘC] Tiêu chí thành công (đo được)
- 100% yêu cầu được trả lời trong 4 giờ làm việc, có dòng trong `warranty-log.csv`
- Yêu cầu còn bảo hành: đề xuất "nhận bảo hành" đúng 10/10 mẫu test
- Yêu cầu hết bảo hành/thiếu serial: đề xuất từ chối/cần bổ sung kèm lý do, 10/10 mẫu

## Ràng buộc & công cụ sẵn có
Không dùng tên khách thật — dùng dữ liệu mô phỏng (mẫu B6 fallback-inputs). Có n8n local, AI Studio, Claude Code (tài khoản lớp). Ngân sách 0.
