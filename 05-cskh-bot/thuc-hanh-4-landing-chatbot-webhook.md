# Hướng dẫn Thực hành 4: Landing Page + Chatbot + n8n Webhook

> Buổi 05 — CSKH Bot dịch vụ bán lẻ · TH4/4 · Capstone · Time-box: 30 phút.

## Mục tiêu

Tạo một landing page bán lẻ đơn giản có chatbot widget chạy end-to-end với workflow n8n. Người dùng có thể mở trang, chat với bot, nhận reply/refusal/ticket và GV xem được route/cache status.

## Input

| Input | Mô tả |
|---|---|
| Workflow TH1-3 | Webhook `/cskh` đã có guardrail/router/cache/LLM/judge/ticket |
| n8n webhook URL | URL production/test của Webhook Node |
| Demo landing page | `test/landing-chatbot-demo.html` mở từ Notebook Step 6 |
| Test cases | `checkpoints/test-cases.json` |
| Prompt hỗ trợ | [`prompts/bt4-prompt.md`](./prompts/bt4-prompt.md) |

## Các bước thực hiện

1. Trước khi tự làm, mở Notebook Step 6 để xem `test/landing-chatbot-demo.html` chat trực tiếp với n8n webhook.
2. Vibe-code `landing-chatbot.html` chạy độc lập bằng HTML/CSS/JS.
3. Landing page cần có:
   - header/nav đơn giản,
   - brand "Retail Care Demo",
   - hero ngắn cho cửa hàng demo,
   - CTA "Chat với CSKH",
   - 3 thẻ lợi ích/dịch vụ,
   - khu vực chính sách tóm tắt.
4. Thêm chatbot widget:
   - nút mở/đóng hoặc panel cố định góc dưới phải,
   - lịch sử hội thoại,
   - input box + nút gửi,
   - loading state,
   - error state,
   - quick question chips.
5. Gắn webhook bằng biến:

```js
const N8N_WEBHOOK_URL = "https://[n8n].webhook.app/cskh";
```

6. Khi user gửi câu hỏi, gọi:

```js
fetch(N8N_WEBHOOK_URL, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    question: userInput,
    source_q_id: "LP-" + Date.now(),
    channel: "landing_page"
  })
})
```

7. Render kết quả:
   - `reply.ticket` → hiển thị "CSKH sẽ liên hệ (ticket #id)",
   - `reply.route="refuse_or_ticket"` → hiển thị refusal an toàn,
   - `reply.answer` → hiển thị answer + nguồn,
   - luôn hiển thị badge `FAQ cache`, `LLM fallback`, `Ticket`, hoặc `Refusal`.
8. Gửi 5 test case qua chatbot trên landing page.
9. Ghi conversation log gồm `khach_hoi`, `intent`, `route`, `cache_hit`, `bot_tra_loi`, `chuyen_nguoi?`, `co_nguon?`, `source_q_id`.
10. Lập FAQ gap list cho các câu bot chưa trả lời được.

## Output

- `landing-chatbot.html` chạy được khi mở browser.
- Landing page nhìn như một trang bán lẻ demo, không chỉ là form chat trống.
- Chatbot gọi webhook thật và hiển thị reply/refusal/ticket.
- Conversation log đủ 5 test case.
- FAQ gap list.

## SLI/SLO nghiệm thu

- [ ] `landing-chatbot.html` mở được trong browser và có bố cục landing page bán lẻ rõ ràng.
- [ ] Chatbot trên landing page gửi câu hỏi tới webhook và nhận reply/ticket end-to-end.
- [ ] UI hiển thị loading/error state khi webhook chậm hoặc lỗi.
- [ ] Log đủ 5 test case.
- [ ] Bot chuyển đúng 2 case, gồm 1 ngoài scope.
- [ ] Không bịa khi không có nguồn.

## Safety

- Node gửi email/ticket thật phải để test mode trong lab.
- Production phải được GV duyệt trước khi bật gửi thật.
- Không hiển thị thông tin nhạy cảm trong UI demo.

## Fallback

Stuck >10 phút: mở `checkpoints/cskh-bot-agent-solution.md`, `checkpoints/conversation-log-sample.xlsx` và `checkpoints/checkpoint-bt4.md`.
