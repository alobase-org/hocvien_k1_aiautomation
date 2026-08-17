# Quy tắc Evidence & Chống Hallucination

Tham chiếu cho Phase 3 + Phase 5. Nguyên tắc tối thượng: **không có bằng chứng verbatim — không có điểm.**

## 1. Evidence là gì

Một evidence item = object có:
```json
{
  "claim": "Đội A dùng kiến trúc microservices",
  "verbatim_quote": "Hệ thống được thiết kế theo kiến trúc microservices với 5 service độc lập",
  "source": "input/team-A-report.pdf",
  "location": "trang 4, mục Kiến trúc"
}
```

**`verbatim_quote` phải là chuỗi CÓ THẬT trong file gốc** — copy nguyên văn, không paraphrase, không
viết lại. Đây là cái validator kiểm tra.

## 2. Validator kiểm tra thế nào

`script/validator.py` → `verify_evidence_recursive`:
1. Đệ quy tìm mọi object có key `verbatim_quote` (kể cả nested trong `fields[]`, `scores[]`).
2. Normalize (lowercase + collapse whitespace) rồi tìm chuỗi trong source.
3. Không tìm thấy → `missing` → confidence −0.2/item → có thể đẩy need_review.

Tại sao normalize: trích dẫn có thể khác whitespace/newline nhẹ. Normalize bắt trúng nội dung mà
vẫn phát hiện hallucination (nội dung khác hẳn).

## 3. Khi nào evidence "mờ" → hạ confidence

| Tình huống | confidence | need_review |
|------------|-----------|-------------|
| Verbatim quote rõ, nhiều chỗ | 0.9–1.0 | false |
| Quote có nhưng 1 chỗ duy nhất, ngắn | 0.75–0.85 | false |
| Field suy luận từ quote (không trực tiếp) | 0.6–0.7 | true |
| Không trích được (thiếu trong bài) | 0.0 | true |

Confidence tổng (candidate/bài) = **min** across all fields/criteria — worst-case governs.

## 4. Field thiếu trong bài

Không bịa evidence. Nếu field không có trong artifact:
```json
{
  "key": "benchmark_p99",
  "value": null,
  "confidence_score": 0.0,
  "need_review": true,
  "evidence": [],
  "extraction_warnings": ["Không tìm thấy số liệu benchmark trong bài nộp"]
}
```
→ Khi chấm, tiêu chí phụ thuộc field này → level thấp (1–2) + confidence thấp + need_review.

## 5. Evidence cho tiêu chí dùng research

Tiêu chí `needs_research=true`: evidence có thể trỏ sang research file thay vì file candidate:
```json
{
  "claim": "Giải pháp tuân thủ chuẩn X",
  "verbatim_quote": "Chuẩn X yêu cầu mã hóa AES-256 tại nghỉ",
  "source": "output/research/SEC-01.md",
  "location": "mục Tiêu chuẩn"
}
```
Tức là: claim về candidate, verbatim_quote là fact tham chiếu. Chấm bằng cách đối chiếu.

## 6. Anti-patterns

- ❌ Dùng paraphrase làm `verbatim_quote` → không khớp → missing
- ❌ Một evidence dùng cho nhiều claim không liên quan
- ❌ `confidence_score` luôn 0.99 (không trung thực) → review queue rỗng → mất cảnh báo
- ❌ Bỏ qua missing evidence, vẫn chấm level cao → vi phạm BR-01
