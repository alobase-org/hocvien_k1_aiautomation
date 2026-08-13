# Workflow Design Package — AI Video Production (Buổi 7)

> Bám chặt `../lab.md` (Video Production Workflow) và `../luong-nghiep-vu.md` (as-is nghiệp vụ gốc).
> Tư duy mới B7: **Engine 4 lớp độc lập công cụ (schema → content artifact → media canary → engine spec) + cổng cứng duyệt ảnh trước khi tốn credit video + kỷ luật `runtime_evidence`**.
> Đây là **tài liệu giảng dạy/worked example** cho học viên buổi 7, không phải bản pitch nội bộ thật — xem ghi chú minh bạch ở `output/06-leadership-deck.md`.
> Sinh theo pipeline W0→W7 của `giao_trinh/skill/vibe-workflow-design-orchestrator/`, đối chiếu với draft có sẵn tại `v2.0-workflow-mindset/Output_B7/` (dùng nguồn as-is khác — xem `output/02-as-is-tobe.md` mục nguồn).

## Cấu trúc

- **`output/`** — deliverable thật của từng pha W0-W7 (bảng, sơ đồ, deck, design doc). Dùng để giảng dạy/tham chiếu khi đứng lớp.
- Root — `README.md` (file này) và `workflow-design-package.json` (manifest schema-valid, `evidence` trỏ ra nguồn sự thật thật).

### `output/` — 7 pha móc nối (W0→W7)

| Pha | File | Deliverable |
|-----|------|-------------|
| W0 Intake | `output/00-intake.md` | Use-case làm rõ + compliance |
| W1 Ma trận | `output/01-usecase-matrix.md` | 10 use-case + Top-3 → pick #1 |
| W2 As-is→ESIA | `output/02-as-is-tobe.md` | As-is 7 bước nguyên bản (`../luong-nghiep-vu.md`) + to-be (bước 1-5) + phạm vi bị cắt (bước 6/7) |
| W3 Hardening | `output/03-hardening.md` | Bảng hardening 4 lớp + cột "Kiểm chứng bằng" (checklist thủ công — chưa có script tự động) + compliance note + tự đánh giá 6 thuộc tính |
| W4 Mermaid | `output/04-mermaid.mmd` | Flowchart LR, 8 node, 2 AI, 2 HITL, 2 fallback |
| W5 Infographic | `output/05-image-prompt.md` | 3 prompt render ảnh — **cả 3 ảnh đã render** (khác B6, không có ảnh có sẵn để tái sử dụng nên phải render mới) |
| W6 Deck | `output/06-leadership-deck.md` | CRAFT 9 slide + lộ trình 30 ngày + ghi chú minh bạch |
| **W7 Design Doc** | `output/workflow-design-doc.md` | **7 phần ráp** (output cuối) |

**Quy tắc móc nối:** output pha N = input pha N+1 (các file trong `output/` tham chiếu lẫn nhau bằng tên file trần, cùng thư mục). Không sinh tài liệu rời.

### Khác biệt so với package Buổi 6

| | Buổi 6 (Content Engine) | Buổi 7 (AI Video Production) |
|---|---|---|
| As-is nguồn | `06-content-engine/luong-nghiep-vu.md` — 7 bước, đội marketing SME | `07-ai-video/luong-nghiep-vu.md` — 7 bước, nối tiếp bước 3 của B6, đội dựng video chuyên nghiệp mà SME nhỏ không có |
| Ảnh minh hoạ | Tái sử dụng 4 PNG có sẵn từ `v2.0-workflow-mindset/lab_6/output/` | 3 prompt tự viết mới, **đã render đủ 3/3** (không có ảnh có sẵn để tái sử dụng) |
| Script validate tự động | `giao_trinh/scripts/validate-b6-artifacts.py` + `validate-b6-n8n-app.py` (14 test) | **Chưa có** — chỉ checklist thủ công `checkpoint-bt1.md`...`checkpoint-bt4.md` |
| Bằng chứng chạy thật | `checkpoint-bt4.md` "✅ Đã validate trên instance thật" | **Chưa có** — package dừng ở thiết kế + checklist, xem `03-hardening.md` mục 3 |
| Draft tham khảo | `v2.0-workflow-mindset/lab_6/output/` | `v2.0-workflow-mindset/Output_B7/` |

## SLO đạt

- W1: 10 use-case, 1 ưu tiên #1 rõ ràng ✅
- W2: 7 bước as-is nguyên bản (không rút gọn), mỗi bước to-be có E/S/I/A, HITL bắt buộc ở 2 cổng duyệt (ảnh + clip) ✅
- W3: đủ 4 lớp hardening; cột "kiểm chứng bằng" ghi trung thực "KHÔNG CÓ test tự động" thay vì làm tròn cho đẹp ✅
- W4: 8 node (≤8), 2 node AI, 2 node HITL, 2 node fallback ✅
- W6: 9 slide, lợi ích ghi rõ "kỳ vọng" vs "đã đo", 0 số bịa (dùng `[cần đo]`) ✅

## Business rules tuân thủ

- **BR-W2 (CRITICAL):** Không sinh video từ storyboard chưa duyệt (AT1 giáo án B7) — cổng cứng, AI không được tự APPROVE.
- **BR-W3:** Chain N→N+1 (schema→scene→storyboard→clip→engine spec).
- **BR-W4:** Số chưa đo → `[cần đo]` — áp cả cho lợi ích "kỳ vọng" trong leadership deck.
- **BR-W5:** Minh bạch: leadership deck ghi rõ phần đào tạo K1 là quy tắc có sẵn của skill sinh tài liệu, không phải ROI trung lập.
- **BR-W6:** Mermaid ≤8 node, node AI cam, ≥1 node HITL đỏ.
- **BR-W7:** Không clone mặt/giọng người thật khi chưa consent văn bản; ảnh trẻ em kế thừa nguyên tắc B6 (chỉ AI sinh, style reference synthetic).
- **BR-W8 (kế thừa từ B6):** Không tự nhận "test-driven" cho bước chưa có test tự động — mọi bước TH1-TH4B ghi rõ "KHÔNG CÓ test tự động" thay vì làm tròn thành "một phần" cho đẹp.

## Validate

Đã chạy và **PASS** (2026-08-12, tái chạy sau khi chèn đủ 3 ảnh render): schema OK, 10/10 evidence verified, confidence 0.75 ≥ 0.7 — xem `output/execution_log.jsonl`.

```bash
# Trên Windows, bắt buộc set UTF-8 trước (script đọc file .md tiếng Việt, mặc định charmap cp1252 sẽ crash)
PYTHONUTF8=1 PYTHONIOENCODING=utf-8 python ../../../../skill/vibe-workflow-design-orchestrator/script/validator.py \
  --run-all \
  --artifact workflow-design-package.json \
  --schema ../../../../skill/vibe-workflow-design-orchestrator/schema/workflow-design-package.schema.json \
  --source ../lab.md --source ../luong-nghiep-vu.md \
  --source ../checkpoints/checkpoint-bt3.md --source ../checkpoints/checkpoint-bt4.md \
  --source ../prompts/bt1-prompt.md --source ../prompts/bt4b-prompt.md \
  --source ../../../01-giao-an/buoi-07-ai-video.md
```

## Downstream

- Track A: HV build TH1→TH4A→TH4B theo `output/workflow-design-doc.md` §7.
- Track B: HV đổi sang kịch bản thật của mình qua `../prompts/custom-input-prompt.md`, giữ nguyên 3 schema + 2 cổng duyệt (ảnh + clip) + `runtime_evidence`.
- Scoring: checklist thủ công `../checkpoints/checkpoint-bt1.md`...`checkpoint-bt4.md`. Chưa có script validate tự động — đề xuất Tuần 1-2 ở `output/06-leadership-deck.md`.
