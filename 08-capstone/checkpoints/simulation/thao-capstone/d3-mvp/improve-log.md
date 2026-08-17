# Improve Log — Weekly Report UI (Thảo)

## Vòng 1 — 21/08 (bug dữ liệu lạ — dấu phẩy nghìn)
- Test thấy: dòng "D02,2,310,000,000" → parse ra tien=2 (split(",") cắt chuỗi số có dấu phẩy nghìn thành mảnh).
- Yêu cầu sửa (1 chỗ): dùng indexOf(",") cắt tại dấu phẩy ĐẦU TIÊN — phần sau nguyên vẹn đưa cho hàm so() lọc số.
- Kết quả: đã sửa — 5/5 test hàm so + parse 2 dòng (1 dòng có dấu phẩy) PASS.

## Phần chưa runtime-test
- Chưa test 10 điểm thật cùng lúc; chưa test số âm (hoàn tiền); chưa test trên điện thoại.
