# Usecase Brief — Đối chiếu công nợ đầu tháng (Linh)

> Học viên: Trần Ngọc Linh · kế toán công nợ công ty phân phối 80 người (dữ liệu mô phỏng) · Buổi 8 TH1

## [BẮT BUỘC] Bài toán
Đầu mỗi tháng, Linh nhận 2 nguồn: file công nợ nội bộ (kế toán) và sao kê công nợ từ 12 đại lý (email/file excel). Tự đối chiếu từng dòng: số đơn, số tiền, ngày thanh toán — lệch đâu thì lập bảng reconciled/discrepancy rồi email từng đại lý mục lệch. 12 đại lý × ~40 dòng, mất 1,5 ngày/tháng, hay lệch do ghi thiếu chiết khấu.

## [BẮT BUỘC] Người dùng
Người xử lý: Linh (kế toán công nợ). Người duyệt: kế toán trưởng. Người nhận output: đại lý (email mục lệch) + Linh + kế toán trưởng.

## [BẮT BUỘC] Input hàng ngày
Tháng 1 lần: file `cong-no-noi-bo.csv` (so_dh, khach_hang, so_tien, ngay_thanh_toan) + file `sao-ke-dai-ly.csv` cùng cấu trúc. Ví dụ dòng lệch: nội bộ 12,500,000 vs sao kê 12,000,000 (thiếu chiết khấu 500k).

## [BẮT BUỘC] Output mong muốn
`reconcile-report.md`: tổng khớp/lech, bảng discrepancy (so_dh, chênh lệch, nghi ngờ nguyên nhân), email draft cho từng đại lý có lệch. Kèm `reconcile-log.csv` (đại lý, khớp, lệch, tổng chênh).

## [BẮT BUỘC] Quy trình xử lý (tách theo loại bước)
1. (Quy tắc cứng) Chuẩn hóa 2 file về cùng kiểu (bỏ dấu chấm nghìn, ngày chuẩn YYYY-MM-DD).
2. (Quy tắc cứng) Ghép theo so_dh, so sánh so_tien + ngay_thanh_toan.
3. (AI phán đoán) Với dòng lệch: đề xuất nguyên nhân (chiết khấu chưa ghi / sai ngày / trùng đơn / thiếu đơn).
4. (Người duyệt) Kế toán trưởng duyệt email gửi đại lý (HITL).
5. (Cứng) Ghi log + xuất email draft.

## [BẮT BUỘC] Tiêu chí thành công (đo được)
- 100% dòng lệch được phân loại nguyên nhân, có dòng trong reconcile-log.csv
- Ghép đúng theo so_dh 40/40 dòng test; dòng lệch sai số tiền bị bắt 10/10 mẫu
- Rút thời gian đối chiếu từ 1,5 ngày xuống dưới 2 giờ

## Ràng buộc & công cụ sẵn có
Dữ liệu đại lý thật nhạy cảm → dùng dữ liệu mô phỏng theo mẫu fallback-inputs B6. Có n8n local, Claude Code, AI Studio. Ngân sách 0.
