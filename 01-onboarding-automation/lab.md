# Lab Handout — Buổi 01 (onboarding-automation)

> 🚧 **PLACEHOLDER** — `/vibe-teach-orchestrator` **Route 11** (SYNTHETIC_DATA / lab).
> File dành cho HỌC VIÊN (sẽ sync sang `studentkit/`). Đáp án/expected output để ở `checkpoints/`.

## Workflow
Onboarding Automation Workflow

## KPI / Sản phẩm đầu ra
3 workflow chạy được: (1) flow nhắc việc Sheets+Gmail, (2) flow Gemini phân loại phản ánh ép JSON, (3) flow soạn email có human-in-the-loop. Toàn bộ API key/credential cấu hình chuẩn trong n8n.

## Điều kiện tiên quyết
Có tài khoản n8n (cloud/self-host) và tài khoản Google. Sẵn 3 Google Sheets mẫu của SME: việc tồn đọng / phản ánh khách hàng / yêu cầu soạn email.

## Công cụ
n8n · Google AI Studio (Gemini API key) · Google Sheets/Gmail (OAuth2 credential) · MCP connector · AI chat

## Các phân đoạn thực hành (TH1 → TH4 = pipeline)
> Output TH_N = Input TH_{N+1}.
### TH1 — Phân đoạn 1 — Lấy API key & cấu hình kết nối (MCP/credential)
- **Mô tả kỹ thuật (Input → Action → Output):** JIT: kết nối an toàn. HV vào Google AI Studio lấy Gemini API key; tạo credential OAuth2 Google Sheets/Gmail trong n8n; cấu hình MCP connector. Output: các credential đã test kết nối thành công = nền cho TH2–TH4.
- **Công cụ:** Google AI Studio + n8n credentials
- **Đầu ra:** ★ Credential & MCP đã kết nối

> TODO (Route 11): prompt copy-paste vào `prompts/`, file starter vào `templates/`, expected output/rescue vào `checkpoints/` (instructor-only).
### TH2 — Phân đoạn 2 — Luồng không-AI: nhắc việc tự động
- **Mô tả kỹ thuật (Input → Action → Output):** JIT: luồng không cần AI. HV dựng flow nhắc việc: Schedule Trigger (8h) → Google Sheets Read (tab CongViec) → IF (Trạng thái ≠ Hoàn thành) → Edit Fields soạn nội dung nhắc → 2 nhánh song song: Append log (NhacViec) + Gmail gửi người phụ trách.
- **Công cụ:** n8n + Google Sheets/Gmail
- **Đầu ra:** ★ flow1_nhac_viec.json

> TODO (Route 11): prompt copy-paste vào `prompts/`, file starter vào `templates/`, expected output/rescue vào `checkpoints/` (instructor-only).
### TH3 — Phân đoạn 3 — Luồng AI: Gemini phân loại phản ánh (JSON)
- **Mô tả kỹ thuật (Input → Action → Output):** JIT: ép AI trả JSON có cấu trúc. HV dựng flow phân loại phản ánh khách hàng SME: Gemini (Message a model) → {category: Bán hàng/CSKH/Nhân sự/Vận hành/Khác, priority, summary} → Edit Fields tách 3 trường → Sheets Update ghi ngược. Xử lý lỗi 429 (Retry) & JSON bọc markdown (Code node).
- **Công cụ:** n8n + Gemini + Sheets
- **Đầu ra:** ★ flow2_phan_loai.json (JSON)

> TODO (Route 11): prompt copy-paste vào `prompts/`, file starter vào `templates/`, expected output/rescue vào `checkpoints/` (instructor-only).
### TH4 — Phân đoạn 4 — Human-in-the-loop: soạn & duyệt email
- **Mô tả kỹ thuật (Input → Action → Output):** JIT: human-in-the-loop. Flow 3A: Gemini soạn email nháp → Gmail Create Draft + Sheet Trạng thái 'Chờ duyệt'. Flow 3B: người duyệt gõ 'Gửi' → IF (Duyệt='Gửi' VÀ chưa 'Đã gửi') → Gmail Send → đánh dấu 'Đã gửi' + ghi giờ. Test case + checklist nghiệm thu.
- **Công cụ:** n8n + Gmail + Sheets
- **Đầu ra:** ★ flow3a/3b email có duyệt

> TODO (Route 11): prompt copy-paste vào `prompts/`, file starter vào `templates/`, expected output/rescue vào `checkpoints/` (instructor-only).


## Bài tập về nhà — TODO
- _TODO_

## Checklist nghiệm thu — TODO
- [ ] _TODO (SLI/SLO đo được)_
