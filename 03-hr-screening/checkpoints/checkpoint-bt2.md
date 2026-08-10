# Checkpoint TH2 — Data Quality (GV/TA)

## Expected state

- [ ] Agent đã đọc `candidate-profile.json`, không bóc lại CV.
- [ ] Workspace có `data-quality.json`.
- [ ] Có `completeness_score`, `missing_fields`, `warnings`, `ready_for_scoring`.
- [ ] `source_candidate_id` khớp TH1.
- [ ] Không có quyết định tuyển/loại.
- [ ] Log TH2 giữ nguyên `run_id`; dùng `SUCCESS`, `NEEDS_REVIEW` hoặc `ERROR` đúng ngữ nghĩa và đúng schema.

## Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Agent sửa file TH1 | `Khôi phục candidate-profile.json; TH2 chỉ được tạo data-quality.json mới.` |
| Không chứng minh kế thừa | `Thêm source_candidate_id lấy trực tiếp từ candidate-profile.json và xác nhận hai ID khớp.` |
| Schema/ID sai nhưng vẫn chạy tiếp | `Ghi TH2_DATA_QUALITY/ERROR vào log rồi dừng; không tạo TH3.` |
| Kẹt quá thời gian | Dùng `checkpoints/data-quality-sample.json` để tiếp tục TH3. |
