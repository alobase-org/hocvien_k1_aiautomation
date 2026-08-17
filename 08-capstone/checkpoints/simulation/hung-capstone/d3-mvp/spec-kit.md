# Spec Kit — MVP Legal Review UI (Hùng)

## PRD rút gọn
- **Mục tiêu 1 câu:** Web app dán văn bản nhiều điều khoản → mỗi điều khoản hiện mức rủi ro + rule + đề xuất, có nút "Trưởng phòng duyệt phản hồi".
- **Phạm vi MVP:** 1 textarea · bấm Review · bảng điều khoản-mức-rule · duyệt từng dòng (HITL).
- **Ngoài phạm vi:** upload PDF, lưu database, gửi email thật.

## Test scenarios
| # | Kịch bản | Kỳ vọng |
|---|----------|---------|
| 1 | "Bên B thanh toán 100% trong 7 ngày không điều kiện" | CAO — A1 |
| 2 | "Phạt vi phạm 12%" | CAO — A2 |
| 3 | "Bảo hành 36 tháng" | TB — B1 |
| 4 | Dữ liệu lạ: "Hai bên phối hợp tốt đẹp" | KHONG_RO — không bịa |
| 5 | Duyệt phản hồi (HITL) | Dòng chuyển "ĐÃ DUYỆT" |
