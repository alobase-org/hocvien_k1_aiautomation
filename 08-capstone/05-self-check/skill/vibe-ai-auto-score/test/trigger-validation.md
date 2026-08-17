# Trigger Validation — vibe-ai-auto-score

Test description có trigger đúng. Đọc description trong SKILL.md rồi đánh giá các câu sau.

## Should trigger (3–5 câu thực tế)
- [ ] "Chấm giúp mấy bài nộp của buổi 05 cho lớp mình"
- [ ] "Đọc folder 05-cskh-bot rồi sinh rubric chấm bài tập cho học viên"
- [ ] "chấm bài học viên buổi CSKH bot, chấm nương tay nhé"
- [ ] "Tạo marking scheme cho lab buổi 04 từ checkpoints của thầy"
- [ ] "Tổng hợp điểm lớp buổi 05 ra dashboard HTML"

## Should NOT trigger (câu bẫy)
- [ ] "Review chất lượng bài viết này giúp" → vibe-review
- [ ] "Tạo đề thi trắc nghiệm 50 câu" → skill đề thi
- [ ] "Phân tích doanh số trong Excel" → data analyst
- [ ] "Sửa lỗi code trong file này" → coding orchestrator
- [ ] "Chấm capstone Viettel production có anti-inflation cứng" → vibe-score-rubric (bản khắt khe)

## Đánh giá
- Nếu ≥4/5 "should trigger" match → trigger OK
- Nếu câu bẫy match → description đang quá rộng → siết EXCLUSION
- Nếu "should trigger" không match → thiếu từ khóa "học viên/buổi/lab/checkpoints" → bổ sung TRIGGER

## Input contract check (riêng skill này)
- [ ] Skill DỪNG hỏi lại nếu input không phải folder buổi dạy (BR-10)
- [ ] Skill dùng `checkpoints/` làm chuẩn 10/10 để hiệu chỉnh descriptors
- [ ] Skill chấm nương tay: bài 70% cốt lõi → ~7/10 (kb/student-grading-calibration)
