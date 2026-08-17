# Test Run — room-booking-processor (Nam, 19/08 tối)

Cách chạy: fallback chat AI (dán SKILL.md + kb + test-case, mỗi TC dán lại kb — theo ghi chú lab 01).

| TC | Kết quả | Verdict |
|----|---------|---------|
| TC1 | XAC_NHAN (20/08 không trùng, 8≤12 người) | PASS |
| TC2 | TU_CHOI + dan_chung "P301 \| 19/08 \| 9:00–10:30" | PASS |
| TC3 | DE_XUAT_KHUNG_KHAC: 8:00-9:30, 9:30-11:00 — không tự chọn | PASS |

Evidence: `output/tc{1,2,3}-booking-review.json` + `output/reply-draft.md` (kèm package).

## Friction
- Lần chạy đầu TC3 AI tự chọn luôn "8:00-9:30" — phải nhắc lại rule 2 ("Buổi sáng KHÔNG tự chọn"). Chat fallback cần dán lại rule mỗi lần — đúng như lab 01 cảnh báo.
