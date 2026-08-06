# W6 — Deck tham mưu lãnh đạo 30 ngày (CRAFT)

> BT6. Optional — dán design doc + Mermaid vào Claude/Gemini (local) HOẶC NotebookLM.
> ⚠️ Bảo mật: hợp đồng có PII → KHÔNG đẩy file thật lên NotebookLM cloud. Chỉ đẩy **design doc đã redact** hoặc chạy local.

## Prompt CRAFT

```text
C — CONTEXT
Deck THAM MƯU LÃNH ĐẠO triển khai workflow AI Automation "Contract Review" trong 30 ngày tới.
Nguồn đã add: Workflow Design Doc (as-is, to-be ESIA, hardening) + Mermaid diagram (file workflow_design/).
Đối tượng: ban giám đốc / trưởng phòng Pháp chế — quan tâm ROI + rủi ro pháp lý, không quan tâm code.

R — ROLE
Strategy Manager + Transformation Consultant. Giọng rõ ràng, tự tin, dữ liệu dẫn dắt.
Thuật ngữ (HITL, ESIA, schema) phải giải thích 1 câu.

A — ACTION
Tạo deck 8 slide:
1. Cover — "Đề xuất AI Automation: Contract Review — Tham mưu 30 ngày".
2. Vấn đề: 2–3h/hợp đồng × 20–50/tháng, Pháp chế 1–2 người không rà hết → sót omission/clause bịa.
3. Quy trình mới (to-be): redact → extract+schema → evidence → report → Pháp chế duyệt (Mermaid).
4. Lợi ích đo được: <10'/hợp đồng; bắt hallucination+omission; Pháp chế chỉ duyệt report. (số thật → điền, chưa đo → [cần đo])
5. Độ tin cậy: 4 lớp hardening (fallback/log/edge/HITL) + 6/6 thuộc tính (4 đạt, 2 một phần). Vì sao lãnh đạo yên tâm: quyết định duyệt LUÔN thuộc human.
6. Lộ trình 30 ngày: Tuần 1 pilot 10 HĐ đã duyệt · Tuần 2 hardening + edge case · Tuần 3 chạy song song (AI + tay) · Tuần 4 go-live + monitoring.
7. Rủi ro & giảm thiểu: (a) AI bịa → evidence check Python; (b) PII lộ → redact 4 cấp + gate mật; (c) sai lệch ngữ cảnh → pilot 10 HĐ đối chiếu.
8. Quyết định cần: duyệt ngân sách n8n Cloud + 1 tuần Pháp chế pilot + chỉ định 1 người champion.

F — FORMAT
- 8 slide, mỗi slide 1 ý + 3–4 bullet + 1 visual (diagram/icon/chart).
- Số liệu có đơn vị (giờ, VND, %). KHÔNG bịa — thiếu ghi [cần đo].
- Chỗ chèn ảnh Mermaid (từ 04-mermaid) + report.xlsx mock.

T — TONE / TARGET
Tiếng Việt chuyên nghiệp, tự tin, không khoa trương. Audience: BGĐ non-tech am hiểu kinh doanh.
```

## Mục tiêu deck
Thuyết phục lãnh đạo duyệt pilot 30 ngày + ngân sách n8n Cloud + allocate 1 Pháp chế champion.

## Lộ trình 30 ngày (tóm tắt)
| Tuần | Hoạt động | Output |
|------|-----------|--------|
| 1 | Pilot trên 10 hợp đồng ĐÃ duyệt (answer-key) | So sánh AI vs quyết định thật, baseline accuracy |
| 2 | Hardening: edge case (scan/OCR, encoding, token limit), redaction regex sót | Workflow production-ready |
| 3 | Chạy song song (AI đề xuất + Pháp chế rà tay) | Đo thời gian thực <10', false-positive rate |
| 4 | Go-live + monitoring `run-log.jsonl` | Handover + runbook, dashboard audit |

## Lợi ích đo được
- Thời gian: **<10'/hợp đồng** vs 2–3h as-is → tiết kiệm ~[cần đo] giờ/tháng.
- Chất lượng: bắt hallucination (clause bịa) + omission (8 điều khoản bắt buộc) mà tay dễ sót.
- Pháp chế: đọc report thay vì全文 → giải phóng capacity cho việc tư luật sư.

> SLI/SLO W6: deck CRAFT 5 phần ✅ · lộ trình 30 ngày ✅ · ≥3 lợi ích đo được ✅ · không bịa số (ghi [cần đo]) ✅.
