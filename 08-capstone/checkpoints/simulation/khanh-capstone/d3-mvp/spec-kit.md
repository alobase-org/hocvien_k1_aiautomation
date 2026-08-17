# Spec Kit — MVP CSKH Chat UI (Khánh)

## PRD rút gọn
- **Mục tiêu 1 câu:** Web app chat CSKH — khách gõ tin, bot trả lời ngay theo KB (đúng số liệu), khiếu nại tự chuyển "nhân viên", có log.
- **Phạm vi MVP:** (1) khung chat lịch sử 2 bên; (2) logic rule cứng local (classify + alias + bảng giá); (3) nút "Nhân viên duyệt gửi" (HITL mô phỏng); (4) log tải CSV được.
- **Ngoài phạm vi:** server thật, Zalo API, đăng nhập, nhiều phiên.

## User stories
1. Với tư cách khách, tôi muốn hỏi "còn không/bao nhiêu" và nhận câu đúng số ngay, không chờ nhân viên.
2. Với tư cách nhân viên, tôi muốn bot tự tách câu nào cần mình (khiếu nại), để chỉ xử lý phần đó.
3. Với tư cách chủ cửa hàng (Khánh), tôi muốn tải log cuối ngày, để biết khách hỏi gì nhiều nhất.

## Test scenarios
| # | Kịch bản | Bước | Kỳ vọng |
|---|----------|------|---------|
| 1 | Hỏi giá + tồn kho | Gõ "airbeat lite còn không, giá bao nhiêu" → Gửi | Bot: còn 18, giá 690.000đ |
| 2 | Hết hàng (DỮ LIỆU LẠI) | Gõ "sạc 65w có hàng không" | "hết hàng" + đề xuất đặt trước — KHÔNG nói còn |
| 3 | Khiếu nại | Gõ "magsnap hỏng rồi đổi đi" | Bot: xin lỗi + "đã chuyển kỹ thuật"; badge "CẦN NHÂN VIÊN" |
| 4 | Alias-bẫy (DỮ LIỆU LẠI) | Gõ "shop bán đồ gì" | KHÔNG match "op" trong "shop" → gợi ý 3 nhóm |
| 5 | Duyệt gửi (HITL) | Bấm "Nhân viên duyệt gửi" sau reply bất kỳ | Reply chuyển sang bong bóng "Đã gửi" |

## Ràng buộc kỹ thuật
1 file index.html, rule cứng JS (dùng lại logic D1), không API ngoài.

## MVP xong khi
5 scenario PASS + nút tải CSV hoạt động.
