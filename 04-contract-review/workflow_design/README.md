# Workflow Design Package — Contract Review (Buổi 4)

> Sinh bởi `/vibe-workflow-design-orchestrator`. Bám chặt `../lab.md` (Contract Review · n8n + Harness Engineering).
> Tư duy mới B4: **Harness (schema+evidence) + Determinism (Python) + Redaction 4 cấp**.

## Cấu trúc — 6 pha móc nối (W0→W7)

| Pha | File | Deliverable |
|-----|------|-------------|
| W0 Intake | `00-intake.md` | Use-case làm rõ + compliance |
| W1 Ma trận | `01-usecase-matrix.md` | 7 use-case + Top-3 → pick #1 |
| W2 As-is→ESIA | `02-as-is-tobe.md` | Bảng as-is 6 bước + to-be + HITL note |
| W3 Hardening | `03-hardening.md` | 4 lớp + 6/6 thuộc tính (4 đạt, 2 một phần) |
| W4 Mermaid | `04-mermaid.mmd` | Flowchart LR, 8 node, AI+HITL+fallback |
| W5 Infographic | `05-image-prompt.md` | Prompt render ảnh + Mermaid source |
| W6 Deck | `06-leadership-deck.md` | CRAFT 8 slide + lộ trình 30 ngày |
| **W7 Design Doc** | `workflow-design-doc.md` | **7 phần ráp** (output cuối) |
| Foundation (4 TH) | `b4-foundation-n8n-harness.md` | Nền n8n + Harness (redact/schema/evidence/HITL) — ref cho Track B |
| Use-case core | `esia-usecase.md` | Hợp đồng dịch vụ + holdout + Track B customize + 8 điều khoản |
| Manifest | `workflow-design-package.json` | Schema-valid, evidence, confidence=0.92 |

**Quy tắc móc nối:** output pha N = input pha N+1. Không sinh tài liệu rời.

## SLO đạt
- W1: 7 use-case, 1 LÀM NGAY ✅
- W2: 6 bước as-is, mỗi bước to-be có E/S/I/A, HITL bước pháp lý+tiền bạc ✅
- W3: đủ 4 lớp hardening, 6/6 thuộc tính ✅
- W4: 8 node (≤8), 1 node AI, 2 node HITL ✅
- W6: 8 slide, ≥3 lợi ích đo được, 0 số bịa ✅

## Business rules tuân thủ
- **BR-W2 (CRITICAL):** Quyết định duyệt hợp đồng LUÔN human — workflow chỉ đề xuất+flag.
- **BR-W3:** Chain N→N+1 (redact→schema→evidence→report).
- **BR-W4:** Số chưa đo → `[cần đo]` (không bịa).
- **BR-W6:** Mermaid ≤8 node, node AI xanh, ≥1 HITL đỏ.
- **BR-W7:** PII redact 4 cấp trước khi qua AI; cấp 4 = cổng dừng.

## Validate
```bash
python3 ~/.claude/skills/vibe-workflow-design-orchestrator/script/validator.py \
  --run-all \
  --artifact workflow-design-package.json \
  --schema ~/.claude/skills/vibe-workflow-design-orchestrator/schema/workflow-design-package.schema.json \
  --source ../lab.md
```

## Downstream
- Track A (G4a): HV build 4 TH trong n8n theo `workflow-design-doc.md` §7.
- Track B (G4b): HV customize hợp đồng cơ quan (giữ package, đổi use-case+checklist trọng số).
- Scoring: `/vibe-score-workflow-design`.
