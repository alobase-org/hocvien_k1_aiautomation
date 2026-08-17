# E2E Test — Workflow booking-reviewer (Nam)

## Workflow dưới test
- Tên n8n: `nam-booking` (webhook /nam-booking)
- Nguồn mượn: `04-contract-review/checkpoints/n8n-contract-review-solution.json` (khung B4)

## Bộ input mẫu
| # | Input | Kỳ vọng |
|---|-------|---------|
| 1 | "Cho phòng HC đặt P301 thứ 4 20/08 9:00-10:30 họp marketing 8 người cần máy chiếu. — Dũng" | XAC_NHAN |
| 2 | "Đặt P301 19/08 9:00-10:30 họp giao ban 10 người. — Hoa" | TU_CHOI + trích dòng lịch Mỹ Linh |
| 3 | "P302 sáng thứ 5 21/08 họp khách hàng 15 người. — Khang" | DE_XUAT_KHUNG_KHAC ≥2 khung, KHÔNG tự chọn |

## Asserts
| # | Assert | Cách kiểm | PASS khi |
|---|--------|-----------|----------|
| 1 | Đồ thị node/connection nguyên vẹn | Chạy auto-check [3] | PASS |
| 2 | Workflow import được | Import vào n8n UI | Không lỗi |
| 3 | Input #1 → XAC_NHAN | So response | đúng + ly_do |
| 4 | Input #2 → TU_CHOI + dan_chung dòng lịch | So response | trích "P301 \| 19/08 \| 9:00-10:30" |
| 5 | Input #3 → DE_XUAT_KHUNG_KHAC, không tự chọn | So response | ≥2 khung liệt kê |

## Kết quả
| Lần | Asserts | Verdict |
|-----|---------|---------|
| 1 | 0/5 | FAIL (đồ thị đứt) |
| 2 | 2/5 | PARTIAL |
| 3 | 5/5 cấu trúc + 0/5 runtime | PASS-CẤU TRÚC (runtime chưa chạy được — xem run-log) |
