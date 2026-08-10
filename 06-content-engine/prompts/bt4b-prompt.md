# Prompt TH4b — Vibe-code app duyệt nội dung

> Chạy ngay sau bt4a, trong cùng phiên chat. Cần ba webhook URL mà bt4a vừa in ra.
> Đây là sản phẩm cuối buổi.

```text
BỐI CẢNH:
Backend đã xong ở bước trước: workflow n8n có BA webhook — `/b6/angles` (chỉ sinh 5 ý tưởng,
rẻ và nhanh), `/b6/generate` (viết đầy đủ bài+kịch bản+seeding+ảnh từ MỘT ý tưởng đã chọn),
và `/b6/approve` (nhận quyết định duyệt). Content đẩy vào Google Sheets với Status "Needs Review".
Giờ dựng phần người thật nhìn vào — không chỉ màn duyệt cuối, mà cả bước chọn ý tưởng TRƯỚC
khi cam kết viết đầy đủ (tránh chờ mù rồi mới biết AI viết về gì, tốn phí ảnh cho ý tưởng
không ai muốn).

INPUT PHẢI ĐỌC TRƯỚC KHI XÂY:
- content-draft.json từ TH2 — biết bài Fanpage và kịch bản TikTok có cấu trúc gì.
- content-assets.json từ TH3 — biết seeding và image brief có cấu trúc gì.
- schemas/content-draft.schema.json và schemas/content-assets.schema.json — hợp đồng dữ liệu.
- templates/brand-voice.md — danh sách 8 điều cấm, dùng làm checklist duyệt.
- BA webhook URL từ bt4a.

YÊU CẦU THỰC HIỆN:
1. Tạo một file index.html duy nhất, HTML/CSS/JS thuần, không build step, không thư viện ngoài.
   Mở trực tiếp bằng trình duyệt là chạy.
2. Đầu file có khu cấu hình gấp lại được, chứa BA ô nhập webhook URL. Không hardcode URL vào code.
2b. Trước màn duyệt, thêm một bước chọn ý tưởng:
   - Nút "Sinh ý tưởng" gọi `/b6/angles`, hiện 5 thẻ ý tưởng (angle_id, ý tưởng, chân dung,
     mục tiêu, kênh phù hợp) để người đọc rồi bấm chọn 1.
   - Nút "Tự đưa ý tưởng" cho người gõ tay ý tưởng riêng (chọn chân dung + mục tiêu qua
     dropdown), bỏ qua bước AI sinh ý tưởng hoàn toàn.
   - Sau khi có ý tưởng đã chọn (từ 1 trong 2 đường), mới hiện nút "Viết nội dung đầy đủ"
     gọi `/b6/generate` kèm nguyên object ý tưởng đã chọn trong body (field `angle`).
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
