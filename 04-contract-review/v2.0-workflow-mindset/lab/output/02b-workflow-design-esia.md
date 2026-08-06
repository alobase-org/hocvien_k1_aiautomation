# Thiết kế Quy trình Mới (To-be Workflow Design - ESIA)

Tài liệu này trình bày thiết kế quy trình To-be sau khi áp dụng khung tư duy ESIA (Eliminate - Simplify - Integrate - Automate) cho use-case **Tự động tổ chức tài liệu**, dựa trên quy trình As-is đã được con người review và hiệu chỉnh tại [02a-workflow-as-is.md](02a-workflow-as-is.md).

---

## 1. Bảng quy trình To-be (Sau ESIA)

| # | Bước (to-be) | E/S/I/A | Chi tiết tối ưu & Điểm chạm HITL | Ai làm (AI/Người) | Nhánh automation |
|---|---|---|---|---|---|
| **1** | Quét thư mục nguồn và đọc metadata tệp tin | **I** (Integrate) | Thu thập danh sách các tệp tin hiện có từ thư mục nguồn local/cloud. Trích xuất tên, phần mở rộng, dung lượng, ngày sửa đổi cuối cùng thành một danh sách quản lý tập trung. | AI Agent | AI Agent (Antigravity/Python) |
| **2** | Đọc nội dung tệp tin & phân loại loại tài liệu | **A** (Automate) | AI đọc lướt nội dung văn bản (đối với `.docx`, `.pdf`, `.txt`) hoặc sử dụng Vision API (đối với hình ảnh scan `.png`, `.jpg`, bao gồm hóa đơn từ Zalo/Viber) để xác định loại tài liệu. | AI Agent | AI Agent (Antigravity/LLM) |
| **3** | Chuẩn hóa tên file theo quy chuẩn | **S** (Simplify) | Tự động tạo tên file mới dựa trên quy định: `[LoaiTaiLieu]_[TenDoiTac/DuAn]_[NgayThang]_[PhienBan].[DuoiFile]`. Loại bỏ các hậu tố thừa thãi (`final_final`, `copy of...`). | AI Agent | AI Agent (LLM Prompting) |
| **4** | Lập kế hoạch di chuyển & đối chiếu cấu trúc thư mục đích | **A** (Automate) | AI đối chiếu với sơ đồ cây thư mục của công ty để đề xuất vị trí lưu trữ mới cho từng file (vd: `/HopDong/2026/`).  <br>**[HITL] Xuất "Proposed Plan" cho người dùng duyệt.** | AI + Con người | AI Agent + Terminal UI |
| **5** | Kiểm tra file trùng lặp qua mã hash | **A** (Automate) | So sánh mã hash MD5/SHA256 của các file. Nếu trùng mã hash, đề xuất gộp hoặc chỉ giữ lại bản mới nhất và chuyển các bản cũ vào thư mục lưu trữ tạm. | AI Agent | Script Python |
| **6** | Thực thi di chuyển/sao chép file | **A** (Automate) | Thực thi di chuyển file vật lý trên ổ đĩa. Tuân thủ nguyên tắc "Copy-then-Verify-then-Delete" để bảo vệ dữ liệu gốc. <br>**[HITL] Chỉ thực hiện xóa file gốc trong thư mục Downloads khi có xác nhận an toàn từ user.** | AI Agent | Script Python |
| **7** | Ghi nhận nhật ký thực thi (Execution Log) | **A** (Automate) | Tự động ghi nhận thông tin thực thi vào file `execution_log.csv` (đường dẫn cũ, đường dẫn mới, thời gian, trạng thái xử lý). | AI Agent | Script Python |
| **8** | Tự động gửi thông báo hoặc chia sẻ file | **A** (Automate) | Tự động gửi link file đã được phân loại đến các kênh truyền thông tương ứng (nhóm Zalo/Email/Slack) thông qua webhook. | AI Agent / n8n | n8n / Slack Node / Zalo API |

---

## 2. Chi tiết các điểm chạm Con người (Human-in-the-Loop - HITL)

Việc tự động hóa 100% quy trình này tiềm ẩn rủi ro phá hủy hoặc thất lạc dữ liệu quan trọng của doanh nghiệp. Do đó, các điểm chạm con người dưới đây là bắt buộc:
1. **Duyệt kế hoạch thực thi (Review Plan - Bước 4):** Trước khi script Python thực tế di chuyển hoặc đổi tên file vật lý trên ổ đĩa, AI Agent phải xuất ra một bảng danh sách dự kiến đổi tên (Proposed Plan). Người dùng sẽ xem qua bảng đề xuất này trên giao diện terminal hoặc dashboard và nhấn "Approve" (Xác nhận) thì quy trình mới tiến hành chạy thực tế.
2. **Xử lý tài liệu ngoại lệ (Exception Handling):** Đối với các tài liệu không thể nhận diện được (file ảnh mờ, file hỏng, hoặc định dạng lạ), AI Agent sẽ di chuyển chúng về thư mục `/Can_Phan_Loai_Thu_Cong/` và gửi thông báo cho quản lý để xử lý bằng tay.
3. **Giữ bản gốc tạm thời (Bước 6):** Script Python thực hiện copy file sang thư mục đích, xác minh tính toàn vẹn (checksum) rồi mới tiến hành dọn dẹp file gốc (sau khi có sự đồng ý của user), tránh trường hợp AI Agent xóa nhầm file khi chưa được cấu hình kiểm thử kỹ lưỡng.

---

## 3. Compliance Note (Lưu ý tuân thủ)

* **Bảo mật dữ liệu (Data Privacy):** Tuyệt đối không gửi trực tiếp nội dung các tài liệu nhạy cảm liên quan đến thông tin cá nhân (PII), bảng lương, hoặc hợp đồng mật lên các API công cộng không có thỏa thuận bảo mật dữ liệu. Khuyến nghị sử dụng các dịch vụ LLM nội bộ (Local LLM) hoặc API phiên bản Enterprise có cam kết không dùng dữ liệu để train model.
