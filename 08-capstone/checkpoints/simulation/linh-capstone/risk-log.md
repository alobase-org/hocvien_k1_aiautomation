# Risk Log — Linh

| # | Rủi ro | Mức | Cách giảm | Trạng thái |
|---|--------|-----|-----------|------------|
| 1 | Dữ liệu đại lý nhạy cảm | Cao | Test toàn bằng dữ liệu mô phỏng (B6 fallback-inputs) | Đã giảm |
| 2 | AI phân loại lệch sai nguyên nhân → email sai | Cao | Rule đánh số exact + dòng KHONG_RO bắt buộc lý do + HITL kế toán trưởng duyệt email | Đã giảm |
| 3 | Chênh dấu chấm nghìn/đơn vị tiền | Trung | Chuẩn hóa bỏ ký tự không phải số trước khi so | Đã giảm |
| 4 | Volume 12 đại lý chưa test full | Trung | Ghi "chưa runtime-test" trong run-log, kế hoạch tuần tới | Đang giảm |
