# Dùng skill này để TỰ CHẤM đồ án capstone (cho học viên)

> Bản skill này là bản copy y nguyên skill giảng viên dùng để chấm đồ án capstone K1.

## Cài
```bash
cp -r skill/vibe-ai-auto-score ~/.claude/skills/
```
Khởi động lại Claude Code.

## Tự chấm
Trong thư mục package đồ án của bạn (`ho-ten-capstone/`), nói với Claude Code:
> "Dùng skill vibe-ai-auto-score. Chấm package này theo rubric `checkpoints/rubric-capstone.json` trong studentkit. Trước khi chấm, chạy `capstone_auto_check.py`. Xuất `self-grading.md` — chấm đúng mức, mỗi điểm kèm evidence trích từ package, không nể."

## Lưu ý
- Skill chấm **nương tay theo calibration** (`kb/student-grading-calibration.md`): làm được ~70% so với bài mẫu GV thì ~7/10. Đừng giật khi điểm thấp hơn mình tưởng — đó là điểm thật, fix rồi chấm lại.
- Điểm tự chấm KHÔNG phải điểm GV. GV sẽ chấm lại bằng cùng skill + runtime-check trên máy GV.
- Chấm tối đa 2 vòng rồi nộp — đừng polish vô tận.
