# Track B — Customize Prompt (B5, OPTIONAL scaffold)

> ⚠️ **Scaffold TẮC — chỉ nếu HV muốn cấu hình nhanh workflow GV thay vì build từ đầu.**
> **MAIN Track B = `track-b-lab.md` (self-build từ đầu theo domain riêng).** Khuyến khích track-b-lab.md.
> Scaffold này = HV thay knowledge DB + intent + trang nhúng (giữ kiến trúc GV) — nhanh nhưng ít "owns" hơn.

```
BỐI CẢNH:
Workflow gốc (GV): CSKH Bot dịch vụ bán lẻ — 15 FAQ, guard/router/cache, LLM fallback, LLM-as-judge, webhook.
HV customize sang domain cơ quan mình.

Học viên:
- Domain/cơ quan: [HV-ĐIỀN: HR / IT helpdesk / sản phẩm X / dịch vụ Y...]
- FAQ nguồn: [HV-ĐIỀN: danh sách câu hỏi-thẻ thường gặp ở cơ quan]
- Trang/landing page nhúng chatbot: [HV-ĐIỀN: landing page HTML / intranet / website / Notion / vibe coding page...]
- Intent đặc thù: [HV-ĐIỀN: có intent nào ngoài 5 chuẩn cần thêm không? vd "nội bộ IT")]

CHỈ DẪN:
1. Giữ NGUYÊN kiến trúc 4 TH (vector DB → guard/router/FAQ cache → LLM fallback+LLM-judge+ticket → webhook chatbot).
2. Thay 15 FAQ sang domain HV (≥10 FAQ, đủ nhóm).
3. Điều chỉnh intent nếu domain cần (vd IT helpdesk thêm "sự cố kỹ thuật" — nhưng ≤6 intent, giữ "ngoài phạm vi").
4. Điều chỉnh guard/router: dấu hiệu prompt injection, chủ đề ngoài phạm vi, dữ liệu nhạy cảm.
5. Điều chỉnh FAQ cache threshold + ngưỡng confidence + rule chuyển người cho domain (vd HR → chuyển người mọi câu có PII).
6. Vibe-code landing page/trang đơn giản có chatbot nhúng (khác trang vibe coding mặc định).

TIÊU CHUẨN ĐẦU RA:
- workflow-hv.md: bot cá nhân hoá (cùng 4 TH, domain HV)
- faq-hv.json: ≥10 FAQ domain HV (zero PII thật)
- diff-vs-gv.md: ≥3 điểm khác (domain / FAQ / intent / guard / cache threshold / ngưỡng / trang nhúng)
- landing-chatbot-hv.html: landing page/trang có chatbot nhúng
- conversation-log-hv: 5 test case domain HV
- Không bịa — thiếu → "[HV-ĐIỀN]"
```

**SLI/SLO (R5)**: customize-prompt ≥3 [HV-ĐIỀN] + diff ≥3 + faq-hv zero PII + landing-chatbot-hv chạy.
**BR-06**: Track B = cấu hình domain, KHÔNG làm lại Track A.
