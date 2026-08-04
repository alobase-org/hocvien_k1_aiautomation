# Hướng dẫn Thực hành 3: LLM Fallback + LLM-as-Judge + HITL Ticket

> Buổi 05 — CSKH Bot dịch vụ bán lẻ · TH3/4 · Time-box: 15 phút.
> Output của bài này là input cho Thực hành 4.

## Mục tiêu

Chỉ dùng LLM khi FAQ cache không hit, sau đó dùng LLM thứ hai làm cổng kiểm soát trước khi bot tự trả lời hoặc tạo ticket.

## Input

| Input | Mô tả |
|---|---|
| Output TH2 | `route`, `cache_hit`, `need_llm`, `need_human`, `intent`, `top3_faq_ids` |
| `templates/chinh-sach-ho-tro.md` | Chính sách bán lẻ để LLM bám nguồn |
| Test cases | `checkpoints/test-cases.json` |
| Prompt hỗ trợ | [`prompts/bt3-prompt.md`](./prompts/bt3-prompt.md) |

## Các bước thực hiện

1. Nhận các case `cache_hit=false` hoặc `need_human=true` từ TH2.
2. Thêm IF Node `Need LLM?`.
3. AI Node answer chỉ chạy khi `need_llm=true` và `cache_hit=false`.
4. LLM answer dùng top-3 FAQ + `chinh-sach-ho-tro.md`, trả lời ngắn, bắt buộc gắn nguồn.
5. Thêm AI Node judge, dùng LLM thứ hai khác node answer.
6. Judge nhận `question`, `answer`, `intent`, `nguon`, `cache_hit`, `route`.
7. Judge trả JSON `{ confidence: 0-1, reason: "...", need_human: true/false }`.
8. IF Node `Human Gate` tạo ticket nếu:
   - `confidence < 0.7`,
   - hoặc intent thuộc `khieu_nai`, `hoan_tien`, `ngoai_pham_vi`,
   - hoặc `nguon="khong_co"`/`"không có"`.
9. Ghi ticket vào Sheets/ticket log với `source_q_id`, `intent`, `confidence`, `reason`, `nguoi_phu_trach`.
10. Test TC2 hoàn tiền và TC4 ngoài scope phải tạo ticket.

## Output

Ticket mẫu:

```json
{
  "ticket_id": "T01",
  "source_q_id": "TC2",
  "intent": "hoan_tien",
  "confidence": 0.82,
  "reason": "Có nguồn FAQ F09 nhưng hoàn tiền là case nhạy cảm cần CSKH cấp 2 xem xét.",
  "nguoi_phu_trach": "Đội hoàn tiền"
}
```

## SLI/SLO nghiệm thu

- [ ] Có đúng 2 case chuyển người: TC2 hoàn tiền + TC4 ngoài scope.
- [ ] Trong 2 case chuyển người, chỉ 1 case là ngoài scope.
- [ ] Confidence luôn có reason, không chỉ là con số.
- [ ] LLM answer chỉ chạy khi `cache_hit=false`.
- [ ] Bot không tự xử lý hoàn tiền/khiếu nại.

## Safety

- LLM answer không được tự hứa hoàn tiền, đổi trả hoặc bồi thường.
- LLM-as-Judge không trả lời khách; chỉ chấm confidence và lý do.
- Ticket là ranh giới an toàn cho case nhạy cảm.

## Fallback

Stuck >8 phút: dùng `checkpoints/tickets-sample.json` và mở `checkpoints/checkpoint-bt3.md`.
