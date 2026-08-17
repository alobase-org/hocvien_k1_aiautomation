---
name: legal-clause-reviewer
description: >
  Review điều khoản văn bản pháp lý xây dựng: trích điều khoản, đối chiếu checklist
  rủi ro nội bộ (KB), phân loại CAO/TB/THẤP kèm dẫn chứng + đề xuất phản hồi.
  Kích hoạt khi nhận "văn bản cần review", "check hợp đồng xây dựng", "pháp lý".
  KHÔNG dùng cho: cho ý kiến pháp lý cuối, ký thay, tư vấn vượt checklist.
---

# Legal Clause Reviewer

## Input contract
- `input/document.md` — văn bản (điều khoản đã đánh số hoặc văn bản thô)
- `kb/risk-checklist.md` — checklist rủi ro xây dựng nội bộ

## Workflow
1. Trích điều khoản Đ1, Đ2... (nếu chưa đánh số).
2. Đối chiếu TỪNG điều khoản với checklist — mỗi phát hiện ghi: điều khoản | rule nào vi phạm | mức | dẫn chứng (trích nguyên văn).
3. Phân loại: CAO (vi phạm rule nhóm A) · TB (nhóm B) · THẤP (nhóm C) · KHONG_RO (không map rule nào — không bịa).
4. Đề xuất phản hồi mỗi điều khoản rủi ro (chỉ theo KB, không tự nghĩ luật).
5. Xuất `legal-review.json` + email draft phản hồi (chờ trưởng phòng duyệt — HITL).

## Rules
- Chỉ áp dụng rule có trong KB — không viện dẫn luật ngoài (trưởng phòng sẽ bổ sung).
- Mức rủi ro KHÔNG được tự nâng/t hạ — bám nhóm A/B/C của checklist.
- Điều khoản không map rule → KHONG_RO + ghi "[cần trưởng phòng xem]".
- 100% điều khoản phải xuất hiện trong output (kể cả an toàn) — chống bỏ sót.

## Cách test
`test/test-case.md` — 5 điều khoản phủ CAO/TB/THẤP/KHONG_RO/thiếu input.
