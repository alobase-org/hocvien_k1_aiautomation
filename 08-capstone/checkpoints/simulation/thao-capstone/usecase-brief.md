# Usecase Brief — Báo cáo tổng hợp kinh doanh tuần tự động (Thảo)

> Học viên: Vũ Minh Thảo · quản lý kinh doanh công ty phân phối 10 điểm bán (mô phỏng) · Buổi 8 TH1

## [BẮT BUỘC] Bài toán
Mỗi sáng thứ 2, Thảo manually thu 10 file doanh số CSV từ 10 điểm bán, hợp nhất, tính tăng trưởng tuần, top sản phẩm, viết email tóm tắt cho giám đốc. Mất 3 giờ mỗi tuần.

## [BẮT BUỘC] Người dùng
Thảo tổng hợp. Giám đốc đọc. Cấp dưới đối chiếu số.

## [BẮT BUỘC] Input hàng ngày
Mỗi tuần 10 file CSV (mã điểm, ngày, sản phẩm, số lượng, doanh thu). Định dạng hơi khác nhau giữa các điểm.

## [BẮT BUỘC] Output mong muốn
Báo cáo 1 trang: tổng doanh thu tuần, tăng trưởng so với tuần trước, top 3 sản phẩm, điểm bán thấp nhất cần chú ý. Gửi email tự động.

## [BẮT BUỘC] Quy trình xử lý (tách theo loại bước)
1. (Cứng) Chuẩn hóa 10 file CSV (cột khác nhau).
2. (Cứng) Hợp nhất + tính tổng, tăng trưởng, ranking.
3. (AI phán đoán) Sinh tóm tắt hành động ("điểm A giảm 20% cần xem").
4. (Người duyệt) Thảo duyệt email trước khi gửi (HITL).

## [BẮT BUỘC] Tiêu chí thành công (đo được)
- 100% số liệu từ file gốc (không AI bịa con số)
- Báo cáo sinh ≤5 phút từ khi có file cuối
- Giảm từ 3 giờ xuống <30 phút mỗi tuần

## Ràng buộc & công cụ sẵn có
Dữ liệu mô phỏng theo fallback-inputs B6. Có n8n (docker), Claude, AI Studio. Không gửi email thật trong MVP — sinh email draft.
