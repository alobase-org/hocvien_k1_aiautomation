# Hướng dẫn Thực hành 3 — Extract Clauses & Harness Schema Validation Gate (15')

> **Thuộc bài lab**: [Buổi 04: Thẩm định hợp đồng tự động](./lab.md)  
> **Tư duy trọng tâm**: **Harness Engineering (Schema Validation & Determinism)** — Bao bọc AI Node (Gemini 3.6 Flash) bằng Code Node kiểm thử JSON Schema (`templates/clause.schema.json`) để đảm bảo dữ liệu đầu ra luôn chuẩn định dạng cấu trúc, kết hợp vòng lặp Retry tất định loại bỏ sai lệch ngẫu nhiên.

---

## 🎯 Mục tiêu bài thực hành
- Vận hành AI Node `TH2 - AI Extract Clauses (Gemini + KB)` (model `gemini-3.6-flash`) để bóc tách danh sách các điều khoản từ văn bản hợp đồng đã redact.
- Vận hành Code Node `TH2 - Schema Validation (clause.schema.json)` đối chiếu dữ liệu JSON từ AI với các tiêu chuẩn trường bắt buộc top-level, metadata và clause details.
- Hiểu rõ cơ chế vòng lặp tự động (Loop Retry max 2 qua Node `TH2 - IF retry < 2`) khi AI trả ra JSON lỗi hoặc thiếu trường bắt buộc trước khi chuyển sang Node `TH2 - Set need_review`.
- Kiểm tra danh sách điều khoản `clauses` đạt chuẩn Schema validation.

---

## 📥 Input → ⚙️ Action → 📤 Output

- **Input**: Văn bản `contract_redacted` từ Thực hành 2 + JSON Schema `templates/clause.schema.json`.
- **Action**: 
  1. Node `TH2 - AI Extract Clauses (Gemini + KB)` gọi API Gemini 3.6 Flash (`generateContent` với `responseMimeType: "application/json"`) trích xuất danh sách điều khoản.
  2. Node `TH2 - Schema Validation (clause.schema.json)` kiểm tra:
     - Các trường top-level bắt buộc: `contract_id`, `metadata`, `clauses`, `confidence_score`, `need_review`.
     - Các trường metadata bắt buộc: `ben_a`, `ben_b`, `ngay_ky`, `loai_hop_dong`.
     - Các trường clause bắt buộc: `id`, `tieu_de`, `noi_dung`, `evidence.verbatim_quote`, `confidence_score`, `need_review`.
     - Tối thiểu 3 điều khoản (`clauses minItems 3`).
  3. Xử lý nhánh rẽ:
     - Nếu `_schema_ok == true` ➡️ Đi tiếp tới Thực hành 4 (`TH3 - Evidence + Omission`).
     - Nếu `_schema_ok == false` ➡️ Node `TH2 - Tang retry counter` ➡️ IF Gate `TH2 - IF retry < 2`: Nếu `retry < 2` thì gửi lại request sang AI Gemini; nếu đã lặp đủ 2 lần vẫn lỗi ➡️ Chuyển sang Node `TH2 - Set need_review (schema fail dai dang)` đặt `need_review = true`.
- **Output**: Mảng `clauses` chuẩn cấu trúc JSON Schema (mẫu hợp đồng bóc đủ 8 điều khoản HD01 - HD08).

---

## 🛠️ Công cụ & Tài nguyên
- **Tool chính**: n8n Nodes: `TH2 - AI Extract Clauses (Gemini + KB)`, `TH2 - Schema Validation (clause.schema.json)`, `TH2 - IF Schema Gate`, `TH2 - IF retry < 2`.
- **Model AI**: Gemini 3.6 Flash (`gemini-3.6-flash`).
- **JSON Schema chuẩn**: `templates/clause.schema.json`.
- **Jupyter Demo Notebook**: Step 4 trong [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb).

---

## 📊 Tiêu chuẩn Nghiệm thu (SLI/SLO)
- [ ] Schema Validation **PASS** bằng Code Node tất định (không phụ thuộc phán đoán cảm tính của AI).
- [ ] Trích xuất đủ các điều khoản trong hợp đồng mẫu (8 điều khoản HD01 - HD08) + Metadata hợp đồng (`ben_a`, `ben_b`, `ngay_ky`, `loai_hop_dong`).
- [ ] Mỗi điều khoản chứa đủ các trường: `id`, `tieu_de`, `noi_dung`, `evidence.verbatim_quote`, `severity`, `confidence_score`, `need_review`, `de_xuat`.
- [ ] Cơ chế lặp Retry tự động kích hoạt tối đa 2 lần khi phát hiện lỗi Schema.

---

## ⏱️ Các bước thực hiện (Time-box 15')

1. **Bước 1 (3') — Khám phá AI Extract Node & Prompt Gemini**:
   - Mở n8n Canvas UI, kiểm tra node **"TH2 - AI Extract Clauses (Gemini + KB)"**.
   - Xem cấu hình API Key, URL `gemini-3.6-flash:generateContent` và System Prompt yêu cầu AI trả ra JSON đúng cấu trúc.

2. **Bước 2 (4') — Khám phá Code Node Schema Validation**:
   - Kiểm tra node **"TH2 - Schema Validation (clause.schema.json)"**.
   - Quan sát danh sách các hằng số kiểm tra `REQUIRED_TOP`, `REQUIRED_META`, `REQUIRED_CLAUSE`, `REQUIRED_EVIDENCE`.

3. **Bước 3 (5') — Trải nghiệm qua Jupyter Notebook Step 4**:
   - Mở notebook [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb).
   - Chạy **Step 4: Vận hành AI Extract & Harness Schema Validation Gate trên n8n**.
   - Xem kết quả inspect node Schema Validation trực tiếp qua API n8n.

4. **Bước 4 (3') — Đánh giá Cấu trúc Output**:
   - Kiểm tra mảng `clauses` nhận được có chứa đủ 8 điều khoản HD01-HD08 và field `verbatim_quote` chính xác không.
   - Sẵn sàng chuyển dữ liệu sang bài **Thực hành 4**.

---

## 🔒 Nguyên tắc Safety & Control
> **Determinism First**: Khung kiểm thử Schema đóng vai trò là "chân phanh tất định". Mọi kết quả không đạt chuẩn cấu trúc sẽ bị chặn ngay lập tức, tự động lặp lại (Retry) tối đa 2 lần, tuyệt đối không cho phép dữ liệu lỗi đi tiếp vào hệ thống.

---

## 🆘 Hướng dẫn khi bị kẹt (Stuck > 8')
- Xem cấu hình chi tiết các node TH2 trong file workflow giải pháp: [checkpoints/n8n-contract-review-solution.json](./checkpoints/n8n-contract-review-solution.json).
