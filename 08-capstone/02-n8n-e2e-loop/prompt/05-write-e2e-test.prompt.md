# Prompt 05 — Viết e2e test TRƯỚC khi sửa workflow

> Viết test xong mới được đụng vào workflow. Đây là toàn ý của vòng e2e-test-first.

---

Bạn là QA engineer viết e2e test cho workflow automation. Viết test cho use case dưới đây TRƯỚC khi workflow tồn tại ở bản customize.

## Bối cảnh
Tôi mượn 1 workflow n8n của buổi học trước làm khung, sẽ sửa cho use case của tôi. Test này là hợp đồng nghiệm thu: sửa tới khi PASS thì thôi. Test phải FAIL với workflow gốc (vì nghiệp vụ khác).

## Chỉ dẫn
1. Từ brief, xác định luồng e2e: input mẫu → trigger → các bước → artifact output.
2. Viết bộ input mẫu: ≥1 trường hợp vàng (đúng mọi thứ) + ≥1 trường hợp xấu (thiếu/garbage) — dùng dữ liệu của tôi, không bịa thêm trường mới ngoài brief.
3. Viết ≥3 assert theo bảng: assert | cách kiểm | PASS khi. Ưu tiên: (a) workflow chạy hết không lỗi, (b) artifact output tồn tại đúng tên, (c) nội dung đúng nghiệp vụ, (d) trường hợp xấu bị xử lý đúng (từ chối/cảnh báo, không crash).
4. Nêu rõ cách chạy test manual trong n8n (trigger bằng gì, xem execution ở đâu, kiểm artifact thế nào). Nếu chưa rõ 'schema' là gì: mở mẫu `04-contract-review/templates/clause.schema.json` — đó là bản hợp đồng kiểu dữ liệu cho file output (trường nào bắt buộc, kiểu gì); assert kiểu 'đúng schema' nghĩa là output thỏa hết các trường đó.
5. KHÔNG viết test cho tính năng không có trong brief.

## Tiêu chuẩn đầu ra
- File `e2e-test.md` theo đúng khung: Workflow dưới test / Bộ input mẫu / Asserts ≥3 / Kết quả
- Mỗi assert kiểm được bằng mắt trong UI n8n hoặc soi file
- Chỉ ra trước: với workflow mượn nguyên bản, assert nào chắc chắn FAIL (chứng minh test có răng)

## Usecase brief

[DÁN usecase-brief.md]

## Input mẫu có sẵn của tôi

[DÁN 2–3 input mẫu]
