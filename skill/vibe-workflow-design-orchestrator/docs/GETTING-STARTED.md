# Getting Started — vibe-workflow-design-orchestrator

## 30 giây đầu tiên

1. Cài đặt (xem `INSTALL.md`).
2. Mở Claude Code, gọi: `/vibe-workflow-design-orchestrator`.
3. Nêu 1 use-case: *"Giúp tôi thiết kế lại quy trình [X]"* — Conductor sẽ dẫn qua 6 pha móc nối.

## Pipeline 6 pha (W1 → W7)

Mỗi pha: **output pha N = input pha N+1**. KHÔNG sinh tài liệu rời.

| Pha | Output | Prompt |
|-----|--------|--------|
| W1 Use-case prioritization | Ma trận Hiệu quả × Độ phức tạp, top-3 | `prompt/01-usecase-impact-matrix.md` |
| W2 as-is → ESIA to-be | Bảng 5 cột → bảng to-be + AI/Người + HITL | `prompt/02-workflow-design-esia.md` |
| W3 Production hardening | 4 lớp (fallback/log/edge/HITL) + 6 thuộc tính | `prompt/03-production-hardening.md` |
| W4 Mermaid | Sơ đồ ≤8 node, AI xanh, HITL đỏ | `prompt/04-mermaid-diagram.md` |
| W5 Infographic | Prompt render ảnh workflow | `prompt/05-generate-workflow-image.md` |
| W6 Leadership deck | Deck CRAFT 5 phần + lộ trình 30 ngày | `prompt/06-notebooklm-leadership-deck.md` |
| W7 Package + validate | Workflow Design Doc 7 phần (template: `output/templates/workflow-design-doc-template.md`) | — |

## 3 use case phổ biến

**1. "Tôi muốn tự động hoá quy trình X nhưng chưa biết thiết kế thế nào"**
→ Chạy trọn W1→W7. Use-case có PII? Chạy `anonymizer.py` ở W0 trước.

**2. Webinar / lab / học viên tự làm bài tập workflow design**
→ Dùng `synthetic-data/company-dong-duong-thuongmai.md` (công ty giả, zero PII)
làm input. Mỗi pha có sample fallback trong `synthetic-data/sample-*.md`.

**3. Rà soát quy trình đang chạy tay, đề xuất automation cho lãnh đạo**
→ Tập trung W2 (as-is/to-be) + W3 (hardening) + W6 (deck). Giao W7 template ráp lại.

## Khi bị stuck

`test/checkpoint-rescue.md` — map "stuck ở pha X → xem sample nào / checkpoint nào".

## Quy tắc vàng (KHÔNG thương lượng)

- **BR-W2:** Bước tiền bạc / PII / quyết định ảnh hưởng người → **BẮT BUỘC HITL**, không automate hoàn toàn.
- **BR-W4:** KHÔNG bịa số liệu. Chưa đo → ghi `[cần đo]`.
- **BR-W5:** Use-case minh hoạ giữ dumb/simple; KHÔNG mention skill nội bộ.

## Tuỳ chỉnh

Skill tổng quát — không gắn company cụ thể. Nếu build cho 1 doanh nghiệp trong context
`vibe-aiworkforce`/`vibe-company-orchestrator`, lưu theo COMPANY_ROOT convention của skill cha
thay vì `~/.claude/skills/`.

Không có placeholder `[CUSTOMIZE: ...]` nào — sẵn sàng dùng ngay.
