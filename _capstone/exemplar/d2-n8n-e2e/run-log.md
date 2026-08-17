# Run Log — Exemplar nghỉ phép

## Vòng 1
- Test: 2/4 assert PASS
- Lỗi thấy: node chuẩn hóa vẫn theo schema `clause.schema.json` của B4 — trường `loai_phep` bị drop; node output ghi `contract-review.json` thay `leave-review.json`.
- Sửa gì: thay Set node schema thành `leave-review` fields; đổi tên file output; thay prompt AI node "red-flag clauses" bằng "đối chiếu chính sách nghỉ phép" (giữ cấu trúc prompt 3 phần cũ).
- Kết luận: FAIL

## Vòng 2
- Test: 3/4
- Lỗi thấy: đơn #2 chạy ra `DE_XUAT_DUYET` — prompt mới chưa yêu cầu dẫn chứng điều khoản vi phạm.
- Sửa gì: thêm vào prompt: "mỗi kết luận trích điều khoản chính sách + câu chữ trong đơn; vi phạm nào cũng phải nêu".
- Kết luận: PARTIAL

## Vòng 3
- Test: 3/4 — PARTIAL.
- Evidence: prompt node đã chuyển nghiệp vụ (soi trực tiếp node trong n8n); assert 1 + 3 + 4 đạt khi GV chạy thử trước buổi (điền execution ID vào đây sau khi chạy: ____________).
- Còn assert 2 (file `leave-review.json` đúng schema): output node vẫn là `report.docx` của B4 — đây chính là "vòng còn lại" GV chỉ cho học viên thấy trong demo: đồ án của các bạn sẽ đóng nốt vòng này.

## Phần chưa runtime-test
- Chưa test webhook Zalo vào thật (mới trigger manual + file).
- Chưa test volume: mới chạy từng đơn, chưa chạy batch 8 đơn/tuần.

## Workflow artifact
- `workflow-leave-request.json` — khung mượn từ B4 (`04-contract-review/checkpoints/n8n-contract-review-solution.json`), đã đổi: tên workflow, webhook path (`b8-leave-review`), prompt AI node (nghiệp vụ nghỉ phép), sticky note trạng thái.
- **Phần CHƯA runtime-test / CHƯA chuyển**: node Schema Validation vẫn theo `clause.schema.json` của B4 (chưa đổi sang leave schema) — khi GV demo live chỉ chạy tới node AI Extract + đọc kết quả de_xuat; phần validate sẽ là bài tập minh họa "phần còn lại của vòng loop" cho học viên thấy.
- GV phải import + chạy thử 1 lần trước buổi (xem checklist README 07-capstone).
