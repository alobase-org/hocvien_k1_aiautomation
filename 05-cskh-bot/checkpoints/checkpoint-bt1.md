# Checkpoint TH1 — Kho tri thức (🔒 INSTRUCTOR-ONLY)

## Expected state
- [ ] FAQ sheet ≥15 mục, 5 nhóm (xác nhận thanh toán/hoàn tiền/kỹ thuật/khiếu nại/liên hệ+thông tin)
- [ ] Mỗi mục: id (F01...) + nhom + cau_hoi + cau_tra_loi + nguon
- [ ] Không có mục nào "không có nguồn" (trừ gap cố ý)

## Rescue map

| Triệu chứng | Nguyên nhân | Sửa |
|-------------|-------------|-----|
| AI sinh <15 FAQ | Prompt không ép số | Chat: "Cần ≥15 FAQ, mỗi nhóm ≥3 mục. Bổ sung các nhóm còn thiếu." |
| Thiếu nhóm "khiếu nại" | AI quên nhóm nhạy cảm | Chat: "Bổ sung nhóm 'khiếu nại' — ít nhất 1 mục." |
| cau_tra_loi dài >60 từ | AI văn vẻ | Chat: "Mỗi câu trả lời ≤60 từ, có bước tiếp theo." |
| Không có cột nguon | AI bỏ qua nguồn | Chat: "Mỗi FAQ phải trỏ nguon (Mục X trong chính sách)." |
| AI bịa chính sách | Không có trong file | Chat: "Chỉ trả lời dựa file đính kèm. Không có → ghi 'chưa có nguồn'." |

## Fast-forward
Stuck >12': import `checkpoints/faq-khoa-hoc-full.json`. **Nhấn**: kho là gốc — bot giỏi tối đa bằng kho.

## Quy tắc
Mở khi HV stuck >8'. TA hỗ trợ trước.
