# Prompt TH4b — Vibe-code app duyệt nội dung

> Chạy ngay sau bt4a, trong cùng phiên chat. Cần hai webhook URL mà bt4a vừa in ra.
> Đây là sản phẩm cuối buổi.

```text
BỐI CẢNH:
Backend đã xong ở bước trước: workflow n8n sinh nội dung và ảnh, đẩy vào Google Sheets với
Status "Needs Review", và có một webhook /b6/approve nhận quyết định duyệt.
Giờ dựng phần người thật nhìn vào: một màn duyệt để người phụ trách xem bài, xem ảnh,
rồi quyết định cho đăng hay trả về sửa.

INPUT PHẢI ĐỌC TRƯỚC KHI XÂY:
- content-draft.json từ TH2 — biết bài Fanpage và kịch bản TikTok có cấu trúc gì.
- content-assets.json từ TH3 — biết seeding và image brief có cấu trúc gì.
- schemas/content-draft.schema.json và schemas/content-assets.schema.json — hợp đồng dữ liệu.
- templates/brand-voice.md — danh sách 8 điều cấm, dùng làm checklist duyệt.
- Hai webhook URL từ bt4a.

YÊU CẦU THỰC HIỆN:
1. Tạo một file index.html duy nhất, HTML/CSS/JS thuần, không build step, không thư viện ngoài.
   Mở trực tiếp bằng trình duyệt là chạy.
2. Đầu file có khu cấu hình gấp lại được, chứa hai ô nhập webhook URL. Không hardcode URL vào code.
3. Màn hình chia hai cột trên máy tính, xếp dọc trên điện thoại:
   - Cột trái: ẢNH do workflow sinh ra, hiển thị đúng tỷ lệ trong image_brief.
     Dưới ảnh là image brief đủ 9 mục dạng bảng.
   - Cột phải: bài Fanpage, kịch bản TikTok dạng bảng 4 dòng, và 5 comment seeding.
4. Bài Fanpage và cột Hình ảnh, Lời thoại của kịch bản TikTok phải sửa trực tiếp được trên màn hình.
   Người duyệt hay sửa vài chữ trước khi đồng ý — đừng bắt họ quay lại chat.
5. Hiển thị số từ của bài Fanpage, tô đỏ nếu ngoài khoảng 120-200 từ.
6. Quét nội dung và cảnh báo trước khi duyệt. Chỉ cảnh báo, KHÔNG tự sửa và KHÔNG chặn:
   - Còn chuỗi [cần bổ sung] trong bài.
   - Có từ thuộc nhóm cấm trong brand-voice.md: cam kết kết quả, hù dọa, câu tuyệt đối
     kiểu "tốt nhất" / "số 1" / "duy nhất", quá 2 emoji.
   - Cột Hình ảnh của kịch bản TikTok có ô nào để trống — buổi sau cần nó để dựng video.
7. Khu quyết định gồm: ô nhập tên người duyệt (bắt buộc), ô ghi chú,
   nút "Duyệt — Approved" và nút "Cần sửa — Needs Review".
   Bấm nút thì POST về webhook /b6/approve kèm post_id, status, người duyệt, ghi chú và nội dung
   đã sửa. Nhận kết quả xong hiển thị Log ID trả về để người dùng biết đã ghi sổ thật.
8. KHÔNG tạo nút đăng bài, không gọi API mạng xã hội nào. Trạng thái cao nhất app này ghi được
   là Approved. Ghi rõ điều đó trên giao diện.
9. App KHÔNG được chứa API key của Gemini, Google hay bất kỳ dịch vụ nào. Mọi thứ đi qua webhook n8n.
10. Toàn bộ chữ trên giao diện bằng tiếng Việt. Màu chủ đạo navy #1B3A6B, cảnh báo đỏ #E74C3C,
    xác nhận xanh #1e8e5a, font Calibri.
11. Nạp dữ liệu để thử: cho phép chọn file JSON từ máy, và tự điền sẵn nội dung từ
    content-draft.json + content-assets.json đang có trong workspace để mở ra là thấy ngay,
    không phải nhập gì.
12. Lưu nội dung đang sửa vào localStorage để F5 không mất bài.

TIÊU CHUẨN BÀN GIAO:
- Đường dẫn file index.html.
- Danh sách các cảnh báo đã cài ở mục 6.
- Xác nhận trong file không có chuỗi nào trông giống API key.
- Một lần chạy thử: mở app, nạp dữ liệu, bấm Cần sửa, cho biết Log ID nhận về là gì.
- Nêu rõ phần nào chưa thử được và vì sao.

QUY TẮC BẢO TOÀN:
- Không sửa ba artifact JSON của TH1-TH3.
- Không sửa workflow n8n đã dựng ở bt4a.
- Không tuyên bố app chạy được nếu mới chỉ mở lên xem giao diện mà chưa gọi được webhook.
```

**Chaining line:** Đây là sản phẩm cuối. Nghiệm thu bằng cách chạy trên brief holdout do giảng viên phát: workflow sinh nội dung mới → app hiện bài và ảnh mới → bấm Approved → mở Google Sheets thấy một dòng Publish_Log.

**HITL:** App chỉ ghi trạng thái. Không có đường nào từ app ra thẳng mạng xã hội — cố ý.
