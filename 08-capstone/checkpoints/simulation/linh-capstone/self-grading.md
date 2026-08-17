# Self-Grading — Linh (lab 05, 24/08)

> Chạy auto-check trước: 5/5 PASS [1]-[5], [6] SKIP lúc đầu → khởi động n8n → chạy lại: PASS (import + webhook chạy, đọc response OK). Sau đó tự chấm bằng skill chấm (kèm lab 05).

| Nhóm | Mức tự chấm | Lý do chính | Evidence |
|------|-------------|-------------|----------|
| Brief + Resource map | 5 | 7 mục, 3 tiêu chí đo được, 6 path thật | usecase-brief.md, resource-map.md |
| D1 | 5 | 4/4 test PASS có output thật | d1-agent-skill/output/recon-analysis.csv |
| D2 | 4 | 5/5 assert nhưng node validation còn B4 (khai rõ) | run-log.md vòng 3 |
| D3 | 5 | 6/6 unit test, 3 vòng cải tiến | improve-log, test log |
| D4 | 4 | Pitch sạch, nhưng ảnh demo mới có 1 | d4-package/pitch.html |

Tổng tự chấm: ~92/100 (chấm nương tay theo calibration).

**Top 3 gap:** (1) D2 node schema chưa chuyển — 2h; (2) ảnh demo còn ít — 30'; (3) chưa test volume — ghi kế hoạch, không fix tuần này.
