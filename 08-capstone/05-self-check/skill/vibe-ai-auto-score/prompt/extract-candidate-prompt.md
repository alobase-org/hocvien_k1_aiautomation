# Prompt: Convert candidate → unified schema

> Dùng cho MỖI candidate ở Phase 3. Output tuân `schema/candidate-unified.schema.json`.

Bạn là Chief Examiner. Convert file gốc `{SOURCE_FILE}` của candidate `{CANDIDATE_ID}` về unified schema
theo các field đã định nghĩa: `{FIELD_LIST}`.

## Quy tắc cốt lõi (chống hallucination)
- **MỖI field** phải có `evidence[]` chứa ≥1 `verbatim_quote` = chuỗi CÓ THẬT trong file gốc (copy
  nguyên văn, không paraphrase). Không có evidence → field đó `confidence_score=0.0`, `need_review=true`.
- `confidence_score` trung thực:
  - 0.9–1.0: quote rõ, nhiều chỗ
  - 0.75–0.85: quote có nhưng ngắn/1 chỗ
  - 0.6–0.7: suy luận từ quote
  - 0.0: field không có trong bài
- Field thiếu → `value=null`, `evidence=[]`, `extraction_warnings` ghi rõ "Không tìm thấy X trong bài".
- `rubric_link` = ID tiêu chí con mà field làm bằng chứng.
- Confidence tổng (candidate) = **min** across fields.

## Sau khi xuất
Validate (bắt buộc):
```
python3 script/validator.py --run-all \
  --artifact output/candidates/{CANDIDATE_ID}.unified.json \
  --schema schema/candidate-unified.schema.json \
  --source {SOURCE_FILE}
```
Nếu có evidence missing → phải sửa quote cho đúng nguyên văn, HOẶC hạ confidence + need_review.
Xem `kb/evidence-rules.md`.
