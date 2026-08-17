# Improve Log — Recon Helper (Linh)

## Vòng 1 — 21/08
- Test thấy: dán số "12.500.000đ" (kèm chữ đ) → app hiểu 12,500,000 nhưng scenario 3 yêu cầu vẫn tính đúng; lần đầu app đọc nguyên chuỗi thành NaN.
- Yêu cầu sửa (1 tính năng): hàm so() lọc chỉ giữ chữ số trước parseInt.
- Kết quả: đã sửa — "12.500.000đ" và "12,500,000" đều ra 12500000.

## Vòng 2 — 22/08
- Test thấy: 2 dòng trùng so_dh phía sao kê → app chỉ xử lý 1 dòng, mất dòng kia (rule TRUNG_DON của skill không áp vào app).
- Yêu cầu sửa: gom nhóm theo so_dh, nếu ≥2 dòng một phía → TRUNG_DON liệt kê đủ.
- Kết quả: đã sửa.

## Vòng 3 — 23/08
- Thêm cột ghi chú độ tin cậy cho dòng KHONG_RO (như skill D1) — nhất quán 2 deliverable.
- Kết quả: đã áp.

## Phần chưa runtime-test
- Chưa test file thật của 12 đại lý (mới 3-5 dòng/lần); chưa test dán lệch cột.
