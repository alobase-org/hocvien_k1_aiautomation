# Self-Grading — Nam (lab 05, 24/08)

> Auto-check lần 1: 3 PASS · 2 FAIL (thiếu mục Ràng buộc; run-log thiếu evidence) → fix cả 2 → lần 2: **5 PASS + 1 SKIP** (n8n chưa chạy được trên máy tôi).

| Nhóm | Mức tự chấm | Lý do | Evidence |
|------|-------------|-------|----------|
| B | 4 | Brief 7 mục sau khi bổ sung Ràng buộc (lần đầu thiếu — auto-check bắt); resource map 3 path thật (đủ tối thiểu, không nhiều) | usecase-brief.md, resource-map.md |
| D1 | 5 | 3/3 PASS có output JSON thật; rule không-tự-chọn hoạt động sau 1 lần nhắc lại | d1-agent-skill/output/*.json |
| D2 | 3 | 5/5 chỉ ở cấu trúc; runtime KHÔNG test được (node 18); node validation còn B4 — khai rõ | run-log.md "chưa runtime-test" |
| D3 | 5 | 4/4 PASS kể cả giao-khung; 2 vòng cải tiến thật (crash mảng rỗng bắt bằng Console F12 — đúng lab 03) | d3-mvp, improve-log |
| D4 | 4 | Pitch sạch, 2 chỗ ⏳ công khai (ảnh, runtime) | pitch.html, acceptance-checklist |

Tự chấm tổng: ~82/100. Top 3 gap: (1) runtime n8n — nâng node rồi chạy auto-check [6] (~2h); (2) node validation chuyển booking schema (~2h); (3) ảnh demo chụp khi runtime.
