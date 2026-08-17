# Đồ án Capstone — Buổi 08: Biến use case của bạn thành giải pháp AI Automation hoàn chỉnh

> Đọc file này trước khi làm bất cứ deliverable nào.

## Đồ án là gì

Bạn chọn **1 use case automation thật** (quy trình đang làm tay ở công ty/cửa hàng/nhóm của bạn). Từ use case đó, bạn xây **đủ 4 deliverable**:

| Mã | Deliverable | Folder lab |
|----|-------------|-----------|
| — | Usecase Brief (input gốc của mọi thứ) | `00-usecase-brief/` |
| D1 | Agent Skill chạy được với agent | `01-agent-skill/` |
| D2 | Workflow n8n theo vòng e2e-test-first | `02-n8n-e2e-loop/` |
| D3 | MVP vibe coding (SDD) | `03-vibe-coding-mvp/` |
| D4 | Package + pitch slide HTML | `04-package-pitch/` |

## Nguyên tắc quan trọng nhất

**Không build từ đầu.** Toàn bộ tài liệu các buổi trước là kho tài nguyên của bạn — workflow n8n mẫu, schema, prompt, app React, template. Nhiệm vụ của bạn là **mượn → sửa → chạy trên use case mới**. Mỗi folder lab có mục "Tài nguyên mượn" chỉ rõ mượn gì ở đâu.

**Chống copy-y-nguyên:** e2e test phải FAIL ít nhất 1 vòng trước khi PASS (ghi run-log); skill phải có test của use case mới; MVP phải chạy trên input thật của bạn. Copy nguyên bản không vượt được nghiệm thu.

**Trung thực runtime-test:** không claim "chạy được" khi mới validate JSON hoặc mới render giao diện.

## Lộ trình 7 ngày (gợi ý)

| Ngày | Việc |
|------|------|
| Buổi 8 (18/08) | TH1 brief + resource map · TH2 khởi động D1/D2 · TH3 checklist + risk · TH4 pitch kế hoạch |
| 19–20/08 | Hoàn thành D1 + D2 |
| 21–23/08 | D3 MVP + ≥1 vòng cải tiến |
| 24/08 | D4 package + slide HTML · **lab 05: auto-check + tự chấm rubric** |
| **25/08 23:59** | **Deadline nộp** (xem `04-package-pitch/README.md` cách nộp) |

## Cách tổ chức thư mục làm bài của bạn

```
ho-ten-capstone/
├── usecase-brief.md            ← từ 00
├── resource-map.md             ← từ 00
├── d1-agent-skill/             ← từ 01
├── d2-n8n-e2e/                 ← từ 02 (workflow JSON + e2e test + run-log)
├── d3-mvp/                     ← từ 03
├── d4-package/                 ← từ 04 (package + slide HTML)
├── acceptance-checklist.md     ← từ buổi 8 TH3, tự tick trước khi nộp
└── risk-log.md                 ← từ buổi 8 TH3
```

Mọi đường dẫn tài nguyên mượn trong các prompt đều tính từ **thư mục gốc studentkit** (nơi chứa `00-khai-giang/`, `01-onboarding-automation/`, …).

## Process 3 tầng của đồ án

| Tầng | Lab | Bạn làm gì |
|------|-----|-----------|
| **Design** | 00 | Use case → brief chuẩn 7 mục (data contract) + resource map |
| **Implement** | 01–03 | 3 đường triển khai: skill · n8n e2e loop · MVP SDD |
| **Package** | 04 | Gộp + pitch HTML |
| **Evaluate** | 05 | Auto-check (kể cả chạy thật workflow trên n8n) + tự chấm rubric trước khi nộp |

Đi đủ 4 tầng = bạn đã triển khai trọn vẹn một use case AI Automation từ thiết kế đến đo lường.
