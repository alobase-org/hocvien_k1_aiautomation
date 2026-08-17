---
name: warranty-request-processor
description: >
  Xử lý yêu cầu bảo hành thiết bị gia dụng: trích thông tin từ tin nhắn/email
  khách, đối chiếu chính sách bảo hành 12 tháng, phân loại lỗi (máy/người dùng/
  thiếu thông tin), đề xuất nhận-từ chối-bổ sung kèm lý do. Kích hoạt khi nhận
  yêu cầu bảo hành cần xử lý, khi được hỏi "xử lý bảo hành", "check warranty".
  KHÔNG dùng cho: đặt lịch sửa, tính phí sửa ngoài bảo hành, khiếu nại.
---

# Warranty Request Processor

## Mục tiêu
Biến 1 tin nhắn yêu cầu bảo hành thành 1 đề xuất xử lý có dẫn chứng: JSON thông tin + đối chiếu chính sách + kiến nghị + lý do. Kỹ thuật duyệt lịch, không tự hẹn.

## Input contract
- `input/warranty-request.md` — nguyên văn tin nhắn/email khách
- `kb/warranty-policy.md` — chính sách bảo hành (checklist quy tắc cứng)
- Ngày xử lý (lấy ngày hiện tại) để tính thời hạn 12 tháng

## Workflow
1. Đọc tin nhắn + chính sách.
2. Trích JSON: `{ho_ten, sdt, loai_may, serial, ngay_mua, su_co, mo_ta_loi}`. Thiếu trường → trả `{trang_thai:"THIEU_DU_LIEU", thieu:[...]}`, không đoán.
3. Phân loại sự cố theo `kb/warranty-policy.md`: `LOI_MAY` / `LOI_NGUOI_DUNG` / `KHONG_RO`.
4. Tính thời hạn: `ngay_mua + 12 tháng` so với ngày xử lý → `CON` / `HET` / `KHONG_RO` (ngày mua chỉ ghi "tháng 3" → KHONG_RO, yêu cầu bổ sung).
5. Kiến nghị:
   - `NHAN_BAO_HANH` khi CON + LOI_MAY
   - `TU_CHOI` khi HET hoặc LOI_NGUOI_DUNG (nêu điều khoản + dẫn chứng câu chữ khách)
   - `CAN_BO_SUNG` khi KHONG_RO hoặc THIEU_DU_LIEU
6. Viết `output/warranty-review.json` + 1 câu trả lời khách soạn sẵn (chờ kỹ thuật duyệt gửi).

## Output contract
- `output/warranty-review.json` — đủ các trường trên, mọi kiến nghị có `ly_do` + `dan_chung` (trích câu chữ tin nhắn hoặc điều khoản)
- KHÔNG tự gửi trả lời khách — output là đề xuất cho người duyệt

## Rules
- Thiếu serial HOẶC ngày mua → không đoán "chắc còn bảo hành" (đoán sai = hẹn khách rồi từ chối, mất uy tín).
- "Ngày mua" chỉ có tháng không có ngày → tính tới cuối tháng đó, ghi chú `dao_dong_31_ngay`.
- Chỉ dùng quy tắc trong `kb/warranty-policy.md` — không tự nghĩ thêm chính sách.
- SĐT phải 10-11 số mới coi là hợp lệ, sai format → đưa vào `thieu`.

## Cách test
- `test/test-case.md`: 3 tin nhắn mẫu (còn bảo hành / hết / thiếu thông tin) + expected + tiêu chí PASS/FAIL
