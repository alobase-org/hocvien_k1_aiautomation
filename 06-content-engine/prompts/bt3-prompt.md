# Prompt TH3 — Comment seeding + image brief + prompt ảnh

> Chạy trong cùng phiên chat sau TH2.

```text
BỐI CẢNH:
Đây là LỚP 3 của Content Engine. Bài đăng đã có ở lớp 2.
Giờ tạo phần đi kèm: comment seeding để bài có hội thoại, và brief ảnh để bài có hình.
Trường image_prompt sẽ được workflow n8n dùng để sinh ảnh thật ở lớp 4 — viết cho máy đọc.

INPUT:
- content-draft.json từ TH2 — đọc file này, seeding phải bám đúng bài đã viết.
- templates/brand-voice.md
- templates/product-brief-sunrise-kids.md — chỉ để tra dữ kiện.
- schemas/content-assets.schema.json

CHỈ DẪN:
1. Đọc content-draft.json. Giữ nguyên brief_id và source_angle_id — không tự sinh mã mới.
2. Viết đúng 5 comment seeding cho bài Fanpage đó:
   - Không câu nào là lời khen doanh nghiệp. Seeding là người đọc thật đang bàn, không phải
     người của thương hiệu đang tự khen.
   - Ít nhất 2 câu là câu hỏi thật mà page trả lời được.
   - Mỗi câu một giọng khác nhau, không cùng một khuôn.
   - Không nêu tên đối thủ. Không bịa ưu đãi.
   - seed_id đánh SEED-01 đến SEED-05.
   - vai_tro chỉ nhận: ASK (hỏi thật), RELATE (đồng cảnh), EXPERIENCE (kể trải nghiệm),
     CONDITION (hỏi điều kiện), CTA_NUDGE (đẩy nhẹ về CTA).
3. Viết image_brief đủ 9 mục. Mục khong_duoc_xuat_hien là bắt buộc và không được rỗng;
   với sản phẩm liên quan trẻ em phải có ràng buộc về mặt trẻ em.
   ty_le chỉ nhận: 1:1, 4:5, 9:16, 16:9.
4. Viết image_prompt bằng TIẾNG ANH, mô tả cảnh cần sinh:
   - KHÔNG đưa chữ cần hiển thị vào prompt. Model sinh ảnh viết sai chính tả tiếng Việt;
     chữ sẽ chèn sau bằng Canva.
   - Nêu rõ bố cục, ánh sáng, tông màu, tỷ lệ.
   - Nêu rõ điều không được xuất hiện, khớp với mục khong_duoc_xuat_hien.
5. Viết review_note: một câu cho người duyệt biết cần soi kỹ chỗ nào trước khi bấm Approved.
6. Tuân thủ mục CẤM trong brand-voice.md.
7. Ghi kết quả thật ra file content-assets.json trong workspace.
8. Validate theo schemas/content-assets.schema.json, tự sửa rồi validate lại cho tới khi PASS.

TIÊU CHUẨN ĐẦU RA:
content-assets.json là JSON hợp lệ gồm:
{
  "brief_id": "",
  "source_angle_id": "",
  "seeding": [ { "seed_id": "SEED-01", "noi_dung": "", "vai_tro": "" } ],
  "image_brief": {
    "muc_tieu": "", "thong_diep_chinh": "", "doi_tuong": "", "kenh": "", "ty_le": "",
    "phong_cach": "", "bo_cuc": "", "chu_tren_anh": "", "khong_duoc_xuat_hien": []
  },
  "image_prompt": "",
  "review_note": ""
}

Sau khi ghi file, đọc lại và báo: ba mã brief_id/source_angle_id có khớp hai lớp trước không,
số seeding, và các vai_tro đã dùng.
Không dựng workflow n8n ở bước này.
```

**Chaining line:** Giữ nguyên chat. Ba file `content-angles.json`, `content-draft.json`, `content-assets.json` là data contract và expected output cho TH4.
