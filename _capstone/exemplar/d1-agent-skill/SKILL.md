---
name: leave-request-processor
description: >
  Xử lý đơn xin nghỉ phép: trích thông tin đơn từ tin nhắn tự nhiên, đối chiếu chính sách
  nghỉ phép, đề xuất duyệt/từ chối kèm lý do. Kích hoạt khi nhận đơn nghỉ phép cần xử lý,
  khi được hỏi "xử lý đơn nghỉ", "check leave request". KHÔNG dùng cho: chấm công,
  tính lương, quản lý dự án.
---

# Leave Request Processor

## Mục tiêu
Biến 1 tin nhắn xin nghỉ phép thành 1 đề xuất duyệt có bằng chứng: JSON thông tin đơn + đối chiếu chính sách + kiến nghị + lý do.

## Input contract
- File `input/leave-request.md` — nội dung nguyên văn đơn (text tự nhiên)
- File `kb/leave-policy.md` — chính sách nghỉ phép (quy tắc cứng, dạng checklist)

## Workflow
1. Đọc đơn + chính sách.
2. Trích JSON: `{ho_ten, loai_phep: annual|sick|unpaid, tu_ngay, den_ngay, so_ngay, ly_do, nguoi_ban_giao}`. Thiếu trường → dừng, trả `{trang_thai: "THIEU_DU_LIEU", thieu: [...]}`.
3. Đối chiếu từng quy tắc trong chính sách → bảng: quy tắc | kết quả | dẫn chứng (trích câu nguyên văn trong đơn).
4. Kiểm tra bàn giao: `nguoi_ban_giao` có giá trị không → flag `BAN_GIAO_THIEU` nếu trống.
5. Kiến nghị: `DE_XUAT_DUYET` / `DE_XUAT_TU_CHOI` / `CAN_BO_SUNG` — kèm 1 câu lý do dựa trên bảng đối chiếu.

## Output contract
- File `output/leave-review.json` — đúng schema trên, mọi kiến nghị có `ly_do` + `dan_chung`
- KHÔNG tự duyệt thay người — output luôn là đề xuất

## Rules
- Thiếu dữ liệu input → trả THIEU_DU_LIEU, không đoán bậy (đoán sai đơn nghỉ = hậu quả thật).
- Mỗi kết luận phải trích được câu chữ từ đơn hoặc điều khoản chính sách — không dẫn chứng thì ghi `[không có dẫn chứng]`.
- Chỉ áp dụng quy tắc có trong `kb/leave-policy.md` — không tự nghĩ thêm chính sách.

## Cách test
- `test/test-case.md`: 2 đơn mẫu (đủ điều kiện / vi phạm báo trước) + output expected + tiêu chí PASS/FAIL
