# Prompt TH2 — Schema sinh content artifact 6–9 cảnh

> Đặt `SOURCE_MODE` trước khi chạy. Giữ cùng phiên chat với TH1.

```text
SOURCE_MODE: MANUAL
# Đổi thành B6_APPROVED nếu có content-draft.json từ Buổi 6.

BỐI CẢNH:
Ba schema đã được sinh và validate ở TH1. Giờ dùng chúng để tạo bộ content artifact thật.

INPUT:
- schemas/video-script.schema.json
- schemas/storyboard.schema.json
- schemas/video-plan.schema.json
- Nếu MANUAL: templates/manual-script-input.md
- Nếu B6_APPROVED: content-draft.json và thông tin trạng thái duyệt nếu có

CHỈ DẪN:
1. Đọc ba schema trước. Không thay schema âm thầm để ép output PASS.
2. Nếu B6_APPROVED: lấy đúng tiktok.khoi; nếu có status mà khác Approved, dừng và báo.
3. Nếu MANUAL: đọc input mẫu, không tự thêm claim/số liệu.
4. Chuẩn hóa thành video-script.json có 6–9 scene. Bốn block HOOK/PROBLEM/SOLUTION/CTA có thể
   tách thành nhiều scene nhưng mỗi scene phải giữ source_block.
5. Tạo storyboard.json: một style_bible dùng chung; mỗi scene có một frame chính. image_prompt
   phải mô tả bố cục, chủ thể, hành động, camera, ánh sáng, tỷ lệ và continuity anchor.
6. Ban đầu mọi frame status=DRAFT, image_asset_ref=null.
7. Tạo video-plan.json cho cùng danh sách scene. Video Generator tổng chạy SEQUENTIAL.
   Vì frame chưa duyệt, clip ban đầu status=BLOCKED và image_asset_ref=null.
8. Mỗi clip phải có motion cho subject/camera/environment và audio đầy đủ. video_prompt phải
   hợp nhất hình + chuyển động + lời thoại + ambience/SFX/music/negative audio.
9. Ước lượng lời thoại phù hợp duration; nếu dài, rút gọn mà không đổi thông điệp.
10. Validate ba artifact theo schema; kiểm chéo project_id, scene_id, frame_id, clip_id.
11. Ghi content-validation-report.md. Nếu lỗi chất lượng không thuộc schema, ghi vào checklist,
    không tuyên bố schema đã đảm bảo nghệ thuật.

TIÊU CHUẨN BÀN GIAO:
- video-script.json, storyboard.json, video-plan.json.
- 6–9 scene.
- Không có reference mồ côi.
- Nêu rõ dữ kiện nào kế thừa B6 và dữ kiện nào do MANUAL cung cấp.
```

**Chaining line:** TH3 chỉ cập nhật asset reference/status sau khi chạy media; không sinh lại kịch bản hay đổi ID.

