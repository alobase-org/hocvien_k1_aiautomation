# Prompt TH4 — Vibe-coding landing page + chatbot + n8n webhook (capstone)

> Tư duy mới: **Vibe coding + n8n webhook** — đưa bot vào một landing page có thể chat thật. TH 4/4.
> Input: workflow TH1-3 + vibe coding. Output: landing page có chatbot live + conversation log 5 case.

## Vibe-code landing page có chatbot → call n8n webhook

```
BỐI CẢNH:
HV vibe-code 1 landing page bán lẻ đơn giản có chatbot widget. Chatbot POST câu hỏi
tới n8n webhook URL (TH2) → nhận reply/refusal/ticket, route và cache status → hiển thị cho user.

CHỈ DẪN (vibe coding — Cursor/Antigravity sinh code):
1. Sinh file `landing-chatbot.html` chạy độc lập bằng HTML/CSS/JS.
2. Landing page cần có:
   - Header/nav đơn giản: brand "Retail Care Demo", link Chính sách, Bảo hành, Liên hệ.
   - Hero ngắn: tiêu đề cửa hàng demo + CTA "Chat với CSKH".
   - 3 thẻ nội dung: Giao nhanh, Đổi trả 7 ngày, Bảo hành 12 tháng.
   - Khu vực chính sách tóm tắt để user hiểu bot hỗ trợ gì.
3. Chatbot widget:
   - Nút mở/đóng hoặc panel cố định góc dưới phải.
   - Lịch sử hội thoại user/bot.
   - Input box + nút Gửi.
   - Loading state "Đang hỏi CSKH..." khi chờ webhook.
   - Error state nếu webhook timeout/lỗi.
   - Quick question chips: "Đơn nội thành bao lâu giao?", "Có xuất hóa đơn VAT không?", "Sản phẩm bảo hành mấy tháng?"
4. JS fetch POST tới webhook URL:
   const N8N_WEBHOOK_URL = "https://[n8n].webhook.app/cskh";
   fetch(N8N_WEBHOOK_URL, {
     method:"POST", headers:{"Content-Type":"application/json"},
     body: JSON.stringify({
       question: userInput,
       source_q_id: "LP-" + Date.now(),
       channel: "landing_page"
     })
   }).then(r=>r.json()).then(showReply)
5. Hiển thị:
   - nếu reply.ticket → "CSKH sẽ liên hệ (ticket #id)"
   - nếu reply.route="refuse_or_ticket" → hiển thị refusal an toàn
   - nếu reply.answer → answer + nguồn + badge nhỏ "FAQ cache" hoặc "LLM fallback"
   - luôn hiển thị badge route/cache_hit để GV kiểm tra pipeline.

TIÊU CHUẨN ĐẦU RA:
- `landing-chatbot.html` chạy được khi mở browser.
- Landing page nhìn được như một trang bán lẻ demo, không chỉ là form chat trống.
- End-to-end: gõ câu trên chatbot → webhook → reply/refusal/ticket hiển thị.
- Conversation log 5 test case: khach_hoi | intent | route | cache_hit | bot_tra_loi | chuyen_nguoi? | co_nguon? | source_q_id.
- FAQ gap list (câu bot không trả lời được).
```

**SLI/SLO**: landing page + chatbot live; 5 test case qua chatbot; 2 chuyển người (1 ngoài scope); không bịa.

**Safety/HITL**: node gửi email/ticket thật → test mode TẮT. Production → GV duyệt.
**Tool upgrade (BR-07)**: B4 n8n → B5 n8n + vibe coding landing page có chatbot + webhook (thêm API layer, KHÔNG hạ cấp).
