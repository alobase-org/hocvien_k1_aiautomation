# Improve Log — MVP Leave Request Helper (exemplar)

> Ghi đúng các vòng đã làm khi build exemplar (tối 17/08). App: `index.html` mở bằng trình duyệt là chạy, không cần server.

## Vòng 1
- Dùng thử thấy: bấm Xử lý xong không biết app đang chạy hay treo; kết quả hiện dưới màn hình phải cuộn tìm.
- Yêu cầu sửa (1 tính năng): nút đổi label "Đang xử lý..." khi chạy + tự cuộn tới kết quả.
- Kết quả: đã áp vào bản hiện tại (xem hàm `xuLy` và `scrollIntoView`).

## Vòng 2
- Dùng thử thấy: dán đoạn văn không phải đơn, app trả kết quả loạn thay vì nói thiếu gì.
- Yêu cầu sửa: render danh sách trường thiếu dạng chip đỏ + verdict THIEU_DU_LIEU, không đoán bậy.
- Kết quả: đã áp (xem nhánh `thieu.length` trong `chay`).

## Vòng 3 (bắt được nhờ chạy unit-test 3 scenario của spec-kit)
- Test thấy: đơn "21-22/08" bị parse sai thành tháng 21; "Em Minh" viết hoa không bắt được tên.
- Yêu cầu sửa: chuẩn hóa khoảng ngày trước khi bóc tách + bắt tên cả khi "Em" viết hoa.
- Kết quả: đã áp; 3/3 scenario PASS (kèm test log trong buổi demo nếu cần).

## Phần chưa runtime-test
- Chưa test trên điện thoại (chỉ máy tính).
- Chưa test đơn 500+ chữ, đơn có nhiều khoảng ngày.
