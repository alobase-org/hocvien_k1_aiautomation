# Improve Log — CSKH Chat UI (Khánh)

## Vòng 1 — 21/08 (syntax đứt đúng kiểu app chết câm)
- Test thấy: mở app bấm "Nhân viên duyệt gửi" → không có gì xảy ra; Console F12 đỏ: chuỗi literal bị đứt ở hàm duyetGui (tôi gõ nhầm ngoặc).
- Yêu cầu sửa (1 chỗ): viết lại đúng cú pháp hàm.
- Kết quả: đã sửa — cả 5 nút hoạt động.

## Vòng 2 — 21/08 (logic alias-bẫy — cùng bug D1)
- Test thấy: "shop bán đồ gì" match nhầm "op" trong "shop" (T4 FAIL) — do copy logic từ D1 bản chưa fix.
- Yêu cầu sửa: áp dụng bản fix D1 (alias dài trước + word-boundary cho alias <5 ký tự).
- Kết quả: đã sửa — T4 PASS, 5/5 PASS.

## Phần chưa runtime-test
- Chưa test trên điện thoại; chưa test gõ liên tiếp 40 tin (chỉ 5); badge "ĐÃ DUYỆT" chưa test double-click.
