# Lab Handout — Buổi 02 (advanced-automation)

> 🚧 **PLACEHOLDER** — `/vibe-teach-orchestrator` **Route 11** (SYNTHETIC_DATA / lab).
> File dành cho HỌC VIÊN (sẽ sync sang `studentkit/`). Đáp án/expected output để ở `checkpoints/`.

## Workflow
Advanced Automation Workflow

## KPI / Sản phẩm đầu ra
Một luồng nghiệp vụ nâng cao hoàn chỉnh: sinh bằng Claude Code, tích hợp đa kênh (Gmail + Telegram), có error workflow & log tập trung, đóng gói bàn giao cho SME.

## Điều kiện tiên quyết
Hoàn thành B1 (đã có credential/API key & 3 flow cơ bản). Cài Claude Code/CLI. Có Telegram bot (tùy chọn).

## Công cụ
n8n · Claude Code/CLI · Gemini / AI Studio · Telegram · Google Workspace · MCP connector

## Các phân đoạn thực hành (TH1 → TH4 = pipeline)
> Output TH_N = Input TH_{N+1}.
### TH1 — Phân đoạn 1 — Tự sinh luồng xử lý yêu cầu khách hàng bằng Claude Code
- **Mô tả kỹ thuật (Input → Action → Output):** JIT: prompt Claude Code mô tả nghiệp vụ (input/bước xử lý/output/điều kiện). HV dùng Claude Code sinh & refactor 1 workflow: scaffold node, sinh expression/Code node, cấu hình kết nối MCP. Output: workflow JSON import chạy được.
- **Công cụ:** Claude Code/CLI + n8n
- **Đầu ra:** ★ Workflow sinh bằng Claude Code

> TODO (Route 11): prompt copy-paste vào `prompts/`, file starter vào `templates/`, expected output/rescue vào `checkpoints/` (instructor-only).
### TH2 — Phân đoạn 2 — Cảnh báo khiếu nại/đơn khẩn đa kênh & chống nghẽn API
- **Mô tả kỹ thuật (Input → Action → Output):** JIT: độ bền của luồng. HV thêm cảnh báo Telegram song song Gmail; bật Retry On Fail; bọc Gemini trong Loop Over Items (Batch=1) + Wait chống quota 429; thêm Code node làm sạch JSON bọc markdown.
- **Công cụ:** n8n + Telegram + Gemini
- **Đầu ra:** ★ Luồng đa kênh + chống lỗi

> TODO (Route 11): prompt copy-paste vào `prompts/`, file starter vào `templates/`, expected output/rescue vào `checkpoints/` (instructor-only).
### TH3 — Phân đoạn 3 — Điều phối yêu cầu đa phòng ban & trả lời đa ngôn ngữ
- **Mô tả kỹ thuật (Input → Action → Output):** JIT: luồng nhiều bước. HV tách sub-workflow, định tuyến theo intent (Switch), thêm nhánh đa ngôn ngữ (Gemini tự dịch email theo cột Ngôn ngữ), dùng data pinning giữ row_number để Update đúng dòng.
- **Công cụ:** n8n + Gemini + sub-workflow
- **Đầu ra:** ★ Sub-workflow + đa ngôn ngữ

> TODO (Route 11): prompt copy-paste vào `prompts/`, file starter vào `templates/`, expected output/rescue vào `checkpoints/` (instructor-only).
### TH4 — Phân đoạn 4 — Đóng gói trợ lý vận hành & bàn giao cho SME
- **Mô tả kỹ thuật (Input → Action → Output):** JIT: vận hành & bàn giao. HV thêm Error Trigger workflow + log tập trung (Run ID|thời gian|trạng thái|lỗi), viết README ngắn, đóng gói export JSON. Checklist nghiệm thu & kịch bản bàn giao cho SME.
- **Công cụ:** n8n + Claude Code
- **Đầu ra:** ★ Luồng đóng gói + log + bàn giao

> TODO (Route 11): prompt copy-paste vào `prompts/`, file starter vào `templates/`, expected output/rescue vào `checkpoints/` (instructor-only).


## Bài tập về nhà — TODO
- _TODO_

## Checklist nghiệm thu — TODO
- [ ] _TODO (SLI/SLO đo được)_
