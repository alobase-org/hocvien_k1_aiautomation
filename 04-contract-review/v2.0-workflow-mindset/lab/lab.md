# Lab — Workflow Mindset: Thiết kế quy trình đáng tin cậy trước khi tự động hóa

> 6 bài tập móc nối. Output bài N = input bài N+1. HV build dần 1 Workflow Design Doc hoàn chỉnh + deck tham mưu lãnh đạo 30 ngày.
> Thời lượng demo: 30 phút (GV demo). 15 phút cuối HV tự chạy 1 bài.

## Mục tiêu lab
- Chọn use-case tối ưu theo ma trận Hiệu quả × Độ phức tạp.
- Thiết kế workflow mới theo ESIA, phân nhánh 3 giải pháp automation.
- Harden workflow cho production (fallback/log/edge/HITL).
- Mô tả workflow bằng Mermaid + render ảnh infographic.
- Dựng deck tham mưu lãnh đạo 30 ngày bằng NotebookLM.

## Bối cảnh role-play
Bạn là quản lý/chiến lược gia. Folder "Tài liệu" của bạn thành bãi rác: ~1.200 file, tên tùy tiện (Document(1).pdf, baocao_final_final.docx), nhiều version lộn xộn, file nằm sai chỗ, tìm 1 tài liệu mất nửa tiếng. Use-case chính xuyên suốt lab: **tự động tổ chức tài liệu + tìm kiếm tài liệu tham khảo**.

> File dữ liệu: `synthetic-data/company-dong-duong-thuongmai.md` (folder lộn xộn mẫu + 10 vấn đề).
> Workflow được giữ **đơn giản (dumb)**: AI Agent chạy các script Python có sẵn để copy/đổi tên file, không cần hệ thống phức tạp.

---

## BT1 · Usecase design — Ma trận ưu tiên (5 phút)

**🎯 Deliverable:** 1 ma trận Hiệu quả × Độ phức tạp + top-3 use-case nên automate trước.
**📊 SLI/SLO:** Ma trận có đủ 4 góc · top-3 use-case ghi rõ lý do.

**Prompt:** `prompts/01-usecase-impact-matrix.md`

### Bước thực hành
1. **(1')** Mở `synthetic-data/company-dong-duong-thuongmai.md`, copy list 10 vấn đề (hoặc tự list vấn đề phòng bạn).
2. **(2')** Mở Claude/Gemini, dán prompt `01-usecase-impact-matrix.md`, thay `[LIST VẤN ĐỀ]`.
3. **(2')** Xem ma trận AI đề xuất. Điều chỉnh nếu AI chấm sai use-case bạn rành.

**Đầu ra:** Ma trận 4 góc + top-3 use-case. → Input BT2.

**📥 Checkpoint cứu hộ:** `checkpoints/checkpoint-bt1.md`
**📸 Expected result:** Ma trận 2×2 + bảng top-3 (xem `fallback-inputs/sample-problems-list.md`)

---

## BT2 · Workflow design — As-is → ESIA to-be (6 phút)

**🎯 Deliverable:** Workflow Design Doc (as-is 5 cột + to-be ESIA + cột AI/người + nhánh automation).
**📊 SLI/SLO:** as-is ≥5 bước · mỗi bước to-be có 1 ký hiệu E/S/I/A · ≥1 bước A ghi nhánh automation.
**🧩 Use-case demo:** Tự động tổ chức tài liệu (folder lộn xộn → folder đúng chuẩn).

**Prompt:** `prompts/02-workflow-design-esia.md`

### Bước thực hành
1. **(1')** Lấy top-1 use-case từ BT1 = "tổ chức tài liệu" (dùng tiếp cùng đoạn chat).
2. **(3')** Dán prompt `02-workflow-design-esia.md`. AI mô tả as-is (đang sắp tài liệu tay) → áp ESIA → đề xuất to-be (AI Agent chuẩn hóa tên + plan + user review + script copy file).
3. **(2')** Rà soát: bước xóa file / move file rủi ro → bắt buộc HITL (user review plan trước khi AI thực thi). Ghi nhánh automation.

**Đầu ra:** Design Doc as-is + to-be. → Input BT3.

**📥 Checkpoint cứu hộ:** `checkpoints/checkpoint-bt2.md`
**📸 Expected result:** `fallback-inputs/sample-esia-tobe.md`

> **Workflow tổ chức tài liệu (đơn giản):**
> ```
> Input: folder lộn xộn
>   → [AI] chuẩn hóa tên (name - type - version - date) + phân tích loại
>   → [AI] tham chiếu policy (cấu trúc folder + cách đặt tên) → build plan
>   → [USER] review plan (HITL — quyết định trước khi move)
>   → [AI Agent] chạy script copy file đúng vị trí / đẩy Drive
> Output: folder đã tổ chức đúng chỗ
> ```
>
> **3 nhánh automation:**
> - **Workflow automation (n8n):** bước có quy tắc rõ, kết nối hệ thống (email, Sheet, API).
> - **Agentic workflow (AI Agent — Claude Code/Codex/Antigravity/OpenClaw/Hermes):** bước cần suy luận, đọc file, quyết định phi cấu trúc. ← **dùng cho tổ chức tài liệu**
> - **App vibe coding:** bước cần giao diện nội bộ cho đội.

---

## BT3 · Improve cho production — Hardening (5 phút)

**🎯 Deliverable:** Design doc phần hardening (4 lớp: fallback/log/edge/HITL).
**📊 SLI/SLO:** 4 lớp đều có · mỗi bước A ghi rõ lớp nào áp dụng.

**Prompt:** `prompts/03-production-hardening.md`

### Bước thực hành
1. **(1')** Lấy to-be từ BT2.
2. **(3')** Dán prompt `03-production-hardening.md`. AI bổ sung 4 lớp hardening.
3. **(1')** Rà soát: bước nào tiền bạc/PII → bắt buộc HITL.

**Đầu ra:** Design doc phần hardening. → Input BT4.

**📥 Checkpoint cứu hộ:** `checkpoints/checkpoint-bt3.md`

> **4 lớp hardening:**
> - **Fallback branch:** input kém chất lượng / AI lỗi → nhánh xử lý thủ công hoặc cảnh báo.
> - **Execution log:** log mọi hành vi (thời gian, input hash, trạng thái, output) để audit.
> - **Edge case:** trường hợp đặc biệt (input rỗng, format sai, ngoài giờ).
> - **Human-in-the-loop:** bước cần con người review trước khi đi tiếp.

---

## BT4 · Vẽ quy trình — Mermaid activity/sequence (5 phút)

**🎯 Deliverable:** 1 Mermaid diagram đã render trên mermaid.live.
**📊 SLI/SLO:** Mermaid hợp lệ · node AI xanh · ≥1 node HITL đỏ · ≤8 node.

**Prompt:** `prompts/04-mermaid-diagram.md`

### Bước thực hành
1. **(1')** Lấy to-be + hardening từ BT2, BT3.
2. **(2')** Dán prompt `04-mermaid-diagram.md` vào AI → nhận mã Mermaid.
3. **(2')** Mở `mermaid.live`, paste mã → xem render. Chỉnh nếu lỗi.

**Đầu ra:** 1 Mermaid render. → Input BT5.

**📥 Checkpoint cứu hộ:** `checkpoints/checkpoint-bt4.md`
**📸 Expected result:** `fallback-inputs/sample-mermaid.mmd`

---

## BT5 · Generate ảnh workflow — Prompt infographic (4 phút)

**🎯 Deliverable:** 1 prompt render ảnh + 1 ảnh workflow infographic.
**📊 SLI/SLO:** Prompt có style spec + Mermaid source · ảnh label tiếng Việt chính xác.

**Prompt:** `prompts/05-generate-workflow-image.md`

### Bước thực hành
1. **(1')** Lấy Mermaid từ BT4.
2. **(2')** Dán prompt `05-generate-workflow-image.md` vào Codex/Nano Banana/Gemini.
3. **(1')** Xem ảnh. Chỉnh prompt nếu chữ lỗi/font sai.

**Đầu ra:** 1 ảnh workflow. → Input BT6.

**📥 Checkpoint cứu hộ:** `checkpoints/checkpoint-bt5.md`

---

## BT6 · NotebookLM deck — Tham mưu lãnh đạo 30 ngày (5 phút)

**🎯 Deliverable:** 1 prompt NotebookLM + 1 deck slide tham mưu lãnh đạo.
**📊 SLI/SLO:** Prompt đủ CRAFT 5 phần · deck có mục tiêu + lộ trình 30 ngày + lợi ích đo được.

**Prompt:** `prompts/06-notebooklm-leadership-deck.md`

### Bước thực hành
1. **(1')** Tạo notebook NotebookLM mới. Add source: design doc (BT2-BT3) + Mermaid (BT4).
2. **(3')** Dán prompt `06-notebooklm-leadership-deck.md` (CRAFT) → generate deck.
3. **(1')** Xem deck. Chỉnh tiêu đề + số liệu lợi ích.

**Đầu ra:** 1 deck tham mưu lãnh đạo. **Final output của chuỗi 6 bài.**

**📥 Checkpoint cứu hộ:** `checkpoints/checkpoint-bt6.md`

---

## 🔁 Workflow mở rộng — Tìm kiếm tài liệu tham khảo (tự thực hành)

> Cùng tư duy Workflow Mindset, áp dụng cho "tìm tài liệu khi bắt đầu 1 việc mới". Dùng sau webinar hoặc cho HV xong nhanh.

**🎯 Deliverable:** folder `reference/` + file `reference_map.md`.

**Workflow (đơn giản):**
```
Input: nội dung đang cần làm (vd: "soạn đề xuất đào tạo AI cho bệnh viện")
  → [AI] extract keyword tìm kiếm ("AI đào tạo", "bệnh viện", "y tế", "đề xuất training"...)
  → [AI] search các folder/Drive → danh sách candidate
  → [AI] rerank mức liên quan/hữu ích → top candidate
  → [AI] đọc sâu top candidate → extract điểm hữu ích → ghi vào reference_map.md
  → [AI Agent] copy file top candidate vào folder reference/
Output: folder reference/ + reference_map.md (bảng File | Vị trí | Điểm hữu ích | Trích đoạn liên quan)
```

**Template reference_map.md:** `templates/reference-map-template.md`

> So sánh 2 workflow: **Tổ chức** = sắp xếp input lộn xộn về đúng chỗ (1 lần / định kỳ). **Tìm kiếm** = lấy ra đúng tài liệu cần khi bắt đầu việc mới (mỗi dự án). Cả hai đều cần AI Agent đọc nội dung + HITL khi cần.


---

## Tiêu chí đánh giá (nộp bài)
Xem `../nop-bai/form-nop-bai-webinar3-v2.md` (5 tiêu chí, level 1-5).

## Câu hỏi phản tư
1. Use-case bạn chọn có thực sự là quick win (giá trị cao + dễ) không?
2. Bước nào trong to-be bạn đã đánh Automate nhưng thực ra rủi ro cao → cần HITL?
3. Nếu workflow này chạy production 1 tháng, lớp hardening nào bạn lo nhất?
