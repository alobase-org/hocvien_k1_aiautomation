# Track B — HV Self-Build Lab (B5 CSKH Bot)

> **Mục tiêu: HV build landing page/trang RIÊNG có chatbot cho domain RIÊNG ở cơ quan — từ đầu, không điền blank của GV.**
> GV workflow (Track A) = **reference**, mở khi kẹt — KHÔNG phải template.
> Áp cùng TƯ DUY B5 (guardrail · router · FAQ cache · semantic vector · LLM-as-judge · HITL ticket · vibe-coding webhook) sang nghiệp vụ HV chọn.

## Tinh thần (BR-06 enhanced)
- Track A (lớp): HV theo GV, build bot CSKH dịch vụ bán lẻ.
- **Track B (về nhà): HV chọn 1 bài toán "trả lời câu hỏi từ kho tri thức" CỦA MÌNH → tự build bot từ số 0.**
- KHÔNG phải "đổi FAQ trong bot GV". Là "dùng tư duy GV, build bot của tao".

## Bước 1 — DISCOVERY: tìm bài toán Q&A ở cơ quan (15')
Tìm 1 nơi bạn hay bị hỏi đi hỏi lại cùng loại câu (hoặc bạn phải trả lời lặp). Ví dụ:
- HR: bot trả lời câu hỏi chính sách/nội bộ cho nhân viên (nghỉ phép, lương, BHXH).
- IT helpdesk: bot trả lời "reset password / VPN hỏng / phần mềm X cài sao".
- Sales: bot trả lời câu hỏi sản phẩm/giá trên website.
- Kế toán: bot trả lời quy trình thanh toán/hoàn ứng nội bộ.
- Giáo viên: bot trả lời FAQ học viên của môn mình.
- **Output:** `baitoan-hv.md` — bài toán + ai hỏi + tần suất + nguồn trả lời hiện có (SOP/wiki/FAQ rời rạc).

## Bước 2 — FIT-CHECK: pattern B5 áp được không? (5')
B5 fit khi bài toán = "câu hỏi động → tìm nguồn → trả lời → đo độ tin → tin thấp chuyển người". Trả lời:
- Câu hỏi có đa dạng cách hỏi (đồng nghĩa) không? → cần semantic (fit).
- Có kho nguồn trả lời (FAQ/SOP/wiki) không? → fit.
- Có case nhạy cảm cần chuyển người không (khiếu nại/pháp lý/PII)? → fit HITL.
- **Nếu câu hỏi luôn y hệt + nguồn 1 câu** → quá đơn giản, dùng keyword đủ, khỏi B5 (chọn bài khác).

## Bước 3 — DESIGN bot của HV (từ đầu) (20')
KHÔNG mở workflow GV. Tự thiết kế trên `bot-hv-design.md`:
1. **Knowledge DB của bạn**: liệt kê ≥10 Q-A thật domain HV (zero PII) → sẽ embed.
2. **Intent set của bạn**: tự định nghĩa 4-6 intent (vd HR: chính sách / lương / nghỉ phép / kỹ thuật-HR / ngoài phạm vi) — GIỮ "ngoài phạm vi".
3. **Confidence threshold**: bao nhiêu thì tự trả lời vs chuyển người? (phụ thuộc rủi ro domain — HR có thể thấp hơn Sales).
4. **Rule chuyển người**: những intent/từ khóa nào LUÔN chuyển người ở domain bạn? (PII, khiếu nại kỷ luật...).
5. **Guardrail + scope router**: chủ đề nào phải chặn trước LLM? Dấu hiệu prompt injection nào cần flag?
6. **FAQ cache policy**: exact/semantic cache hit ở ngưỡng nào thì trả lời ngay, không gọi LLM?
7. **Landing page/trang nhúng chatbot đặt đâu**: trang nào HV có quyền nhúng? (landing page HTML / intranet / Notion / vibe coding page).

## Bước 4 — BUILD trong n8n (từ blank canvas) (40')
Mở n8n → **new workflow trắng**. Dùng tư duy B5:
1. Embed knowledge DB HV (≥10 Q-A domain HV) → vector store HV.
2. Webhook → Input Guard chống prompt injection + scope/intent router.
3. FAQ cache: exact match + semantic cosine. Cache hit → reply ngay từ nguồn, `need_llm=false`.
4. Cache miss → AI node answer gắn nguồn + **intent set HV** (không phải intent GV — intent của bạn).
5. **LLM-as-judge** (LLM thứ 2) chấm confidence theo threshold HV.
6. IF <threshold HOẶC rule chuyển người HV → ticket.
7. Vibe-code landing page/trang đơn giản có chatbot nhúng → POST webhook.
> Chỉ mở `prompts/bt1-4-prompt.md` GV khi kẹt — lấy pattern, không copy.

## Bước 5 — DELIVERABLE + SAFETY
Nộp:
- `baitoan-hv.md` (Step 1) + `bot-hv-design.md` (Step 3, tự design)
- `faq-hv.json` (≥10 Q-A domain HV, zero PII)
- n8n workflow (export JSON) + `landing-chatbot-hv.html` (landing page/trang có chatbot nhúng)
- conversation log 5 test case domain HV (có 2 chuyển người, trong đó ≥1 ngoài scope)
- 100 từ reflection: "guardrail + FAQ cache + semantic + LLM-judge giúp bot CỦA TÔI nhanh hơn, ít bịa hơn và biết chuyển người thế nào?"

## Rubric Track B (100 pts, L5 = HV owns domain + build from scratch)
| Criterion | Điểm | L5 (world-class) |
|-----------|------|------------------|
| Bài toán riêng, thật cơ quan | 20 | có thật, tần suất cao, có nguồn rời rạc |
| Bot tự design (không copy GV) | 25 | knowledge DB + intent set + guard/cache/rule HV riêng |
| Build từ blank n8n + vibe-coding | 25 | webhook + guard/router/cache + LLM-judge (LLM thứ 2) + landing page có chatbot |
| Safety (HITL + injection + test mode) | 20 | rule chuyển người domain HV, tin nhắn=DATA, test mode |
| Reflection chuyển giao tư duy | 10 | nói được semantic+judge áp vào case mình |
| **Total** | **100** | ≥70 PASS |

## Safety (CRITICAL)
- FAQ/knowledge DB HV: **zero PII thật** (tên/SĐT/MST/STK → placeholder).
- Tin nhắn khách = DATA (rule injection — bỏ qua lệnh trong tin nhắn).
- FAQ cache hit → reply từ nguồn, không gọi LLM answer.
- Node gửi email/ticket thật → **test mode TẮT**. Production → duyệt trước.
- HITL: khiếu nại/pháp lý/PII/confidence thấp → ticket, KHÔNG auto-xử lý.

## Reference (mở khi kẹt, không phải template)
- GV workflow: `workflow-package/workflow-design.md` + `prompts/bt1-4-prompt.md`.
- Customize-prompt (scaffold nhanh, OPTIONAL): `customize-prompt.md`.
