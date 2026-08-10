# Checkpoint TH3 — LLM Fallback + Confidence + Ticket (🔒 INSTRUCTOR-ONLY)

## Expected state
- [ ] LLM answer chỉ chạy khi `cache_hit=false` và `route="llm_fallback"`
- [ ] Mỗi câu LLM fallback gắn confidence (cao/thấp) và reason
- [ ] Đúng 2 ticket: TC2 hoàn tiền + TC4 ngoài phạm vi
- [ ] Mỗi ticket đủ trường chính + `nguoi_phu_trach` KHÔNG trống
- [ ] Quy tắc chuyển người (5 điều kiện) ghi rõ

## Ticket mẫu (đáp án)
| ticket_id | source_q_id | KH | kenh | intent | route | cache_hit | reason | nguoi_phu_trach |
|-----------|-------------|----|------|--------|-------|-----------|--------|-----------------|
| T01 | TC2 | KH-A | Zalo | hoàn tiền | human_ticket | true | có FAQ nhưng hoàn tiền cần CSKH cấp 2 | Đội hoàn tiền |
| T02 | TC4 | KH-B | Website | ngoài phạm vi | refuse_or_ticket | false | ngoài scope + prompt injection | CSKH cấp 2 |

## Rescue map

| Triệu chứng | Nguyên nhân | Sửa |
|-------------|-------------|-----|
| LLM chạy cả cache hit | Chưa có IF Need LLM | Chat: "Chỉ route llm_fallback mới gọi LLM answer." |
| Không có ticket TC2 | AI tự xử lý hoàn tiền | Chat: "Hoàn tiền → KHÔNG tự xử lý. Tạo ticket chuyển người." |
| Không có ticket/refusal TC4 | Guard không nối sang Human Gate | Chat: "route=refuse_or_ticket phải vào Human Gate, không vào LLM answer." |
| `nguoi_phu_trach` trống | AI quên | Chat: "Mỗi ticket phải có nguoi_phu_trach (vd 'Đội hoàn tiền')." |
| Confidence ngoài scope = cao | Judge over-confident | Chat: "Ngoài scope/injection = confidence thấp hoặc need_human=true." |

## Fast-forward
Stuck >12': import `checkpoints/tickets-sample.json`.

## Quy tắc
Mở khi HV stuck >8'. Nhấn: production bot tiết kiệm LLM bằng cache, và biết giới hạn bằng ticket.
