# Test case — room-booking-processor (Nam)

> Ngày xử lý: 19/08/2026, lịch theo kb/room-schedule.md

## TC1 — xác nhận được (kỳ vọng XAC_NHAN)
"Cho phòng HC đặt P301 thứ 4 (20/08) 9:00-10:30 họp nhóm marketing 8 người, cần máy chiếu. — Dũng"
PASS khi: không trùng (19/08 mới có lịch), sức chứa OK, có reply-draft.

## TC2 — trùng lịch (kỳ vọng TU_CHOI)
"Đặt P301 19/08 9:00-10:30 họp giao ban 10 người. — Hoa"
PASS khi: TU_CHOI + dan_chung trích dòng "P301 | 19/08 | 9:00–10:30 | Mỹ Linh".

## TC3 — mơ hồ buổi sáng (kỳ vọng DE_XUAT_KHUNG_KHAC)
"P302 sáng thứ 5 (21/08) họp khách hàng 15 người. — Khang"
PASS khi: liệt kê ≥2 khung sáng còn trống (8:00-9:30, 9:30-11:00...), KHÔNG tự chọn.
