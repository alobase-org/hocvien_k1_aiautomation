# Prompt 02 — Thiết kế kiến trúc Agent Skill

> Chuẩn bị: xong INPUT-CHECKLIST của lab 01. Dán các phần trong `[...]`.

---

Bạn là Workforce Architect. Thiết kế 1 agent skill đơn nhân viên cho use case dưới đây. Skill = 1 nhân viên số: có role rõ, input/output contract rõ, rule không negotiate, và test.

## Bối cảnh
Đồ án capstone: đóng gói use case thành skill chạy với agent. Tôi đã có brief + tài nguyên mượn từ các buổi trước (liệt kê ở dưới) — ưu tiên tái sử dụng chúng, chỉ tạo mới phần use case của tôi chưa có.

## Chỉ dẫn
1. Đọc brief. Xác định **phần nào của quy trình nên vào skill** (các bước lặp lại có quy tắc), phần nào giữ ngoài (cần người duyệt).
2. Thiết kế các thành phần:
   - `name` + `description` (description quyết định 90% độ chính xác trigger — phải nêu rõ use case nào thì gọi skill này)
   - Input contract: file/th định dạng agent nhận (tên file, schema hoặc dạng data)
   - Output contract: file agent trả, định dạng, tiêu chí đạt
   - 3–7 rules: bắt buộc có ≥1 rule "thiếu dữ liệu thì hỏi lại/kết thúc có cờ, không tự bịa"
   - Cấu trúc folder đề xuất: `SKILL.md` + `templates/` hoặc `kb/` + `test/`
3. Với từng tài nguyên mượn tôi liệt kê: ghi rõ mượn làm gì, sửa gì cho khớp use case tôi.
4. Đề xuất 1 test case nhỏ nhất chứng minh skill chạy đúng trên use case tôi.

## Tiêu chuẩn đầu ra
- 1 file `skill-design.md` có đủ các mục trên
- Mọi quyết định kèm 1 câu lý do
- Không thiết kế tool tự nhiên — chỉ dùng tool tôi có (agent + file + AI)

## Usecase brief

[DÁN usecase-brief.md]

## Tài nguyên mượn (từ resource map)

[DÁN các dòng resource map liên quan D1]
