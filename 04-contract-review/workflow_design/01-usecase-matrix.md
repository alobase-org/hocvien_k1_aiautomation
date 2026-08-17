# W1 — Ma trận ưu tiên Hiệu quả × Độ phức tạp

> BT1. Chấm 2 trục cho các use-case Pháp chế có thể automate, chọn quick win.
> Context: phòng Pháp chế 1–2 người, ~20–50 hợp đồng/tháng. (W0 intake)

## Cách chấm
- **Impact (1–5):** tác động nếu giải quyết (5 = rất lớn về chi phí/thời gian/chất lượng).
- **Difficulty (1–5):** nỗ lực triển khai (1 = data sẵn, quy tắc rõ; 5 = phi cấu trúc, nhiều role, dữ liệu rác).

## Ma trận 2×2
| | Phức tạp ≤2 (Dễ) | Phức tạp ≥3 (Khó) |
|---|---|---|
| **Impact ≥4 (Cao)** | LÀM NGAY (quick win) | LÊN KẾ HOẠCH |
| **Impact ≤3 (Thấp)** | KHI RẢNH | BỎ |

## Bảng use-case Pháp chế
| # | Use-case | Impact | Difficulty | Góc | Lý do |
|---|----------|--------|------------|-----|-------|
| 1 | Rà clause bịa + omission trên hợp đồng dịch vụ (redact→schema→evidence→report) | 5 | 2 | LÀM NGAY | Rủi ro pháp lý cao, quy tắc rõ (8 điều khoản bắt buộc), data text sẵn, LLM extract tốt |
| 2 | Rà trùng lặp điều khoản giữa các phụ lục | 3 | 2 | KHI RẢNH | Ít pain, đối tác ít khi khiếu nại |
| 3 | Đối chiếu giá trị hợp đồng vs báo giá/PO | 4 | 3 | LÊN KẾ HOẠCH | Giá trị dùng cho kế toán, cần nối hệ thống ERP |
| 4 | Tóm tắt hợp đồng cho lãnh đạo phi-pháp lý | 3 | 2 | KHI RẢNH | Tiện nhưng không giảm rủi ro pháp lý |
| 5 | Rà hợp đồng lao động (chấm dứt, Bảo hiểm XH) | 4 | 4 | LÊN KẾ HOẠCH | Nhiều role, luật đổi liên tục, checklist khác hợp đồng dịch vụ |
| 6 | Phát hiện điều khoản bất lợi từ template đối tác | 4 | 4 | LÊN KẾ HOẠCH | Phi cấu trúc, cần luật sư train |
| 7 | Trích deadline/giá trị vào Sheet theo dõi | 3 | 1 | KHI RẢNH | Dễ nhưng Impact thấp; gộp chung vào #1 |

## Top-3 nên automate TRƯỚC
1. **#1 — Rà clause bịa + omission (Contract Review):** Impact 5 × Difficulty 2 = quick win rõ ràng. Đây là use-case lab B4 chọn. Giảm rủi ro pháp lý chết người (hallucination) + tiết kiệm 2–3h/hợp đồng.
2. **#3 — Đối chiếu giá trị vs PO:** Impact 4, cần kế hoạch nối ERP — làm sau khi #1 chạy ổn.
3. **#5 — Hợp đồng lao động:** Impact 4 nhưng Difficulty 4 (luật đổi) — Track B HV customize sau.

## Kết luận pick
**Use-case thiết kế: #1 Contract Review** → input cho W2 (as-is→ESIA).

> SLI/SLO W1: ma trận đủ ≥5 use-case · có Top-3 · 1 use-case ở góc 🟢 LÀM NGAY → **đạt**.
