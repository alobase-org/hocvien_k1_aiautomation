---
name: recon-match-analyzer
description: >
  Phân tích dòng lệch công nợ giữa file nội bộ và sao kê đại lý: ghép theo so_dh,
  chênh lệch số tiền/ngày, đề xuất nguyên nhân (chiết khấu chưa ghi / sai ngày /
  trùng đơn / thiếu đơn). Kích hoạt khi nhận "bảng lệch công nợ", "phân tích
  discrepancy", "đối chiếu công nợ". KHÔNG dùng cho: hạch toán, thuế, thu hồi nợ.
---

# Recon Match Analyzer

## Mục tiêu
Nhận bảng các dòng lệch (đã ghép so_dh) → phân loại nguyên nhân từng dòng + email draft cho đại lý.

## Input contract
- `input/discrepancies.csv`: so_dh, khach_hang, tien_noi_bo, tien_sao_ke, ngay_noi_bo, ngay_sao_ke
- `kb/recon-rules.md`: rule phân loại nguyên nhân

## Workflow
1. Đọc CSV + rules. Thiếu cột → trả `{trang_thai:"THIEU_COT", thieu:[...]}`, không chạy tiếp.
2. Với mỗi dòng: tính chênh = tien_noi_bo - tien_sao_ke; so ngày.
3. Phân loại theo kb: CHIET_KHAU_CHUA_GHI (nội bộ > sao kê, bội số 50k tròn), SAI_NGAY (chênh ngày ≤3 ngày cuối tháng), TRUNG_DON (so_dh xuất hiện 2 lần), THIEU_DON (1 bên trống), KHONG_RO.
4. Xuất `output/recon-analysis.csv` (thêm cột nguyen_nhan + do_tin_cay) + `output/email-drafts.md` mỗi đại lý 1 draft.
5. Email draft: nêu dòng lệch + nguyên nhân đề xuất + nhờ xác nhận — KHÔNG đổ lỗi.

## Output contract
- `output/recon-analysis.csv` đủ cột mới; mỗi dòng KHONG_RO phải có 1 câu lý do
- `output/email-drafts.md` chỉ chứa draft, không tự gửi

## Rules
- Chênh không rơi vào pattern nào → KHONG_RO, không đoán "chắc do chiết khấu" (email sai nguyên nhân = mất lòng tin đại lý).
- TRUNG_DON phải liệt kê cả 2 dòng trùng, đừng bỏ 1 dòng.
- Mọi phân loại kèm do_tin_cay (cao/trung/thấp) dựa trên độ khớp pattern.

## Cách test
`test/test-case.md`: 4 dòng lệch mẫu + kỳ vọng phân loại + PASS/FAIL.
