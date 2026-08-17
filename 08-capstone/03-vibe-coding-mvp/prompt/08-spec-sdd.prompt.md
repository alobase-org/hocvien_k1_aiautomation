# Prompt 08 — Sinh bộ đặc tả SDD cho MVP (prompt 3 phần: Bối cảnh / Chỉ dẫn / Tiêu chuẩn đầu ra)

---

## Bối cảnh
Tôi đang xây MVP web app cho use case dưới đây bằng vibe coding. Triết lý SDD: đặc tả chuẩn trước — AI sinh code theo đặc tả. MVP chỉ cần chạy được luồng chính: input → xử lý → output, 1 người dùng, không đăng nhập, không database.

## Chỉ dẫn
1. Đọc use case brief. Trích: người dùng chính, input, output, quy tắc cứng, bước cần AI phán đoán.
2. Sinh `spec-kit.md` theo đúng khung:
   - **PRD rút gọn:** mục tiêu 1 câu; phạm vi MVP 2–4 tính năng; ngoài phạm vi (liệt kê thứ bỏ rơi để MVP nhỏ).
   - **User stories ≥3:** format "Với tư cách X, tôi muốn Y, để Z" — bám người dùng thật trong brief.
   - **Test scenarios ≥3:** kịch bản kiểm bằng tay trên app, mỗi cái có bước + kỳ vọng thấy gì.
   - **Ràng buộc kỹ thuật:** web app 1 trang, chạy preview/local.
3. Mọi nội dung phải trace về brief — không bịa tính năng không có trong brief (muốn thêm thì ghi riêng mục "Đề xuất sau MVP").
4. Kết thúc bằng checklist: "MVP xong khi ..." (3–5 điều đếm được).

## Tiêu chuẩn đầu ra
- 1 file spec-kit.md hoàn chỉnh theo khung trên
- User stories dùng đúng người dùng của brief
- Test scenarios kiểm được bằng tay (bấm/nhập/soi)
- Không vượt phạm vi MVP

## Usecase brief

[DÁN usecase-brief.md]
