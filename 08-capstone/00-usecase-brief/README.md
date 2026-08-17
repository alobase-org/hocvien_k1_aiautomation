# Lab 00 — Usecase Brief (input gốc của toàn bộ đồ án)

## Mục tiêu
Biến mô tả use case tự nhiên của bạn thành **data contract chuẩn**: sau file này, mọi deliverable (D1–D4) đều nhận cùng một brief, không đổi giữa chừng.

## File input cần cung cấp
- `input/usecase-brief.template.md` — form điền (bản đầu của bạn chính là input)
- `input/resource-map.template.md` — bảng tài nguyên mượn từ B1–B7
- `input/risk-log.template.md` — dùng lại ở TH3

## Prompt để chạy

| Prompt | Input | Output |
|--------|-------|--------|
| `prompt/01-refine-usecase.prompt.md` | `usecase-brief.md` bản sơ bộ | `usecase-brief.md` bản chuẩn hóa |

## Các bước
1. Copy `usecase-brief.template.md` ra thư mục đồ án của bạn, điền sơ bộ bằng tay (15').
2. Dán nội dung vào prompt 01, chạy với AI, nhận lại bản chuẩn hóa — kiểm tra lại từng trường, AI bịa thì sửa.
3. Duyệt StudentKit, điền `resource-map.md` (tối thiểu 3 tài nguyên, path thật).

## Nghiệm thu
- [ ] Brief đủ 7 mục (6 mục [BẮT BUỘC] + mục Ràng buộc tùy chọn)
- [ ] ≥2 tiêu chí thành công đo được (có con số hoặc PASS/FAIL)
- [ ] Resource map ≥3 dòng, path tồn tại thật
- [ ] AI không bịa thông tin ngoài những gì bạn cung cấp (kiểm tra từng claim)

## Tài nguyên mượn
- Mẫu tiêu chí thành công đo được: `studentkit/04-contract-review/templates/checklist-rui-ro.md` (B4 — cách viết checklist rủi ro đếm được)
- Mẫu mô tả luồng nghiệp vụ input → output: `studentkit/06-content-engine/luong-nghiep-vu.md` (B6)
- Mẫu dữ liệu mô phỏng nếu use case cần dữ liệu nhạy cảm: `studentkit/06-content-engine/fallback-inputs/` (B6) và `studentkit/03-hr-screening/fallback-inputs/` (B3)
