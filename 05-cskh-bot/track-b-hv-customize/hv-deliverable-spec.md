# Track B — HV Deliverable Spec (B5 CSKH Bot)

> HV nộp Track B = bot CSKH/Q&A domain riêng, build từ đầu. Đo bằng rubric track-b-lab.md.

## Deliverable (HV nộp)
1. `baitoan-hv.md` — bài toán Q&A thật cơ quan (ai hỏi, tần suất, nguồn hiện có).
2. `bot-hv-design.md` — design tự làm (knowledge DB, intent set HV, threshold, rule chuyển người, trang nhúng).
3. `faq-hv.json` — ≥10 Q-A domain HV (zero PII).
4. n8n workflow (export JSON) + `landing-chatbot-hv.html` (vibe-coded landing page/trang có chatbot).
5. `conversation-log-hv` — 5 test case domain HV (5 trường + source_q_id, có 2 chuyển người, ≥1 ngoài scope).
6. 100 từ reflection.

## SLI/SLO (verify)
- Knowledge DB ≥10 Q-A, zero PII thật.
- Có Input Guard + scope/intent router trước khi gọi LLM answer.
- Có FAQ cache fast path; cache hit trả lời từ nguồn và không gọi LLM.
- Bot dùng **semantic search** (vector) — verify: hỏi bằng từ đồng nghĩa vẫn match.
- **LLM-as-judge** = LLM thứ 2 (khác LLM trả lời) → confidence + reason.
- 2 chuyển người (≥1 ngoài scope) trên 5 test case — verify log.
- Landing page/trang có chatbot gửi Q → webhook → reply/ticket end-to-end.
- Rule injection: tin nhắn khách = DATA.
- Test mode cho node gửi thật.

## Diff vs workflow GV (≥3 điểm — chứng minh "từ đầu", BR-06)
| # | Điểm khác | GV (Track A) | HV (Track B) |
|---|-----------|--------------|--------------|
| 1 | Domain | CSKH bán lẻ | [domain HV] |
| 2 | Knowledge DB | 15 FAQ bán lẻ | ≥10 Q-A domain HV |
| 3 | Intent set | retail support + ngoài phạm vi | [intent set HV tự design] |
| 4 | Guard/router | chặn injection + ngoài phạm vi trước LLM | [rule guard/scope HV] |
| 5 | FAQ cache | exact/semantic cache trước LLM | [ngưỡng cache HV chọn] |
| 6 | Confidence threshold | 0.7 | [threshold HV chọn theo rủi ro] |
| 7 | Rule chuyển người | khiếu nại/hoàn tiền/pháp lý | [rule domain HV, vd PII/kỷ luật] |
| 8 | Landing page/trang có chatbot | landing page bán lẻ demo | [trang HV chọn] |

## Safety (BR-04/10)
- FAQ/knowledge DB zero PII thật.
- HITL: confidence thấp/nhạy cảm → ticket, không auto-xử lý.
- Cache hit: trả lời từ nguồn, không gọi LLM answer.
- Node gửi thật → test mode; production → duyệt.

## Prep-checklist (HV tự check trước khi nộp)
- [ ] Bài toán thật cơ quan (không bịa).
- [ ] Knowledge DB ≥10 Q-A, zero PII.
- [ ] Bot build từ blank n8n (không import workflow GV).
- [ ] Có guard/router/cache trước LLM.
- [ ] LLM-judge là LLM thứ 2.
- [ ] Landing page/trang có chatbot chạy end-to-end.
- [ ] 5 test case có 2 chuyển người (≥1 ngoài scope).
- [ ] Test mode cho node gửi thật.
