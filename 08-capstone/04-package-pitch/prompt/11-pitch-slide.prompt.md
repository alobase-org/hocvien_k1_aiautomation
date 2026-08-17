# Prompt 11 — Sinh pitch slide HTML từ package

> Input: template `template/html-slide.template.html` + nội dung package của bạn.

---

Bạn là người kể chuyện dự án. Điền khung slide HTML dưới đây bằng nội dung THẬT từ package tôi mô tả.

## Bối cảnh
Đây là slide pitch đồ án capstone, người xem là giảng viên + lớp. Chuẩn tốt: cụ thể, có số liệu, có bằng chứng, không sáo rỗng. Màu/fonts giữ nguyên template (không sửa CSS).

## Chỉ dẫn
1. Đọc mô tả package (dán dưới đây): brief, resource map, kết quả D1/D2/D3, checklist, risk log.
2. Điền 6 slide theo chủ đề mỗi slide trong template:
   - S1 tên + 1 dòng mô tả · S2 bài toán (con số thật từ brief) · S3 giải pháp + bảng tài nguyên mượn (path thật) · S4 demo (ghi chú ảnh — tôi tự chèn ảnh vào `anh-demo/`) · S5 nghiệm thu (assert x/y, vòng run-log, vòng improve) · S6 kế hoạch.
3. Mọi con số phải trace về package — không phóng đại ("tự động 100%" chỉ ghi khi checklist có).
4. Giữ nguyên cấu trúc HTML/CSS/JS của template, chỉ thay nội dung text và src ảnh.
5. Output: toàn bộ file HTML hoàn chỉnh, sẵn sàng lưu thành `pitch.html`.

## Tiêu chuẩn đầu ra
- 6 slide, không còn chỗ `[ĐIỀN ...]`/`[TÊN ...]`
- ≥4 con số thật (tần suất, số assert, số vòng, số tài nguyên mượn)
- Câu dài nhất ≤25 từ
- Mở bằng trình duyệt là chạy (không phụ thuộc file ngoài trừ ảnh)

## Mô tả package của tôi

[DÁN: brief + resource-map + tóm tắt kết quả D1/D2/D3 + acceptance-checklist + risk-log]

## Template HTML

[DÁN nội dung template/html-slide.template.html]
