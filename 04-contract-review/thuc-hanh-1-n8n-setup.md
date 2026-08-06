# Hướng dẫn Thực hành 1 — Tự động Cấu hình n8n (npx) & Vận hành Jupyter Demo Notebook & Web App (15')

> **Thuộc bài lab**: [Buổi 04: Thẩm định hợp đồng tự động](./lab.md)  
> **Tư duy trọng tâm**: **Auto-Config & Instant Demo (Tự động cấu hình & Vận hành trực quan)** — Triển khai n8n local bằng `python3 auto_import_n8n.py` với tính năng tự động nạp Workflow solution v4 1-click, kết hợp vận hành Jupyter Notebook demo từng bước và ứng dụng ReactJS Web App cho học viên mà không mất thời gian cài đặt từng node thủ công.

---

## 🎯 Mục tiêu bài thực hành
- Học viên & Giảng viên khởi chạy thành công n8n local qua **npx n8n Compose / Python Script** với workflow giải pháp `checkpoints/n8n-contract-review-solution.json` được nạp sẵn tự động.
- Mở và chạy tương tác trực tiếp file Jupyter Notebook [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb) (Step 0 & Step 1) để kiểm tra kết nối n8n REST API và khởi chạy giao diện Web App Legal AI Guard (`http://localhost:5173`).
- Chạy tự động bộ Unit & E2E Test (`test/run_e2e_tests.py`) đạt kết quả **PASSED 8/8 test cases**.

---

## 📥 Input → ⚙️ Action → 📤 Output

- **Input**: Thư mục [test/](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test) chứa `interactive_e2e_runner.py`, `auto_import_n8n.py`, `04_contract_review_lab_demo.ipynb`, `run_e2e_tests.py` và thư mục Web App `app/`.
- **Action**: 
  1. Khởi chạy dịch vụ n8n local và nạp tự động solution workflow: `python3 test/auto_import_n8n.py` (hoặc `npx n8n start`).
  2. Mở Jupyter Notebook `test/04_contract_review_lab_demo.ipynb` trên VS Code hoặc Jupyter Lab.
  3. Thực thi Cell **Step 0** (Kiểm tra & tự động nạp n8n workflow, đăng nhập REST API với `admin@alobase.vn` / `Password123!`) và **Step 1** (Khởi chạy ứng dụng Web App ReactJS `app/` tại `http://localhost:5173`).
- **Output**: 
  - n8n service sẵn sàng tại `http://localhost:5678` chứa sẵn workflow **B4 K1 - Contract Review Agent (Webhook text + Report DOCX) - v4**.
  - Giao diện Web App ReactJS (Legal AI Guard) sẵn sàng tại `http://localhost:5173`.
  - Kết quả Unit Test & E2E Runner trả về **PASSED 8/8 test cases**.

---

## 🛠️ Công cụ & Tài nguyên
- **Tool chính**: npx n8n Engine / Node.js + Python 3 + ReactJS Web App (`app/`).
- **File cấu hình mẫu**: `test/interactive_e2e_runner.py`, `test/auto_import_n8n.py`.
- **Tự động Import & Auto-Config**: `python3 test/auto_import_n8n.py`.
- **Interactive Jupyter Notebook**: [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb).
- **Test Runner & Test Suite**: `test/run_e2e_tests.py`, `test/test_n8n_workflows.py`.

---

## 📊 Tiêu chuẩn Nghiệm thu (SLI/SLO)
- [ ] Dịch vụ n8n khởi chạy thành công tại `http://localhost:5678` và tự động import workflow `n8n-contract-review-solution.json`.
- [ ] Mở Jupyter Notebook [`04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb) và chạy Cell Step 0 (Đăng nhập API) & Step 1 (ReactJS Web App) thành công.
- [ ] Báo cáo E2E Test Suite (`python3 run_e2e_tests.py`) trả về kết quả **PASSED 100%** (8/8 test cases).

---

## ⏱️ Các bước thực hiện (Time-box 15')

1. **Bước 1 (3') — Khởi chạy n8n & Import Solution Workflow**:
   - Mở Terminal, di chuyển vào thư mục `test` và chạy script auto-import:
     ```bash
     cd test
     python3 auto_import_n8n.py
     ```
   - *Thông tin đăng nhập n8n*:
     - **Email**: `admin@alobase.vn`
     - **Password**: `Password123!`

2. **Bước 2 (5') — Mở & Trải nghiệm Jupyter Demo Notebook (Step 0 & Step 1)**:
   - Mở file [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb) trong VS Code.
   - Chạy **Cell Step 0** để xác minh kết nối n8n REST API và nhận link Canvas UI workflow.
   - Chạy **Cell Step 1** để kiểm tra/bật ứng dụng ReactJS Web App tại `http://localhost:5173`.

3. **Bước 3 (5') — Chạy bộ kiểm thử tự động E2E Test Suite**:
   - Chạy trực tiếp file `run_e2e_tests.py`:
     ```bash
     python3 run_e2e_tests.py
     ```
   - Kiểm tra kết quả 8 bài test xanh toàn bộ (PASSED 8/8).

4. **Bước 4 (2') — Đánh giá & Chuyển bước**:
   - Đảm bảo n8n sẵn sàng tại `http://localhost:5678` và Web App tại `http://localhost:5173`. Sẵn sàng sang **Thực hành 2** (Redaction 4 Cấp).

---

## 🔒 Nguyên tắc Safety & Control
> **Auto-Config First**: Việc tự động cấu hình workflow qua script `auto_import_n8n.py` và Jupyter Notebook giúp giảng viên & học viên loại bỏ hoàn toàn các lỗi thao tác thủ công, tập trung tối đa vào việc làm chủ tư duy Harness Engineering, Bảo mật dữ liệu Redaction và Kiểm soát AI tất định.

---

## 🆘 Hướng dẫn khi bị kẹt (Stuck > 8')
- Mở file giải pháp workflow: [checkpoints/n8n-contract-review-solution.json](./checkpoints/n8n-contract-review-solution.json).
