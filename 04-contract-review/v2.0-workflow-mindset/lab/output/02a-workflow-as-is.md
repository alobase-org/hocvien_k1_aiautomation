# As-is (Hiện trạng: Sắp xếp tài liệu thủ công)

## Quy trình: Sắp xếp tài liệu vào folder đúng
**Người thực hiện:** Quản lý / Chiến lược gia công ty Đông Dương Thương Mại  
**Tần suất:** Hàng ngày, tổng thời gian khoảng 2-3 giờ/tuần  
**Mục đích:** Sắp xếp các tài liệu rải rác từ các nguồn (email, Zalo, Drive, download) vào thư mục của phòng ban/dự án tương ứng để tiện tra cứu.

| # | Bước | Người thực hiện | Input | Output | Điểm nghẽn / Lỗi lặp |
|---|---|---|---|---|---|
| **1** | Nhận file từ nhiều nguồn khác nhau | Quản lý | File đính kèm từ Zalo, Email, link Drive | Các file tải về lộn xộn trong thư mục `Downloads` | Dữ liệu bị phân tán, dễ tải thiếu hoặc nhầm bản. |
| **2** | Mở từng file để xem nội dung | Quản lý | File thô chưa biết rõ nội dung | Hiểu nội dung chính của tài liệu | Cực kỳ tốn thời gian khi số lượng file lớn (hàng trăm file/lần). |
| **3** | Quyết định vị trí lưu trữ (folder nào) | Quản lý | Hiểu biết về nội dung file | Lựa chọn thư mục đích phù hợp | Thiếu quy chuẩn (policy) thống nhất dẫn đến việc lưu trữ tùy hứng, không đồng bộ giữa các thành viên. |
| **4** | Đổi tên file thủ công (hoặc để nguyên) | Quản lý | File ở dạng thô | File đã đổi tên | Đặt tên tùy tiện (`Document(1).pdf`, `baocao_final_final.docx`), dẫn đến việc khó tra cứu và không kiểm soát được phiên bản. |
| **5** | Di chuyển/Copy file vào thư mục đích | Quản lý | File đã đổi tên | File nằm trong thư mục đích | Thao tác kéo thả thủ công dễ nhầm lẫn thư mục, dễ xảy ra lỗi ghi đè làm mất dữ liệu của các phiên bản khác. |
| **6** | Tìm kiếm tài liệu khi cần | Quản lý | Từ khóa nhớ mang máng | File tài liệu cần tìm | Mất trung bình 15-30 phút/lần mở lần lượt các folder để dò tìm do cấu trúc thư mục lộn xộn. |

* **Tổng thời gian lãng phí:** ~3 giờ/tuần để sắp xếp + ~2 giờ/tuần tìm kiếm = **5 giờ/tuần/nhân sự.**

---

## 👥 Xác nhận & Hiệu chỉnh từ Người dùng (Human Review)

> [!IMPORTANT]
> Đây là bước Human-in-the-Loop (HITL) bắt buộc trong Bước 2 của quy trình thiết kế để đảm bảo AI không mô tả sai thực trạng thực tế của doanh nghiệp.

### Trạng thái Review: 
- **Người thực hiện:** Nguyễn Văn A (Quản lý vận hành - Đông Dương Thương Mại)
- **Ngày review:** 2026-07-11
- **Đánh giá:** Quy trình As-is do AI phác thảo sơ bộ đã phản ánh chính xác 85% các bước thủ công hiện tại. Tuy nhiên cần bổ sung và hiệu chỉnh một số điểm nghẽn thực tế sau để làm dữ liệu đầu vào cho bước ESIA (To-be).

### Các điểm hiệu chỉnh/bổ sung thủ công:
1. **Bổ sung chi tiết tại Bước 1 (Nhận file):** Các nguồn file thực tế phức tạp hơn, bao gồm cả các file xuất ra từ phần mềm ERP nội bộ và ảnh chụp hóa đơn gửi qua Viber/Zalo của khách hàng.
2. **Hiệu chỉnh tại Bước 5 (Di chuyển file):** Ngoài việc kéo thả thủ công nhầm thư mục, một vấn đề lớn là nhân sự thường quên xóa file cũ ở thư mục `Downloads`, dẫn đến việc ổ cứng máy tính cá nhân nhanh chóng bị đầy và chứa hàng chục bản copy không rõ phiên bản nào mới nhất.
3. **Bổ sung Bước 7 (Gửi báo cáo / Chia sẻ file):** Sau khi sắp xếp xong, người thực hiện phải copy link file hoặc gửi file đính kèm thủ công qua nhóm chat Zalo của phòng ban liên quan để báo cáo. Bước này tốn thêm khoảng **1 giờ/tuần** nhưng AI đã bỏ sót trong bản thảo ban đầu.
4. **Cập nhật số liệu lãng phí thực tế:** Tổng thời gian thực tế lãng phí của một nhân sự là khoảng **6 giờ/tuần** (thay vì 5 giờ như AI ước tính ban đầu).
