# Prompt TH4 — Đóng gói thành workflow n8n

> Chạy trong cùng phiên chat sau TH1–TH3. Coding Agent phải được kết nối với n8n qua MCP/API.

```text
BỐI CẢNH:
Đây là LỚP 4 — bước đóng gói. Ba lớp nghiệp vụ đã được chạy và kiểm chứng bằng artifact trong workspace. Hãy dùng chúng làm data contract, ví dụ chuẩn và expected output để xây một workflow n8n chạy end-to-end trên CV mới.

INPUT PHẢI ĐỌC TRƯỚC KHI XÂY:
- CV Markdown mẫu.
- candidate-profile.json từ TH1.
- data-quality.json từ TH2.
- scoring-result.json từ TH3.
- templates/JD-nhan-vien-kinh-doanh-B2B-junior.md.
- templates/rubric-kinh-doanh-B2B-100.json.
- templates/scorecard-schema.md.
- Ba JSON Schema nghiệp vụ và schemas/run-log-entry.schema.json.
- run-log.jsonl từ TH1–TH3.

YÊU CẦU THỰC HIỆN:
1. Đọc và xác nhận ba artifact cùng candidate_id, schema nối tiếp hợp lệ và rubric tối đa 100.
2. Kiểm tra kết nối n8n và tham khảo các workflow đang dùng Vertex/Google Sheets trong cùng instance trước khi cấu hình.
3. Tạo hoặc cập nhật một workflow n8n có bốn vùng rõ ràng:
   - Lớp 1: nhận CV Markdown mới, gọi Vertex bằng HTTP Request và tạo candidate_profile đúng schema TH1.
   - Lớp 2: kiểm tra dữ liệu theo đúng luật TH2 và tạo data_quality.
   - Lớp 3: áp rubric cố định theo TH3 và tạo scoring_result; không để model tự đổi trọng số.
   - Lớp 4: tạo scorecard dễ đọc, append Google Sheets và để HR duyệt.
4. Học viên không phải tự viết expression dài. Bạn chịu trách nhiệm cấu hình node, expression, connection và credential reference.
5. Vertex HTTP Request phải dùng cấu hình hiện có trên n8n: endpoint/model và Generic Header Auth credential đang hoạt động; không ghi API key vào workflow JSON.
6. Cột Bằng chứng chính phải dùng evidence_summary dễ đọc, không đổ object JSON vào một ô.
7. Cột Câu hỏi phỏng vấn phải lấy từ scoring_result.interview_questions và nối mỗi câu bằng ký tự xuống dòng.
8. Trạng thái mặc định là Chờ HR duyệt. Không tự gửi thư mời/từ chối và không tự quyết định tuyển dụng.
9. Thêm sticky note tiếng Việt cho từng lớp và ghi rõ nơi có thể đổi nguồn CV hoặc chạy nhiều CV.
10. Validate workflow sau khi tạo. Giữ workflow Inactive cho đến khi người dùng bật.
11. Chạy thử với CV mẫu nếu cơ chế trigger cho phép. Sau đó hướng dẫn người dùng chạy CV holdout để nghiệm thu.
12. Export workflow thành file JSON solution trong khu vực checkpoint dành cho giảng viên.
13. Trong workflow chính, sau khi ghi Scorecard thành công, append một dòng `WORKFLOW_COMPLETE/SUCCESS` vào tab `Run Log` với các cột đúng schema log.
14. Tạo một Error Workflow riêng: `Error Trigger → Edit Fields → Google Sheets`, append `WORKFLOW_ERROR/ERROR` vào cùng tab `Run Log`, rồi liên kết nó trong Workflow Settings. Không thêm nhánh bắt lỗi vào từng lớp.
15. Không ghi CV nguyên văn, prompt, credential hoặc API key vào log. Ghi chú rõ Error Trigger chỉ bắt execution tự động, không bắt lỗi khi bấm Execute Workflow thủ công.

TIÊU CHUẨN BÀN GIAO:
- workflow_id và tên workflow trên n8n.
- File export JSON parse được.
- Danh sách node theo bốn lớp.
- Kết quả validation và phần chưa thể runtime-test.
- Hướng dẫn đúng một thao tác để chạy CV holdout.
- Google Sheet có section Trạng thái HR, Người duyệt, Quyết định HR và Ghi chú HR.
- Google Sheet có tab `Run Log` với header: `run_id, candidate_id, step, status, input_ref, output_ref, schema_validation, error_code, error_message, processed_at`.

QUY TẮC BẢO TOÀN:
- Không sửa hoặc xóa workflow ngoài phạm vi bài tập.
- Nếu workflow bài tập đã tồn tại, đọc nó trước rồi cập nhật thay vì tạo bản trùng lặp.
- Không tuyên bố chạy thành công nếu mới chỉ validate cấu trúc.
```

**HITL:** AI chỉ đề xuất ưu tiên xem xét. Quyết định tuyển dụng luôn thuộc HR.
