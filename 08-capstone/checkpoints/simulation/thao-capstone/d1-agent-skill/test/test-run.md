# Test Run — weekly-report-summarizer (Thảo, 19/08)
Chạy bằng script Python tự viết theo workflow SKILL.md (số liệu vòng cứng, AI chỉ viết câu).

| TC | Kết quả | Verdict |
|----|---------|---------|
| TC1 | Tổng 2,310,000,000đ, tăng +10.0%, không cảnh báo | PASS |
| TC2 | Tổng 1,800,000,000đ, giảm -14.3% → CẢNH_BAO | PASS |
| TC3 | THIEU_DU_LIEU (thiếu file tuần trước) | PASS |

Evidence: `output/tc{1,2,3}-summary.json`
