# Lab 05 — Deliverable cuối: TỰ CHẤM trước khi nộp (Evaluate)

> Lab này khép vòng: **Design (lab 00) → Implement (lab 01–03) → Package (lab 04) → Evaluate (lab này)**. Làm xong ở đây bạn mới thật sự "triển khai xong một use case AI Automation" — vì đã đo được sản phẩm của mình bằng chính tiêu chí GV sẽ dùng.

## Mục tiêu
Trước khi nộp, bạn tự chạy 2 lớp kiểm:
1. **Auto-check deterministic** — script kiểm cấu trúc, đồ thị workflow, run-log, pitch + **chạy thật workflow của bạn trên n8n với 1 input** (đúng bước GV sẽ làm khi chấm). Không chấm điểm, chỉ PASS/FAIL.
2. **Tự chấm rubric** — bạn chấm package của mình theo đúng rubric GV dùng (dán cho AI hỗ trợ, nhưng bạn là người chấm cuối).

## File input cần cung cấp
- `input/` không cần — input chính là **package của bạn** (ho-ten-capstone/)
- Rubric: GV chia sẻ `checkpoints/rubric-capstone.json` trong studentkit

## Prompt để chạy

| Prompt | Input | Output |
|--------|-------|--------|
| `prompt/12-self-grade.prompt.md` | package + rubric | `self-grading.md` (bảng tự chấm + kế hoạch fix) |

## Các bước

### Bước 1 — Auto-check (5 phút)
```bash
# n8n local đang chạy thì check [6] runtime sẽ chạy luôn; chưa chạy thì mở terminal gõ: npx n8n start
python3 05-self-check/tool/capstone_auto_check.py <thư-mục-package-của-bạn>
```
- Mọi dòng `[FAIL]` → quay lại lab tương ứng fix rồi chạy lại.
- `[SKIP] n8n local` → khởi động n8n rồi chạy lại: đây là lần **workflow của bạn được import + chạy input thật trước khi GV làm điều tương tự**. Nếu script báo lỗi import/webhook, tốt hơn là bạn phát hiện trước GV.

### Bước 2 — Tự chấm bằng skill chấm bài (30 phút)
Lab này kèm **nguyên bộ skill chấm bài của giảng viên** (thư mục `skill/` bên dưới) — chính công cụ GV dùng để chấm bạn:
1. Copy folder `skill/vibe-ai-auto-score/` vào `~/.claude/skills/` (Claude Code), khởi động lại.
2. Trong thư mục package của bạn, gọi: *"Dùng skill chấm bài vừa cài, chấm package này theo rubric `checkpoints/rubric-capstone.json` (trong studentkit). Xuất self-grading.md, chấm đúng mức — không nể."*
3. Skill sẽ chấm từng criterion kèm evidence verbatim trích từ package của bạn.

**Không dùng Claude Code?** Fallback: chạy `prompt/12-self-grade.prompt.md` với AI thường — cùng nguyên tắc (bạn chấm, AI đối chiếu evidence).

### Bước 3 — Fix top 3 gap rồi chấm lại
Chỉ fix 3 criterion có trọng số × khoảng cách lớn nhất (prompt 12 sẽ chỉ ra), rồi chạy lại bước 1+2. Tối đa 2 vòng — đừng polish vô tận.

### Bước 4 — Đóng gói nộp
Nộp kèm `self-grading.md` trong package (GV rất thích đọc phần này — cho thấy bạn biết đánh giá sản phẩm mình).

## Nghiệm thu (đếm được)
- [ ] Auto-check: 5/5 check [1]-[5] PASS, check [6] đã chạy (không SKIP)
- [ ] `self-grading.md` có điểm từng nhóm criterion + ≥3 gap + kế hoạch fix
- [ ] Đã fix ít nhất 1 vòng sau tự chấm (giữ bản cũ để so)
- [ ] `self-grading.md` nằm trong package nộp

## Tài nguyên mượn
- **Skill chấm bài: `skill/vibe-ai-auto-score/`** (kèm ngay lab này — bộ skill thật GV dùng, đã gồm auto-check capstone trong `script/capstone_auto_check.py` + `kb/capstone-b8-auto-check.md`)
- Rubric chấm: `checkpoints/rubric-capstone.json` (trong studentkit 08-capstone — chính là rubric GV chấm bạn)
- Pattern e2e qua n8n API (nếu muốn hiểu script làm gì): `04-contract-review/test/interactive_e2e_runner.py` (B4)
