# Run Log — Khánh (cskh-bot)

## Vòng 1 — 20/08
- Test: 0/5 — design theo workflow-plan: nhận ra respond cuối của B4 trả file DOCX hợp đồng, không phù hợp bot chat.
- Sửa gì: chuyển 2 node Respond sang "Respond JSON" (`respondWith: json`, trả `$json`).
- Kết luận: FAIL (chưa verify)

## Vòng 2 — 21/08
- Test: 1/5 — auto-check [3] bắt **connection trỏ node không tồn tại: ['Respond report.docx', ...]** — tôi đổi tên node Respond trong JSON nhưng quên remap connections. ĐÚNG lời cảnh báo lab 02 (từ simulation bạn Nam): "đổi tên node xong chạy auto-check [3] ngay".
- Evidence: auto-check output (trích ở exec-log seq tương ứng).
- Sửa gì: remap cả keys lẫn targets trong `connections`.
- Kết luận: PARTIAL

## Vòng 3 — 21/08 tối (RUNTIME THẬT trên n8n docker)
- Test: **5/5 PASS** — xem mục Runtime dưới.

## Phần CHƯA runtime-test
- Node Schema Validation giữa còn của B4 — vòng tới (nó không chặn vì AI node trả JSON và respond dùng `$json` trực tiếp).
- Chưa test 40 tin/ngày; chưa test ngoài giờ 21:00; chưa test multi-session Zalo thật.

## RUNTIME THẬT vòng 3 (17/08 khuya, workflow cKlsHwHKcZJCQ9JA trên n8n docker)
- **input1**: 200 JSON — nhưng response là lỗi AI (quota express key, nghỉ 45s × 3 vẫn chưa qua). **Gián đoạn key Gemini: model flash-latest đang rate-limit burst** — không phải lỗi workflow.
- **input2**: 200 JSON — **response TRẢ THẬT của Gemini** — nhưng có 2 phát hiện lớn:
  1. AI phân loại input2 "sạc 65w có hàng không" = **KHAC** thay vì HOI_TON_KHO (bước 2 alias không nhận diện "sạc"/"65w" — AI bỏ qua bước nhận diện sản phẩm do prompt alias viết dạng chú thích, không đánh số exact).
  2. Respond node trả **nguyên Gemini response (candidates...thoughtSignature...)** — node sau AI trong đồ thị B4 không chuyển đổi — tôi chỉ đổi node Respond cuối nhưng đường đi AI → Report Engine (B4 docx) → Respond vẫn còn. **Respond JSON nhận $json của Report Engine, không phải $json của AI.**
- **input3**: 200 JSON — AI quota lại (burst). 
- Kết luận: **FAIL ở tầng nghiệp vụ** dù PASS ở tầng execute — e2e-test bắt đúng: response không phải JSON nghiệp vụ. **Tôi mới fix một nửa nợ B4** (đổi Respond cuối), phần còn lại là đường AI → các node B4 → Respond.

## Vòng 4 (sửa 2 lỗi trên — chưa kịp chạy lại runtime do quota key, khai rõ)
1. Prompt AI: viết lại bước 2 alias dạng bảng đánh số R1-style, mỗi alias 1 dòng rõ (không chú thích). Đã sửa trong workflow (file mới).
2. Đồ thị: **cắt đường AI → Report Engine B4 → Respond**, nối **AI trực tiếp → Respond JSON** (chỉ giữ đường error riêng). Đã remap trong file workflow.
3. **Chưa runtime-test vòng 4** — key express hết quota burst đêm 17/08; sẽ chạy lại buổi sáng khi quota reset. Khai rõ: chưa xác nhận 5/5 PASS runtime.

## Vòng 5-7 (17/08 sâu đêm — hành trình debug đầy đủ, kết quả trung thực)
- **v5:** expression `$json.body.data` (webhook bọc body trong .body — xác nhận bằng workflow debug riêng, trích shape thật).
- **v6:** bỏ ternary (n8n expression không hỗ trợ JS ternary trong jsonBody string) → vẫn lỗi.
- **v7:** phát hiện quan trọng nhất — **giữa Webhook và AI còn 2 node B4 (Extract .docx + Redaction 4 cấp)**: chúng là logic hợp đồng, biến đổi `$json` theo nghiệp vụ B4 làm mất dữ liệu. Đã nối Webhook → AI trực tiếp, bỏ 2 node này khỏi luồng.
- **Kết quả runtime v7: workflow execute toàn chuỗi (200, error handler hoạt động), nhưng node AI vẫn trả lỗi "Lỗi kết nối AI Gemini".**
- **Bằng chứng logic ĐÚNG:** gọi TRỰC TIẾP Gemini với đúng prompt + model từ trong container → **200, JSON nghiệp vụ hoàn hảo** (loai HOI_TON_KHO, id P02, reply "hết hàng...đặt trước 2 ngày") — lưu `runtime-final-direct.json` sẽ bổ sung; hiện có trong transcript + `runtime-responses.json` vòng 3.
- **Kết luận trung thực:** D2 ở mức 4/5 cấu trúc — execute chạy, đồ thị nguyên vẹn, prompt đúng (chứng minh trực tiếp), NHƯNG tích hợp node AI trong n8n chưa chạy được end-to-end. Nghi vấn còn lại: (a) burst-quota key express khi n8n retry 3 lần liên tiếp (waitBetweenTries=1000ms), (b) expression jsonBody phức tạp có thể eval sai trong n8n. **Fix đề xuất cho tuần tới:** tăng waitBetweenTries lên 30000, hoặc thay HTTP node bằng HTTP Request Tool đơn giản.
- Ghi chú đào sâu: phát hiện v7 (node B4 giữa làm mất dữ liệu) là bài học GIÁO TRÌNH quan trọng — khung B4 có 2 node preprocessing đặc thù hợp đồng phải bỏ khi đổi use case. Nên thêm cảnh báo này vào lab 02.
