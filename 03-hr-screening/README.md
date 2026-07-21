# Bộ thực hành Buổi 03 — HR Screening 4 lớp

## Cách học

Không import workflow hoàn chỉnh ở đầu buổi. Học viên chạy bốn prompt trong cùng phiên Coding Agent:

1. TH1 tạo `candidate-profile.json`.
2. TH2 đọc TH1 và tạo `data-quality.json`.
3. TH3 đọc hai file trước cùng JD/rubric và tạo `scoring-result.json`.
4. TH4 dùng toàn bộ artifact đã kiểm chứng để Coding Agent xây workflow trực tiếp trên n8n.

## File học viên dùng

- `templates/cv-b2b-junior-input.md`: CV synthetic đầu vào.
- `templates/JD-nhan-vien-kinh-doanh-B2B-junior.md`: JD đã chốt.
- `templates/rubric-kinh-doanh-B2B-100.json`: rubric 100 điểm.
- `templates/scorecard-schema.md`: cấu trúc scorecard.
- `schemas/*.schema.json`: hợp đồng schema và kiểu dữ liệu cho TH1–TH3 cùng từng dòng log.
- `run-log.jsonl`: nhật ký chạy tối giản; một dòng JSON cho mỗi TH, cùng `run_id`, không chứa CV nguyên văn hoặc secret.
- `prompts/bt1-prompt.md` đến `bt4-prompt.md`: chuỗi prompt liên kết.

## File giảng viên/checkpoint

- JSON mẫu của TH1–TH3 và `run-log-sample.jsonl` để fast-forward khi học viên bị kẹt.
- CV holdout để nghiệm thu TH4.
- Workflow n8n hoàn chỉnh là solution/fallback của TH4, không phải starter.

## Sản phẩm cuối

Một workflow n8n nhận CV Markdown mới, tái tạo ba lớp đã kiểm chứng, tạo scorecard kèm câu hỏi phỏng vấn và ghi Google Sheets để HR duyệt.
