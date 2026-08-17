# Capstone Hà — Xử lý yêu cầu bảo hành tự động

> Mở file này trước tiên.

Use case: khách gửi yêu cầu bảo hành qua email/Zalo → đề xuất nhận/từ chối/bổ sung kèm lý do theo chính sách 12 tháng, trả lời khách soạn sẵn, log CSV.

Package chứa gì:
- `usecase-brief.md` + `resource-map.md` — input gốc (lab 00)
- `d1-agent-skill/` — skill `warranty-request-processor` (SKILL.md + kb + test 3/3 PASS + output thật)
- `d2-n8n-e2e/` — workflow `workflow-warranty-request.json` (khung B4 chuyển nghiệp vụ) + e2e-test 5 assert + run-log 3 vòng (vòng 1 FAIL)
- `d3-mvp/` — app `index.html` (mở là chạy, xem RUN.md) + spec-kit + improve-log 3 vòng
- `d4-package/pitch.html` — slide pitch 6 trang
- `anh-demo/` — (trống trong simulation: GV chụp thật khi runtime-test; khi HV thật nộp, ảnh bắt buộc do chính HV chụp)
- `acceptance-checklist.md` + `risk-log.md`

Phần chưa runtime-test (xem run-log): webhook Zalo thật, node schema validation còn của B4, batch 10 tin.
