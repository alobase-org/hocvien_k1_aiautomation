# 07-capstone: Exemplar giảng viên

> GV dùng demo 15' buổi 8 (19:55–20:10), làm chuẩn so sánh khi chấm.
> Sync sang studentkit `_capstone/` theo manifest, chia cho học viên SAU khi GV demo xong (khung tham chiếu, không phải template copy).

## Nội dung
- `exemplar/usecase-brief.md`: brief use case "xử lý đơn xin nghỉ phép" (mức tối thiểu chuẩn)
- `exemplar/resource-map.md`: 6 tài nguyên mượn từ B4/B5/skill
- `exemplar/d1-agent-skill/`: skill mini hoàn chỉnh: SKILL.md + kb/ + test/
- `exemplar/d2-n8n-e2e/`: e2e-test + run-log 3 vòng (vòng 1 FAIL) + workflow JSON khung B4 đã chuyển nghiệp vụ
- `exemplar/d3-mvp/`: spec-kit + improve-log 3 vòng + app `index.html` chạy thật (3/3 scenario)
- `exemplar/pitch.html`: slide HTML 6 slide, mở trình duyệt là chạy

## Kịch bản demo 15'
1. (3') Mở pitch.html, bấm qua 6 slide, nói chuyện theo slide, không đọc nguyên văn.
2. (4') Mở d2-n8n-e2e/run-log.md: nhấn vòng 1 FAIL: "workflow mượn nguyên bản fail ngay vì nghiệp vụ khác, đó là bằng chứng tôi đã loop thật".
3. (4') Chạy thử live: mở skill d1 chạy TC1, hoặc mở n8n chạy workflow với đơn #1 (chuẩn bị sẵn tab).
4. (4') Chốt: 4 deliverable tương ứng 4 thư mục lab, "các bạn làm y hệt khung này với use case của mình, mức tối thiểu như tôi vừa show".

## Chuẩn bị trước buổi
- [ ] Kiểm tra pitch.html mở tốt trên máy chiếu (font và phím mũi tên)
- [ ] Điền GEMINI API key vào node "AI Extract + Policy Check" (key đang là placeholder) nếu demo qua node AI
- [ ] Mở `exemplar/d3-mvp/index.html`, dán đơn #1 chạy thử 1 lần (app chạy local không cần key)
- [ ] Nếu demo live: import workflow exemplar vào n8n local trước, chạy thử 1 lần
- [ ] Mở sẵn 3 tab: pitch.html · run-log.md · n8n/skill
