---
name: cskh-reply-drafter
description: >
  Soạn câu trả lời CSKH cửa hàng điện thoại từ tin nhắn khách: phân loại (HOI_GIA/
  HOI_TON_KHO/HOI_BAO_HANH/KHIEU_NAI/KHAC), nhận diện sản phẩm qua alias, tra bảng
  kb/products.json lấy số LIỆU THẬT, soạn trả lời đúng tone, khiếu nại thì tạo ticket
  chuyển người. Kích hoạt khi nhận "tin nhắn khách", "soạn trả lời CSKH", "phân loại
  tin hỗ trợ". KHÔNG dùng cho: đặt hàng, thu tiền, hứa bảo hành ngoài chính sách.
---

# CSKH Reply Drafter

## Mục tiêu
1 tin nhắn khách → 1 JSON {loai, san_pham, du_lieu_tra, reply_draft, can_chuyen_nguoi} — reply soạn sẵn chờ nhân viên duyệt.

## Input contract
- `input/message.md` — nguyên văn tin khách
- `kb/products.json` — bảng giá/tồn kho/bảo hành (số liệu NGUỒN SỰ THẬT)
- `kb/chinh-sach.md` — chính sách + tone + quy tắc escalation

## Workflow
1. Phân loại theo 5 loại trên (mơ hồ → KHAC).
2. Nhận diện sản phẩm: match alias trong products.json. Không match → `san_pham: null`.
3. Tra bảng: giá/stock/warranty_months — **CHỈ dùng số trong products.json, cấm bịa**.
4. KHIEU_NAI: dừng soạn giải pháp — tạo ticket {ly_do, muc: CAO/TRUNG} + câu xin lỗi chuẩn, `can_chuyen_nguoi: true`.
5. Soạn reply theo tone kb/chinh-sach.md (thân thiện, ≤3 câu, có số liệu kèm nguồn).
6. Xuất JSON + 1 dòng log CSV.

## Output contract
- `output/reply-draft.json` — đủ trường; mọi con số có `nguon: "products.json#<id>"`
- KHIEU_NAI mà reply tự hứa đổi/trả = SAI quy tắc (chỉ xin lỗi + chuyển)

## Rules
- Số liệu không có trong bảng → trả "em kiểm tra lại giúp mình" + flag THIEU_DU_LIEU — không đoán.
- Ton kho = 0 → trung thực "hết hàng", đề xuất đặt trước, không nói "còn nhiều".
- KHIEU_NAI luôn con người xử — bot không hứa thời gian hay kết quả.
- Tin quen mặt (KHAC) → gợi ý 3 câu hỏi thường gặp, không bịa câu trả lời.

## Cách test
`test/test-case.md` — 4 tin mẫu phủ 4 loại + 1 tin số liệu thiếu.
