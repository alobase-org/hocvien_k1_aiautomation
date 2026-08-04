# Continuity Bridge — Buổi 5 ← Buổi 4 (Contract Review)

> G1. HV đọc 30 giây = biết "B4 có gì, B5 thêm gì". Exact-vocab kế thừa B4.

## Recap (HV đã có sau B4) — ≥3 ý, NGUYÊN vocab B4
1. **Harness Engineering** — schema validate cấu trúc + evidence verbatim bắt clause bịa → Agent đáng tin.
2. **Determinism** — validate bằng **Code node Python trong n8n** (PASS/FAIL tất định, không tin mood AI).
3. **Redaction 4 cấp** — che PII trước khi qua AI (CCHC).
4. **n8n workflow** — HV tự build n8n (Trigger → Node → Code node Python → IF → Write). Credential OAuth2/API key từ B2.
5. **HITL** — report có section "Người duyệt + ngày + quyết định"; AI không duyệt thay human.
6. **Pipeline/data contract** — output N = input N+1; `run-log.jsonl`.

## Extend-map (B5 thêm gì — TƯ DUY MỚI: Guardrail + FAQ Cache + Semantic Search + LLM-as-judge + Vibe-coding chatbot)

B5 đổi input: hợp đồng (tĩnh, văn bản dài) → **câu hỏi khách** (động, không lường trước). Cùng tư duy "đáng tin" nhưng thêm 4 tầng mới:

| Điểm mới B5 | Nối vào ý B4 nào | Vì sao là mở rộng |
|-------------|------------------|--------------------|
| **Prompt injection guard + scope router** | Redaction/Harness Gate (B4) | B4 chặn dữ liệu rủi ro trước AI; B5 chặn lệnh độc hại và chủ đề ngoài phạm vi trước LLM answer |
| **FAQ cache fast path** | Determinism/Code node (B4) | Câu đã biết thì trả lời bằng nguồn có sẵn, nhanh và tất định hơn gọi LLM |
| **Semantic search (vector)** xây knowledge DB | Schema/structured data (B4) | B4 dữ liệu cấu trúc 1 file; B5 nhiều FAQ → cần **tìm theo NGHĨA** (vector), không phải từ khóa |
| **LLM-as-judge** → confidence | Evidence verbatim "kiểm chứng AI" (B4) | B4 code check evidence có trong văn bản; B5 **dùng LLM thứ 2 đánh giá độ tin cậy câu trả lời** → confidence. Cùng tư duy "đo, không tin" |
| **HITL ticket khi confidence thấp** | HITL section report (B4) | B4 human duyệt report cuối; B5 **auto-routing**: confidence thấp HOẶC nhạy cảm → tự tạo ticket chuyển người |
| **Vibe coding landing page + n8n webhook** | n8n workflow (B4) | B4 workflow chạy manual/schedule; B5 **landing page có chatbot → call n8n webhook** trả lời real-time. Thêm lớp UI + API |
| **Intent/scope + "ngoài phạm vi"** | (mới cho CSKH) | Cho bot quyền nói "tôi không biết" → từ chối/chuyển người. Fix lỗi "2 outside-scope" → "2 chuyển người, 1 ngoài scope" |

## Vocab kế thừa (NGUYÊN B4) + vocab MỚI B5
- **Kế thừa:** `harness` · `schema` · `evidence` · `determinism` · `Code node Python` · `HITL` · `run-log.jsonl` · `n8n workflow`.
- **Mới B5:** `prompt injection guard` · `scope router` · `FAQ cache` · `semantic search` · `vector embedding` · `knowledge database` · `LLM-as-judge` · `confidence` · `intent` · `ticket/routing` · `webhook` · `vibe coding landing page` · `chatbot widget`.

## Tool continuity (BR-07: B5 ≥ B4 — THÊM, không hạ cấp)
- **B4:** n8n (Code node Python, workflow manual).
- **B5:** n8n **+ vibe coding landing page có chatbot + webhook** — thêm lớp giao diện + real-time API. Toolset chỉ tăng, KHÔNG hạ cấp về "free chat + Sheets".

## Slide recap gợi ý
- `[concept_comparison]` **"B4: Agent rà văn bản (tĩnh) → B5: Bot trả lời khách (động) + LLM-as-judge đo độ tin"**.
