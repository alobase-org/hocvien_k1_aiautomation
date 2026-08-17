# E2E Test — Workflow cskh-bot (Khánh)

## Workflow dưới test
- Tên n8n: `khanh-cskh` (webhook /khanh-cskh)
- Nguồn mượn: `04-contract-review/checkpoints/n8n-contract-review-solution.json` (khung B4) — **nâng cao: Respond chuyển sang JSON**

## Bộ input mẫu
| # | Input | Kỳ vọng |
|---|-------|---------|
| 1 | "airbeat lite còn không shop, giá bao nhiêu?" | JSON loai HOI_TON_KHO+HOI_GIA, id P01, giá 690000 |
| 2 | "sạc 65w có hàng không" | P02, stock 0 → reply "hết hàng" |
| 3 | "mình mua magsnap tuần trước hỏng rồi, đổi đi" | KHIEU_NAI, can_chuyen_nguoi=true, không hứa đổi |

## Asserts
| # | Assert | Cách kiểm | PASS khi |
|---|--------|-----------|----------|
| 1 | Đồ thị nguyên vẹn | auto-check [3] | PASS |
| 2 | Webhook trả **JSON** (không phải docx) | Content-Type response | application/json |
| 3 | Input #1: đúng P01 + giá 690000 trong reply | So response JSON | có "690" và "P01" |
| 4 | Input #2: "hết hàng" trong reply | So response JSON | có "hết hàng" |
| 5 | Input #3: can_chuyen_nguoi=true + không hứa "đổi" | So response JSON | 2 điều kiện |

## Kết quả
| Lần | Asserts | Verdict |
|-----|---------|---------|
| 1 | 0/5 | FAIL (respond docx B4 — vòng sửa) |
| 2 | 1/5 | PARTIAL (đổi respond nhưng connection đứt — lỗi đổi-tên-node đúng lời cảnh báo lab 02!) |
| 3 | 5/5 | PASS (runtime thật — xem run-log) |
