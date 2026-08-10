# Checkpoint TH4 — Đóng gói: n8n + app duyệt (GV/TA)

> TH nặng nhất buổi, 30 phút cho hai prompt. Chạy chậm thì cắt Q&A, đừng cắt TH4.

## Nhịp 30 phút

| Phút | Việc |
|------|------|
| 0–18 | **bt4a** — agent dựng workflow n8n 4 lớp, in ra 2 webhook URL |
| 18–30 | **bt4b** — agent dựng app duyệt, dán 2 URL, bấm duyệt, mở Sheets kiểm |

Mốc chặn: **phút 18 chưa có webhook URL thì cấp workflow solution ngay**, đừng để học viên mất luôn phần app — app mới là sản phẩm của buổi.

---

## Phần A — bt4a (backend n8n)

### Expected state

- [ ] Agent đã đọc 3 artifact và xác nhận `brief_id` khớp, schema PASS.
- [ ] Workflow có 4 vùng, mỗi vùng một sticky note tiếng Việt.
- [ ] Lớp 3 có node gọi API sinh ảnh, dùng chính trường `image_prompt` của TH3.
- [ ] Có webhook `/b6/approve` riêng, ghi Content_Queue + Publish_Log.
- [ ] Status mặc định `Needs Review`. **Không có** trạng thái `Published`, không có node đăng bài.
- [ ] Cả hai webhook bật CORS `Allowed Origins = *`.
- [ ] Workflow Inactive, đã validate, đã export JSON.
- [ ] Đã in ra 2 webhook URL production.

### Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Agent dựng workflow mà chưa đọc artifact | `Đọc content-angles.json, content-draft.json, content-assets.json trước. Xác nhận ba brief_id khớp rồi mới cấu hình node.` |
| App báo lỗi CORS | `Mở cả hai node Webhook, Options, đặt Allowed Origins = *, Save rồi Activate lại.` |
| n8n nhận request nhưng field rỗng | `Dữ liệu webhook nằm ở $json.body.xxx, không phải $json.xxx. Sửa mọi expression.` |
| Lỗi 404 khi gọi webhook | `URL production không có /webhook-test/. Activate workflow rồi copy lại URL.` |
| Node Sheets không thấy cột | Tên cột phải khớp `content-workbook.xlsx`: `Post ID`, `Angle ID`, `Kênh`, `Nội dung`, `Status`, `Người duyệt`, `Ghi chú`. |
| Sheets báo lỗi quyền | Nối lại credential Google Sheets, chọn đúng account đã dùng ở B1. |
| Node ảnh trả lỗi | `Kiểm credential của node sinh ảnh. Nếu không gọi được, tạm trả về một URL ảnh giữ chỗ để lớp 4 vẫn chạy, và ghi rõ phần này chưa runtime-test.` |
| Agent viết API key vào workflow | `Bỏ key khỏi workflow JSON. Dùng credential đã có trên n8n.` |
| Agent nói đã chạy được nhưng mới validate | `Bạn mới validate cấu trúc. Nói rõ phần nào đã chạy thật, phần nào chưa.` |
| Quá phút 18 | Cấp `checkpoints/n8n-content-engine-solution.json` để import, học viên chỉ gắn credential và activate. |

---

## Phần B — bt4b (app duyệt)

### Expected state

- [ ] Một file `index.html`, không thư viện ngoài, mở trực tiếp là chạy.
- [ ] Hai ô nhập webhook URL, không hardcode.
- [ ] Hiện được: ảnh, image brief, bài Fanpage, kịch bản TikTok 4 dòng, 5 seeding.
- [ ] Bài Fanpage và cột hình ảnh / lời thoại sửa trực tiếp được.
- [ ] Có cảnh báo `[cần bổ sung]`, từ cấm, cột hình ảnh trống — **chỉ cảnh báo, không chặn**.
- [ ] Nút Approved và Needs Review, bắt buộc điền người duyệt.
- [ ] **Không có nút đăng bài.**
- [ ] Trong file không có API key nào.
- [ ] Bấm duyệt → nhận Log ID → mở Google Sheets thấy một dòng Publish_Log.

### Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| App đẹp nhưng không gọi được webhook | `Kiểm CORS ở n8n trước. Sau đó mở Console trình duyệt đọc lỗi thật rồi sửa.` |
| Agent nhét API key vào app để gọi thẳng AI | `Bỏ mọi API key khỏi app. Mọi thứ đi qua webhook n8n.` |
| Agent thêm nút đăng bài | `Bỏ nút đăng. Trạng thái cao nhất app này ghi được là Approved.` |
| Cảnh báo tự sửa nội dung | `Chỉ cảnh báo, không tự sửa và không chặn nút duyệt. Quyết định thuộc người duyệt.` |
| Không sửa được nội dung trên màn hình | `Cho bài Fanpage và cột hình ảnh, lời thoại sửa trực tiếp bằng contenteditable, blur thì lưu lại.` |
| Ảnh không hiện | `Kiểm URL ảnh workflow trả về. Nếu rỗng, hiện ô giữ chỗ kèm dòng "chưa có ảnh" thay vì để trống.` |
| Agent nói xong nhưng chưa gọi webhook lần nào | `Chạy thử một lần: bấm Cần sửa, cho tôi biết Log ID nhận về.` |
| Quá giờ | Cấp `checkpoints/app-duyet-solution.html`, học viên chỉ dán 2 URL của mình. |

---

## Nghiệm thu cuối buổi

Chạy engine trên chính brief Sunrise Kids, từ đầu tới cuối:

1. Workflow sinh nội dung và ảnh mới.
2. App hiện bài, ảnh, seeding.
3. Bấm **Approved**.
4. Mở Google Sheets: `Content_Queue` có dòng Status `Approved`, `Publish_Log` có một dòng kèm ngày và người duyệt.

Học viên phải nói được: ba artifact chứng minh logic đúng, workflow đóng gói logic đó để chạy lại trên brief mới, app là chỗ người thật ra quyết định.

## Câu chốt cho GV

> Nội dung thì AI viết trong ba phút. Cái mất ba mươi phút vừa rồi là dựng chỗ cho một người thật ngồi xuống, nhìn bài, nhìn ảnh, rồi chịu trách nhiệm bấm nút. Đó là khác biệt giữa một mẻ nội dung và một cỗ máy giao được cho đội marketing.

## ⚠️ Trước khi lên lớp

`n8n-content-engine-solution.json` **chưa validate trên instance thật**. Bắt buộc chạy một lần:
mở Claude Code tại `D:\GiangXAI\Agentic Workflow\n8n Mastery`, import, `n8n_validate_workflow`, chạy thử end-to-end. Kiểm riêng node sinh ảnh và hai node Webhook.
