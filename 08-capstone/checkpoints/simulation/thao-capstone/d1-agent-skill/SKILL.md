---
name: weekly-report-summarizer
description: >
  Sinh tóm tắt báo cáo kinh doanh tuần từ bảng số liệu hợp nhất: tổng doanh thu,
  tăng trưởng so tuần trước, top 3 sản phẩm, điểm bán cần chú ý. Số liệu CHỈ từ
  bảng input — AI chỉ viết câu chữ. Kích hoạt khi nhận "bảng doanh số tuần",
  "sinh tóm tắt báo cáo". KHÔNG dùng cho: dự báo, lập kế hoạch.
---

# Weekly Report Summarizer

## Input contract
- `input/weekly-summary.csv` (ngay,tong_doanh_thu,so_don) — đã hợp nhất từ 10 điểm
- `input/last-week.csv` (cùng cấu trúc) — để tính tăng trưởng
- `kb/rules.md` — ngưỡng cảnh báo

## Workflow
1. Kiểm 2 file đủ cột → thiếu trả THIEU_DU_LIEU.
2. (Cứng) Tính: tổng tuần này, tổng tuần trước, % tăng trưởng, top 3 sản phẩm (từ bảng chi tiết nếu có), điểm thấp nhất.
3. So ngưỡng KB: giảm >10% so tuần trước → CẢNH_BAO; điểm <50% trung bình → CẦN_CHÚ_Ý.
4. Sinh tóm tắt 5-7 câu (mọi con số PHẢI copy từ bước 2, không làm tròn tự ý).
5. Xuất JSON + email draft (chờ Thảo duyệt — HITL).

## Rules
- Con số chỉ lấy từ bảng — thiếu → trả THIEU_DU_LIEU, không ước lượng.
- % tăng trưởng = (tuần_nay - tuần_trước)/tuần_trước × 100, làm tròn 1 chữ số.
- Không khuyên hành động vượt dữ liệu (chỉ nêu "cần xem", không "nên sa thải"...).

## Cách test
`test/test-case.md` — 3 ca: tăng trưởng bình thường, giảm mạnh (cảnh báo), thiếu file tuần trước.
