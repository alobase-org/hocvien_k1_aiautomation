# Test Run — cskh-reply-drafter (Khánh, 19/08)
Chạy script Python theo workflow SKILL.md (classify + alias + tra bảng vòng cứng).

| TC | Loại | ID | Verdict |
|----|------|-----|---------|
| TC1 | HOI_GIA+HOI_TON_KHO | P01 | PASS |
| TC2 | HOI_TON_KHO | P02 | PASS |
| TC3 | KHIEU_NAI | P04 | PASS |
| TC4 | HOI_BAO_HANH | P03 | PASS |
| TC5 | KHAC | None | PASS |

Evidence: `output/tc{1..5}-reply-draft.json` + `output/cskh-log.csv` — 5/5.

## Friction
- TC5 lần đầu match nhầm "op" trong "shop" (substring bug) → fix word-boundary (xem exec-log seq 13-15).
