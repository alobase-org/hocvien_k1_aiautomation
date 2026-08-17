# Spec Kit — MVP Weekly Report UI (Thảo)

## PRD rút gọn
- **Mục tiêu 1 câu:** Web app dán CSV doanh số tuần này + tuần trước → thấy tổng, tăng trưởng, cảnh báo, email draft copy được.
- **Phạm vi MVP:** 2 textarea CSV · nút Tính · bảng kết quả + badge cảnh báo · nút Copy email draft.
- **Ngoài phạm vi:** upload file, gửi email thật, nhiều tuần liên tiếp.

## Test scenarios
| # | Kịch bản | Kỳ vọng |
|---|----------|---------|
| 1 | Tuần này 2.31t / tuần trước 2.1t | +10%, không cảnh báo |
| 2 | Tuần này 1.8t / tuần trước 2.1t | -14.3% → badge CẢNH_BAO đỏ |
| 3 | Dữ liệu lạ: tuần trước trống | THIEU_DU_LIEU, không tính bừa |
| 4 | Dấu phẩy nghìn "2,310,000,000" (DỮ LIỆU LẠI) | Vẫn tính đúng 2.31 tỷ |
