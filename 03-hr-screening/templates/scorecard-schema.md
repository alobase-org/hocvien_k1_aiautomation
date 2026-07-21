# Data contract và Scorecard — HR Screening B2B Junior

## Artifact nối tiếp

| Lớp | File | Trường khóa |
|---|---|---|
| TH1 | `candidate-profile.json` | `candidate_id`, dữ kiện chuẩn hóa, `evidence`, `evidence_summary` |
| TH2 | `data-quality.json` | `source_candidate_id`, `completeness_score`, `missing_fields`, `warnings`, `ready_for_scoring` |
| TH3 | `scoring-result.json` | `source_candidate_id`, `criteria`, `total_score`, `result`, `human_review_required`, `interview_questions[]` |

`candidate_id` và `source_candidate_id` phải giống nhau qua ba lớp.

## Nhật ký vận hành tối giản

TH1–TH3 append vào `run-log.jsonl`; workflow n8n append vào tab `Run Log`. Mỗi bản ghi tuân theo `schemas/run-log-entry.schema.json` với 10 trường: `run_id`, `candidate_id`, `step`, `status`, `input_ref`, `output_ref`, `schema_validation`, `error_code`, `error_message`, `processed_at`.

- Schema/ID sai: `ERROR` và dừng bước sau.
- Artifact hợp lệ nhưng dữ liệu cần HR xác minh: `NEEDS_REVIEW`.
- Workflow ghi Scorecard xong: `WORKFLOW_COMPLETE/SUCCESS`.
- Lỗi execution tự động: Error Workflow ghi `WORKFLOW_ERROR/ERROR`.
- Không đưa CV nguyên văn, prompt, credential hoặc API key vào log.

## Cột Google Sheets của TH4

| # | Cột |
|---:|---|
| 1 | Thời gian |
| 2 | Mã ứng viên |
| 3 | Tên ứng viên |
| 4 | Điểm Sales |
| 5 | Điểm B2B |
| 6 | Điểm Prospecting |
| 7 | Điểm Giao tiếp |
| 8 | Điểm CRM/Pipeline |
| 9 | Điểm Thành tích |
| 10 | Điểm Thị trường |
| 11 | Điểm Công cụ/CV |
| 12 | Tổng điểm |
| 13 | Kết quả |
| 14 | Dữ liệu thiếu |
| 15 | Bằng chứng chính |
| 16 | Câu hỏi phỏng vấn |
| 17 | Trạng thái HR |
| 18 | Người duyệt |
| 19 | Quyết định HR |
| 20 | Ghi chú HR |

## Quy tắc bắt buộc

- `Bằng chứng chính` lấy từ `evidence_summary`, không ghi nguyên object JSON vào một ô.
- `Câu hỏi phỏng vấn` nối 2–4 phần tử của `interview_questions[]` bằng ký tự xuống dòng.
- `Trạng thái HR` mặc định là `Chờ HR duyệt`.
- Không có evidence thì tiêu chí không được chấm điểm.
- Không dùng thuộc tính nhạy cảm.
- Workflow không tự mời, tự từ chối hoặc tự quyết định tuyển dụng.
