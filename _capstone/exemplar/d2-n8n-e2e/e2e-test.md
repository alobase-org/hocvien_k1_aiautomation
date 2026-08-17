# E2E Test — Workflow duyệt nghỉ phép (exemplar)

## Workflow dưới test
- Tên n8n: `leave-request-reviewer`
- Nguồn mượn: `04-contract-review/checkpoints/n8n-contract-review-solution.json` — giữ khung nhận input → chuẩn hóa → AI check theo KB → output có lý do; thay clause-check bằng policy-check.

## Bộ input mẫu
| # | Input | Kỳ vọng |
|---|-------|---------|
| 1 | Đơn annual báo trước 4 ngày, có bàn giao | PASS — đề xuất duyệt |
| 2 | Đơn annual báo trước 1 ngày | FAIL nghiệp vụ — đề xuất từ chối |

## Asserts
| # | Assert | Cách kiểm | PASS khi |
|---|--------|-----------|----------|
| 1 | Workflow chạy hết | Execution pane n8n | Status success, không node đỏ |
| 2 | Artifact sinh ra | Kiểm file `leave-review.json` | Tồn tại sau chạy, đúng schema |
| 3 | Đơn #1 đề xuất duyệt | So `de_xuat` | `DE_XUAT_DUYET` + có `ly_do` |
| 4 | Đơn #2 đề xuất từ chối | So `de_xuat` + `dan_chung` | `DE_XUAT_TU_CHOI` + dẫn chứng "báo trước 1 ngày" |

## Kết quả
| Lần | Asserts PASS | Verdict |
|-----|---------------|---------|
| 1 | 2/4 | FAIL |
| 2 | 3/4 | PARTIAL |
| 3 | 3/4 | PARTIAL — assert 2 chưa đạt: output node vẫn report.docx của B4 (xem run-log) |
