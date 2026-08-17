# Test Run — legal-clause-reviewer (Hùng, 19/08)
Chạy script Python theo workflow SKILL.md (đối chiếu vòng cứng KB, AI chỉ soạn đề xuất).

| TC | Mức | Rule | Verdict |
|----|------|------|---------|
| TC1 | CAO | A1/A3 | PASS |
| TC2 | CAO | A2 | PASS |
| TC3 | TB | B1 | PASS |
| TC4 | THẤP | C1 | PASS |
| TC5 | KHONG_RO | [cần trưởng phòng xem] | PASS |

Evidence: `output/tc{1..5}-review.json` — 5/5, kể cả KHONG_RO không bịa mức.

## Friction
- Lần chạy đầu TC1 bị map cả A1 lẫn A3 (2 rule cùng match) — quyết định ghi gộp "A1/A3" thay vì chọn 1 (trung thực hơn là che).
