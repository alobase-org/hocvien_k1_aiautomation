# Hướng dẫn Thực hành 1: Auto-Config n8n + Vector Knowledge DB

> Buổi 05 — CSKH Bot dịch vụ bán lẻ · TH1/4 · Time-box: 15 phút.
> Output của bài này là input cho Thực hành 2.

## Mục tiêu

Tự động khởi chạy n8n, import workflow solution vào n8n local qua Notebook, sau đó quan sát cách 15 FAQ bán lẻ được chuẩn bị thành vector store để bot tìm câu trả lời theo ý nghĩa câu hỏi, không chỉ theo keyword.

## Input

| Input | Mô tả |
|---|---|
| `test/05_cskh_bot_lab_demo.ipynb` | Notebook demo tự động import workflow và gửi test case |
| `checkpoints/n8n-cskh-bot-solution.json` | Workflow solution để auto-import vào n8n |
| `templates/faq-khoa-hoc.json` | 15 FAQ bán lẻ, có `id`, `nhom`, `cau_hoi`, `cau_tra_loi`, `nguon` |
| Embedding credential | Google AI Studio/OpenAI credential từ B2 |
| Prompt hỗ trợ | [`prompts/bt1-prompt.md`](./prompts/bt1-prompt.md) |

## Các bước thực hiện

1. Mở `test/05_cskh_bot_lab_demo.ipynb`.
2. Chạy **Step 0** để tự động khởi chạy n8n và import `checkpoints/n8n-cskh-bot-solution.json`.
3. Mở `http://localhost:5678`, kiểm tra workflow **B5 K1 - Retail CSKH Bot (Guard + Cache + Landing Chatbot)** đã có sẵn.
4. Chạy **Step 1** trong notebook để inspect các node workflow từ n8n API.
5. Load `templates/faq-khoa-hoc.json` vào n8n hoặc notebook.
6. Dùng HTTP Request Node gọi Embedding API cho từng FAQ.
7. Text đưa vào embedding nên ghép `cau_hoi + " " + cau_tra_loi`.
8. Dùng Code Node gom kết quả thành `vector-store.json`.
9. Mỗi object trong vector store cần có `faq_id`, `nhom`, `cau_hoi`, `cau_tra_loi`, `nguon`, `vector`.
10. Kiểm tra đủ 15 vector và FAQ về "phí giao hàng" có vector.

## Output

`vector-store.json` gồm 15 object:

```json
{
  "faq_id": "F03",
  "nhom": "đơn hàng",
  "cau_hoi": "Có phí giao hàng không?",
  "cau_tra_loi": "Miễn phí giao hàng cho đơn từ 500.000 VNĐ trong nội thành...",
  "nguon": "Mục 1. Giao nhận",
  "vector": [0.012, -0.03]
}
```

## SLI/SLO nghiệm thu

- [ ] Có đúng 15 vector.
- [ ] Mỗi FAQ có đúng 1 vector.
- [ ] Mỗi vector gắn đúng `faq_id`, `nhom`, `nguon`.
- [ ] Notebook Step 0-1 chạy được và workflow đã import vào n8n local.
- [ ] Output TH1 dùng được làm input cho TH2.

## Safety

FAQ là dữ liệu synthetic cho lab. Không đưa PII thật, số điện thoại thật, mã đơn thật hoặc thông tin khách thật vào knowledge DB.

## Fallback

Stuck >8 phút: chạy `python3 test/auto_import_n8n.py`, dùng `checkpoints/faq-khoa-hoc-full.json` và mở `checkpoints/checkpoint-bt1.md`.
