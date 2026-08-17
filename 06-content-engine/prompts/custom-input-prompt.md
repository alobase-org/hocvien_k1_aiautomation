# Prompt mở rộng — Đổi sang sản phẩm của bạn

> Dùng **sau khi** đã hoàn thành TH4. Coding Agent phải đọc workflow và app hiện tại trước khi sửa.
> Trong lớp bạn chạy engine trên trung tâm tiếng Anh. Về nhà, đổi nó sang việc thật của bạn.

## Trước khi bắt đầu

Chuẩn bị ba thứ, mỗi thứ một file trong workspace. Đây là phần **bạn phải tự viết** — AI không biết doanh nghiệp bạn.

| File | Nội dung | Mẹo |
|---|---|---|
| `product-brief.md` | Sản phẩm, cách vận hành, điều khách hay nói, điều bạn KHÔNG làm | Chỗ nào chưa có số liệu thì ghi thẳng là chưa có, đừng bịa cho đủ |
| `chan-dung.md` | 2–3 nhóm khách, mỗi nhóm một mã (KH1, KH2…), nêu họ đang nghĩ gì và sợ gì | Không có mã rõ ràng thì AI sẽ tự bịa ra nhóm khách |
| `brand-voice.md` | Giọng nói, và **danh sách cấm** | Phần cấm quan trọng hơn phần giọng |

Mục "điều bạn KHÔNG làm" và danh sách cấm là hai thứ giữ cho nội dung không trôi thành quảng cáo suông. Đừng bỏ qua.

---

## Prompt 1 — Đổi nguyên liệu

```text
BỐI CẢNH:
Tôi đã có Content Engine chạy được: workflow n8n bốn lớp và một app duyệt.
Engine đang chạy với brief của một trung tâm tiếng Anh. Giờ đổi sang sản phẩm của tôi.

INPUT:
- product-brief.md, chan-dung.md, brand-voice.md — nguyên liệu mới của tôi.
- Workflow n8n hiện tại và file app duyệt.

CHỈ DẪN:
1. Đọc workflow hiện tại từ n8n trước khi sửa. Không tạo bản trùng lặp.
2. Chỉ thay phần nguyên liệu trong hằng số NGUYEN_LIEU của app và các biến đầu vào của lớp 1.
   GIỮ NGUYÊN cấu trúc bốn lớp và ba schema.
3. Trong app, sửa tiêu đề trang và các câu gợi ý cho hợp sản phẩm mới.
4. Giữ nguyên luật: không bịa số liệu, thiếu thì ghi [cần bổ sung], không cam kết kết quả,
   không nêu tên đối thủ.
5. Cập nhật danh sách từ cấm trong app cho đúng ngành của tôi.
6. Chạy thử một lần và cho tôi biết: ý tưởng có nhắm đúng mã chân dung mới của tôi không,
   và bài viết có bịa số nào không.

TIÊU CHUẨN BÀN GIAO:
- Danh sách chỗ đã sửa.
- Xác nhận ba schema không đổi.
- Kết quả một lần chạy thật.
```

Phần lớn trường hợp **chỉ cần prompt này**. Cấu trúc engine không phụ thuộc vào ngành.

---

## Prompt 2 — Đổi kênh đăng

```text
Engine đang viết cho Fanpage và kịch bản TikTok. Tôi muốn đổi thành [ĐIỀN: LinkedIn / Blog SEO /
Zalo OA / Email / Instagram].

CHỈ DẪN:
1. Đọc schemas/content-draft.schema.json trước. Thêm kênh mới vào schema, giữ nguyên các trường cũ.
2. Sửa prompt lớp 2 trong workflow: nêu rõ format của kênh mới — độ dài, cấu trúc, cách mở đầu,
   kiểu CTA.
3. Sửa app duyệt để hiện kênh mới, cho sửa trực tiếp như hai kênh cũ.
4. Nếu bỏ hẳn một kênh cũ thì xóa cả trong schema, prompt và app — đừng để trường mồ côi.

TIÊU CHUẨN BÀN GIAO:
- Schema mới.
- Một bài mẫu của kênh mới.
- Xác nhận app hiện đủ các kênh.
```

Một kênh mới cần ba chỗ sửa đồng bộ: **schema, prompt lớp 2, và app**. Sửa thiếu một chỗ là engine gãy — chính vì vậy schema đáng để đọc trước.

---

## Prompt 3 — Chạy nhiều brief một lượt

```text
Tôi muốn chạy engine cho nhiều sản phẩm cùng lúc thay vì từng cái một.

CHỈ DẪN:
1. Đọc workflow hiện tại. Chỉ thay vùng đầu vào, giữ nguyên bốn lớp nghiệp vụ.
2. Đọc danh sách brief từ [ĐIỀN: Google Sheets / thư mục file / form]. Mỗi brief là một item n8n riêng,
   có brief_id riêng.
3. Content_Queue phải ghi mỗi sản phẩm một dòng, phân biệt được bằng brief_id.
4. Thêm sticky note tiếng Việt ở vùng đầu vào để sau này biết chỗ nào custom được.
5. Chú ý chi phí: mỗi brief tốn ba lần gọi AI cộng một lần sinh ảnh. Cho tôi biết ước tính
   trước khi chạy hàng loạt.

TIÊU CHUẨN BÀN GIAO:
- Danh sách node thêm/sửa.
- Ba test case: một brief đủ thông tin, một brief thiếu thông tin, ba brief cùng lúc.
- Xác nhận các lớp nghiệp vụ không bị thay đổi.
```

---

## Prompt 4 — Sửa app duyệt theo ý bạn

```text
Trong app duyệt, [ĐIỀN yêu cầu]. Chỉ sửa đúng phần đó, không đụng phần gọi webhook và phần cảnh báo.
```

Vài yêu cầu hay dùng:

- *Thêm nút "Tải về .txt" để lưu bài và kịch bản ra file.*
- *Thêm ô ghi lý do bắt buộc khi bấm "Cần sửa", để người viết biết phải sửa gì.*
- *Cho phép duyệt riêng phần chữ và phần ảnh, hai trạng thái tách nhau.*
- *Đổi màu chủ đạo sang màu thương hiệu của tôi.*
- *Thêm cảnh báo nếu bài không nhắc tới tên sản phẩm lần nào.*

---

## Ba chỗ đừng đụng

| Chỗ | Vì sao |
|---|---|
| Ba JSON Schema | Chúng là hợp đồng giữa Coding Agent, n8n và app. Sửa một bên thì ba bên phải sửa theo |
| Status dừng ở `Approved` | Cố ý không có `Published`. Muốn đăng thật thì đó là một workflow riêng, có kiểm soát riêng |
| Luật không bịa số liệu | Đây là thứ giữ cho engine dùng được thật. Bỏ nó đi thì bạn có một cỗ máy sản xuất rủi ro |

## Khi agent sửa hỏng

```
Hoàn tác thay đổi vừa rồi. Đọc lại workflow và app ở trạng thái trước đó rồi báo tôi.
```

Với n8n, mở workflow → menu ba chấm → **Workflow history** để quay lại phiên bản cũ.
Với app, giữ một bản `index-backup.html` trước mỗi lần sửa lớn.
