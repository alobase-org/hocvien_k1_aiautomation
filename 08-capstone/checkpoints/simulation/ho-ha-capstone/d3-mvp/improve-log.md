# Improve Log — MVP Warranty Helper (Hà)

## Vòng 1 — 21/08 (build đầu bằng AI Studio Build theo spec-kit)
- Dùng thử thấy: bấm Xử lý → app đứng im rồi biến mất kết quả (crash). Kiểm console: "d.ngayMau_display is not a function" — AI sinh code gọi hàm không tồn tại.
- Yêu cầu sửa (1 tính năng): thay dòng hiển thị ngày mua bằng chuỗi tự format.
- Kết quả: đã sửa — chạy được 1/3 scenario.

## Vòng 2 — 22/08
- Test thấy: tin #1 (còn bảo hành, đủ thông tin) vẫn ra CAN_BO_SUNG — soi thấy SĐT "0900.000.012" không được trích (regex chỉ bắt nhóm 3-3-4, tin của khách nhóm 4-3-3).
- Yêu cầu sửa: trích SĐT bằng cách quét chuỗi số-chấm-cách rồi kiểm 10-11 chữ số.
- Kết quả: đã sửa — 3/3 scenario PASS.

## Vòng 3 — 23/08 (thêm 1 case lỗi do người dùng)
- Test thêm tin "tủ lạnh vỡ nhựa tay cầm do làm rơi" → TU_CHOI đúng (lỗi người dùng). 4/4 PASS.
- Còn 1 lỗi hiển thị nhỏ: hạn bảo hành hiển thị lệch 1 ngày (15/03/2026 → hiện 2027-03-14) do múi giờ khi format — logic quyết định không sai (dùng so sánh Date trực tiếp). Ghi nhận, chưa sửa vì không ảnh hưởng đề xuất.

## Phần chưa runtime-test
- Chưa test trên điện thoại; chưa test tin dài >300 chữ, tin có nhiều ngày tháng lẫn lộn.
- Chưa test upload ảnh kèm tin (khách hay chụp máy gửi kèm).
