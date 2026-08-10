# Checkpoint TH3 — Rubric 100 điểm (GV/TA)

## Expected state

- [ ] Agent đọc hai JSON trước, JD và rubric.
- [ ] Workspace có `scoring-result.json`.
- [ ] Có đúng tám criteria; tổng `max_points` bằng 100.
- [ ] Tổng `score` bằng `total_score` và nằm trong 0–100.
- [ ] Mỗi điểm có evidence; không có evidence thì 0.
- [ ] `source_candidate_id` khớp TH1–TH2 và `human_review_required=true`.
- [ ] Có 2–4 `interview_questions`, bám evidence hoặc dữ liệu cần xác minh và không hỏi thuộc tính nhạy cảm.
- [ ] Validate PASS theo `schemas/scoring-result.schema.json`.
- [ ] Log TH3 giữ nguyên `run_id`, đúng `TH3_SCORING_RESULT` và đúng schema; không chạy TH4 nếu có `ERROR`.

## Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Model đổi trọng số | `Đọc lại rubric JSON và dùng nguyên max_points; không tự sửa rubric.` |
| Tổng điểm sai | `Tính lại total_score từ criteria và kiểm tra tổng max_points đúng 100.` |
| Chấm không có bằng chứng | `Đặt tiêu chí không có evidence về 0 và ghi rõ trong scoring_note.` |
| Log không nối tiếp | `Đọc lại hai dòng log trước, giữ nguyên run_id và append đúng một dòng TH3.` |
| Kẹt quá thời gian | Dùng `checkpoints/scoring-result-sample.json` để tiếp tục TH4. |
