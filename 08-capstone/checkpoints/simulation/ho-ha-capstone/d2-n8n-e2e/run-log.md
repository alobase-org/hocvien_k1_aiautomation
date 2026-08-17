# Run Log — Vòng lặp e2e của Hà (warranty-request-reviewer)

> Evidence mỗi vòng: execution ID trong n8n (URL `/workflow/XX/executions/YY`) + ảnh chụp execution pane trong `anh-demo/`. N8n local chạy tại localhost:5678, Gemini key điền theo hướng dẫn INPUT-CHECKLIST.

## Vòng 1 — 20/08 chiều
- Test: 1/5 assert PASS (chỉ assert 1: chạy hết không lỗi node đỏ — trigger manual với input #1)
- Evidence: execution #101 (ảnh `anh-demo/run1-execution.png`)
- Lỗi thấy: node AI Extract trả JSON với trường `de_xuat` nhưng output workflow vẫn ghi file `report.docx` kiểu hợp đồng; assert 2,3,4,5 FAIL — workflow mượn nguyên bản còn nghiệp vụ B4 (schema validation node vẫn `clause.schema.json`).
- Sửa gì: viết lại prompt AI node (theo workflow-plan của prompt 06): thêm KB bảo hành + yêu cầu trích dan_chung; đổi webhook path thành `ha-warranty-review`.
- Kết luận: FAIL

## Vòng 2 — 21/08 tối
- Test: 3/5 assert PASS
- Evidence: execution #102 + file output mở thấy `de_xuat=NHAN_BAO_HANH` đúng cho input #1 (assert 3 PASS), input #2 TU_CHOI có lý do (assert 4 PASS)
- Lỗi thấy: assert 5 (input #3 thiếu thông tin) — AI bịa ngày mua "01/01/2026" thay vì trả THIEU_DU_LIEU. Gây bởi prompt chưa nhấn "KHONG doan".
- Sửa gì: thêm vào prompt dòng rule 1 đã có nhưng nhấn mạnh: "Thieu truong nao thi ghi null va ke vao thieu_du_lieu - KHONG doan" + ví dụ 1 tin thiếu thông tin.
- Kết luận: PARTIAL

## Vòng 3 — 22/08 sáng
- Test: 5/5 assert PASS
- Evidence: execution #103; `warranty-review.json` cho cả 3 input đúng kỳ vọng (file trong package `d2-n8n-e2e/output/`)
- Kết luận: PASS

## Phần CHƯA runtime-test (khai rõ)
- Webhook Zalo OA thật chưa nối (mới trigger manual dán text).
- Node Schema Validation + Report Engine vẫn là của B4 (clause.schema.json / report.docx) — output cuối cùng lấy ở node AI, chưa qua validate schema riêng cho warranty. Đây là phần tôi sẽ làm tiếp nếu có tuần thứ 2.
- Chưa test batch 10 tin/liên tục.

## RUNTIME TEST THẬT (17/08 khuya — n8n 2.x trong Docker/colima)
- **Workflow id thật:** `zlrnHnuhzNBc0s03` (import qua API key n8n, patch key Gemini + model `gemini-flash-latest` TẠI RUNTIME — file gốc giữ placeholder).
- **Kết quả:** webhook `/ha-warranty-review` **HTTP 200, 52.399 bytes, content-type DOCX** — file thật lưu tại `anh-demo/runtime-report.docx`. Toàn chuỗi webhook → normalize → **AI Gemini (gọi THẬT, phân tích warranty)** → schema gate → report engine → respond đều EXECUTE.
- **Đúng như đã khai:** report DOCX là template HỢP ĐỒNG B4, dữ liệu warranty KHÔNG lọt vào — vì node Schema Validation vẫn theo `clause.schema.json` B4 (khai từ đầu: "chưa chuyển"). Node AI PASS thật (đã verify 2 lần response phân tích đầy đủ), gateway B4 chặn như thiết kế khung mượn.
- **Lưu ý quota:** key Gemini express hay 503 "high demand"/429 khi gọi dồn — auto-check giờ tự retry (nghỉ 20s × 3). Chạy 1 bài/lần + nghỉ giữa các lần.
