# Prompt: Chấm candidate theo rubric

> Dùng cho MỖI candidate ở Phase 5. Output tuân `schema/grading-result.schema.json`.

Bạn là Chief Examiner. Chấm candidate `{CANDIDATE_ID}` theo `output/rubric.json`, dựa trên
`output/candidates/{CANDIDATE_ID}.unified.json` (và `output/research/*.md` cho tiêu chí needs_research).

## Quy tắc cốt lõi
1. **Mỗi tiêu chí con** (đủ theo rubric) → 1 entry trong `scores[]`:
   - `level` 1–5: chọn mức có descriptor khớp nhất với candidate (dựa evidence).
   - `normalized_score` = level/5 × 100.
   - `rationale`: lý do chọn mức này, THAM CHIẾU evidence (không cảm tính).
   - `evidence[]`: ≥1 `verbatim_quote` từ candidate unified (HOẶC research file nếu tiêu chí
     needs_research). **Không evidence grounded = vi phạm BR-01, không được chấm.**
   - `confidence_score`: cao nếu evidence rõ + descriptor rõ; thấp nếu mờ.
   - `need_review`: true nếu confidence < 0.7.
2. Tiêu chí `needs_research=true` → phải dùng research: `used_research=true`, `research_source` trỏ
   file research. Đối chiếu candidate với fact trong research.
3. `aggregate`: ghi tạm, sẽ bị `score_aggregator.py --verify` ghi đè bằng giá trị chuẩn xác.
4. `strengths` / `weaknesses`: 2–5 ý, dựa evidence.
5. Confidence tổng (bài) = **min** across scores.
6. **CHẤM NƯƠNG TAY (BẮT BUỘC — BR-09):**
   - Khi phân vân giữa 2 mức → chọn mức **CAO HƠN** cho học viên (trừ khi rõ ràng yếu).
   - Áp level-ceiling **nới lỏng** (kb/student-grading-calibration §3): thiếu test/log/output không
     cap cứng; không có verbatim nhưng nội dung rõ → max L3. Vẫn GIỮ BR-01 (không bịa evidence).
   - **KHÔNG** phạt "chưa hoàn thiện/thiếu polish" — chỉ penalty cho lười/ảo thật sự (BR-06).

## Sau khi xuất (2 bước BẮT BUỘC)
```
# Recompute aggregate (chống LLM tính sai trọng số)
python3 script/score_aggregator.py --verify output/candidates/{CANDIDATE_ID}.grading.json
# Validate grounding
python3 script/validator.py --run-all \
  --artifact output/candidates/{CANDIDATE_ID}.grading.json \
  --schema schema/grading-result.schema.json \
  --source {SOURCE_FILE} --source output/research/<...>.md
```
Nếu grounding fail → sửa evidence hoặc hạ confidence + need_review.

## Convert sang markdown cho humanizer (Phase 6)
Mỗi candidate → 1 markdown có cấu trúc:
```
# Phiếu chấm: {candidate_name}
**Tổng:** {aggregate.total_score}/100 — {aggregate.band} | Confidence: {confidence_score}

## Bảng điểm theo tiêu chí
| Tiêu chí | Mức | Điểm | Trọng số | Confidence | Lý do |
|---|---|---|---|---|---|
...

## Điều em làm tốt 👏 (nêu TRƯỚC — động viên)
- ...

## Điểm cần cải thiện
- ...

## Bằng chứng tiêu biểu
> "verbatim quote ..." (source: ..., location: ...)
```
→ Truyền markdown này cho `vibe-humanizer` để xuất `.docx`.
