# Thiết kế Chi tiết Use-case: Tự động tổ chức và sắp xếp tài liệu (Document Organization Workflow)

## 1. Mô tả bài toán & Usecase
* **Bối cảnh:** Tại Công ty Đông Dương Thương Mại, lượng tài liệu phát sinh hàng ngày từ nhiều nguồn khác nhau (email, Zalo, Drive, download từ internet) rất lớn. Sau 6 tháng, thư mục "Tài liệu" trở nên vô cùng lộn xộn với khoảng 1.200 file không theo bất kỳ quy chuẩn nào.
* **Vấn đề tồn tại:** 
  - Tên file đặt tùy tiện, thiếu nhất quán (ví dụ: `Document(1).pdf`, `baocao_final_final.docx`).
  - Tồn tại quá nhiều phiên bản của cùng một tài liệu khiến nhân viên không biết đâu là bản mới nhất để sử dụng.
  - File nằm sai chỗ, chồng chéo, lẫn lộn giữa tài liệu công việc và cá nhân.
  - Tốn quá nhiều thời gian tìm kiếm (trung bình 30 phút/lần).
* **Mục tiêu tự động hóa:** Xây dựng một AI Agent sử dụng mô hình ngôn ngữ lớn (LLM) để đọc hiểu nội dung tệp tin, tự động phân loại tài liệu, chuẩn hóa tên file theo quy định của doanh nghiệp và di chuyển/sao chép chúng về đúng cấu trúc thư mục mục tiêu một cách an toàn, chính xác.

## 2. Dữ liệu đầu vào (Input) & Đầu ra (Output)
* **Dữ liệu đầu vào (Input):**
  - Thư mục nguồn (folder lộn xộn trên máy tính cá nhân hoặc cloud drive) chứa các tài liệu đa định dạng: văn bản (`.docx`, `.pdf`), bảng tính (`.xlsx`), hình ảnh scan/chụp (`.png`, `.jpg`), file ghi chú (`.txt`, `.md`).
  - Bộ quy chuẩn đặt tên file và sơ đồ cây thư mục (Directory Policy) của công ty.
  - Các script Python hỗ trợ xử lý file vật lý (copy, move, rename).
* **Kết quả đầu ra (Output):**
  - Thư mục đích được tổ chức phân cấp rõ ràng theo năm/tháng hoặc theo phòng ban/dự án (ví dụ: `/HopDong/2026/`, `/BaoCao/Thang07/`).
  - Các file được chuẩn hóa tên theo cú pháp thống nhất: `[LoaiTaiLieu]_[TenDoiTac/DuAn]_[NgayThang]_[PhienBan].[DuoiFile]`.
  - File log ghi nhận chi tiết lịch sử thực thi (`execution_log.csv`) bao gồm: đường dẫn gốc, đường dẫn đích mới, trạng thái xử lý, mã hash kiểm tra trùng lặp và thời gian thực hiện.

## 3. Giá trị kỳ vọng (Expected Value)
* **Định lượng (Quantitative):**
  - Tiết kiệm ít nhất **4 - 5 giờ làm việc/tuần** cho mỗi nhân sự quản lý thông qua việc loại bỏ các thao tác kéo-thả, đổi tên thủ công.
  - Rút ngắn thời gian tìm kiếm tài liệu từ **30 phút xuống còn dưới 3 phút** nhờ cấu trúc thư mục tối ưu và tên file rõ ràng.
  - Giải phóng từ **20% - 30% dung lượng lưu trữ** lãng phí do việc dọn dẹp các tệp trùng lặp.
* **Định tính (Qualitative):**
  - Nâng cao trải nghiệm làm việc của nhân sự, giảm thiểu sự ức chế khi không tìm thấy tài liệu quan trọng trong tình huống khẩn cấp.
  - Thiết lập tính kỷ luật dữ liệu (data discipline) trong doanh nghiệp, tạo nền tảng vững chắc để xây dựng hệ thống quản trị tri thức (Knowledge Base) hoặc RAG (Retrieval-Augmented Generation) sau này.

## 4. Rủi ro cần quản lý (Risks & Mitigation)
* **Rủi ro 1: AI đọc hiểu sai nội dung dẫn đến phân loại sai thư mục hoặc đổi tên không đúng.**
  - *Biện pháp giảm thiểu:* Sử dụng prompt phân loại có cấu trúc chặt chẽ (JSON mode) kèm theo các ví dụ (few-shot). Thiết lập thư mục đệm `/RecycleBin_Pending/` hoặc `/Can_Kiem_Tra/` cho các trường hợp độ tin cậy của AI (confidence score) thấp hơn 80%.
* **Rủi ro 2: AI ghi đè làm mất hoặc hư hỏng dữ liệu gốc của file quan trọng.**
  - *Biện pháp giảm thiểu:* Áp dụng nguyên tắc "Copy-then-Verify-then-Delete". Script Python chỉ thực hiện sao chép file sang thư mục đích, xác minh tính toàn vẹn (checksum) rồi mới tiến hành dọn dẹp file gốc. Không cho phép AI Agent xóa trực tiếp file gốc nếu chưa được cấu hình kiểm thử kỹ lưỡng.
* **Rủi ro 3: Xung đột quyền truy cập tệp tin (File locked) hoặc mất kết nối mạng giữa chừng.**
  - *Biện pháp giảm thiểu:* Thiết kế script Python có cơ chế xử lý lỗi ngoại lệ (Try-Catch), tự động bỏ qua các file đang mở (locked) và lưu vào danh sách chờ xử lý ở phiên làm việc sau, tránh làm sập toàn bộ luồng tự động hóa.

## 5. Điểm chạm Con người (Human-in-the-Loop - HITL)
* **Duyệt kế hoạch thực thi (Review Plan):** Trước khi script Python thực tế di chuyển hoặc đổi tên file vật lý trên ổ đĩa, AI Agent phải xuất ra một bảng danh sách dự kiến đổi tên (Proposed Plan). Người dùng sẽ xem qua bảng đề xuất này trên giao diện terminal hoặc dashboard và nhấn "Approve" (Xác nhận) thì quy trình mới tiến hành chạy thực tế.
* **Xử lý tài liệu ngoại lệ (Exception Handling):** Đối với các tài liệu không thể nhận diện được (file ảnh mờ, file hỏng, hoặc định dạng lạ), AI Agent sẽ di chuyển chúng về thư mục `/Can_Phan_Loai_Thu_Cong/` và gửi thông báo cho quản lý để xử lý bằng tay.

## 6. Các ràng buộc & Điều kiện biên khác (Constraints & Assumptions)
* **Bảo mật dữ liệu (Data Privacy):** Tuyệt đối không gửi trực tiếp nội dung các tài liệu nhạy cảm liên quan đến thông tin cá nhân (PII), bảng lương, hoặc hợp đồng mật lên các API công cộng không có thỏa thuận bảo mật dữ liệu. Khuyến nghị sử dụng các dịch vụ LLM nội bộ (Local LLM) hoặc API phiên bản Enterprise có cam kết không dùng dữ liệu để train model.
* **Ràng buộc hạ tầng:** Giải pháp phải hoạt động trực tiếp dưới dạng một công cụ độc lập trên máy local của người dùng (chạy bằng Python), không yêu cầu setup server hay hệ thống cơ sở dữ liệu phức tạp của doanh nghiệp, giúp việc triển khai nhanh chóng và dễ dàng.
