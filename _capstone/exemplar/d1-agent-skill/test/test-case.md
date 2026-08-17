# Test case — leave-request-processor

## TC1 — đơn hợp lệ (kỳ vọng DE_XUAT_DUYET)
Input: "Chào sếp, em Minh xin nghỉ phép annual 2 ngày 21-22/08 (báo hôm 15/08), việc em đã bàn giao cho Lan."

PASS khi `output/leave-review.json`:
- `ho_ten=Minh`, `loai_phep=annual`, `so_ngay=2`, `nguoi_ban_giao=Lan`
- Bảng đối chiếu: quy tắc báo trước 3 ngày → ĐẠT (15→21 cách 4 ngày làm việc)
- `de_xuat=DE_XUAT_DUYET`, có `ly_do` + `dan_chung`

## TC2 — đơn vi phạm (kỳ vọng DE_XUAT_TU_CHOI)
Input: "Em Minh xin nghỉ annual 4 ngày từ mai ạ." (gửi chiều hôm trước; không nêu bàn giao)

PASS khi:
- Quy tắc báo trước 3 ngày → VI PHẠM, dẫn chứng = "từ mai"
- Flag `BAN_GIAO_THIEU` (nguoi_ban_giao rỗng)
- `de_xuat=DE_XUAT_TU_CHOI` + ly_do nêu 2 lỗi

## Kết quả chạy thật (GV điền khi demo)
| TC | Verdict | Ghi chú |
|----|---------|---------|
| TC1 | PASS / FAIL | |
| TC2 | PASS / FAIL | |
