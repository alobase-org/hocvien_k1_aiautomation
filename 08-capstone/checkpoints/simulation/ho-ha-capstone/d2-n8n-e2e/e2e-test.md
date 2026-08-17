# E2E Test — Workflow xử lý yêu cầu bảo hành (Hà)

## Workflow dưới test
- Tên workflow n8n: `warranty-request-reviewer`
- Nguồn mượn: `04-contract-review/checkpoints/n8n-contract-review-solution.json` (khung B4)

## Bộ input mẫu (dữ liệu mô phỏng)
| # | Input | Nội dung | Ghi chú |
|---|-------|----------|---------|
| 1 | Yêu cầu còn bảo hành | "Máy giặt Electrolux em Mỹ Dung mua 15/03/2026, serial EL88231, giờ không vắt. SĐT 0900.000.012" | kỳ vọng: NHẬN BẢO HÀNH |
| 2 | Yêu cầu hết bảo hành | "Nồi chiên mua 01/01/2025 không nóng, serial AF1122, em Hùng 0900.000.015" | kỳ vọng: TỪ CHỐI kèm lý do |
| 3 | Yêu cầu thiếu thông tin | "Máy lạnh nhà em bị nhỏ nước, sửa giúp em" | kỳ vọng: CẦN BỔ SUNG (thiếu serial + ngày mua) |

## Asserts

| # | Assert | Cách kiểm | PASS khi |
|---|--------|-----------|----------|
| 1 | Workflow chạy hết không node đỏ | Execution pane n8n | Status success |
| 2 | Artifact `warranty-review.json` sinh ra đúng schema (khách, máy, serial, trong_bao_hanh, de_xuat, ly_do) | Mở file sau chạy | File tồn tại, đủ trường, đúng kiểu |
| 3 | Input #1 → `de_xuat = NHAN_BAO_HANH` | So nội dung | Đúng + có `ly_do` |
| 4 | Input #2 → `de_xuat = TU_CHOI` + lý do "hết 12 tháng" | So nội dung | Đúng + có dẫn chứng ngày mua |
| 5 | Input #3 → `de_xuat = CAN_BO_SUNG` + danh sách trường thiếu | So nội dung | Đúng + liệt kê thiếu gì |

## Kết quả mỗi lần chạy
| Lần | Ngày | Asserts PASS | Verdict | Ghi run-log |
|-----|------|---------------|---------|-------------|
| 1 | 18/08 (buổi học) | 0/5 | FAIL (chưa sửa workflow — còn nghiệp vụ hợp đồng) | vòng 1 |

## Friction lúc viết test
- [F3] Ban đầu không biết ghi "cách kiểm" cho assert 2 (schema là gì?) — phải mở `04-contract-review/templates/clause.schema.json` xem mẫu mới hiểu. Lab 02 README có gợi ý nhưng_prompt 05 không giải thích "schema là gì" cho người chưa đọc B4 kỹ.
