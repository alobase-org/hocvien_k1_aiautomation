# E2E Test — Workflow legal-reviewer (Hùng)

## Asserts
| # | Assert | PASS khi |
|---|--------|----------|
| 1 | Đồ thị nguyên vẹn | auto-check [3] |
| 2 | Respond JSON | content-type application/json |
| 3 | Văn bản có "thanh toán 100% không điều kiện" → CAO/A1 | response có "CAO" + "A1" |
| 4 | Văn bản 5 điều khoản → đủ 5 trong output | đếm D1..D5 |
