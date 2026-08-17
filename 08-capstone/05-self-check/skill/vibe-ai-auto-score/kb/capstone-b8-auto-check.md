# Capstone B8 — Auto-Check trước khi chấm (deterministic pre-check)

> Áp dụng khi chấm đồ án capstone khóa AI Automation K1 (package `ho-ten-capstone/`).
> Chạy TRƯỚC giai đoạn đọc bài và chấm rubric — loại ngay bài lỗi cấu trúc, tiết kiệm ~10 phút/bài.

## Cách chạy
```bash
python3 script/capstone_auto_check.py <thư-mục-package-hv> [--input "tin test"] \
    [--n8n-url http://localhost:5678] [--email admin@alobase.vn] [--password Password123!]
```
Yêu cầu: n8n local đang chạy (để check [6] runtime: import workflow + gọi webhook + đọc response).

## 6 check (exit code 0 = không có FAIL)
1. Cấu trúc package (13 file chuẩn)
2. Brief 7 mục + ≥2 tiêu chí đo được
3. Đồ thị workflow n8n nguyên vẹn (connection không trỏ node mồ côi — lỗi phổ biến khi HV rename node)
4. Run-log ≥2 vòng + ≥1 FAIL + evidence
5. pitch.html đủ 6 slide, không placeholder
6. RUNTIME: import workflow vào n8n + chạy 1 input qua webhook

## Đưa vào grading
- FAIL ở [1]–[5] → trả bài chưa chấm rubric (đề nghị HV chạy `05-self-check` rồi nộp lại).
- FAIL ở [6] → criterion D2a (workflow chạy use case mới) tối đa mức 2, ghi evidence từ output script.
- Script KHÔNG phán đoán nghiệp vụ đúng/sai trong output — phần đó vẫn do graded-by-rubric với evidence verbatim (đọc output của lần chạy runtime).
- HV được tự chạy tool này trước khi nộp (nó nằm trong studentkit lab 05-self-check) — điểm tự chấm `self-grading.md` là input tham khảo, không phải điểm GV.

## Nguồn gốc
Pattern n8n REST API mượn từ B4 `interactive_e2e_runner.py`; được chuẩn hóa thành tool dùng chung GV+HV ngày 17/08/2026 sau teaching simulation B8 (xác nhận runtime-check bắt buộc vì run-log evidence có thể bịa).
