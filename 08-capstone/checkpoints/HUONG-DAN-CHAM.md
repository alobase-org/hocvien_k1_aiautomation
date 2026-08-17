# Hướng dẫn chấm đồ án capstone (GV)

## Công cụ
- Rubric: `checkpoints/rubric-capstone.json` (capstone-k1-rubric-v1 — schema vibe-score-rubric, đã validate)
- Skill chấm: `vibe-ai-auto-score` (đã cài ở `~/.claude/skills/vibe-ai-auto-score/`) — skill chấm bài học viên có evidence + calibration nương tay

## Quy trình chấm 1 bài
1. HV nộp zip `capstone_[ho-ten]_[slug].zip` — giải nén vào thư mục tạm.
2. **Chạy auto-check trước khi đọc bài** (chống claim ảo, tiết kiệm ~10 phút/bài):
   ```bash
   python3 08-capstone/05-self-check/tool/capstone_auto_check.py <thư-mục-package-hv>
   ```
   Script tự: kiểm cấu trúc + đồ thị workflow + run-log + pitch, rồi **import workflow vào n8n + chạy 1 input qua webhook** (bước runtime-check cũ làm tay). FAIL cấu trúc → trả bài ngay chưa cần chấm. Lưu ý: script KHÔNG phân loại được nghiệp vụ đúng/sai trong output — GV vẫn đọc output của lần chạy đó.
3. **Runtime-check thủ công phần script chưa phủ** (chống claim ảo):
   - D2: import `d2-n8n-e2e/workflow-*.json` vào n8n, chạy 1 input mẫu — xác nhận không node đỏ, artifact sinh ra.
   - D3: mở app MVP theo `d3-mvp/RUN.md` (≤3 lệnh hoặc link preview), chạy 1 luồng input → output.
   - D4: mở `pitch.html`, bấm qua 6 slide, kiểm không còn placeholder.
   - D1: đọc SKILL.md + mở `test/test-run.md` đối chiếu evidence.
   - Đọc `self-grading.md` của HV: chỗ nào HV tự chấm cao hơn kết quả GV → hỏi đáp (đó là teaching moment tốt nhất).
3. Chạy vibe-ai-auto-score với rubric-capstone.json trên package — mỗi điểm phải có verbatim evidence trong package.
4. Đối chiếu criterion D4c (trung thực): checklist của HV khớp kết quả runtime-check của GV?
5. Tổng hợp + phản hồi từng HV trong 3 ngày sau deadline.

## Lưu ý calibration
- D2c (run-log ≥2 vòng có FAIL) là criterion chống copy quan trọng nhất — HV không có vòng FAIL nào thì hỏi đáp trực tiếp trước khi trừ.
- Chấm trên artifact, không chấm lời kể. HV ghi "chưa runtime-test" trung thực → không trừ phần khai báo, chỉ chấm phần đã claim.
- Điểm total = weighted sum theo rubric (validator recompute — không tự tính tay).
- Rule phân giải D3b: app không chạy lại được trên máy GV → tối đa mức 3 + yêu cầu HV gửi video 60 giây trong 48h để bảo vệ mức cao hơn.
- Rule exemplar: use case trùng "nghỉ phép" phải có input + chính sách khác exemplar, nếu không criterion B2/D2c bị xem là copy.

## Sau khi chấm
- Gộp kết quả lớp → báo cáo nội bộ `noi_bo/` (điểm từng criterion, điểm chung, gap thường gặp).
- Bài xuất sắc (≥85): xin phép HV đưa vào `_capstone/exemplar-hv/` làm exemplar cho K2.
