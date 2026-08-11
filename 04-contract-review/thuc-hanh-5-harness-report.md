# Hướng dẫn Thực hành 5 — Full Master Pipeline Automation & Report Engine Word (25', capstone)

> **Thuộc bài lab**: [Buổi 04: Thẩm định hợp đồng tự động](./lab.md)  
> **Tư duy trọng tâm**: **Full Pipeline Automation & Professional Reporting (OOXML & HITL)** — Nối gộp toàn bộ các bước thành 1 Master Workflow n8n chạy tự động 1-click end-to-end (kết nối Webhook & ReactJS Web App), tự động tính điểm rủi ro và render file Báo cáo Thẩm định Hợp đồng dạng Word (`report.docx`) chuẩn thể thức văn bản hành chính theo Nghị định 30 có khung ký duyệt HITL.

---

## 🎯 Mục tiêu bài thực hành
- Nối liền toàn bộ luồng xử lý trên n8n: **Webhook Trigger ➡️ Normalize Input ➡️ TH1 Redaction 4 Cấp ➡️ TH2 AI Extract Gemini 3.6 Flash & Schema Validation Loop ➡️ TH3 Evidence & Omission Check ➡️ TH4 Policy Review vs KB Red Flags ➡️ TH5 Report Engine + Build report.docx ➡️ Respond report.docx**.
- Vận hành Node `TH5 - Report Engine + Build report.docx` (tự động tính điểm Contract Risk Score `0-100` và đóng gói file Word OOXML ZIP mà không cần phụ thuộc thư viện bên ngoài).
- Kích hoạt pipeline 1-click qua ứng dụng ReactJS Web App (`http://localhost:5173`) hoặc Jupyter Notebook Step 6.
- Kiểm tra file Báo cáo Word `report.docx` hoàn chỉnh gồm: Quốc hiệu/Tiêu ngữ, Bảng tổng hợp điểm rủi ro, Bảng điều khoản bị thiếu, Bảng bẫy rủi ro Red Flags, Bảng rà soát chi tiết từng điều khoản kèm emoji severity (🔴 HIGH / 🟡 MED / 💡 LOW) và Bảng ký duyệt HITL.

---

## 📥 Input → ⚙️ Action → 📤 Output

- **Input**: Request chứa văn bản hợp đồng từ Webhook (`POST /webhook/contract-review`) hoặc ReactJS Web App (`http://localhost:5173`).
- **Action**: 
  1. Master Pipeline n8n tự động chạy qua tất cả các cổng kiểm soát (Redaction 4 Cấp, Schema Gate, Evidence Match, Policy Review).
  2. Node `TH5 - Report Engine + Build report.docx`:
     - Công thức tính điểm rủi ro: `Contract Risk Score = max(0, 100 - nHigh*12 - nMed*4 - nRedFlagHigh*8 - nHallu*20 - nOmit*10)`.
     - Phê duyệt tự động: `approved = (score >= 70 && nHallu == 0 && nRedFlagHigh == 0)`.
     - Render tài liệu XML WordprocessingML (`document.xml`, `styles.xml`) với phông chữ chuẩn **Times New Roman**, cỡ chữ 13-14pt, giãn dòng 1.15-1.5, lề chuẩn hành chính (trên/dưới 20mm, trái 30mm, phải 15mm).
     - Đóng gói file thành định dạng binary `report.docx`.
  3. Node `Respond report.docx` trả file binary Word về trực tiếp cho Web App/Notebook client.
- **Output**: File Word Báo cáo Thẩm định Hợp đồng `report.docx` được tự động tải về máy người dùng.

---

## 🛠️ Công cụ & Tài nguyên
- **Tool chính**: Master Workflow n8n v4 (`B4 K1 - Contract Review Agent (Webhook text + Report DOCX) - v4`), ReactJS Web App (`http://localhost:5173`), Jupyter Notebook Step 6.
- **Node chính**: `TH5 - Report Engine + Build report.docx` & `Respond report.docx`.
- **Jupyter Demo Notebook**: Step 6 trong [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb).

---

## 📊 Tiêu chuẩn Nghiệm thu (SLI/SLO)
- [ ] Master Workflow chạy end-to-end **1-click** từ file hợp đồng `.docx` / dán text trên Web App đến ra file báo cáo Word.
- [ ] File `report.docx` tạo ra mở được bằng Microsoft Word / Google Docs mà không bị lỗi đính kèm.
- [ ] Báo cáo tuân thủ chuẩn thể thức văn bản hành chính (Nghị định 30): Có Quốc hiệu/Tiêu ngữ, Tên cơ quan ban hành, Tiêu đề Báo cáo, 5 mục nội dung La Mã rõ ràng.
- [ ] Phản ánh chính xác các chỉ tiêu: Contract Risk Score, số lượng rủi ro HIGH/MED, danh sách thiếu điều khoản, red flags và bảng ý kiến phê duyệt HITL.

---

## ⏱️ Các bước thực hiện (Time-box 25')

1. **Bước 1 (3') — Khám phá Node Report Engine OOXML (TH5)**:
   - Mở n8n Canvas UI, chọn node **"TH5 - Report Engine + Build report.docx"**.
   - Quan sát công thức tính điểm `score`, logic kiểm tra `approved` và hàm `buildZip` tự đóng gói tài liệu OOXML `.docx`.

2. **Bước 2 (5') — Trải nghiệm Pipeline 1-Click trên ReactJS Web App**:
   - Truy cập giao diện ReactJS Web App tại `http://localhost:5173`.
   - Nhấn nút **"Nạp Hợp đồng Mẫu (Red Flags Test)"** hoặc nạp file `.docx`.
   - Nhấn **"Phân tích & Xuất Báo cáo Word"**.
   - Quan sát trình duyệt tự động gọi n8n Webhook và nhận về file `report.docx`.

3. **Bước 3 (7') — Trải nghiệm Pipeline qua Jupyter Notebook Step 6**:
   - Mở notebook [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb).
   - Chạy **Step 6: Vận hành Master Pipeline & Tự động xuất Báo cáo Word trên n8n**.
   - Kiểm tra kết quả báo cáo hiển thị 5 dòng đầu và số lượng paragraph tạo ra.

4. **Bước 4 (6') — Kiểm định File Báo cáo Word (`report.docx`)**:
   - Mở file `report.docx` vừa tạo trong Microsoft Word / Pages.
   - Kiểm tra:
     - Header: CÔNG TY/ĐƠN VỊ THẨM ĐỊNH - PHÒNG PHÁP CHẾ & Quốc hiệu Tiêu ngữ.
     - Mục I: Tóm tắt kết quả (Score / 100, HIGH / MED, Red flags / Omission / Hallucination).
     - Mục II: Điều khoản bị thiếu (TC05 - Chấm dứt & Hậu quả chấm dứt).
     - Mục III: Bẫy rủi ro pháp lý (các mục HIGH kèm Redline).
     - Mục IV: Rà soát điều khoản đã có (bảng 8 điều khoản kèm emoji 🔴/🟡/💡).
     - Mục V: Khung quyết định của người thẩm định (HITL approval check-box).

5. **Bước 5 (4') — Nghiệm thu với Giảng viên**:
   - Báo cáo kết quả workflow chạy 1-click thành công và xuất file Báo cáo Word hoàn chỉnh.

---

## 🔒 Nguyên tắc Safety & Control (Human-in-the-Loop)
> **CRITICAL**: AI & Python Workflow chỉ đóng vai trò trợ lý số bóc tách và đề xuất báo cáo. **Quyết định phê duyệt cuối cùng (Approval/Signature) luôn thuộc về Chuyên viên Pháp chế hoặc Quản lý cấp cao (HITL - Human-in-the-loop)** thông qua khung ký duyệt ở Mục V của Báo cáo.

---

## 🆘 Hướng dẫn khi bị kẹt (Stuck > 10')
- Mở file workflow giải pháp toàn diện: [checkpoints/n8n-contract-review-solution.json](./checkpoints/n8n-contract-review-solution.json).
