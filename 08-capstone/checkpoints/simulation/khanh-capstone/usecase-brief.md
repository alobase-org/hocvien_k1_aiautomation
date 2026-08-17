# Usecase Brief — Trợ lý CSKH cửa hàng điện thoại (Khánh)

> Học viên: Lê Minh Khánh · chủ cửa hàng điện thoại 2 mặt bằng + 3 nhân viên (mô phỏng) · Buổi 8 TH1

## [BẮT BUỘC] Bài toán
Khách nhắn Zalo OA + fanpage + chat web (~40 tin/ngày): hỏi giá, còn hàng không, bảo hành bao lâu, khiếu nại. Nhân viên trả lời rải rác trong giờ, tối và CN không ai trả → mất khách. Khiếu nại hay rơi vào tranh cãi vì không ai nhớ đúng chính sách.

## [BẮT BUỘC] Người dùng
Khách hàng hỏi. Bot trả lời câu thường (giá/tồn kho/bảo hành/FAQ). Nhân viên duyệt + nhận chuyển khiếu nại (HITL). Khánh xem log tuần.

## [BẮT BUỘC] Input hàng ngày
Tin nhắn tự nhiên: "airbeat lite còn không shop", "bảo hành máy giặt à nhầm tai nghe bao lâu", "tôi mua tuần trước hỏng rồi đổi đi". ~40 tin/ngày, đa ngôn ngữ nói lái, gõ tắt.

## [BẮT BUỘC] Output mong muốn
Trả lời khách ≤30 giây cho câu thường (đúng giá/tồn kho theo bảng, đúng chính sách bảo hành); khiếu nại → tạo ticket chuyển nhân viên + câu xin lỗi chuẩn; mọi tin vào `cskh-log.csv` (giờ, loại, sản phẩm, trả lời/ chuyển).

## [BẮT BUỘC] Quy trình xử lý (tách theo loại bước)
1. (AI phán đoán) Phân loại tin: HOI_GIA / HOI_TON_KHO / HOI_BAO_HANH / KHIEU_NAI / KHAC.
2. (Cứng) Nhận diện sản phẩm (alias) → tra bảng products: giá, tồn kho, bảo hành.
3. (Cứng) Khiếu nại → KHÔNG tự xử: tạo ticket + chuyển nhân viên.
4. (Người duyệt) Câu trả lời do bot soạn theo tone chuẩn + chính sách — nhân viên bấm duyệt gửi (HITL).
5. (Cứng) Ghi log 1 dòng/tin.

## [BẮT BUỘC] Tiêu chí thành công (đo được)
- 100% tin thường có câu trả lời soạn sẵn ≤30 giây + dòng log
- Đúng giá/tồn kho 10/10 tin test (không bịa số)
- Khiếu nại 10/10 được chuyển người, không bot tự hứa

## Ràng buộc & công cụ sẵn có
Dùng bảng sản phẩm + chính sách mô phỏng (mượn B5). Có n8n (docker), Claude, AI Studio. Ngân sách 0. Không trả lời thay nhân viên khi khiếu nại.
