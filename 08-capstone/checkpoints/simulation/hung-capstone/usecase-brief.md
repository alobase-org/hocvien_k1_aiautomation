# Usecase Brief — Trợ lý Review Văn Bản Luật (Hùng)

> Học viên: Trần Quốc Hùng · pháp chế công ty xây dựng 200 người (mô phỏng) · Buổi 8 TH1

## [BẮT BUỘC] Bài toán
Công ty nhận ~15 hợp đồng/văn bản pháp lý/tháng từ nhà thầu, nhà cung cấp. Hùng review từng điều khoản theo checklist rủi ro nội bộ, ghi nhận điều khoản nguy hiểm, soyt phản hồi. Mỗi hợp đồng mất 2-3 giờ, hay bỏ sót điều khoản lạ.

## [BẮT BUỘC] Người dùng
Hùng review chính. Trưởng phòng pháp chế duyệt phản hồi (HITL). Bên đối tác nhận phản hồi.

## [BẮT BUỘC] Input hàng ngày
Văn bản PDF/DOCX ~15/tháng, 10-30 điều khoản, đa dạng loại (hợp đồng xây dựng, thuê thiết bị, NDA...).

## [BẮT BUỘC] Output mong muốn
`legal-review.json` (điều khoản | mức rủi ro | dẫn chứng | đề xuất phản hồi) + email draft phản hồi đối tác.

## [BẮT BUỘC] Quy trình xử lý (tách theo loại bước)
1. (Cứng) Trích điều khoản (đánh số).
2. (AI phán đoán) Đối chiếu từng điều khoản với checklist rủi ro (KB nội bộ).
3. (Cứng) Phân loại rủi ro (CAO/TB/THẤP theo rule).
4. (Người duyệt) Trưởng phòng duyệt phản hồi (HITL).

## [BẮT BUỘC] Tiêu chí thành công (đo được)
- 100% điều khoản được review (không bỏ sót)
- 10/10 điều khoản nguy hiểm test bị bắt đúng
- Thời gian review giảm từ 2-3h xuống <1h

## Ràng buộc & công cụ sẵn có
Dữ liệu văn bản mô phỏng. Có n8n (docker), Claude, AI Studio. Không đưa dữ liệu thật lên AI công cộng (ràng buộc bảo mật).
