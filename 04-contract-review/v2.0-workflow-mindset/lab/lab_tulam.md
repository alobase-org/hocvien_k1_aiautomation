# 🧑‍💻 Lab Tự Làm — Workflow Mindset: Thiết kế quy trình đáng tin cậy trước khi tự động hóa

> **Hướng dẫn dành cho Học viên tự thực hành.**
> Bạn sẽ áp dụng toàn bộ 6 bước Workflow Mindset cho **quy trình riêng của bạn** (hoặc của doanh nghiệp bạn).
> Output Bước N = Input Bước N+1. Cuối cùng bạn sẽ có 1 Workflow Design Doc hoàn chỉnh + deck tham mưu lãnh đạo 30 ngày.

---

## 📌 Hướng dẫn chung

### Cách thức làm bài
- **Bước 1:** Copy các file template trong folder `templates/` về chỉnh sửa theo use-case riêng của bạn.
- **Bước 2:** Sử dụng các prompt có sẵn trong folder `prompts/` để chạy với AI (Antigravity, Claude, Gemini, ChatGPT...).
- **Bước 3:** Lưu **tất cả** kết quả đầu ra vào folder `output_tulam/`.
- **Bước 4:** Cuối cùng, nộp bài theo hướng dẫn ở cuối tài liệu này.

### Cấu trúc thư mục

```
lab/
├── templates/          ← Copy template ra chỉnh sửa, điền thông tin use-case của bạn
│   ├── 01-impact-difficulty-matrix-template.md
│   ├── 01b-usecase-design-template.md
│   ├── 02a-as-is-table-template.md
│   ├── 02b-workflow-design-doc-template.md
│   ├── 03-production-hardening-template.md
│   ├── 04-mermaid-diagram-template.mmd
│   ├── 05-workflow-image-prompt-template.md
│   ├── 06-leadership-deck-template.md
│   └── 07-reference-map-template.md
├── prompts/            ← Dùng prompt có sẵn để chạy AI
│   ├── 01-usecase-impact-matrix.md
│   ├── 01b-usecase-design.md
│   ├── 02-workflow-design-esia.md
│   ├── 03-production-hardening.md
│   ├── 04-mermaid-diagram.md
│   ├── 05-generate-workflow-image.md
│   └── 06-notebooklm-leadership-deck.md
├── output_tulam/       ← Lưu TẤT CẢ kết quả của bạn vào đây
│   ├── notebooklm_input/
│   └── reference/
└── output/             ← (Tham khảo) Kết quả mẫu của giáo viên
```

### 💡 Mẹo
- Xem kết quả mẫu trong folder `output/` để hiểu format đầu ra mong muốn.
- Mỗi bước đều có template tương ứng — hãy copy template và **điền thông tin riêng** trước khi chạy prompt.
- Trong prompt, thay thế nội dung trong ngoặc vuông `[...]` bằng dữ liệu thực tế của bạn.

---

## Bước 0 · Setup môi trường — Antigravity & Extensions (3 phút)

- **🎯 Mục tiêu:** Chuẩn bị và cài đặt các công cụ, extension bổ trợ trên Antigravity IDE.
- **💡 Vì sao làm bước này:** Sử dụng Antigravity IDE làm môi trường pair-programming với AI.

### Bước thực hành
1. Khởi động **Antigravity IDE** và mở thư mục chứa mã nguồn lab (`v2.0-workflow-mindset`).
2. Truy cập Extensions Marketplace, tìm và cài đặt:
   - **Office Viewer** (mở file `.docx`, `.pptx` trực tiếp).
   - **Mermaid Preview** / **Mermaid Chart** (hiển thị sơ đồ `.mmd`).
3. Kiểm tra: Mở file [04-mermaid-diagram-template.mmd](templates/04-mermaid-diagram-template.mmd) → click **Preview** để xem sơ đồ.

**🎯 Deliverable:** Môi trường Antigravity sẵn sàng.

---

## Bước 1 · Usecase design — Ma trận ưu tiên & Chi tiết Usecase (10 phút)

- **🎯 Mục tiêu:** Chọn use-case ưu tiên của **doanh nghiệp bạn** và thiết kế chi tiết.
- **💡 Vì sao làm bước này:** Tránh lãng phí nguồn lực vào quy trình phức tạp nhưng giá trị thấp.

### Bước thực hành

#### 1a. Ma trận ưu tiên
1. **Liệt kê vấn đề:** Tự list 5-10 vấn đề/quy trình thủ công **tại doanh nghiệp bạn** cần cải thiện.
2. **Copy template:** Mở file [01-impact-difficulty-matrix-template.md](templates/01-impact-difficulty-matrix-template.md), copy nội dung và điền thông tin các vấn đề của bạn.
3. **Chạy prompt:** Mở file [prompts/01-usecase-impact-matrix.md](prompts/01-usecase-impact-matrix.md), thay `[LIST VẤN ĐỀ]` bằng danh sách vấn đề bạn vừa liệt kê, dán vào AI.
4. **Lưu kết quả:** Lưu output vào file `output_tulam/01-usecase-impact-matrix.md`.

#### 1b. Thiết kế chi tiết Use-case
5. **Copy template:** Mở file [01b-usecase-design-template.md](templates/01b-usecase-design-template.md), copy và điền thông tin use-case bạn chọn.
6. **Chạy prompt:** Mở file [prompts/01b-usecase-design.md](prompts/01b-usecase-design.md), thay phần `[THÔNG TIN ĐẦU VÀO]` bằng use-case bạn chọn, dán vào AI.
7. **Lưu kết quả:** Lưu output vào file `output_tulam/01b-usecase-design.md`.

**🎯 Deliverable:**
- File `output_tulam/01-usecase-impact-matrix.md` — Ma trận 4 góc + top-3 use-case.
- File `output_tulam/01b-usecase-design.md` — Thiết kế chi tiết use-case.

**📊 SLI/SLO:**
- Ma trận có đủ 4 góc, top-3 use-case ghi rõ lý do.
- File usecase-design có đầy đủ 6 mục (mô tả, input/output, value, risk, HITL, ràng buộc).

**📸 Tham khảo kết quả mẫu:** [output/01-usecase-impact-matrix.md](output/01-usecase-impact-matrix.md), [output/01b-usecase-design.md](output/01b-usecase-design.md)

---

## Bước 2 · Workflow design — As-is → ESIA to-be (10 phút)

- **🎯 Mục tiêu:** Phân tích quy trình hiện tại (As-is) và thiết kế quy trình mới (To-be) theo khung ESIA cho **use-case của bạn**.
- **💡 Vì sao làm bước này:** Tự động hóa một quy trình tồi = quy trình tồi chạy nhanh hơn. Phải thiết kế lại trước!

### Bước thực hành

#### 2a. Mô tả quy trình hiện tại (As-is)
1. **Copy template:** Mở file [02a-as-is-table-template.md](templates/02a-as-is-table-template.md), copy và **tự điền** hiện trạng quy trình hiện tại của doanh nghiệp bạn (≥5 bước).
2. **Chạy prompt:** Mở file [prompts/02-workflow-design-esia.md](prompts/02-workflow-design-esia.md), đưa nội dung file `output_tulam/01b-usecase-design.md` làm input, dán vào AI.
3. **Lưu kết quả:** Lưu bảng As-is vào file `output_tulam/02a-workflow-as-is.md`.
4. **⚠️ [HITL — Quan trọng!]** Đọc và **chỉnh sửa thủ công** file `output_tulam/02a-workflow-as-is.md` để đảm bảo phản ánh đúng thực tế doanh nghiệp bạn.

#### 2b. Thiết kế quy trình mới (To-be ESIA)
5. **Copy template:** Mở file [02b-workflow-design-doc-template.md](templates/02b-workflow-design-doc-template.md), tham khảo cấu trúc.
6. Từ As-is đã review, tiếp tục chạy prompt để AI áp dụng ESIA → đề xuất To-be.
7. **Lưu kết quả:** Lưu vào file `output_tulam/02b-workflow-design-esia.md`.
8. Rà soát: bước nào AI đề xuất Automate nhưng rủi ro cao → cần bổ sung HITL.

**🎯 Deliverable:**
- File `output_tulam/02a-workflow-as-is.md` — Hiện trạng quy trình (đã review bởi con người).
- File `output_tulam/02b-workflow-design-esia.md` — Quy trình To-be ESIA.

**📊 SLI/SLO:** As-is ≥5 bước · mỗi bước to-be có 1 ký hiệu E/S/I/A · ≥1 bước A ghi nhánh automation.

**📸 Tham khảo kết quả mẫu:** [output/02a-workflow-as-is.md](output/02a-workflow-as-is.md), [output/02b-workflow-design-esia.md](output/02b-workflow-design-esia.md)

---

## Bước 3 · Kiến trúc Hybrid & Hardening (10 phút)

- **🎯 Mục tiêu:** Phân rã quy trình To-be thành kiến trúc 3 trụ cột (n8n + AI Agent + Vibe-coded App) và bổ sung 4 lớp Hardening.
- **💡 Vì sao làm bước này:** Hệ thống hiện đại không để 1 thành phần làm tất cả. Cần phân rã trách nhiệm + phòng thủ sâu.

### Bước thực hành
1. **Copy template:** Mở file [03-production-hardening-template.md](templates/03-production-hardening-template.md), copy và điền thông tin quy trình của bạn.
2. **Chạy prompt:** Mở file [prompts/03-production-hardening.md](prompts/03-production-hardening.md), đưa nội dung file `output_tulam/02b-workflow-design-esia.md` làm input, dán vào AI.
3. **Lưu kết quả:** Lưu vào file `output_tulam/03-production-hardening.md`.
4. Rà soát sự phân chia trách nhiệm giữa n8n, AI Agent và Vibe-coded App. Kiểm tra 4 lớp Hardening (Fallback, Log, Edge case, HITL).

**🎯 Deliverable:** File `output_tulam/03-production-hardening.md` — Kiến trúc hybrid + 4 lớp hardening.

**📸 Tham khảo kết quả mẫu:** [output/03-production-hardening.md](output/03-production-hardening.md)

---

## Bước 4 · Vẽ quy trình — Mermaid diagram (8 phút)

- **🎯 Mục tiêu:** Trực quan hóa quy trình To-be bằng sơ đồ Mermaid.
- **💡 Vì sao làm bước này:** Sơ đồ trực quan giúp dev hiểu cách code, giúp stakeholder nắm được luồng vận hành.

### Bước thực hành
1. **Copy template:** Mở file [04-mermaid-diagram-template.mmd](templates/04-mermaid-diagram-template.mmd), tham khảo cấu trúc sơ đồ mẫu.
2. **Chạy prompt:** Mở file [prompts/04-mermaid-diagram.md](prompts/04-mermaid-diagram.md), đưa nội dung file `output_tulam/02b-workflow-design-esia.md` và `output_tulam/03-production-hardening.md` làm input, dán vào AI.
3. **Lưu kết quả:** Lưu mã Mermaid vào file `output_tulam/04-mermaid-diagram.mmd`.
4. **Kiểm tra:** Mở file `.mmd` trên IDE (dùng Mermaid Preview) hoặc paste lên [mermaid.live](https://mermaid.live) để xem render. Chỉnh sửa nếu lỗi.

**🎯 Deliverable:** File `output_tulam/04-mermaid-diagram.mmd` — Sơ đồ quy trình Mermaid.

**📸 Tham khảo kết quả mẫu:** [output/04-mermaid-diagram.mmd](output/04-mermaid-diagram.mmd)

---

## Bước 5 · Generate ảnh workflow — Prompt infographic (8 phút)

- **🎯 Mục tiêu:** Tạo ảnh infographic quy trình bằng AI, dùng tiếng Việt.
- **💡 Vì sao làm bước này:** Sơ đồ kỹ thuật Mermaid khó hiểu với bộ phận kinh doanh/quản lý. Ảnh đồ họa dễ truyền thông hơn.

### Bước thực hành
1. **Copy template:** Mở file [05-workflow-image-prompt-template.md](templates/05-workflow-image-prompt-template.md), chọn phương án phù hợp (Before-After / Storytelling / System Architecture), thay nội dung `[...]` bằng thông tin use-case của bạn.
2. **Chạy prompt:** Mở file [prompts/05-generate-workflow-image.md](prompts/05-generate-workflow-image.md), tham khảo và tùy chỉnh cho use-case của bạn bằng tiếng Việt.
3. **Sinh ảnh:** Dán prompt vào công cụ sinh ảnh AI (Antigravity, Imagen, Midjourney...).
4. **Lưu kết quả:**
   - Lưu prompt đã chỉnh vào file `output_tulam/05-workflow-image-prompt.md`.
   - Lưu 3 ảnh: `output_tulam/05-workflow-before-after.png`, `output_tulam/05-workflow-storytelling.png`, `output_tulam/05-workflow-system-architecture.png`.
   - Chọn 1 ảnh chính lưu thành `output_tulam/05-workflow-infographic.png`.

**🎯 Deliverable:**
- File `output_tulam/05-workflow-image-prompt.md` — Prompt sinh ảnh.
- 3 ảnh workflow + 1 ảnh infographic chính trong folder `output_tulam/`.

**📸 Tham khảo kết quả mẫu:** Xem folder `output/` (các file `05-*.png`).

---

## Bước 6 · NotebookLM deck — Tham mưu lãnh đạo 30 ngày (10 phút)

- **🎯 Mục tiêu:** Tạo slide deck đề xuất triển khai AI Automation trong 30 ngày, bao gồm đề xuất cử nhân sự đi học khóa AI Automation K1 (Alobase, khai giảng 16/07/2026).
- **💡 Vì sao làm bước này:** Kế hoạch hay cần lãnh đạo phê duyệt. NotebookLM tổng hợp nhanh tài liệu thành slide thuyết phục.

### Bước thực hành
1. **Copy template:** Mở file [06-leadership-deck-template.md](templates/06-leadership-deck-template.md), copy và điền thông tin doanh nghiệp bạn.
2. **Convert PDF:** Chuyển các file markdown từ Bước 1-3 (`output_tulam/01b-usecase-design.md`, `output_tulam/02a-workflow-as-is.md`, `output_tulam/02b-workflow-design-esia.md`, `output_tulam/03-production-hardening.md`) sang PDF, lưu vào `output_tulam/notebooklm_input/`.
3. **Tạo notebook:** Truy cập [NotebookLM](https://notebooklm.google.com), tạo notebook mới, thêm các file PDF từ bước trên.
4. **Chạy prompt:** Mở file [prompts/06-notebooklm-leadership-deck.md](prompts/06-notebooklm-leadership-deck.md), dán prompt CRAFT vào NotebookLM → generate deck.
5. **Lưu kết quả:** Xem deck, chỉnh tiêu đề + số liệu, lưu vào `output_tulam/06-leadership-deck.md`.

**🎯 Deliverable:**
- Thư mục `output_tulam/notebooklm_input/` chứa các file PDF nguồn.
- File `output_tulam/06-leadership-deck.md` — Deck tham mưu lãnh đạo.

**📸 Tham khảo kết quả mẫu:** [output/06-leadership-deck.md](output/06-leadership-deck.md)

---

## 🔁 Workflow mở rộng — Tìm kiếm tài liệu tham khảo (tự thực hành thêm)

> Cùng tư duy Workflow Mindset, áp dụng cho "tìm tài liệu khi bắt đầu 1 việc mới".

**Deliverable:** folder `output_tulam/reference/` + file `output_tulam/reference_map.md`.
**Template:** [07-reference-map-template.md](templates/07-reference-map-template.md)

**Workflow:**
```
Input: nội dung đang cần làm (vd: "soạn đề xuất đào tạo AI cho bệnh viện")
  → [AI] extract keyword tìm kiếm
  → [AI] search các folder/Drive → danh sách candidate
  → [AI] rerank → top candidate
  → [AI] đọc sâu top candidate → extract điểm hữu ích → ghi vào reference_map.md
  → [AI Agent] copy file top candidate vào folder reference/
Output: folder output_tulam/reference/ + output_tulam/reference_map.md
```

---

## 📝 Checklist tự kiểm tra trước khi nộp bài

Trước khi nộp, hãy tự kiểm tra:

- [ ] **Bước 1:** Có file `output_tulam/01-usecase-impact-matrix.md` (ma trận 4 góc, top-3 use-case)
- [ ] **Bước 1b:** Có file `output_tulam/01b-usecase-design.md` (thiết kế chi tiết use-case)
- [ ] **Bước 2a:** Có file `output_tulam/02a-workflow-as-is.md` (hiện trạng, ≥5 bước, đã review thủ công)
- [ ] **Bước 2b:** Có file `output_tulam/02b-workflow-design-esia.md` (to-be ESIA)
- [ ] **Bước 3:** Có file `output_tulam/03-production-hardening.md` (kiến trúc hybrid + hardening)
- [ ] **Bước 4:** Có file `output_tulam/04-mermaid-diagram.mmd` (sơ đồ Mermaid render được)
- [ ] **Bước 5:** Có ≥1 ảnh workflow + file prompt trong `output_tulam/`
- [ ] **Bước 6:** Có file `output_tulam/06-leadership-deck.md` (deck tham mưu lãnh đạo)
- [ ] **Use-case riêng:** Nội dung là **use-case của bạn**, KHÔNG phải copy y nguyên kết quả mẫu

---

## Câu hỏi phản tư

1. Use-case bạn chọn có thực sự là quick win (giá trị cao + dễ) không?
2. Bước nào trong to-be bạn đã đánh Automate nhưng thực ra rủi ro cao → cần HITL?
3. Nếu workflow này chạy production 1 tháng, lớp hardening nào bạn lo nhất?

---

## 📮 Hướng dẫn nộp bài để nhận chấm test

### Bước 1: Zip folder lại
Nén toàn bộ folder `output_tulam/` thành 1 file `.zip`:
- **macOS:** Click phải vào folder `output_tulam` → chọn **"Compress"** (Nén).
- **Windows:** Click phải vào folder `output_tulam` → chọn **"Send to" → "Compressed (zipped) folder"**.
- **Hoặc dùng Terminal:**
  ```bash
  cd lab/
  zip -r output_tulam.zip output_tulam/
  ```

### Bước 2: Upload lên Google Drive
1. Truy cập [Google Drive](https://drive.google.com).
2. Upload file `output_tulam.zip` lên Drive.
3. **⚠️ Quan trọng: Đặt chế độ Share Public:**
   - Click phải vào file → **"Share"** → **"Get link"**.
   - Chuyển từ "Restricted" sang **"Anyone with the link"** (Bất kỳ ai có liên kết).
   - Quyền: **Viewer** (Người xem).
   - Copy link chia sẻ.

### Bước 3: Nộp bài theo form
Truy cập link form bên dưới, điền thông tin và dán link Google Drive:

> 🔗 **[Form Nộp Bài Test](https://forms.gle/cFR5GVeJ7bcRA1ur5)**

---

> ✅ **Sau khi nộp bài**, giáo viên sẽ chấm và phản hồi kết quả test. Chúc bạn thực hành tốt! 🚀
