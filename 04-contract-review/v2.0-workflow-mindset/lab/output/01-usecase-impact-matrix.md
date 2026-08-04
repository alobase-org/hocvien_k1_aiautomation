# Kết quả chạy mẫu BT 1 — Ma trận Hiệu quả × Độ phức tạp

Đây là kết quả chạy mẫu của **Bài tập 1 (Bước 1 · Usecase design)** khi thực hiện phân tích 10 vấn đề được liệt kê trong file `synthetic-data/company-dong-duong-thuongmai.md` bằng prompt `prompts/01-usecase-impact-matrix.md`.

---

## 1. Bảng đánh giá Use-case

| # | Use-case | Impact (1-5) | Difficulty (1-5) | Góc ma trận | Lý do ngắn |
|---|---|:---:|:---:|---|---|
| **1** | **Tự động chuẩn hóa tên + phân loại file** | **5** | **2** | 🟢 LÀM NGAY (Quick Win) | AI đọc hiểu và đổi tên file rất nhanh, giải quyết triệt để rác tên file. |
| **2** | **Tổ chức file vào đúng folder** | **5** | **2** | 🟢 LÀM NGAY (Quick Win) | Đã có sẵn script Python để thực thi, AI chỉ cần phân loại loại tài liệu. |
| **3** | **Phát hiện & gộp file trùng lặp** | **4** | **2** | 🟢 LÀM NGAY (Quick Win) | Sử dụng mã hash (MD5/SHA256) đơn giản để loại bỏ file trùng. |
| **4** | **Nhận diện version mới nhất** | **4** | **3** | 🟡 LÊN KẾ HOẠCH | Cần logic so sánh thời gian chỉnh sửa hoặc phân tích nội dung so khớp. |
| **5** | **Tìm kiếm tài liệu nhanh** | **5** | **3** | 🟡 LÊN KẾ HOẠCH | Cần lập chỉ mục (index) hoặc RAG để tìm kiếm theo ngữ cảnh. |
| **6** | **Gợi ý tài liệu cho dự án mới** | **5** | **3** | 🟡 LÊN KẾ HOẠCH | Cần AI trích xuất từ khóa và đối chiếu ngữ cảnh các dự án cũ. |
| **7** | **Tự động tìm và gửi file cho đồng nghiệp**| **4** | **3** | 🟡 LÊN KẾ HOẠCH | Đòi hỏi kết nối API công cụ chat (Zalo/Slack/Teams) và phân quyền. |
| **8** | **Thống nhất policy đặt tên** | **5** | **3** | 🟡 LÊN KẾ HOẠCH | Phụ thuộc nhiều vào sự thống nhất quy trình và con người trước. |
| **9** | **Gom dữ liệu tham khảo đa nguồn** | **4** | **4** | 🟡 LÊN KẾ HOẠCH | Phức tạp trong việc kết nối nhiều API khác nhau (Drive, OneDrive, Email). |
| **10**| **Tự động xóa file cũ theo retention** | **3** | **3** | 🔴 BỎ (Tạm thời) | Rủi ro xóa nhầm cao, lợi ích không quá cấp bách. |

---

## 2. Ma trận 2×2 (Hiệu quả × Độ phức tạp)

| | HIỆU QUẢ CAO (Impact ≥ 4) | HIỆU QUẢ THẤP (Impact ≤ 3) |
|---|---|---|
| **DỄ LÀM (Difficulty ≤ 2)** | **🟢 LÀM NGAY (Quick Wins)**<br>• UC1: Chuẩn hóa tên + phân loại file<br>• UC2: Tổ chức file vào đúng folder (Có script Python sẵn)<br>• UC3: Phát hiện & gộp file trùng | **🟡 KHI RẢNH**<br>*(Không có use-case nào)* |
| **KHÓ LÀM (Difficulty ≥ 3)** | **🟡 LÊN KẾ HOẠCH**<br>• UC4: Nhận diện version mới nhất<br>• UC5: Tìm kiếm tài liệu nhanh<br>• UC6: Gợi ý tài liệu cho dự án mới<br>• UC7: Tự động tìm & gửi file cho đồng nghiệp<br>• UC8: Thống nhất policy đặt tên<br>• UC9: Gom dữ liệu đa nguồn | **🔴 BỎ (Tạm thời)**<br>• UC10: Tự động xóa file cũ |

---

## 3. Top-3 Use-case khuyên dùng Automate TRƯỚC

1. **Tổ chức file vào đúng folder theo policy (Kết hợp UC1 & UC2) [ƯU TIÊN SỐ 1]**
   - *Lý do:* Giải quyết trực tiếp vấn đề thất lạc tài liệu, giúp dọn dẹp folder gọn gàng tức thì. Do có sẵn các template cấu trúc và script Python để thực thi, AI Agent chỉ cần phân tích nội dung rồi gọi script để chạy, cực kỳ tối ưu và an toàn.
2. **Phát hiện & gộp file trùng lặp (UC3)**
   - *Lý do:* Giảm ngay dung lượng lưu trữ thừa thãi và dọn dẹp các bản copy rác một cách tự động thông qua việc so khớp hash của file.
3. **Tìm kiếm tài liệu nhanh theo ngữ cảnh (UC5)**
   - *Lý do:* Giúp loại bỏ hoàn toàn việc tốn 30 phút tìm kiếm thủ công cho nhân viên. Dù cần lên kế hoạch xây dựng cơ sở dữ liệu hoặc index tài liệu, nhưng lợi ích đem lại cho hiệu suất công việc là khổng lồ.

**👉 Lựa chọn Use-case cho Bước 2:** **Tự động tổ chức tài liệu (phân loại + di chuyển file đúng folder theo policy, có người duyệt trước - HITL).**
