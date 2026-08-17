# Acceptance Checklist — Hà (tự chấm, cập nhật 24/08)

## Chung
- [x] Brief đủ 7 mục, tiêu chí thành công đo được
- [x] Resource map ≥3 tài nguyên, path thật (6 dòng)
- [x] Risk-log ≥3 rủi ro + cách giảm

## D1 — Agent Skill
- [x] SKILL.md frontmatter name + description rõ trigger
- [x] Folder: SKILL.md + kb + test
- [x] ≥1 test PASS trên input bảo hành của mình

## D2 — n8n e2e
- [x] Workflow import + chạy không lỗi (chạy manual qua n8n local 24/08)
- [x] e2e-test ≥3 assert (5 assert)
- [x] run-log ≥2 vòng, có ≥1 vòng FAIL, có evidence (execution ID)

## D3 — MVP
- [x] spec-kit đủ PRD + 3 user stories + 3 test scenarios
- [x] App chạy luồng input → output 1 lần đầu cuối
- [x] improve-log ≥1 vòng (3 vòng)

## D4 — Package + pitch
- [x] Package đủ cấu trúc chuẩn
- [x] pitch.html mở được, 6 slide, không còn [ĐIỀN ...]
- [x] Có ảnh demo (3 ảnh chụp: n8n execution, app, log)

## Trung thực
- [x] Mọi claim "chạy được" có bằng chứng (ảnh/run-log/output)
- [ ] Phần chưa runtime-test được ghi rõ → còn 1 chỗ chưa ghi hết (webhook Zalo thật chưa test — đã ghi trong run-log nhưng chưa ghi vào pitch slide 5) ⏳ sửa trước nộp
