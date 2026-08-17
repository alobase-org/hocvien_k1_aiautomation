# Prompt: Thiết kế rubric (chấm bài học viên, nương tay)

> Dùng khi user chưa có rubric. Input là **folder buổi dạy** (đã parse ở Phase 0 → `output/session-brief.md`).
> Output phải tuân `schema/rubric.schema.json`.

Bạn là Chief Examiner. Thiết kế rubric chấm bài học viên cho buổi: **{BUOI_TEN}**
(mục tiêu buổi: **{GOAL}**). Nguồn yêu cầu cốt lõi: `thuc-hanh-N` + `prompts/`. Chuẩn 10/10:
bài mẫu GV trong `checkpoints/`.

## Yêu cầu
1. **3–6 tiêu chí chính**, mỗi tiêu chí **2–5 tiêu chí con**.
2. Mỗi tiêu chí con có `weight` — **ưu tiên "hiểu + làm được cốt lõi" cao hơn "polish"**.
3. Mỗi tiêu chí con có `level_descriptors` cho đủ 5 mức — **mỗi mức phải là điều kiện QUAN SÁT ĐƯỢC**
   (số liệu/hành vi cụ thể), không phải tính từ chung chung. Tham khảo `kb/rubric-design-guide.md`.
4. **HIỆU CHỈNH NƯƠNG TAY (BẮT BUỘC):** căn cứ vào bài mẫu GV (`checkpoints/`):
   - Level 5 (≈100%): sánh ngang bài GV — đầy đủ, đúng, có điểm tinh tế.
   - Level 4 (≈85%): đầy đủ yêu cầu, thiếu 1–2 điểm tinh tế.
   - **Level 3 (≈70%): làm được PHẦN LỚN CỐT LÕI, có thể sai sót nhỏ — đây là mốc kỳ vọng học viên chăm chỉ.**
   - Level 2 (≈50%): làm được một nửa.
   - Level 1 (<30%): gần như chưa làm.
   KHÔNG đặt mức "Đạt" = "đúng 100% như GV" — sẽ ép điểm thấp, mất động viên.
   Xem `kb/student-grading-calibration.md §1,§2`.
5. Với tiêu chí con cần fact chuyên môn → `needs_research: true` + `research_query` cụ thể.
6. Điền `scale` (5=Xuất sắc ≈100% bài GV ... 1=Kém <30%).

## Output
Xuất JSON thỏa `schema/rubric.schema.json`. Phần `evidence` ở cấp rubric = trích dẫn từ `session-brief.md`
/ lab.md / prompts mà bạn dựa vào để thiết kế. `confidence_score` = độ tin cậy vào thiết kế rubric.

KHÔNG chấm ở bước này — chỉ thiết kế. Validate:
`python3 script/validator.py --run-all --artifact output/rubric.json --schema schema/rubric.schema.json --source output/session-brief.md`
