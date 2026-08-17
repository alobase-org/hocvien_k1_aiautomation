# E2E Test — Workflow weekly-report (Thảo)

## Asserts
| # | Assert | PASS khi |
|---|--------|----------|
| 1 | Đồ thị nguyên vẹn | auto-check [3] PASS |
| 2 | Webhook trả JSON | Content-Type application/json |
| 3 | Input có tuần trước → tang_truong_pct đúng | có "-14.3" hoặc "+10.0" |
| 4 | Input thiếu tuần trước → THIEU_DU_LIEU | response có "THIEU_DU_LIEU" |
