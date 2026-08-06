# Prompt Bước 1b — Thiết kế chi tiết Use-case (Usecase Design)

> Mục đích: Nhận diện chi tiết use-case đã chọn để đầu tư tự động hóa trước khi đi vào thiết kế workflow chi tiết.
> Chạy trong: Antigravity / AI Chat.

```text
BỐI CẢNH:
Tôi đã thực hiện phân tích ma trận ưu tiên và quyết định chọn một use-case để đầu tư tự động hóa. Hãy giúp tôi tạo tài liệu thiết kế chi tiết (01b-usecase-design.md) cho bài toán này.

=== HƯỚNG DẪN DÀNH CHO NGƯỜI DÙNG ===
- Bạn hãy thay thế nội dung dưới phần [THÔNG TIN ĐẦU VÀO] bằng Tên use-case hoặc mô tả ngắn của use-case bạn chọn.
- MẶC ĐỊNH nếu bạn để trống (hoặc giữ nguyên dòng mặc định dưới đây), AI sẽ tự động chọn và thiết kế cho use-case demo: "Tự động tổ chức và sắp xếp tài liệu/file trong doanh nghiệp" dựa trên bối cảnh Công ty Đông Dương Thương Mại.
=====================================

[THÔNG TIN ĐẦU VÀO]
Tên/mô tả ngắn của Use-case: Mình muốn làm luồng lấy ảnh bài làm của học sinh (đã chụp trước), nhận dạng, chấm điểm. Rồi 1 luồng tạo bài tập về nhà cho học sinh thì nên như thế nào. Cảm ơn thầy Lộc.

CHỈ DẪN VÀ CẤU TRÚC ĐẦU RA:
Hãy viết một tài liệu Markdown hoàn chỉnh có cấu trúc như sau:

# Thiết kế Chi tiết Use-case: [Tên Use-case]

## 1. Mô tả bài toán & Usecase
- Mô tả chi tiết bối cảnh, vấn đề và mục tiêu của use-case này khi được tự động hóa. (Nếu chạy use-case mặc định, hãy mô tả dựa trên bối cảnh: Công ty Đông Dương Thương Mại, folder "Tài liệu" có 1.200 file lộn xộn, tên tùy tiện, nhiều phiên bản trùng lặp, mất 30 phút tìm kiếm...).

## 2. Dữ liệu đầu vào (Input) & Đầu ra (Output)
- **Input:** Các loại file, định dạng, nguồn dữ liệu đầu vào (ví dụ: folder lộn xộn chứa file PDF, Docx, ảnh, OneDrive, Google Drive...).
- **Output:** Trạng thái kết quả đầu ra mong muốn (ví dụ: folder được cấu trúc rõ ràng, file được đổi tên theo chuẩn, báo cáo log thực thi...).

## 3. Giá trị kỳ vọng (Expected Value)
- **Định lượng (Quantitative):** Tiết kiệm bao nhiêu giờ/tuần, tăng tốc độ xử lý bao nhiêu %, giảm dung lượng rác bao nhiêu... (Nếu chạy use-case mặc định, hãy ghi số liệu kỳ vọng: tiết kiệm 4-5 giờ/tuần, giảm thời gian tìm kiếm từ 30 phút xuống dưới 3 phút, giải phóng 20%-30% dung lượng lưu trữ).
- **Định tính (Qualitative):** Nâng cao trải nghiệm làm việc, dễ dàng tìm kiếm, giảm bực bội cho nhân sự, chuẩn hóa quy trình dữ liệu doanh nghiệp.

## 4. Rủi ro cần quản lý (Risks & Mitigation)
- Các rủi ro có thể xảy ra khi vận hành tự động (ví dụ: AI nhận diện sai loại tài liệu, ghi đè/xóa nhầm file quan trọng, lỗi quyền truy cập hệ thống...).
- Phương án giảm thiểu tương ứng (mitigation).

## 5. Điểm chạm Con người (Human-in-the-Loop - HITL)
- Xác định rõ khi nào quy trình cần con người can thiệp (ví dụ: Duyệt kế hoạch di chuyển file trước khi chạy script thực tế, xử lý các file không nhận diện được...).

## 6. Các ràng buộc & Điều kiện biên khác (Constraints & Assumptions)
- Ràng buộc về công nghệ, chính sách bảo mật (ví dụ: Không lưu file PII/hợp đồng lên cloud công khai, chỉ chạy script Python trên môi trường máy local của người dùng...).

YÊU CẦU:
- Viết bằng tiếng Việt chuyên nghiệp, súc tích, thực tế.
- Trình bày dạng Markdown đẹp mắt, có bảng biểu hoặc gạch đầu dòng rõ ràng.
```
