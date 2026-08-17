# Improve Log — Legal Review UI (Hùng)

## Vòng 1 — 21/08 (regex A2 viết sai lần đầu)
- Test thấy: "Phạt vi phạm 12%" không match — regex đầu tiên tôi viết `/phạt vi phạm\s*1[0-9]%/` sót case 20%+ và không bắt "12%" (thiếu nhánh).
- Yêu cầu sửa (1 chỗ): viết lại regex có nhánh 2-chữ-số `(1[0-9]|[2-9]\d)%` + danh sách tường minh.
- Kết quả: đã sửa — 5/5 PASS.

## Phần chưa runtime-test
- Chưa test văn bản 30 điều khoản; tách câu theo "." có thể cắt nhầm câu chứa số thập phân; chưa test PDF thật.
