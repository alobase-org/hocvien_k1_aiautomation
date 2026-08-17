# E2E Test — Workflow recon-analyzer (Linh)

## Workflow dưới test
- Tên n8n: `linh-recon` (webhook /linh-recon)
- Nguồn mượn: `04-contract-review/checkpoints/n8n-contract-review-solution.json` (khung B4)

## Bộ input mẫu (CSV dán vào webhook data)
| # | Input | Kỳ vọng |
|---|-------|---------|
| 1 | 1 dòng DH001 12.5tr/12tr | CHIET_KHAU_CHUA_GHI + chênh 500,000 |
| 2 | 1 dòng KHÔNG_RO (chênh 333,777) | KHONG_RO + lý do, không đoán |
| 3 | 1 dòng THIEU_DON (sao kê trống) | THIEU_DON |

## Asserts
| # | Assert | Cách kiểm | PASS khi |
|---|--------|-----------|----------|
| 1 | Chạy hết không node đỏ | Execution pane | success |
| 2 | Response có JSON phân loại mỗi dòng | So response webhook | đủ trường nguyen_nhan + do_tin_cay |
| 3 | Input #1 đúng CHIET_KHAU_CHUA_GHI + chênh 500,000 | So nội dung | đúng + có dan_chung |
| 4 | Input #2 KHÔNG_RO + có lý do | So nội dung | có ≥1 câu lý do |
| 5 | Có email draft phân theo đại lý | So response | draft có tên đại lý + không đổ lỗi |

## Kết quả
| Lần | Asserts | Verdict |
|-----|---------|---------|
| 1 | 1/5 | FAIL |
| 2 | 4/5 | PARTIAL |
| 3 | 5/5 | PASS |
