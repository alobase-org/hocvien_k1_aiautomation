# Test case — warranty-request-processor (Hà)

> Ngày xử lý giả định: 20/08/2026

## TC1 — còn bảo hành (kỳ vọng NHAN_BAO_HANH)
Input: "Máy giặt Electrolux em Mỹ Dung mua 15/03/2026, serial EL88231, giờ không vắt. SĐT 0900.000.012"

PASS khi `output/warranty-review.json`:
- `ho_ten=Mỹ Dung`, `serial=EL88231`, `ngay_mua=2026-03-15`, phân loại `LOI_MAY` (không vắt)
- `thoi_han=CON` (15/03/2026 + 12 tháng = 15/03/2027 > 20/08/2026)
- `de_xuat=NHAN_BAO_HANH` + `ly_do` + `dan_chung`

## TC2 — hết bảo hành (kỳ vọng TU_CHOI)
Input: "Nồi chiên mua 01/01/2025 không nóng, serial AF1122, em Hùng, 0900.000.015"

PASS khi:
- `thoi_han=HET` (01/01/2025 + 12 tháng = 01/01/2026 < 20/08/2026), dẫn chứng ngày mua
- `de_xuat=TU_CHOI` + lý do nêu "hết 12 tháng"

## TC3 — thiếu thông tin (kỳ vọng CAN_BO_SUNG / THIEU_DU_LIEU)
Input: "Máy lạnh nhà em bị nhỏ nước, sửa giúp em"

PASS khi:
- `thieu` chứa serial, ngay_mua (và có thể ho_ten, sdt)
- KHÔNG bịa ngày mua; `de_xuat=CAN_BO_SUNG` + liệt kê thiếu gì
