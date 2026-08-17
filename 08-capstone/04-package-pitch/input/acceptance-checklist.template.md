# Acceptance Checklist — Tự chấm trước khi nộp

> Dùng từ buổi 8 TH3, cập nhật tới khi nộp. Tick thật — GV sẽ runtime-check lại.

## Chung
- [ ] Brief đủ 7 mục, tiêu chí thành công đo được
- [ ] Resource map ≥3 tài nguyên, path thật
- [ ] Risk-log ≥3 rủi ro + cách giảm

## D1 — Agent Skill
- [ ] SKILL.md frontmatter name + description rõ trigger
- [ ] Folder: SKILL.md + template/kb + test
- [ ] ≥1 test PASS trên input của use case mình

## D2 — n8n e2e
- [ ] Workflow import + chạy không lỗi
- [ ] e2e-test ≥3 assert
- [ ] run-log ≥2 vòng, có ≥1 vòng FAIL, mỗi vòng có evidence (execution ID/ảnh)

## D3 — MVP
- [ ] spec-kit đủ PRD + ≥3 user stories + ≥3 test scenarios
- [ ] App chạy luồng input → output 1 lần đầu cuối
- [ ] improve-log ≥1 vòng cải tiến

## D4 — Package + pitch
- [ ] Package đủ cấu trúc chuẩn
- [ ] pitch.html mở được, 6 slide, không còn `[ĐIỀN ...]`
- [ ] Có ảnh demo thật

## Trung thực
- [ ] Mọi claim "chạy được" đều có bằng chứng (ảnh/run-log/output)
- [ ] Phần chưa runtime-test được ghi rõ
