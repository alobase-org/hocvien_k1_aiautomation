# Lab 01 — Deliverable D1: Agent Skill cho use case của bạn

## Mục tiêu
Đóng gói use case thành **1 skill chạy được với agent** (Claude Code / AI tương tự): agent đọc SKILL.md là biết làm gì, nhận input đúng định dạng, trả output đúng contract.

## File input cần cung cấp
- `input/INPUT-CHECKLIST.md` — checklist những file bạn phải chuẩn bị trước khi chạy prompt
- Bản thân `usecase-brief.md` (từ lab 00) — input chính
- 1–2 cặp input/output mẫu của use case bạn (để làm test)

## Prompt để chạy

| Prompt | Input | Output |
|--------|-------|--------|
| `prompt/02-design-skill.prompt.md` | usecase-brief + resource map | `skill-design.md` (kiến trúc skill) |
| `prompt/03-write-skill.prompt.md` | skill-design.md | `SKILL.md` + cấu trúc folder |
| `prompt/04-test-skill.prompt.md` | SKILL.md + mẫu input/output | `test-run.md` (kết quả test ≥1 PASS) |

## Các bước
1. Xong `INPUT-CHECKLIST.md` mới chạy prompt 02.
2. Prompt 02 sinh kiến trúc: tên skill, mô tả trigger, input contract, output contract, rules, test — kiểm tra khớp brief trước khi sang bước sau.
3. Prompt 03 sinh SKILL.md + các file kèm (templates/, kb/ nếu cần).
4. Cài skill vào agent của bạn rồi chạy prompt 04 để test trên input mẫu:
   - Claude Code: copy folder skill vào `~/.claude/skills/<ten-skill>/`, khởi động lại Claude Code, gõ tên skill để kiểm tra trigger.
   - Agent khác: đặt folder vào thư mục skills tương ứng theo tài liệu agent đó.
   - KHÔNG có agent? Fallback hợp lệ: dán toàn bộ SKILL.md vào chat AI thường + dán input mẫu, chạy các bước theo workflow trong skill, ghi rõ trong package là "chạy qua chat, không qua agent" (trừ nhỏ điểm trình bày, không rớt mức nghiệm thu). Lưu ý: chat không nhớ rule giữa các lần test — mỗi lần chạy test mới phải dán lại SKILL.md + kb.

## Vòng debug khi test FAIL (không viết lại từ đầu)
- FAIL ở 1 test case → chỉ chạy lại ĐÚNG case đó (dán lại SKILL.md + kb + input của case fail), không chạy lại cả 3.
- Nguyên nhân thường gặp: AI bỏ qua 1 rule → dán lại nguyên văn rule đó vào tin nhắn + yêu cầu "nêu điều khoản áp dụng"; thiếu dữ liệu mà AI tự bịa → nhắc rule "thiếu thì trả THIEU_DU_LIEU".
- Sửa gì phải sửa ở SKILL.md/kb (nguồn sự thật), không chỉ sửa trong chat — lần chạy sau chat không nhớ.

## Nghiệm thu (đếm được)
- [ ] `SKILL.md` có frontmatter `name` + `description` (description nói rõ khi nào trigger)
- [ ] Folder skill có tối thiểu: `SKILL.md` + 1 file template hoặc kb + 1 file test
- [ ] Input/output contract ghi rõ tên file, định dạng
- [ ] ≥1 test chạy PASS trên input mẫu **của use case bạn** (không phải test của tài nguyên mượn)
- [ ] Có ít nhất 1 rule kiểu "nếu thiếu dữ liệu thì hỏi lại, không tự bịa"

## Tài nguyên mượn (mở thật ra xem trước)
- `skill/vibe-workflow-design-orchestrator/SKILL.md` — exemplar cấu trúc SKILL.md chuẩn (frontmatter, mục, workflow) — mượn cấu trúc, KHÔNG mượn nghiệp vụ
- `skill/vibe-workflow-design-orchestrator/schema/` — cách tổ chức schema cho input/output contract
- `05-cskh-bot/templates/faq.json` + `chinh-sach-ho-tro.md` (B5) — mẫu tổ chức kho tri thức nếu use case của bạn cần KB
- `04-contract-review/templates/checklist-rui-ro.md` (B4) — mẫu viết rules dạng checklist
