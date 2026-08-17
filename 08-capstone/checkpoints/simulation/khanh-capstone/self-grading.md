# Self-Grading — Khánh (lab 05, 24/08)

> Auto-check lần 1 (21/08): 3 PASS · 3 FAIL — 1 FAIL là pitch chưa có (đúng — làm D4 sau), 2 FAIL còn lại là runtime AI quota. Sau khi hoàn thiện D4: chạy lại — kết quả ghi ở dưới.

| Nhóm | Mức tự chấm | Lý do | Evidence |
|------|-------------|-------|----------|
| B | 5 | 7 mục, 3 tiêu chí đo được, 4+ path B4/B5 thật + khai cả chỗ bỏ (lab_tulam không hợp) | usecase-brief, resource-map |
| D1 | 5 | 5/5 PASS có output JSON thật + log CSV; fix alias-bẫy có improve-trail | d1-agent-skill/output/ |
| D2 | 4 | 4 vòng run-log runtime THẬT; bắt 2 lỗi nghiệp vụ lớn vòng 3; v4 đã fix đồ thị + prompt nhưng runtime v4 chưa chạy lại (quota) | run-log + runtime-responses.json |
| D3 | 5 | 5/5 PASS (2 vòng cải tiến thật); HITL + CSV hoạt động | test log 5/5 |
| D4 | 4 | Pitch sạch; ảnh demo ⏳ chờ runtime v4 | pitch.html |

Tự chấm tổng: ~87/100. Top 3 gap: (1) runtime v4 khi quota reset (~30'); (2) ảnh demo; (3) node schema validation B4 giữa luồng (không chặn nhưng nên ghi rõ hơn).
