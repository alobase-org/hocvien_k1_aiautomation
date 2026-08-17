# Improve Log — Booking Helper (Nam)

## Vòng 1 — 21/08 (crash đúng kiểu lab 03 cảnh báo)
- Test thấy: dán tin mơ hồ "P302 sáng thứ 5..." → app chết im, Console (F12) đỏ: "Cannot read properties of undefined (reading 'replace')".
- Nguyên nhân (tìm nhờ Console): `t.match(...)||[]` cho mảng rỗng — **mảng rỗng vẫn truthy trong JS** → `kh[0]` undefined.
- Yêu cầu sửa (1 chỗ): check `kh && kh[0]` thay vì `kh?`.
- Kết quả: đã sửa — 4/4 scenario PASS. Bài học nhớ lâu: fallback `||[]` không cứu được truthy-check.

## Vòng 2 — 22/08 (thiết kế test scenario)
- Test thấy: ban đầu tôi chỉ test trùng chính xác 9:00-10:30 vs 9:00-10:30; scenario "Dữ liệu lạ" trong template bắt tôi thêm case giao-khung 10:00-11:00 — hóa ra quan trọng: đúng là trùng mà check chính xác sẽ lọt.
- Yêu cầu sửa: hàm `giao()` so giao khung thay vì so bằng chuỗi.
- Kết quả: đã sửa — T3 (giao 30 phút) bây giờ TU_CHOI đúng.

## Phần chưa runtime-test
- Chưa test trên điện thoại; chưa test 15 tin liên tiếp; lịch pre-fill cứng 1 tuần (chưa có nút cập nhật lịch).
