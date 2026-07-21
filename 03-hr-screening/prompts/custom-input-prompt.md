# Prompt mở rộng — Đổi nguồn CV hoặc chạy hàng loạt

> Dùng sau khi đã hoàn thành TH4. Coding Agent phải đọc workflow hiện tại trước khi sửa.

```text
BỐI CẢNH:
Tôi đã có workflow n8n HR Screening 4 lớp chạy được với một CV Markdown mẫu. Workflow có các data contract: candidate_profile → data_quality → scoring_result → scorecard.

MỤC TIÊU:
Thay nguồn CV mẫu bằng [ĐIỀN: Form Upload / Google Drive / Google Sheets / Webhook / Email] và hỗ trợ [một CV / nhiều CV].

CHỈ DẪN:
1. Đọc workflow hiện tại từ n8n trước khi thay đổi; không tạo bản trùng lặp.
2. Chỉ thay vùng input và bước chuyển file thành CV Markdown.
3. Giữ nguyên bốn data contract và các node: TH1 bóc tách, TH2 tạo Data Quality, TH3 tạo Scoring Result, TH4 tạo Scorecard.
4. Nếu đầu vào là PDF/DOCX, thêm node trích xuất text trước TH1.
5. Nếu chạy hàng loạt, mỗi CV phải là một n8n item riêng và có candidate_id riêng.
6. Không ghi API key vào workflow, không dùng thuộc tính nhạy cảm và không tự động loại ứng viên.
7. Thêm sticky note tiếng Việt tại vùng input để học viên biết chỗ custom.
8. Validate workflow và nêu rõ phần nào đã runtime-test.

TIÊU CHUẨN BÀN GIAO:
- Danh sách node được thêm/sửa.
- Mapping từ nguồn mới sang candidate_id + cv_markdown.
- Ba test case: một CV đủ dữ liệu, một CV thiếu dữ liệu, nhiều CV.
- Xác nhận các node nghiệp vụ sau vùng input không bị thay đổi.
```
