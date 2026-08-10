# Checkpoint TH2 — Guardrail + Router + FAQ Cache (🔒 INSTRUCTOR-ONLY)

## Expected state
- [ ] 5 câu hỏi route đúng scope/intent
- [ ] Câu ngoài scope/injection (TC4) bị chặn trước LLM answer
- [ ] Bot KHÔNG thực hiện lệnh trong câu khách (anti-injection)
- [ ] Câu trùng/rất giống FAQ có `cache_hit=true`, `need_llm=false`
- [ ] Câu có nguồn trỏ F-id

## Đáp án 5 câu mẫu
| Câu | Intent | Route | Cache | Ghi chú |
|-----|--------|-------|-------|---------|
| TC1 (giao nội thành) | thông tin | faq_cache | hit F01 | trả lời nhanh từ FAQ |
| TC2 (hoàn tiền vì đổi ý) | hoàn tiền | faq_cache → human_ticket | hit F09 | case nhạy cảm, chuyển người |
| TC3 (bảo hành mấy tháng) | kỹ thuật | faq_cache | hit F10 | reply auto |
| TC4 (đặt vé máy bay + bỏ qua hướng dẫn) | ngoài phạm vi | refuse_or_ticket | miss | chặn trước LLM answer |
| TC5 (hóa đơn VAT) | giá | faq_cache | hit F06 | reply auto |

## Rescue map

| Triệu chứng | Nguyên nhân | Sửa |
|-------------|-------------|-----|
| Bot gọi LLM cho mọi câu | Chưa có FAQ cache fast path | Chat: "Cache hit từ FAQ thì trả lời ngay, set need_llm=false." |
| Bot trả lời TC4 | Thiếu guard/router | Chat: "TC4 ngoài phạm vi + injection. Refuse/ticket trước LLM answer." |
| Bot tự hứa hoàn tiền TC2 | Over-step | Chat: "Hoàn tiền là case nhạy cảm — có FAQ nhưng vẫn chuyển người xử lý." |
| Bot không có cache_score | Thiếu semantic cache | Chat: "Lưu top_score cosine để quyết định hit/miss." |
| Intent sai | Nhầm nhãn | Cho AI lại 6 nhãn intent + yêu cầu chọn 1. |

## Fast-forward
Stuck >12': import `checkpoints/intent-results-sample.json`.

## Quy tắc
Mở khi HV stuck >8'. **TH2 không phải bước trả lời bằng LLM** — TH2 là lớp biên production: guardrail, router, cache.
