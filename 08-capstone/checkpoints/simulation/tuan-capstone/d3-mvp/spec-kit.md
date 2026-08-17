# Spec Kit — MVP Leave Request Helper (exemplar)

## PRD rút gọn
- **Mục tiêu 1 câu:** Web app để trưởng nhóm dán 1 đơn nghỉ phép và nhận đề xuất duyệt/từ chối kèm lý do theo chính sách.
- **Phạm vi MVP:** (1) textarea dán đơn; (2) nút "Xử lý" gọi rule + AI; (3) kết quả: JSON trích + bảng đối chiếu + kiến nghị; (4) nút copy kết quả vào log.
- **Ngoài phạm vi:** đăng nhập, lưu database, gửi Zalo, tính dư phép.

## User stories
1. Với tư cách trưởng nhóm, tôi muốn dán đơn nghỉ và thấy ngay đề nghị duyệt/từ chối kèm lý do, để trả lời nhân viên trong vài phút.
2. Với tư cách trưởng nhóm, tôi muốn thấy trường nào của đơn thiếu (người bàn giao...), để hỏi bổ sung đúng chỗ.
3. Với tư cách trưởng nhóm, tôi muốn copy 1 dòng log cho mỗi đơn, để giữ sổ phép không phải ghi tay.

## Test scenarios
| # | Kịch bản | Bước | Kỳ vọng |
|---|----------|------|---------|
| 1 | Đơn hợp lệ | Dán đơn #1 → Xử lý | Thấy DE_XUAT_DUYET + lý do + bảng xanh |
| 2 | Đơn vi phạm | Dán đơn #2 → Xử lý | Thấy DE_XUAT_TU_CHOI + 2 lỗi vi phạm |
| 3 | Đơn rác | Dán đoạn văn không phải đơn → Xử lý | Thấy THIEU_DU_LIEU + danh sách trường thiếu |

## Ràng buộc
Web app 1 trang (AI Studio Build), rule cứng check trong code, phần phán đoán bàn giao gọi AI.

## MVP xong khi
- 3 scenario trên chạy đúng tay
- Copy log ra dòng CSV đúng format
- ≤3s cho 1 đơn
