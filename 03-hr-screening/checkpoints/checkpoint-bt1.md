# Checkpoint TH1 — Candidate Profile (GV/TA)

## Expected state

- [ ] Học viên chạy Prompt TH1 trong Coding Agent, chưa mở n8n.
- [ ] Workspace có file thật `candidate-profile.json`.
- [ ] JSON parse được và có `candidate_id`, `candidate_name`, `months_sales`, `months_b2b`.
- [ ] Có `evidence` để truy vết và `evidence_summary` để HR đọc.
- [ ] Không có thuộc tính nhạy cảm.
- [ ] `run-log.jsonl` có một dòng hợp lệ: cùng `run_id`, `step=TH1_CANDIDATE_PROFILE`, `status=SUCCESS`, `schema_validation=PASS`.

## Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Agent chỉ trả JSON trong chat | `Hãy ghi chính kết quả này thành file candidate-profile.json trong workspace và đọc lại để kiểm tra.` |
| JSON bị bọc markdown | `Ghi JSON thuần vào file, không markdown fence và không comment.` |
| Thiếu evidence | `Đọc lại CV; mỗi dữ kiện quan trọng phải có trích dẫn ngắn, không suy diễn.` |
| Thiếu log | `Append đúng một JSON object TH1 vào run-log.jsonl và validate bằng schemas/run-log-entry.schema.json.` |
| Kẹt quá thời gian | Dùng `fallback-inputs/candidate-profile-bt1-sample-output.json`, đổi tên thành `candidate-profile.json`, rồi tiếp tục TH2. |
