# Bộ thực hành Buổi 06 — Content Engine

## Cách học

Không phát workflow hay app hoàn chỉnh ở đầu buổi. Học viên chạy bốn prompt trong cùng phiên Coding Agent:

1. TH1 tạo `content-angles.json` — ý tưởng bài viết, mỗi ý nhắm đúng một chân dung.
2. TH2 đọc TH1 và tạo `content-draft.json` — bài Fanpage và kịch bản TikTok.
3. TH3 đọc TH2 và tạo `content-assets.json` — comment seeding, image brief và prompt ảnh.
4. TH4 dùng ba artifact đã kiểm chứng để Coding Agent xây workflow n8n (bt4a) rồi dựng app duyệt (bt4b).

## Vì sao ba JSON là tiền đề của workflow

- Chúng chứng minh logic từng lớp chạy đúng **trước khi** tự động hóa.
- Chúng định nghĩa schema để Coding Agent biết cấu hình node, và app biết render cái gì.
- Chúng là expected output để test workflow.
- Chúng khoanh vùng lỗi: ý tưởng lệch chân dung là lớp 1, bài sai giọng là lớp 2, seeding khen rỗng là lớp 3.

## File học viên dùng

- `templates/product-brief-sunrise-kids.md` — brief synthetic. **Cố tình thiếu** học phí, ưu đãi, ngày khai giảng.
- `templates/chan-dung-khach-hang.md` — ba chân dung phụ huynh, có mã PH1/PH2/PH3.
- `templates/brand-voice.md` — giọng và 8 điều cấm.
- `templates/channel-format-spec.md` — spec Fanpage và kịch bản TikTok.
- `templates/content-workbook.xlsx` — workbook Google Sheets làm sổ cái.
- `schemas/*.schema.json` — hợp đồng dữ liệu cho TH1–TH3.
- `prompts/bt1` → `bt4b` — chuỗi prompt liên kết.
- `prompts/custom-input-prompt.md` — dùng sau buổi, đổi engine sang sản phẩm của mình.

## File giảng viên / checkpoint

- `fallback-inputs/content-angles-bt1-sample-output.json` — fallback TH1. Để ngoài `checkpoints/` vì là đầu vào hợp lệ.
- `checkpoints/content-draft-sample.json`, `content-assets-sample.json` — fallback TH2, TH3.
- `checkpoints/checkpoint-bt1..bt4.md` — expected state và rescue map.
- `checkpoints/n8n-content-engine-solution.json` — **solution/fallback của TH4a, không phải starter.**
- `checkpoints/app-duyet-solution.html` — solution của TH4b.
- `checkpoints/content-workbook-demo.xlsx` — bản đã điền, dùng khi demo 15 phút.

## Nghiệm thu

```bash
python giao_trinh/scripts/validate-b6-artifacts.py <thư-mục-của-học-viên>
```

Kiểm ba tầng và trả exit code 0/1:

1. **Schema** — cấu trúc và số đếm.
2. **Kế thừa** — `brief_id` và `source_angle_id` có khớp qua ba lớp không.
3. **Văn phong** — số từ, thời lượng, emoji, từ cấm, số liệu bịa, chất lượng seeding, ràng buộc ảnh.

Mốc văn phong **cố ý không nằm trong schema**: đưa "bài phải 120–200 từ" vào schema sẽ biến một bài viết hay thành lỗi parse. Riêng `so_tu` luôn được đếm lại độc lập vì agent hay khai sai con số này.

## Sản phẩm cuối

Một app duyệt nội dung: hiện bài Fanpage, kịch bản TikTok, ảnh và comment seeding; người phụ trách bấm Approved hoặc Needs Review; trạng thái ghi xuống Google Sheets qua n8n.

Trạng thái cao nhất là **Approved**. Không có nút đăng bài — cố ý.

## Nối sang Buổi 7

Kịch bản TikTok trong `content-draft.json` là input của Buổi 7 (Tạo video AI). Cột `hinh_anh` phải ghi đủ để người khác dựng được video — đừng để trống.
