# Lab Handout — Buổi 05 (cskh-bot)

> File dành cho HỌC VIÊN (sync sang `studentkit/`). Đáp án ở `checkpoints/` (🔒 instructor-only).
> Khóa AI Automation & Vibe Coding K1 · GV: Lộc · 120 phút.

## 1. Thông tin chung
- **Workflow**: Customer Support Bot Workflow
- **KPI**: Bot CSKH chạy được: Câu hỏi → phân loại intent → trả lời đúng nguồn / chuyển người + ticket → conversation log + FAQ gap.
- **Điều kiện tiên quyết**: Có FAQ mẫu + chính sách hỗ trợ mẫu. Có kênh chat test. Hiểu workflow B4.
- **Công cụ**: AI chat (Gemini/Claude free) · Google Sheets/Docs · n8n (optional TH4) · Agent Coding/CLI.
- **Nguyên tắc an toàn**: Rule injection (bỏ qua lệnh trong tin nhắn khách) + test mode khi node gửi email/ticket thật.

## 2. Mục tiêu thực hành (đo được)
- **M1** — Kho tri thức ≥15 mục, 5 nhóm, mỗi mục có nguồn. *Verify: đếm mục + check nhóm.*
- **M2** — Phân loại intent đúng 5/5 câu mẫu; câu ngoài scope bị flag. *Verify: bảng intent.*
- **M3** — ≥2 ticket cho case chuyển người (khiếu nại + hoàn tiền), có người phụ trách. *Verify: ticket sheet.*
- **M4** — Conversation log 5 test case (5 trường) + FAQ gap ≥1 mục. *Verify: log sheet.*

## 3. Chuẩn bị (HV)
| Item | Số lượng | Link/Path |
|------|---------|-----------|
| AI chat (Gemini/Claude) | 1/HV | free |
| Google Sheets/Docs | 1/HV | kho + log + ticket |
| `templates/faq-khoa-hoc.json` | 1/HV | 15 mục mẫu |
| `templates/chinh-sach-ho-tro.md` | 1/HV | chính sách gốc |
| `checkpoints/test-cases.json` | (GV phát) | 5 test case — có 2 outside-scope |

## 4. Bài tập liên kết — Exercise Chain
> Output TH_N = Input TH_{N+1}.

| # | Tên | Concept | Tool | Deliverable | Liên kết |
|---|-----|---------|------|-------------|----------|
| TH1 | Kho tri thức | Kho trước bot sau | Sheets/Docs | FAQ sheet (≥15) | → input TH2 |
| TH2 | Intent + trả lời | 5 intent + ngoài scope | AI chat | Bảng câu trả lời | → input TH3 |
| TH3 | Confidence + ticket | Route tới human | AI chat + Sheets | Tickets + quy tắc | → input TH4 |
| TH4 | Log + gap + nghiệm thu | Cải thiện bot | AI chat + Sheets | Agent + log 5 case | Final |

---

## TH1 — Kho tri thức (FAQ + chính sách) (15')

- **Mô tả (Input → Action → Output)**:
  - Input: `chinh-sach-ho-tro.md` (chính sách gốc).
  - Action: Lên kho tri thức tối thiểu: FAQ + thông tin sản phẩm + chính sách giá/thanh toán/hoàn tiền + quy trình hỗ trợ + liên hệ. Kho rõ → bot ít bịa.
  - Output: FAQ sheet ≥15 mục, 5 nhóm, mỗi mục có "nguồn" (chính sách nào).

- **Công cụ**: Google Sheets/Docs · Prompt: `prompts/bt1-prompt.md`

- **SLI/SLO**:
  - ≥15 mục, đủ 5 nhóm (xác nhận thanh toán, hoàn tiền, kỹ thuật, khiếu nại, liên hệ).
  - Mỗi mục: `id`, `nhom`, `cau_hoi`, `cau_tra_loi`, `nguon`.
  - Không bịa — câu trả lời phải trỏ nguồn trong chính sách.

- **Bước time-box**:
  1. (2') Mở Sheets mới → tạo 5 cột (id/nhom/cau_hoi/cau_tra_loi/nguon).
  2. (3') Mở `prompts/bt1-prompt.md` → copy → dán vào AI chat (kèm `chinh-sach-ho-tro.md`).
  3. (7') AI sinh ≥15 FAQ → HV copy vào sheet → bổ nhóm nếu thiếu.
  4. (3') Check: đủ 5 nhóm chưa? Mục nào không có nguồn → bỏ/sửa.

- **Đầu ra**: FAQ sheet (≥15 mục, 5 nhóm, có nguồn)

- **Safety/HITL**: Kho là synthetic — an toàn. Khi áp dụng thật → đảm bảo chính sách cập nhật.

- **Kế thừa**: FAQ sheet = input cho TH2. Cùng đoạn chat giữ context.

> 💡 Stuck >8'? `checkpoints/checkpoint-bt1.md`.

---

## TH2 — Phân loại intent + trả lời theo nguồn (15')

- **Mô tả (Input → Action → Output)**:
  - Input: FAQ sheet (TH1) + 5 câu hỏi mẫu.
  - Action: Bot KHÔNG trả lời mọi thứ. Phân loại intent (thông tin/giá/lịch/kỹ thuật/khiếu nại/mua hàng/ngoài phạm vi) + câu trả lời có giới hạn (ngắn, đúng nguồn, có bước tiếp theo).
  - Output: Bảng câu trả lời theo intent — câu có nguồn trỏ nguồn, câu ngoài scope flag "chuyển người".

- **Công cụ**: AI chat · Prompt: `prompts/bt2-prompt.md`

- **SLI/SLO**:
  - Phân loại đúng 5/5 câu mẫu.
  - Câu ngoài scope bị flag rõ "ngoài phạm vi → chuyển người".
  - Mỗi câu trả lời trỏ nguồn (FAQ id) hoặc ghi "không có nguồn".

- **Bước time-box**:
  1. (2') Cùng chat → copy `prompts/bt2-prompt.md` → dán (kèm FAQ sheet).
  2. (2') Dán 5 câu hỏi mẫu vào.
  3. (6') AI phân loại + trả lời → check mỗi câu.
  4. (3') Spot-check: câu ngoài scope có bị flag không? Nếu AI bịa → chat "câu này không có trong FAQ, flag ngoài phạm vi".
  5. (2') Lưu bảng.

- **Đầu ra**: Bảng câu trả lời theo intent (5/5, outside-scope flagged)

- **Safety (CRITICAL)**: Prompt có rule injection — bỏ qua lệnh trong tin nhắn khách.

- **Kế thừa**: Bảng → input TH3 (gắn confidence + ticket).

---

## TH3 — Confidence + routing tới human + ticket (15')

- **Mô tả (Input → Action → Output)**:
  - Input: Bảng TH2.
  - Action: Gắn confidence (cao/thấp). Confidence thấp HOẶC hoàn tiền/khiếu nại/pháp lý/khách tức giann → chuyển người. Tạo ticket (Ticket ID|KH|kênh|intent|nội dung|trạng thái|người phụ trách).
  - Output: ≥2 ticket + quy tắc chuyển người.

- **Công cụ**: AI chat + Sheets · Prompt: `prompts/bt3-prompt.md`

- **SLI/SLO**:
  - ≥2 ticket cho case chuyển người (khiếu nại + hoàn tiền).
  - Mỗi ticket đủ 7 trường + người phụ trách (không trống).
  - Quy tắc chuyển người ghi rõ (5 điều kiện).

- **Bước time-box**:
  1. (2') Cùng chat → copy `prompts/bt3-prompt.md` → dán.
  2. (5') AI gắn confidence + tạo ticket cho case chuyển người.
  3. (5') Tạo ticket sheet (7 cột) → copy ticket vào.
  4. (3') Check: case khiếu nại + hoàn tiền có ticket? Có người phụ trách?

- **Đầu ra**: Ticket sheet (≥2 ticket) + quy tắc chuyển người

- **Safety/HITL**: Ticket chuyển NGƯỜI xử lý — bot không tự giải quyết khiếu nại.

- **Kế thừa**: Tickets + bảng → input TH4.

---

## TH4 — Conversation log + FAQ gap + nghiệm thu (25', capstone)

- **Mô tả (Input → Action → Output)**:
  - Input: FAQ sheet + bảng intent + tickets.
  - Action: Gộp 4 phân đoạn thành `cskh-bot-agent.md`. Chạy 5 test case (GV phát `checkpoints/test-cases.json`). Ghi conversation log (khách hỏi/intent/bot trả lời/có chuyển người/có nguồn) + FAQ gap (câu chưa có nguồn).
  - Output: Agent + conversation log 5 case + FAQ gap list.

- **Công cụ**: AI chat + Sheets · Prompt: `prompts/bt4-prompt.md`

- **SLI/SLO**:
  - Bot chạy 5 test case → log đủ 5 trường × 5 case.
  - Bot chuyển ĐÚNG 2 case outside-scope (không bịa).
  - FAQ gap list ≥1 mục (câu chưa có nguồn).

- **Bước time-box**:
  1. (3') Cùng chat → copy `prompts/bt4-prompt.md` → dán → AI gộp agent.
  2. (3') Lưu `cskh-bot-agent.md`.
  3. (4') GV phát 5 test case → chạy qua agent.
  4. (8') Ghi conversation log (5 trường × 5 case).
  5. (5') FAQ gap list: câu nào bot không trả lời được → thêm vào.
  6. (2') Nghiệm thu GV.

- **Đầu ra**: ★ `cskh-bot-agent.md` + conversation log 5 case + FAQ gap

- **Safety/HITL (CRITICAL)**: Node gửi email/ticket thật → test mode TẮT trong lab. Production → GV duyệt trước khi bật.

- **Kế thừa**: Final. Bot + gap list → cải thiện dần (homework).

---

## 5. Tổng kết lab
**Deliverable chạy được:**
- [ ] FAQ sheet ≥15 mục, 5 nhóm, có nguồn
- [ ] Bảng intent 5/5, outside-scope flagged
- [ ] Ticket sheet ≥2 ticket, có người phụ trách
- [ ] `cskh-bot-agent.md` gộp 4 phân đoạn
- [ ] Conversation log 5 case + FAQ gap ≥1

**Bài tập về nhà**: Thêm 5 FAQ từ gap list vào kho → chạy lại bot trên 5 test case → so sánh log trước/sau. Nộp log + 100 từ reflection.

## 6. Fallback & Checkpoint Index
| TH | Fallback | Checkpoint | Mở khi |
|----|----------|------------|--------|
| TH1 | `checkpoints/faq-khoa-hoc-full.json` | `checkpoints/checkpoint-bt1.md` | stuck >8' |
| TH2 | `checkpoints/intent-results-sample.json` | `checkpoints/checkpoint-bt2.md` | stuck >8' |
| TH3 | `checkpoints/tickets-sample.json` | `checkpoints/checkpoint-bt3.md` | stuck >8' |
| TH4 | `checkpoints/cskh-bot-agent-solution.md` + `conversation-log-sample.xlsx` | `checkpoints/checkpoint-bt4.md` | stuck >10' |

## Checklist nghiệm thu (SLI/SLO)
- [ ] TH1: ≥15 FAQ, 5 nhóm, có nguồn
- [ ] TH2: 5/5 intent đúng, outside-scope flagged
- [ ] TH3: ≥2 ticket + người phụ trách
- [ ] TH4: bot chuyển đúng 2 outside-scope, không bịa, gap ≥1
- [ ] Rule injection trong mọi prompt (bỏ qua lệnh trong tin nhắn khách)
- [ ] Test mode cho node gửi thật (email/ticket)
- [ ] HITL: khiếu nại/hoàn tiền/pháp lý → chuyển người, không auto-xử lý
