# Phân tích Usecase Design — Ma trận Hiệu quả × Độ phức tạp (BT 1a)

Dưới đây là kết quả phân tích độ ưu tiên tự động hóa cho danh sách 6 vấn đề mặc định của phòng ban/doanh nghiệp dựa trên ma trận Hiệu quả (Impact) và Độ phức tạp (Difficulty).

---

## 1. Bảng Đánh Giá Chi Tiết Use-Case

| # | Use-case | Impact (1-5) | Difficulty (1-5) | Góc ma trận | Lý do ngắn |
|:---:|---|:---:|:---:|---|---|
| **1** | **Tổ chức dữ liệu & tài liệu lộn xộn** | **5** | **2** | 🟢 LÀM NGAY (Quick Win) | Đã có sẵn script Python để thực thi, AI Agent chỉ cần đọc cấu trúc và chạy script. Tiết kiệm 30 phút tìm kiếm mỗi lần. |
| **2** | **Sales tổng hợp báo cáo doanh số từ 3 cửa hàng** | **4** | **2** | 🟢 LÀM NGAY (Quick Win) | Dữ liệu doanh số từ các cửa hàng thường có cấu trúc cột cố định, dễ gộp tự động bằng script Excel/Python. |
| **3** | **CSKH trả lời 5 câu hỏi lặp đi lặp lại qua Zalo** | **4** | **2** | 🟢 LÀM NGAY (Quick Win) | Phạm vi câu hỏi hẹp (chỉ 5 câu FAQ), luật rõ ràng, dễ cấu hình chatbot hoặc webhook tự động hóa. |
| **4** | **HR sàng lọc 200 CV mỗi đợt tuyển** | **4** | **3** | 🟡 LÊN KẾ HOẠCH | CV ở định dạng phi cấu trúc (PDF/Word/Ảnh) và tiêu chí lọc thay đổi theo đợt, cần tích hợp LLM và quy trình duyệt HITL. |
| **5** | **Kế toán nhập tay hóa đơn vào Excel** | **5** | **4** | 🟡 LÊN KẾ HOẠCH | Hóa đơn có nhiều định dạng/ảnh scan khác nhau, cần công nghệ OCR độ chính xác cao và LLM xử lý dữ liệu tài chính nhạy cảm. |
| **6** | **Marketing viết caption FB mỗi ngày** | **3** | **2** | ⚪ KHI RẢNH | Dễ dàng sinh nội dung bằng LLM theo prompt có sẵn, nhưng tác động đo lường được lên doanh số chưa cao và ít khẩn cấp. |

---

## 2. Ma Trận Ưu Tiên 2×2 (Hiệu quả × Độ phức tạp)

| | HIỆU QUẢ CAO (Impact ≥ 4) | HIỆU QUẢ THẤP (Impact ≤ 3) |
|---|---|---|
| **DỄ LÀM (Difficulty ≤ 2)** | **🟢 LÀM NGAY (Quick Wins)**<br>• UC1: Tổ chức dữ liệu & tài liệu lộn xộn (Impact 5, Difficulty 2)<br>• UC2: Sales tổng hợp báo cáo doanh số (Impact 4, Difficulty 2)<br>• UC3: CSKH trả lời FAQ qua Zalo (Impact 4, Difficulty 2) | **⚪ KHI RẢNH**<br>• UC6: Marketing viết caption FB (Impact 3, Difficulty 2) |
| **KHÓ LÀM (Difficulty ≥ 3)** | **🟡 LÊN KẾ HOẠCH**<br>• UC4: HR sàng lọc CV (Impact 4, Difficulty 3)<br>• UC5: Kế toán nhập hóa đơn (Impact 5, Difficulty 4) | **🔴 BỎ (Tạm thời)**<br>*(Không có use-case nào)* |

---

## 3. Top-3 Use-Case Nên Tự Động Hóa TRƯỚC

1. **Tổ chức dữ liệu & tài liệu lộn xộn (UC1) [ƯU TIÊN SỐ 1]**
   - *Lý do:* Giải quyết trực tiếp nỗi đau mất 30 phút tìm kiếm tài liệu của quản lý phòng ban. Do có sẵn các file mẫu dữ liệu giả lập và các script Python tự động hóa để di chuyển/đổi tên file vật lý, AI Agent chỉ cần đọc hiểu cấu trúc để thực thi, đảm bảo độ phức tạp ở mức cực thấp nhưng mang lại giá trị tức thì.
2. **Sales tổng hợp báo cáo doanh số từ 3 cửa hàng (UC2)**
   - *Lý do:* Tiết kiệm ngay 4 giờ làm việc thủ công vào mỗi cuối tuần cho nhân viên Sales, loại bỏ nguy cơ sai sót số liệu do sao chép thủ công trên các file Excel.
3. **CSKH trả lời 5 câu hỏi lặp đi lặp lại qua Zalo (UC3)**
   - *Lý do:* Tối ưu hóa thời gian phản hồi cho khách hàng (phản hồi ngay lập tức), giải phóng sức lao động của nhân viên hỗ trợ khỏi những câu hỏi lặp đi lặp lại nhàm chán.

---

**👉 Đề xuất Use-case cho Bước 1b tiếp theo:** **Tổ chức dữ liệu & tài liệu lộn xộn (Tự động hóa chuẩn hóa tên file và sắp xếp vào đúng folder theo quy định).**
