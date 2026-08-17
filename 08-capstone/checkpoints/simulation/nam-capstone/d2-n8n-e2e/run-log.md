# Run Log — Nam (booking-reviewer)

## Vòng 1 — 20/08 tối
- Test: 0/5 — KHÔNG chạy được gì.
- Evidence: chạy `capstone_auto_check.py` trên attempt 1 → `[FAIL] đồ thị nguyên vẹn — connection trỏ node không tồn tại: ['AI Booking Check (Gemini)']` (file `attempts/attempt1-broken.json`).
- Lỗi thấy: tôi đổi tên node AI thành "AI kiem tra booking" ngay trong UI cho dễ đọc — workflow chết sạch, không warning gì trước đó.
- Sửa gì: hỏi GV (xem exec-log seq 20-23) → làm lại rename theo đúng cách: đổi tên xong mở từng connection nối lại, rồi chạy auto-check xác nhận PASS.
- Kết luận: FAIL

## Vòng 2 — 21/08 trưa
- Test: 2/5 (assert 1,2 PASS — đồ thị + import OK; assert 3-5 không thể verify)
- Evidence: `attempts/attempt2-prose-rules.json` — prompt rule viết văn xuôi.
- Lỗi thấy: theo kịch bản test tay với AI (dán prompt attempt 2): input #3 "sáng thứ 5" → AI chọn luôn "8:00" — vi phạm rule không-tự-chọn; input #2 thiếu trích dòng lịch. Prompt văn xuôi làm AI bỏ qua 2 rule.
- Sửa gì: viết lại prompt theo đúng chỉ dẫn prompt 06: rule ĐÁNH SỐ R1-R5, mỗi rule 1 dòng exact + ví dụ phủ định ("'sáng sớm' KHÔNG đồng nghĩa 7:30").
- Kết luận: PARTIAL

## Vòng 3 — 21/08 tối
- Test: 5/5 Ở MỨC CẤU TRÚC (auto-check [3] PASS, prompt rule đánh số, đúng mapping use case).
- Evidence: `workflow-booking-request.json` (final) + auto-check chạy trong lab 05 ngày 24/08 (xem self-check).
- Kết luận: PASS-CẤU TRÚC

## Phần CHƯA runtime-test (khai rõ)
- **n8n chưa chạy được trên máy tôi:** cài `npx n8n start` báo lỗi node version (máy còn node 18, n8n cần ≥20) — chưa kịp nâng cấp trước deadline. GV runtime-check trên máy GV khi chấm sẽ ra kết quả cuối của assert 3-5.
- Node Schema Validation + Report vẫn của B4 (chưa chuyển booking schema) — sticky note trong workflow khai rõ.
- Chưa test batch 15 tin/tuần, chưa test webhook Zalo thật.

## Evidence tổng (24/08, sau auto-check)
- Cấu trúc: `capstone_auto_check.py` [3] PASS (final), [3] FAIL cho attempt1 (trích ở vòng 1) — file attempt kèm package.
- Runtime: **chưa runtime-test** (n8n cần node ≥20, máy tôi node 18 — risk #2). Không có execution ID, không có ảnh — không claim. GV runtime-check lúc chấm là kết quả cuối của assert 3-5.
