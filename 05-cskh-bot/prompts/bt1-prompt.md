# Prompt TH1 — Vector knowledge DB (Semantic search nền)

> Tư duy mới: **Semantic search** — embed FAQ thành vector để tìm theo NGHĨA. TH 1/4.
> Input: `templates/faq-cskh.md` (15 FAQ). Output: `vector-store.json` (15 vector).

## n8n: Read FAQ → HTTP Embedding API → Code node store

```
BỐI CẢNH:
Xây knowledge DB dạng vector cho 15 FAQ dịch vụ bán lẻ. Mỗi FAQ → 1 vector embedding.

CHỈ DẪN (n8n):
1. Read node → load templates/faq-cskh.md (15 FAQ, 5 nhóm).
2. Loop Over Items → HTTP node gọi Embedding API:
   - Google AI Studio: POST gemini text-embedding-004, model text-embedding-004
     body: { "content": { "parts": [{ "text": "{{ $json.cau_hoi + ' ' + $json.cau_tra_loi }}" }] } }
   - Hoặc OpenAI embeddings.
3. Code node store → gộp faq_id + nhom + vector.

TIÊU CHUẨN ĐẦU RA:
- vector-store.json: 15 object, mỗi object { faq_id, nhom, cau_hoi, cau_tra_loi, vector: [float...] }.
```

**HV làm trong n8n:** Read → HTTP (Embedding API) → Code node → Write `vector-store.json`.

**Chaining**: vector store → input TH2 (cosine similarity).
**Tư duy**: "kho tri thức trước bot sau" (kế thừa B4 structured) + semantic (tìm theo nghĩa).
