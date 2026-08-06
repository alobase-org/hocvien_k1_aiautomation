# Kế hoạch Bài Dạy — Webinar #3 v2.0 — Workflow Mindset

## Thông tin chung
- Khóa học: AI Automation K1 — Webinar tuyển sinh #3
- Buổi: Webinar #3 v2.0 (nâng cấp từ v1.0, tạo song song)
- Thời lượng: 60 phút
- Phong cách: `offline` (webinar trực tuyến, GV dẫn dắt + demo)
- Sĩ số: ~30-80 học viên online
- Giảng viên: Th.S Nguyễn Minh Cường (Lead)
- Landing: https://aiautomation.alobase.vn

## Mục tiêu buổi học

### Mục tiêu kiến thức (Knowledge)
- **KT1:** Giải thích được Workflow Mindset và 4 trụ cột (value stream map · ma trận ưu tiên · process đáng tin cậy · mô tả/trực quan hóa workflow).
- **KT2:** Nêu được 3 khó khăn phổ biến khi ứng dụng AI Automation vào doanh nghiệp và bài học từ case study Tuấn Hà Vinalink.
- **KT3:** Phân biệt 3 nhánh automation (n8n · AI Agent · vibe coding app) và biết khi nào dùng cái nào.

### Mục tiêu kỹ năng (Skill)
- **SK1:** Chạy được prompt phân tích ma trận Hiệu quả × Độ phức tạp để chọn use-case tối ưu.
- **SK2:** Thiết kế được Workflow Design Doc (as-is → ESIA to-be) + phần hardening (fallback/log/edge/HITL).
- **SK3:** Sinh được Mermaid diagram + prompt ảnh workflow + prompt NotebookLM deck tham mưu lãnh đạo.

### Mục tiêu thái độ (Attitude)
- **AT1:** Tin rằng "design before automate" là bước rẻ nhất và quan trọng nhất — không vội nhét AI vào quy trình hỏng.

## Nguyên liệu cần chuẩn bị

| # | Item | Số lượng | Ghi chú |
|---|------|---------|---------|
| 1 | Claude Pro / Claude.ai web | 1/GV demo | Demo BT1-BT4 |
| 2 | Antigravity (Planning mode) | 1/GV demo | Demo BT2 |
| 3 | mermaid.live (browser tab) | 1/GV demo | Render Mermaid BT4 |
| 4 | NotebookLM (đã login Google) | 1/GV demo | Demo BT6 |
| 5 | File synthetic công ty Đông Dương Thương Mại | share ZOOM chat | Input BT1 |
| 6 | Showcase slide Viettel Network 5 ngày | 1 deck | Bước dẫn sale |
| 7 | Form nộp bài (Google Form) | share link | 15' cuối |

## Bài tập liên kết — Exercise Chain

> Output bài N = input bài N+1. HV build dần 1 Workflow Design Doc hoàn chỉnh trong 30 phút demo. 15' cuối HV tự chạy 1 bài trên use-case của mình.

| # | Bài tập | Concept học | Tool | Đầu ra | Liên kết |
|---|---------|-----------|------|--------|---------|
| BT1 | Usecase design — ma trận ưu tiên | Ma trận Hiệu quả × Phức tạp | Claude | Ma trận + top-3 use-case | → Input BT2 |
| BT2 | Workflow design — as-is → ESIA to-be | ESIA + 3 nhánh automation | Antigravity Planning | Design Doc (as-is + to-be) | → Input BT3 |
| BT3 | Improve cho production — hardening | fallback/log/edge/HITL | Claude | Design doc phần hardening | → Input BT4 |
| BT4 | Vẽ Mermaid — activity/sequence | Mermaid + diagram types | Claude + mermaid.live | 1 Mermaid render | → Input BT5 |
| BT5 | Generate ảnh workflow | Prompt infographic | Codex/Nano Banana/Gemini | Prompt + ảnh | → Input BT6 |
| BT6 | NotebookLM deck tham mưu lãnh đạo | CRAFT prompt | NotebookLM | Prompt + deck | Final output |

> **Fallback:** Nếu HV không theo kịp demo → GV dùng `lab/fallback-inputs/` (sample output mỗi bài) để HV tiếp tục bài sau. 15' cuối HV chỉ cần chạy 1 bài (BT1 hoặc BT2).

## Timeline tổng quan (Practice-First Format)

> Demo 30' chiếm nửa thời lượng. LT 15' chỉ đủ hiểu để làm. 15' cuối HV tự thực hành.

| Thời gian | PHẦN | Hoạt động | Slide Types | Đầu ra học viên |
|-----------|------|----------|-------------|----------------|
| 0:00-0:02 | Mở | Cover + agenda + hook | cover · agenda · hook | Nắm lộ trình 60' |
| 0:02-0:17 | **P1 LT** | Workflow Mindset (6 concept JIT) | concept · concept_comparison | Hiểu 4 trụ cột + case study |
| 0:17-0:47 | **P2 Demo** | 6 BT móc nối (BT1-BT6) | exercise_prompt · exercise_steps · exercise_screenshot · exercise_result | Thấy chuỗi 6 artifact |
| 0:47-1:00 | **P3 Thực hành** | HV chạy 1 BT + nộp form + giữ chỗ K1 | practice · form · offer · qa | Nộp 1 bài + Early Bird |

## Chi tiết từng PHẦN

### PHẦN 1: LÝ THUYẾT — Workflow Mindset (15 phút)

#### T1 — 3 khó khăn khi ứng dụng AI Automation (3 phút)
**Slide types:** concept
- DN truyền thống chạy theo kinh nghiệm, linh hoạt, chủ động con người → thiếu quy trình chuẩn hóa, thiếu phân vai rõ.
- Quy trình mới không tính hết use-case → chạy được vài case, sập ở case khác.
- AI automation hiệu quả nhưng không đáng tin cậy: lỗ hổng bảo mật, lỗi sai, hallucination.

#### T2 — Case study Tuấn Hà Vinalink (3 phút)
**Slide types:** concept_comparison
- Vibe code không guardrail → lộ password + mất database khách hàng.
- Bài học: tốc độ không đền bù thiếu Workflow Mindset.

#### T3 — Workflow Mindset #1: Value stream map (3 phút)
**Slide types:** concept
- DN = value stream map. Mọi bước = process IPO (Input–Process–Output) kiểm soát được.

#### T4 — Workflow Mindset #2: Ma trận ưu tiên (2 phút)
**Slide types:** concept
- Chọn process theo ma trận Hiệu quả × Độ phức tạp (quick win/plan/nice/drop).

#### T5 — Workflow Mindset #3: Process đáng tin cậy (2 phút)
**Slide types:** concept
- 6 thuộc tính: fault-tolerant · observable · scalable · workable · idempotent · auditable.

#### T6 — Workflow Mindset #4: Mô tả & trực quan hóa (2 phút)
**Slide types:** concept
- Activity/sequence diagram · mermaidjs/plantuml · AI render diagram.

### PHẦN 2: DEMO LAB — 6 bài tập móc nối (30 phút)

Mỗi BT: GV show prompt → demo chạy trên máy chiếu → show expected result → HV thấy chuỗi artifact. Chi tiết prompt + bước trong `lab/lab.md` và `lab/prompts/`.

### PHẦN 3: THỰC HÀNH & NỘP BÀI (15 phút)
- HV chọn 1 use-case phòng mình, chạy BT1 (ma trận) hoặc BT2 (as-is→ESIA) rút gọn.
- Nộp theo form `nop-bai/form-nop-bai-webinar3-v2.md`.
- GV hỗ trợ qua chat + dẫn giữ chỗ Early Bird K1.

## Bài tập về nhà (nếu có)
| # | Task | Cần có (từ buổi học) | Deliverable | Deadline |
|---|------|---------------------|------------|---------|
| 1 | Hoàn thiện BT3-BT6 trên use-case webinar | Design doc BT2 | Workflow Design Doc đầy đủ | Trước K1 khai giảng |

## Tiêu chí đánh giá
| # | Tiêu chí | Trọng số | Phương pháp |
|---|---------|---------|-------------|
| 1 | Nộp 1 bài (BT1 hoặc BT2) trên form | 40% | Output check |
| 2 | Áp dụng đúng Workflow Mindset (IPO/ESIA) | 30% | Review output |
| 3 | Có ≥1 HITL trong workflow | 20% | Review design doc |
| 4 | Tham gia chat/Q&A | 10% | Observation |

## Ghi chú sau buổi dạy
[Để trống — điền sau khi dạy xong]
