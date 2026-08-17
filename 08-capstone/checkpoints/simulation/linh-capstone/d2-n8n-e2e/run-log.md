# Run Log — Linh (recon-analyzer)

## Vòng 1 — 20/08
- Test: 1/5 assert (chỉ assert 1 chạy hết)
- Evidence: execution #201, ảnh `anh-demo/linh-run1.png`
- Lỗi thấy: AI phân loại mọi dòng chênh dương thành CHIET_KHAU_CHUA_GHI kể cả chênh 333,777 (không bội 50k) — prompt đưa rule dạng văn xuôi, AI bỏ qua điều kiện "bội số 50.000".
- Sửa gì: viết lại rule trong prompt thành danh sách đánh số, mỗi rule 1 dòng điều kiện if — exact; thêm ví dụ phủ định ("333,777 KHÔNG phải bội 50k → KHONG_RO").
- Kết luận: FAIL

## Vòng 2 — 21/08
- Test: 4/5
- Evidence: execution #202
- Lỗi thấy: input #2 trả CHIET_KHAU_CHUA_GHI lần nữa — tôi phát hiện do khi dán CSV, dấu chấm nghìn làm AI hiểu sai phép trừ. 
- Sửa gì: thêm bước chuẩn hóa ở trước node AI (bỏ dấu chấm nghìn) — mượn ý node Normalize của B4.
- Kết luận: PARTIAL

## Vòng 3 — 22/08
- Test: 5/5 PASS. Evidence: execution #203.
- Kết luận: PASS

## Phần CHƯA runtime-test
- Node Schema Validation + Report vẫn theo B4 (chưa schema recon) — output đọc ở node AI.
- Chưa test 12 đại lý × 40 dòng full; mới test từng dòng đơn lẻ.
- Webhook nhận qua email thật chưa nối.
