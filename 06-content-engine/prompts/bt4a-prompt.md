# Prompt TH4a — Đóng gói backend thành workflow n8n

> Chạy trong cùng phiên chat sau TH1–TH3. Coding Agent phải được kết nối với n8n qua MCP/API.
> Làm bt4a xong mới sang bt4b — app duyệt cần webhook URL do bước này sinh ra.

```text
BỐI CẢNH:
Đây là LỚP 4, phần backend. Ba lớp nghiệp vụ đã chạy và được kiểm chứng bằng artifact trong workspace.
Hãy dùng chúng làm data contract, ví dụ chuẩn và expected output để xây một workflow n8n chạy
end-to-end trên một brief mới.

INPUT PHẢI ĐỌC TRƯỚC KHI XÂY:
- content-angles.json từ TH1.
- content-draft.json từ TH2.
- content-assets.json từ TH3.
- templates/product-brief-sunrise-kids.md.
- templates/chan-dung-khach-hang.md.
- templates/brand-voice.md.
- templates/channel-format-spec.md.
- Ba JSON Schema trong schemas/.

YÊU CẦU THỰC HIỆN:
1. Đọc và xác nhận ba artifact cùng brief_id, source_angle_id tồn tại trong danh sách angle,
   và cả ba validate PASS theo schema tương ứng. Nếu không khớp, báo lại và dừng.
2. Kiểm tra kết nối n8n. Tham khảo các workflow đang dùng Gemini/Google Sheets trong cùng instance
   trước khi cấu hình, để tái dùng đúng credential đang hoạt động.
3. Tạo một workflow n8n có bốn vùng rõ ràng, mỗi vùng một sticky note tiếng Việt:

   Lớp 1 — Sinh ý tưởng:
   nhận brief mới + file chân dung, gọi Gemini bằng HTTP Request,
   tạo content_angles đúng schema TH1. Bắt buộc phủ tối thiểu 2 chân dung.

   Lớp 2 — Viết nội dung:
   chọn angle theo tham số đầu vào (mặc định angle đầu tiên),
   tạo content_draft đúng schema TH2: bài Fanpage 120-200 từ và kịch bản TikTok đúng 4 khối.

   Lớp 3 — Seeding, image brief và ẢNH:
   tạo content_assets đúng schema TH3, rồi dùng chính trường image_prompt gọi API sinh ảnh
   bằng HTTP Request và trả về URL ảnh. Ảnh là thứ người duyệt sẽ nhìn ở app, không được bỏ qua.

   Lớp 4 — Đưa vào hàng đợi duyệt:
   ghi một dòng vào Google Sheets tab Content_Queue với Status mặc định "Needs Review",
   kèm nội dung bài, URL ảnh và toàn bộ seeding.

4. Ngoài luồng trên, tạo thêm một webhook riêng đường dẫn /b6/approve nhận quyết định duyệt từ app:
   cập nhật Status trong Content_Queue theo Post ID và ghi một dòng vào tab Publish_Log
   gồm Log ID, Post ID, Kênh, Status, Ngày duyệt, Người duyệt, Ghi chú.
5. Status hợp lệ chỉ gồm: Idea, Draft, Needs Review, Approved, Scheduled.
   KHÔNG tạo trạng thái Published và KHÔNG thêm bất kỳ node đăng bài nào lên mạng xã hội.
   Buổi học dừng ở Approved.
6. Cả hai node Webhook phải bật CORS với Allowed Origins = *, vì app duyệt là file HTML
   mở trực tiếp trong trình duyệt nên gọi cross-origin.
7. Mọi expression đọc dữ liệu webhook phải qua $json.body.xxx, không phải $json.xxx.
8. Học viên không phải tự viết expression dài. Bạn chịu trách nhiệm cấu hình node, expression,
   connection và credential reference.
9. KHÔNG ghi API key vào workflow JSON. Dùng credential đang có trên n8n.
10. Cột nội dung trong Sheets phải là văn bản đọc được, không đổ nguyên object JSON vào một ô.
    Kịch bản TikTok ghi mỗi khối một dòng.
11. Validate workflow sau khi tạo. Giữ workflow Inactive cho tới khi người dùng tự bật.
12. Export workflow thành file JSON vào khu vực checkpoint dành cho giảng viên.

TIÊU CHUẨN BÀN GIAO:
- workflow_id và tên workflow trên n8n.
- File export JSON parse được.
- Danh sách node theo bốn lớp.
- HAI webhook URL production: đường sinh nội dung và đường /b6/approve.
  Đây là thứ bt4b cần — in ra rõ ràng.
- Kết quả validation, và nêu rõ phần nào chưa runtime-test được.
- Hướng dẫn đúng một thao tác để chạy brief holdout.

QUY TẮC BẢO TOÀN:
- Không sửa hoặc xóa workflow ngoài phạm vi bài tập.
- Nếu workflow bài tập đã tồn tại, đọc nó trước rồi cập nhật thay vì tạo bản trùng lặp.
- Không tuyên bố chạy thành công nếu mới chỉ validate cấu trúc.
- Không tự bịa học phí, ưu đãi, ngày khai giảng hay số học viên vào prompt của bất kỳ node nào.
  Thiếu thông tin thì để [cần bổ sung] đi tiếp tới người duyệt.
```

**Chaining line:** Giữ nguyên chat. Hai webhook URL vừa in ra là input bắt buộc của bt4b.

**HITL:** Workflow chỉ đưa nội dung vào hàng đợi. Quyết định đăng luôn thuộc người phụ trách, thực hiện qua app duyệt ở bt4b.
