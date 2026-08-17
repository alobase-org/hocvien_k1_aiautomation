# Prompt 03 — Viết SKILL.md hoàn chỉnh

> Input: `skill-design.md` từ prompt 02.

---

Bạn là kỹ sư đóng gói skill. Biến thiết kế dưới đây thành skill chạy được.

## Bối cảnh
Skill sẽ được cài vào agent (Claude Code hoặc tương tự) để chạy use case thật của tôi. Exemplar cấu trúc tôi tham khảo: `skill/vibe-workflow-design-orchestrator/SKILL.md`.

## Chỉ dẫn
1. Sinh `SKILL.md` hoàn chỉnh:
   - Frontmatter YAML: `name` (kebab-case, ngắn), `description` (nêu rõ khi nào trigger + khi nào KHÔNG)
   - Mục theo thứ tự: Mục tiêu → Input contract → Các bước thực hiện (workflow đánh số) → Output contract → Rules → Cách test
   - Mỗi rule giải thích LÝ DO ngắn theo sau (agent hiểu context tốt hơn lệnh trống)
2. Sinh các file kèm theo đúng cấu trúc folder trong thiết kế: template input, template output, kb (nếu thiết kế có).
3. Sinh 1 file `test/test-case.md`: input mẫu của use case tôi + output expected + tiêu chí PASS/FAIL.
4. Liệt kê chính xác: tôi cần đặt những file nào ở đâu để agent nhận skill.

## Tiêu chuẩn đầu ra
- SKILL.md ≤150 dòng, tiếng Việt, thuật ngữ Anh giữ nguyên
- Input/output contract nêu tên file + định dạng cụ thể
- Không bịa tính năng không có trong thiết kế

## Thiết kế skill

[DÁN skill-design.md]

## Cặp input/output mẫu của use case tôi

[DÁN 1–2 cặp mẫu]
