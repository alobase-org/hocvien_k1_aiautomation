---
name: room-booking-processor
description: >
  Xử lý yêu cầu đặt phòng họp: trích thông tin (phòng, ngày, khung giờ, số người,
  thiết bị) từ tin nhắn tự nhiên, đối chiếu lịch phòng và quy tắc (sức chứa, giờ
  cho phép), phát hiện trùng lịch, đề xuất xác nhận/từ chối/đề xuất khung khác.
  Kích hoạt khi nhận "yêu cầu đặt phòng họp", "check phòng trống", "booking".
  KHÔNG dùng cho: mượn thiết bị rời, họp online, catering.
---

# Room Booking Processor

## Mục tiêu
Biến 1 tin nhắn đặt phòng họp thành 1 đề xuất xử lý: xác nhận (không trùng, hợp quy tắc) / từ chối (trùng hoặc vi phạm) / đề xuất khung khác (tin mơ hồ).

## Input contract
- `input/booking-request.md` — nguyên văn tin nhắn
- `kb/booking-rules.md` — quy tắc phòng + lịch hiện có (dạng bảng khung giờ)
- File lịch: `kb/room-schedule.md` (cập nhật tuần)

## Workflow
1. Đọc tin + rules + lịch. Thiếu trường → `{trang_thai:"THIEU_DU_LIEU", thieu:[...]}`, không đoán.
2. Trích JSON: `{nguoi_dat, phong, ngay, khung_gio, so_nguoi, thiet_bi}`.
3. (Cứng) Check trùng: khung giờ đã có trong `room-schedule.md` chưa.
4. (Cứng) Check quy tắc: sức chứa phòng, khung giờ cho phép (7:30–17:30), thiết bị có sẵn.
5. (AI phán đoán) Tin ghi "buổi sáng/sáng sớm" → đề xuất khung cụ thể còn trống.
6. Kiến nghị: `XAC_NHAN` / `TU_CHOI` (nêu điều khoản + dòng lịch trùng) / `DE_XUAT_KHUNG_KHAC` (liệt kê 2 khung trống gần nhất).
7. Soạn câu trả lời người đặt (chờ Nam duyệt — HITL).

## Output contract
- `output/booking-review.json` — đủ trường trên, mọi kiến nghị có `ly_do` + `dan_chung` (trích dòng lịch hoặc điều khoản)
- `output/reply-draft.md` — câu trả lời soạn sẵn

## Rules
- Trùng lịch phải trích nguyên dòng lịch bị trùng (người đặt có quyền biết đụng với ai).
- "Buổi sáng" KHÔNG tự chọn 7:30 — đề xuất 2 khung, để người đặt chọn (chọn hộ dễ sai ý).
- Sức chứa: phòng 12 người không nhận nhóm 15 — từ chối thẳng, không đề "ghép ghế".
- Thiếu ngày/khung giờ → THIEU_DU_LIEU.

## Cách test
`test/test-case.md`: 3 tin mẫu (xác nhận / trùng lịch / mơ hồ buổi sáng).
