# Risk Log — Khánh

| # | Rủi ro | Mức | Cách giảm | Trạng thái |
|---|--------|-----|-----------|------------|
| 1 | AI phân loại sai → số sai | Cao | Số liệu vòng cứng bảng local; AI chỉ soạn câu; HITL duyệt | Đã giảm |
| 2 | Key Gemini express burst-quota (đã dính thật 17/08) | Cao | Tự retry ×3 + giãn cách; runtime vòng 4 chạy lại sáng mai | Đang giảm |
| 3 | Alias-bẫy ("op" trong "shop") | Trung | Đã fix word-boundary + test riêng T4 | Đã giảm |
| 4 | Respond trả Gemini response thay JSON (dính thật vòng 3) | Cao | Đã cắt đường B4, AI → Respond trực tiếp (v4) — chờ runtime xác nhận | Đang giảm |
