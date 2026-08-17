# Workflow Design Package — Content Engine (Buổi 6)

> Bám chặt `../lab.md` (Content Engine · n8n + Hybrid AI Automation) và `../luong-nghiep-vu.md` (as-is nghiệp vụ gốc).
> Tư duy mới B6: **Hybrid Architecture (n8n + AI Agent + Vibe App) + Schema kế thừa (harness nhẹ) + Cổng duyệt dừng cứng ở Approved**.
> Đây là **tài liệu giảng dạy/worked example** cho học viên buổi 6, không phải bản pitch nội bộ thật — xem ghi chú minh bạch ở `output/06-leadership-deck.md`.

## Cấu trúc — output/ vs process/ (2026-08-11, tách rõ)

Thư mục tách làm 2 phần theo đúng bản chất nội dung — không lẫn deliverable với nhật ký/bằng chứng:

- **`output/`** — deliverable thật của từng pha W0-W7 (bảng, sơ đồ, deck, design doc). Đây là thứ dùng để giảng dạy/tham chiếu khi đứng lớp.
- **`process/`** — nhật ký thiết kế, lý do đổi hướng, tự đánh giá độ tin cậy, log phát triển test, execution log thô. Đây là thứ dùng để hiểu "vì sao lại làm vậy" hoặc audit lại quyết định cũ — không cần đọc khi giảng dạy thường ngày.
- **Root** — `README.md` (file này) và `workflow-design-package.json` (manifest schema-valid, `output_ref` trỏ vào `output/`, `evidence` trỏ ra ngoài package tới nguồn sự thật thật).

### `output/` — 6 pha móc nối (W0→W7)

| Pha | File | Deliverable |
|-----|------|-------------|
| W0 Intake | `output/00-intake.md` | Use-case làm rõ + compliance |
| W1 Ma trận | `output/01-usecase-matrix.md` | 10 use-case + Top-3 → pick #1 |
| W2 As-is→ESIA | `output/02-as-is-tobe.md` | As-is 7 bước nguyên bản + to-be + phạm vi bị cắt |
| W3 Hardening | `output/03-hardening.md` | Bảng hardening 4 lớp + cột "Kiểm chứng bằng" + compliance note |
| W4 Mermaid | `output/04-mermaid.mmd` | Flowchart LR, 8 node, AI+HITL+2 fallback |
| W5 Infographic | `output/05-image-prompt.md` | 4 ảnh tái sử dụng từ lab_6 + prompt gốc |
| W6 Deck | `output/06-leadership-deck.md` | CRAFT 8 slide + lộ trình 30 ngày + ghi chú minh bạch |
| **W7 Design Doc** | `output/workflow-design-doc.md` | **7 phần ráp** (output cuối) |
| Foundation (4 TH) | `output/b6-foundation-n8n-hybrid.md` | Nền n8n + Hybrid Architecture — ref cho Track B |
| Use-case core | `output/esia-usecase.md` | Sunrise Kids TH1-TH4b + Track B customize + 8 điều cấm |
| Ảnh minh hoạ | `output/*.png` (4 file) | `before_after_diagram.png`, `system_architecture_diagram.png`, `horizontal_infographic.png`, `storytelling_infographic.png` |

**Quy tắc móc nối:** output pha N = input pha N+1 (các file trong `output/` tham chiếu lẫn nhau bằng tên file trần, cùng thư mục). Không sinh tài liệu rời.

### `process/` — nhật ký & bằng chứng, không phải deliverable

| File | Nội dung |
|------|----------|
| `process/02-changelog.md` | Lý do đổi hướng thiết kế TH1 (HITL 1 cổng → 2 cổng), 2026-08-09 |
| `process/03-hardening-evidence.md` | Lớp Judge (thiết kế + so sánh B5), tự đánh giá 6 thuộc tính độ tin cậy, nhật ký 14 test case TH4a/TH4b (`validate-b6-n8n-app.py`) |
| `process/execution_log.jsonl` | Log thực thi thô của validator |

### Root

| File | Vai trò |
|------|---------|
| `workflow-design-package.json` | Manifest schema-valid, `output_ref` trỏ vào `output/`, `evidence` (verbatim_quote) trỏ ra nguồn sự thật ngoài package, `confidence=0.8`, `need_review=true` |

## SLO đạt

- W1: 10 use-case, 1 ưu tiên #1 rõ ràng ✅
- W2: 7 bước as-is nguyên bản (không rút gọn), mỗi bước to-be có E/S/I/A, HITL bắt buộc ở bước duyệt ✅
- W3: đủ 4 lớp hardening + cột kiểm chứng bằng test thật cho TH1-TH3; TH4a/TH4b ghi rõ là gap kèm 10 test đề xuất ✅
- W4: 8 node (≤8), 1 node AI, 1 node HITL, 2 node fallback ✅
- W6: 8 slide, lợi ích ghi rõ "kỳ vọng" vs "đã đo", 0 số bịa (dùng `[cần đo]`) ✅

## Business rules tuân thủ

- **BR-W2 (CRITICAL, mạnh hơn B4):** Quyết định "Approved" LUÔN thuộc người phụ trách marketing — không có trạng thái `Published`, không có node/nút đăng bài, dù chỉ đề xuất.
- **BR-W3:** Chain N→N+1 (angle→draft→assets→Content_Queue→Publish_Log).
- **BR-W4:** Số chưa đo → `[cần đo]` (không bịa) — áp cả cho lợi ích "kỳ vọng" trong leadership deck.
- **BR-W5:** Minh bạch: leadership deck ghi rõ phần đào tạo K1 là quy tắc có sẵn của skill sinh tài liệu, không phải ROI trung lập.
- **BR-W6:** Mermaid ≤8 node, node AI cam, ≥1 node HITL đỏ.
- **BR-W7:** Ảnh AI sinh không tham chiếu ai thật → được phép có người/trẻ em (khác ảnh chụp thật cần consent) VÀ tối đa 1 dòng tiêu đề/CTA ngắn ≤8 từ (test thật: model render dấu tiếng Việt đúng); nội dung dài hơn vẫn để trống cho Canva, kiểm bằng test.
- **BR-W8 (mới, riêng B6):** Không tự nhận "test-driven" cho bước chưa có test tự động — TH4a/TH4b ghi rõ "KHÔNG CÓ test tự động" thay vì làm tròn thành "một phần" cho đẹp.

## Validate

```bash
python3 ../../../../skill/vibe-workflow-design-orchestrator/script/validator.py \
  --run-all \
  --artifact workflow-design-package.json \
  --schema ../../../../skill/vibe-workflow-design-orchestrator/schema/workflow-design-package.schema.json \
  --source ../lab.md
```

> Lưu ý: README của buổi 4 tham chiếu `~/.claude/skills/vibe-workflow-design-orchestrator/...` — skill thực tế nằm trong repo tại `giao_trinh/skill/vibe-workflow-design-orchestrator/`, không phải thư mục global `~/.claude/skills/`. Lệnh trên dùng path tương đối đúng trong repo.

Kiểm riêng 3 artifact TH1-TH3 (độc lập với package thiết kế này):

```bash
python giao_trinh/scripts/validate-b6-artifacts.py
```

## Downstream

- Track A (G6a): HV build TH1→TH4a→TH4b trong n8n + App theo `output/workflow-design-doc.md` §7.
- Track B (G6b): HV customize sản phẩm/thương hiệu riêng theo `../prompts/custom-input-prompt.md`, giữ nguyên 3 schema + 4 lớp + cổng duyệt dừng ở Approved.
- Scoring TH1-TH3: `giao_trinh/scripts/validate-b6-artifacts.py`. Scoring TH4a/TH4b: kết hợp checklist thủ công (`../checkpoints/checkpoint-bt4.md`) + `giao_trinh/scripts/validate-b6-n8n-app.py` (14 test tĩnh, xem nhật ký `process/03-hardening-evidence.md` mục 3).
