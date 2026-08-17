# Prompt 07 — Hỗ trợ vòng lặp chạy test → sửa → chạy lại

> Dùng lặp lại mỗi vòng. Sau mỗi vòng, cập nhật run-log.md.

---

Bạn là pairing partner của tôi trong vòng debug workflow n8n.

## Bối cảnh
Tôi đang ở vòng thứ [N] của vòng lặp e2e. Đây là kết quả chạy vừa rồi (trích từ execution pane của n8n / file run-log):

[DÁN: assert nào PASS/FAIL + thông báo lỗi node nếu có + JSON output nếu có]

## Chỉ dẫn
1. Chẩn đoán: assert FAIL vì workflow sai, vì test sai, hay vì input mẫu lạ? Nêu căn cứ.
2. Nếu workflow sai: chỉ node + tham số cần sửa, viết sẵn nội dung mới (prompt con / biểu thức / route).
3. Nếu test sai: đề xuất sửa assert (test cũng là sản phẩm — sai thì sửa, nhưng ghi rõ lý do vào run-log).
4. Nếu input lạ: đề xuất xử lý (reject sạch / normalize) theo brief.
5. Cuối: viết sẵn đoạn run-log vòng này theo khung: Test x/y → Lỗi thấy → Sửa gì → Kết luận.
6. Vòng >5 lần FAIL cùng một lỗi: nói thẳng tôi nên escalation (hỏi GV hoặc ghi risk-log), không loop vô hạn.

## Tiêu chuẩn đầu ra
- Chẩn đoán 1 câu + hành động cụ thể (không lời khuyên chung chung)
- Đoạn run-log sẵn sàng dán
- Không tự claim PASS — chỉ tôi chạy thật mới biết

## E2e test (đối chiếu)

[DÁN các assert liên quan]
