# W0 — Intake (Use-case làm rõ)

> Workflow Design Package — Buổi 4 Contract Review.
> Nguồn sự thật: `../lab.md` (lab.handout B4). Anonymize: use-case synthetic, zero PII thật.

## Use-case
**Rà soát hợp đồng dịch vụ (Contract Review) bằng n8n + Harness Engineering.**

Công ty 200–500 NV, tiếp nhận ~20–50 hợp đồng/tháng (dịch vụ cloud, thuê mặt bằng, NDA, lao động…).
Pháp chế chỉ 1–2 người, không rà hết bằng tay → bỏ sót điều khoản rủi ro (omission) hoặc tin clause AI/đối tác bịa (hallucination).

## Phòng ban
Pháp chế / Pháp lý — người dùng cuối là chuyên viên pháp chế, duyệt report thay vì đọc trọn hợp đồng.

## Ràng buộc compliance (constraint)
- Hợp đồng chứa PII đối tác (tên đại diện, MST, giá trị) + điều khoản nhạy cảm nghiệp vụ (BMTT, độc quyền).
- Cấp mật (bí mật nhà nước / hồ sơ ĐVKT thật) → **KHÔNG qua AI công**, cổng DỪNG (redaction cấp 4).
- Quyết định "duyệt hợp đồng" luôn thuộc human (BR-W2) — workflow chỉ đề xuất + flag.

## Mục tiêu đo được (KPI — từ lab.md §1)
- <10'/hợp đồng (vs 2–3h rà tay).
- Bắt clause AI bịa (hallucination) + omission (thiếu điều khoản bắt buộc).
- Pháp chế chỉ duyệt `report.xlsx`, không đọc lại全文.

## Tool (theo lab.md)
- **n8n Cloud** (chính): Manual Trigger → Code node Python (redact/schema/evidence) → AI node (Gemini extract) → Write report.
- Antigravity/Codex (phụ): sinh code Python cho Code node nếu HV stuck.

## Data contract (chain N→N+1, `source_contract_id`)
`contract.docx → contract-redacted.md → clauses.json (schema-valid) → evidence-checked.json → report.xlsx` + `run-log.jsonl`.

## Anonymizer note
Use-case dùng `templates/contract-mau-hop-dong-dich-vu.docx` (synthetic, zero PII thật) → KHÔNG cần chạy `anonymizer.py`.
Track B (HV customize hợp đồng cơ quan) → bắt buộc redaction cấp 1–2 trước khi đưa vào workflow (xem W2).
