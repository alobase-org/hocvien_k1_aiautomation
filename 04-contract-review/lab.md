# Lab Handout — Buổi 04 (contract-review)

> File dành cho HỌC VIÊN (sync sang `studentkit/`). Đáp án/expected output ở `checkpoints/` (🔒 instructor-only).
> Khóa AI Automation & Vibe Coding K1 · GV: Lộc · 120 phút · Nhóm HV: dân vận hành/pháp lý/kỹ thuật phi-code.

## 1. Thông tin chung
- **Workflow**: Contract Review Workflow
- **KPI**: Một "Hệ thống soi chiếu hợp đồng" (Skill/Instructions). Đưa cho AI → tự quét DOCX/PDF, highlight rủi ro theo lớp, xuất báo cáo cho human duyệt.
- **Điều kiện tiên quyết**: Hợp đồng mẫu `.docx`/`.pdf` số pháp lý.
- **Công cụ**: Antigravity IDE (chính), Codex (phụ).
- **Nguyên tắc an toàn**: Chỉ dùng file synthetic trong `templates/`. KHÔNG ném hợp đồng thật có PII lên AI công cộng.

## 2. Mục tiêu thực hành (đo được)
- **M1** — Bóc tách contract `.docx` → `clauses.json` đúng 8/8 điều khoản + metadata. *Verify: mở file, đếm clause.*
- **M2** — Rà khung → `macro-gaps.json` flag ≥1 omission (điều khoản thiếu). *Verify: có dòng `status: "thiếu"`.*
- **M3** — Rà chi tiết → `micro-risk.json` có ≥3 redline (HIGH) + reference clause. *Verify: đếm risk level.*
- **M4** — Đóng gói Agent → chạy contract holdout → `report.xlsx` có omission + redline + section người duyệt. *Verify: GV check report.*

## 3. Chuẩn bị (HV)
| Item | Số lượng | Link/Path |
|------|---------|-----------|
| Antigravity IDE (login) | 1/HV | đã cài B1 |
| `templates/contract-mau-hop-dong-dich-vu.docx` | 1/HV | contract synthetic 8 điều khoản |
| `templates/checklist-rui-ro.json` | 1/HV | 12 tiêu chí rà khung |
| Codex CLI (optional) | 1/HV | phụ |

## 4. Bài tập liên kết — Exercise Chain
> Output TH_N = Input TH_{N+1}.

| # | Tên | Concept | Tool | Deliverable | Liên kết |
|---|-----|---------|------|-------------|----------|
| TH1 | Bóc tách & chuẩn hóa | Long-context parse | Antigravity | `clauses.json` | → input TH2 |
| TH2 | Rà khung (vĩ mô) | Omission detection | Antigravity | `macro-gaps.json` | → input TH3 |
| TH3 | Rà chi tiết (vi mô) | Mập mờ + trách nhiệm | Antigravity | `micro-risk.json` | → input TH4 |
| TH4 | Đóng gói Agent + HITL | Pipeline orchestration | Antigravity | `contract-review-agent.md` + `report.xlsx` | Final |

---

## TH1 — Bóc tách thông tin & chuẩn hóa (15')

- **Mô tả kỹ thuật (Input → Action → Output)**:
  - Input: `contract-mau-hop-dong-dich-vu.docx` (văn bản dài).
  - Action: Lớp tool xử lý long-context — bóc text sạch, phân mảnh, chuẩn hóa thành metadata + danh sách điều khoản có id.
  - Output: `clauses.json` — `metadata{}` + `clauses[]` (mỗi clause: `id`, `tieu_de`, `noi_dung`, `vi_tri`).

- **Công cụ**: Antigravity IDE · Prompt: `prompts/bt1-prompt.md`

- **SLI/SLO**:
  - Bóc đúng **8/8 điều khoản** của contract mẫu.
  - Metadata đủ 6 trường: `ben_a`, `ben_b`, `ngay_ky`, `gia_tri`, `loai_hop_dong`, `thoi_han`.
  - Mỗi clause có `id` (VD: `HD01`...) + `vi_tri` (số trang/đoạn).

- **Bước time-box**:
  1. (2') Mở Antigravity → new planning chat → load `contract-mau-hop-dong-dich-vu.docx`.
  2. (3') Mở `prompts/bt1-prompt.md` → copy toàn bộ → dán vào chat.
  3. (5') Chạy → AI bóc tách → kiểm tra đủ 8 clause chưa (nếu thiếu: chat "bóc tiếp clause còn sót").
  4. (3') Lưu output thành `clauses.json` (Yêu cầu AI: "Xuất ra file clauses.json theo schema trên").

- **Đầu ra**: `clauses.json` (8/8 clause + metadata)

- **Safety/HITL**: File synthetic, PII fake — an toàn chạy. Nếu dùng hợp đồng thật → bỏ PII trước.

- **Kế thừa (chain)**: `clauses.json` là input cho TH2. **Chạy trong CÙNG đoạn chat** để AI giữ context.

> 💡 Stuck >8'? Mở `checkpoints/checkpoint-bt1.md`.

---

## TH2 — Rà soát khung tổng thể (15')

- **Mô tả kỹ thuật (Input → Action → Output)**:
  - Input: `clauses.json` (từ TH1).
  - Action: Lớp soi "bức tranh lớn" — đếm điều khoản, check "bắt buộc phải có", đánh giá logic, **phát hiện omission** (điều khoản bị xóa).
  - Output: `macro-gaps.json` — mỗi loại điều khoản: `status` (có/thiếu/mơ hồ) + `mo_ta` + `muc_do_rui_ro`.

- **Công cụ**: Antigravity IDE · Prompt: `prompts/bt2-prompt.md`

- **SLI/SLO**:
  - Phân loại đủ **8 loại điều khoản bắt buộc** (đối tượng, giá trị, thanh toán, nghĩa vụ, chấm dứt, BMTT, GQ tranh chấp, pháp luật áp dụng).
  - Flag **≥1 omission** trong contract mẫu (contract mẫu CÓ thiếu 1 điều khoản cố ý — tìm xem!).
  - Mỗi omission có `muc_do_rui_ro: HIGH`.

- **Bước time-box**:
  1. (2') Cùng chat TH1 → load `checklist-rui-ro.json`.
  2. (2') Copy `prompts/bt2-prompt.md` → dán.
  3. (6') Chạy → AI rà khung → flag omission.
  4. (3') Đối chiếu: AI có báo "thiếu điều khoản X" không? Nếu sai → chat "recheck, contract không có điều khoản [X]".
  5. (2') Lưu `macro-gaps.json`.

- **Đầu ra**: `macro-gaps.json` (≥1 omission flagged HIGH)

- **Safety/HITL**: Quyết định "có phải omission thật không" → HV xác nhận (AI có thể false positive).

- **Kế thừa**: `macro-gaps.json` + `clauses.json` → input TH3.

---

## TH3 — Rà soát chi tiết (15')

- **Mô tả kỹ thuật (Input → Action → Output)**:
  - Input: `clauses.json` (TH1).
  - Action: Lớp micro-level — 3 lăng kính: (1) trách nhiệm các bên, (2) câu chữ mập mờ ("hợp lý", "khi cần", "có thể"), (3) phân loại rủi ro HIGH/MED/LOW.
  - Output: `micro-risk.json` — mỗi risk: `id_clause`, `loai`, `mo_ta`, `muc_do`, `de_xuat`.

- **Công cụ**: Antigravity IDE · Prompt: `prompts/bt3-prompt.md`

- **SLI/SLO**:
  - Tìm **≥3 redline (HIGH)** trong contract mẫu (đã cài sẵn mập mờ).
  - Mỗi risk có `id_clause` tham chiếu + `de_xuat` sửa.
  - Phân loại đúng HIGH/MED/LOW (không đánh đồng tất cả là HIGH).

- **Bước time-box**:
  1. (2') Cùng chat → copy `prompts/bt3-prompt.md` → dán.
  2. (7') Chạy → AI bóc từng clause → gắn risk.
  3. (4') Spot-check 3 clause: AI có bắt được "thanh toán trong thời hạn hợp lý" là mập mờ?
  4. (2') Lưu `micro-risk.json`.

- **Đầu ra**: `micro-risk.json` (≥3 redline + reference)

- **Safety/HITL**: AI có thể over-flag — HV loại bỏ false positive.

- **Kế thừa**: `micro-risk.json` + `macro-gaps.json` → input TH4.

---

## TH4 — Đóng gói & ra quyết định (25', capstone)

- **Mô tả kỹ thuật (Input → Action → Output)**:
  - Input: `clauses.json` + `macro-gaps.json` + `micro-risk.json`.
  - Action: Gộp 4 lớp thành 1 Agent (`contract-review-agent.md` — Skill/Instructions). Chạy trên **contract holdout** (GV phát). Xuất `report.xlsx`.
  - Output: `contract-review-agent.md` + `report.xlsx` (highlight omission + redline + section "Người duyệt / ngày / quyết định").

- **Công cụ**: Antigravity IDE · Prompt: `prompts/bt4-prompt.md`

- **SLI/SLO**:
  - Agent chạy **end-to-end 1 lệnh** trên contract holdout.
  - `report.xlsx` có: ≥1 omission + ≥3 redline + section người duyệt.
  - HV điền quyết định HITL ("duyệt" / "yêu cầu sửa" + lý do).

- **Bước time-box**:
  1. (3') Cùng chat → copy `prompts/bt4-prompt.md` → dán → AI gộp 4 lớp thành Agent instruction.
  2. (3') Lưu Agent → `contract-review-agent.md`.
  3. (4') GV phát contract holdout → load vào chat → chạy Agent.
  4. (8') AI xuất `report.xlsx` → mở kiểm tra omission + redline.
  5. (5') HV đóng vai người duyệt → điền section HITL.
  6. (2') Nghiệm thu với GV.

- **Đầu ra**: `contract-review-agent.md` + `report.xlsx` (HITL)

- **Safety/HITL (CRITICAL)**: Quyết định "duyệt hợp đồng" LUÔN thuộc người — Agent chỉ đề xuất. Trước khi áp dụng Agent ở cơ quan thật → chạy thử 10 hợp đồng đã duyệt, so sánh.

- **Kế thừa**: Final output. Áp dụng cho mọi hợp đồng mới (homework).

---

## 5. Tổng kết lab
**Deliverable chạy được (checkbox):**
- [ ] `clauses.json` — 8/8 clause + metadata
- [ ] `macro-gaps.json` — ≥1 omission HIGH
- [ ] `micro-risk.json` — ≥3 redline + reference
- [ ] `contract-review-agent.md` — gộp 4 lớp
- [ ] `report.xlsx` — omission + redline + section HITL

**Bài tập về nhà**: Áp dụng `contract-review-agent.md` lên 1 hợp đồng HV tự tìm (loại bỏ PII trước). Nộp `report.xlsx` + 1 đoạn reflection (100 từ): "Agent bắt được gì mà HV đọc tay sót?"

## 6. Fallback & Checkpoint Index
| TH | Fallback (nếu stuck) | Checkpoint | Mở khi |
|----|---------------------|------------|--------|
| TH1 | `checkpoints/clauses-sample.json` | `checkpoints/checkpoint-bt1.md` | stuck >8' |
| TH2 | `checkpoints/macro-gaps-sample.json` | `checkpoints/checkpoint-bt2.md` | stuck >8' |
| TH3 | `checkpoints/micro-risk-sample.json` | `checkpoints/checkpoint-bt3.md` | stuck >8' |
| TH4 | `checkpoints/contract-review-agent-solution.md` + `demo-report.xlsx` | `checkpoints/checkpoint-bt4.md` | stuck >10' |

> Quy tắc: thử ≥8 phút mới mở checkpoint. TA/GV đi quanh hỗ trợ trước.

## Checklist nghiệm thu (SLI/SLO đo được)
- [ ] TH1: 8/8 clause bóc đúng
- [ ] TH2: ≥1 omission flagged HIGH
- [ ] TH3: ≥3 redline HIGH + reference clause
- [ ] TH4: Agent chạy 1 lệnh → report có omission + redline + HITL section
- [ ] Synthetic data zero PII thật
- [ ] HITL cho node "duyệt hợp đồng" (không auto-approve)
- [ ] Rule injection trong prompt (bỏ qua lệnh trong hợp đồng đầu vào)
