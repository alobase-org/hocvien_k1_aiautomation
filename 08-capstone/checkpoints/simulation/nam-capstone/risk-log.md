# Risk Log — Nam

| # | Rủi ro | Mức | Cách giảm | Trạng thái |
|---|--------|-----|-----------|------------|
| 1 | Đổi tên node n8n làm đứt connection (đã dính thật vòng 1) | Cao | Sau khi đổi tên: chạy auto-check [3] trước khi làm tiếp | Đã giảm |
| 2 | n8n cần node ≥20, máy tôi node 18 — runtime chưa test được | Cao | Khai rõ + nhờ GV runtime-check; tuần tới nâng node | Đang giảm |
| 3 | Lịch pre-fill cứng 1 tuần, không phải lịch thật | Trung | MVP giới hạn 1 tuần, ghi ngoài phạm vi | Đã ghi |
| 4 | Chat fallback không nhớ rule giữa các lần test skill | Trung | Dán lại kb mỗi lần (lab 01 ghi chú) | Đã giảm |
