# Hướng dẫn Thực hành 2 — Redaction 4 cấp bảo mật dữ liệu trước khi qua AI (15')

> **Thuộc bài lab**: [Buổi 04: Thẩm định hợp đồng tự động](./lab.md)  
> **Tư duy trọng tâm**: **Redaction 4 cấp (Bảo mật dữ liệu nguồn CCHC & Data Privacy First)** — Che thông tin nhạy cảm (PII, MST, tài chính, tên người đại diện) trong Code Node n8n trước khi gửi dữ liệu sang AI Cloud, đồng thời đặt cổng Security Gate dừng luồng nếu phát hiện từ khóa tối mật.

---

## 🎯 Mục tiêu bài thực hành
- Khám phá và vận hành Code Node `TH1 - Redaction 4 Cap` trong n8n Workflow đối với hợp đồng đầu vào (`.docx` / text).
- Bảo đảm 100% PII cá nhân (Email, SĐT), Mã số thuế (MST), Giá trị tài chính và Tên đại diện được che bằng placeholder mà **không làm thay đổi cấu trúc các điều khoản hợp đồng**.
- Đặt cổng kiểm soát Security Gate Cấp 4 dừng workflow ngay lập tức nếu văn bản chứa từ khóa tối mật (`toi mat`, `tuyet mat`, `bi mat nha nuoc`).
- Quan sát kết quả biến `contract_redacted` trong Notebook Step 3 làm đầu vào an toàn cho bài Thực hành 3.

---

## 📥 Input → ⚙️ Action → 📤 Output

- **Input**: Văn bản hợp đồng thô từ node `Extract .docx / Normalize Input` (gốc là file `templates/contract-mau-hop-dong-dich-vu.docx` chứa PII: Tên đại diện Nguyễn Văn An, Trần Thị Bình, SĐT, Email, MST, Giá trị tài chính).
- **Action**: 
  1. Đọc văn bản hợp đồng vào Node `TH1 - Redaction 4 Cap`.
  2. Code Node Regex thực hiện Redaction 4 cấp độ:
     - **Cấp 1 (PII cá nhân)**: Che Email `[email redact]`, SĐT `0xxx`.
     - **Cấp 2 (Doanh nghiệp & Tài chính)**: Che Mã số thuế `[MST redact]`, Giá trị tài chính `[gia tri redact]`.
     - **Cấp 3 (Nhạy cảm nghiệp vụ)**: Che tên người đại diện thành `Dai dien Ben A`, `Dai dien Ben B`.
     - **Cấp 4 (Security Gate Tối mật)**: Quét từ khóa `toi mat`, `tuyet mat`, `bi mat nha nuoc` (đã strip dấu) ➡️ `throw new Error('SECURITY GATE CAP 4...')` dừng workflow ngay lập tức.
- **Output**: Thuộc tính `contract_redacted` trong JSON item chứa văn bản đã che 100% thông tin nhạy cảm.

---

## 🛠️ Công cụ & Tài nguyên
- **Tool chính**: n8n Workflow Node `TH1 - Redaction 4 Cap` (Code Node JavaScript/Python Regex) & Jupyter Notebook Step 3.
- **File solution n8n**: `checkpoints/n8n-contract-review-solution.json`.
- **File mẫu đầu vào**: `templates/contract-mau-hop-dong-dich-vu.docx`.

---

## 📊 Tiêu chuẩn Nghiệm thu (SLI/SLO)
- [ ] **100% PII cá nhân (Email, SĐT)** được chuyển thành placeholder (`[email redact]`, `0xxx`).
- [ ] **Mã số thuế + Giá trị tài chính** được chuyển thành `[MST redact]`, `[gia tri redact]`.
- [ ] **Tên đại diện 2 bên** được chuẩn hóa thành `Dai dien Ben A`, `Dai dien Ben B`.
- [ ] **Cổng Security Gate Cấp 4 hoạt động chuẩn xác**: dừng luồng nếu phát hiện từ khóa tối mật.
- [ ] **Cấu trúc điều khoản giữ nguyên 100%**, chỉ che giá trị, không làm mất bất kỳ tiêu đề hoặc nội dung điều khoản nào.

---

## ⏱️ Các bước thực hiện (Time-box 15')

1. **Bước 1 (3') — Khám phá Node Redaction trên Canvas UI**:
   - Truy cập n8n Canvas UI (`http://localhost:5678`), mở workflow solution **B4 K1 - Contract Review Agent...**.
   - Mở node **"TH1 - Redaction 4 Cap"** để xem đoạn mã xử lý 4 cấp độ Redaction.

2. **Bước 2 (5') — Trải nghiệm Redaction qua Jupyter Notebook Step 3**:
   - Mở notebook [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb).
   - Chạy **Step 3: Vận hành Node Redaction 4 Cấp Bảo mật PII trên n8n**.
   - Notebook sẽ gọi n8n API (`GET /api/v1/workflows/{id}`) để lấy và hiển thị trực tiếp cấu hình mã nguồn Node Redaction.

3. **Bước 3 (4') — Kiểm tra kết quả Redacted Text**:
   - Quan sát văn bản hợp đồng sau khi qua bước Redaction:
     - Email: `[email redact]`
     - SĐT: `0xxx`
     - Mã số thuế: `[MST redact]`
     - Giá trị hợp đồng: `[gia tri redact]`
     - Tên đại diện: `Dai dien Ben A`, `Dai dien Ben B`
   - Xác nhận cấu trúc các điều khoản HD01, HD02, HD03... vẫn được giữ nguyên đầy đủ.

4. **Bước 4 (3') — Thử nghiệm Security Gate Cấp 4**:
   - Thử chèn từ khóa "Tối mật" hoặc "Bí mật nhà nước" vào hợp đồng đầu vào.
   - Chạy thử workflow và xác nhận Node `TH1 - Redaction 4 Cap` báo lỗi `SECURITY GATE CAP 4` dừng luồng lập tức.

---

## 🔒 Nguyên tắc Safety & Control
> **CRITICAL**: Đây chính là cổng kiểm soát dữ liệu nguồn (Privacy Gate). Nếu hợp đồng chứa thông tin thuộc Cấp 4 (Mật / Bí mật nhà nước), hệ thống sẽ dừng workflow (STOP) và tuyệt đối không gửi sang AI Cloud công cộng.

---

## 🆘 Hướng dẫn khi bị kẹt (Stuck > 8')
- Xem cấu hình mã nguồn node trong [checkpoints/n8n-contract-review-solution.json](./checkpoints/n8n-contract-review-solution.json) tại vị trí node ID `th1-redaction`.
