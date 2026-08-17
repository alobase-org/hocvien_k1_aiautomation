# Test Run — warranty-request-processor (Hà, 19/08)

> Cách chạy: dán toàn bộ SKILL.md + kb + test-case vào Claude (chat) — dùng fallback "chạy qua chat, không qua agent" như lab 01 hướng dẫn. Ngày xử lý: 20/08/2026.

| TC | Kết quả chính | Verdict |
|----|---------------|---------|
| TC1 | hạn bảo hành 2027-03-15 → CON → NHAN_BAO_HANH (có ly_do + dan_chung "không vắt") | PASS |
| TC2 | hạn 2026-01-01 → HET → TU_CHOI (lý do "hết 12 tháng", dẫn chứng ngày mua 01/01/2025) | PASS |
| TC3 | THIEU_DU_LIEU: thiếu serial, ngay_mua, ho_ten, sdt → CAN_BO_SUNG, không bịa ngày mua | PASS |

Output thật: `output/tc{1,2,3}-warranty-review.json` (kèm package).

## Friction
- [F4] Sợ cài skill vào Claude Code ("đặt folder vào ~/.claude/skills" nghe kỹ thuật) → dùng fallback chat. Fallback này cứu được nhưng test qua chat không nhớ rule giữa 3 TC (phải dán lại kb mỗi lần) — ghi hạn chế trong package.
- [F5] TC2 lần chạy đầu AI trả "TU_CHOI vì lỗi người dùng" trong khi lỗi là "không nóng" (LOI_MAY) — phải nhắc lại rule "chỉ dùng quy tắc trong kb". Sửa bằng cách thêm 1 dòng vào prompt chạy: "phân tích theo từng điều khoản kb, nêu điều khoản nào áp dụng".
