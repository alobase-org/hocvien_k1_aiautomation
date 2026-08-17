# Lab 04 — Deliverable D4: Package + Pitch slide HTML

## Mục tiêu
Đóng gói cả đồ án (brief + D1 + D2 + D3 + checklist + risk log) thành **1 package chuẩn** kèm **slide pitch HTML** mở được trong trình duyệt — đây là sản phẩm nộp để chấm.

## File input cần cung cấp
- `input/INPUT-CHECKLIST.md`
- `input/acceptance-checklist.template.md` — tự chấm trước khi nộp (dùng từ buổi 8 TH3)
- `input/package-structure.md` — cấu trúc thư mục nộp chuẩn
- `template/html-slide.template.html` — khung slide HTML (6 slide)
- 3 deliverable D1–D3 đã xong

## Prompt để chạy

| Prompt | Input | Output |
|--------|-------|--------|
| `prompt/10-package.prompt.md` | cấu trúc package + các artifact | Package kiểm tra đủ + checklist tick |
| `prompt/11-pitch-slide.prompt.md` | package + template HTML | `pitch.html` hoàn chỉnh |

## Các bước
1. Theo `package-structure.md`, gom artifact vào đúng chỗ; thiếu gì quay lại lab tương ứng làm nốt.
2. Tự chấm bằng `acceptance-checklist.md` — tick thật, chưa đạt thì làm nốt, không tự bịa tick.
3. Copy `template/html-slide.template.html`, chạy prompt 11 để AI điền nội dung slide từ package của bạn.
4. Mở `pitch.html` bằng trình duyệt, bấm qua từng slide, sửa tay chỗ gật gù.
5. Nộp cả package (zip) theo hướng dẫn cuối file này.

## Nghiệm thu (đếm được)
- [ ] Package đủ 100% cấu trúc trong `package-structure.md`
- [ ] `acceptance-checklist.md` tick xong, mọi dòng ⏳ đã xử lý hoặc ghi lý do trong risk-log
- [ ] `pitch.html` mở được, đủ 6 slide, không còn chỗ `[ĐIỀN ...]`
- [ ] Slide có ảnh chụp demo thật (D2 execution pane / D3 app / D4 output)
- [ ] Risk-log có ≥3 rủi ro + cách giảm

## Cách nộp (deadline 2026-08-25 23:59)
1. Zip thư mục `ho-ten-capstone/` thành `ho-ten-capstone.zip`.
2. Nộp qua link Drive GV công bố trong nhóm Zalo lớp (đặt quyền xem), đúng format tên: `capstone_[ho-ten]_[ten-use-case-slug].zip`.
3. Nộp muộn: mỗi ngày trễ trừ 1 mức trên criterion "Package đủ cấu trúc"; sau 27/08 23:59 không nhận nữa (trừ trường hợp báo trước có lý do, GV duyệt từng case).
4. Lưu ý: use case trùng exemplar "nghỉ phép" của GV thì PHẢI thay input + chính sách thật của đơn vị mình, nếu không criterion tái sử dụng bị xem là copy.

## Tài nguyên mượn
- Nội dung slide bám khung pitch exemplar của GV: `_capstone/exemplar/pitch.html` (trong studentkit — GV chia sau khi demo buổi 8)
- Cách viết tiêu chí đếm được: `04-contract-review/templates/checklist-rui-ro.md` (B4)
