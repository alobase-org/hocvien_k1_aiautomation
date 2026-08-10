# Dependency Map — vibe-workflow-design-orchestrator

Skill này **tự đứng được** — toàn bộ prompt, script, schema, template, synthetic-data
nằm gọn trong folder. Không có dependency cốt lõi bắt buộc.

## Downstream / Delegate (KHÔNG bắt buộc — dùng khi cần)

Đây là các skill được delegate ở đầu ra. Cài thêm nếu muốn chạy tiếp chuỗi value chain:

| Skill | Khi nào cần | Vai trò |
|-------|-------------|---------|
| `vibe-score-workflow-design` | Muốn chấm/thẩm định package vừa sinh | Đánh giá 6 tiêu chí, ra band điểm + tư vấn gap |
| `vibe-aiworkforce` | Đã chốt thiết kế, muốn build workforce/agent execute | Thi công AI workforce chạy to-be |
| `vibe-slide-orchestrator` | Muốn render deck PPTX thật từ W6 | Sinh slide trình lãnh đạo |
| `vibe-diagram-orchestrator` | Chỉ cần vẽ Mermaid rời, không cần cả package | Vẽ sơ đồ nhanh |
| `deep-research` | Cần research mở trước khi thiết kế | Thu thập bối cảnh |

## Công cụ runtime (local-first)

- **Python 3.9+** — chạy `validator.py`, `anonymizer.py`, `review_queue.py`.
- **Một LLM client** (Claude Code / Gemini / Antigravity / Codex) — dán prompt copy-paste
  hoặc chạy inline ở Planning mode.
- KHÔNG cần n8n, KHÔNG cần API key để chạy pipeline (n8n chỉ là một trong 3 nhánh
  automation gợi ý cho bước "Automate" ở W2).
