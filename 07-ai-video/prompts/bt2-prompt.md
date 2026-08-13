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
- Nếu B6_APPROVED: content-draft.json (bắt buộc). Nếu workspace còn giữ được từ phiên B6:
  content-angles.json (lấy brief_title) và hai file của B6 —
  `06-content-engine/templates/chan-dung-khach-hang.md`, `06-content-engine/templates/brand-voice.md`
  (lấy mô tả chân dung thật và giọng thương hiệu). Không bắt buộc phải có — content-draft.json chỉ
  mang MÃ chân dung (vd "PH1"), không mang mô tả, nên nếu thiếu hai file này phải tự nêu rõ ở báo cáo
  là target_audience/brand_style được suy luận, không phải nguồn B6 gốc (xem bước 2b, 4b).

CHỈ DẪN:
1. Đọc ba schema trước. Không thay schema âm thầm để ép output PASS.
2a. Nếu B6_APPROVED: content-draft.json (output TH2 của B6) không có field trạng thái duyệt — trạng
    thái Approved chỉ tồn tại ở Google Sheets Content_Queue của B6, một tầng sau file này. KHÔNG tự
    giả định file đưa vào đã qua duyệt. Hỏi thẳng người dùng: "Nội dung trong content-draft.json này
    đã được bấm Approved ở Buổi 6 (app duyệt TH4b) chưa?" Nếu người dùng xác nhận CHƯA hoặc không chắc,
    dừng lại và báo — không tiếp tục sinh video-script từ nội dung chưa duyệt.
2b. Nếu B6_APPROVED: copy nguyên văn `brief_id` và `source_angle_id` từ content-draft.json sang
    video-script.json — không được để null, không tự sinh mã khác. Lấy đúng `tiktok.khoi`.
    `project_id` = chính `brief_id` (đủ điều kiện pattern `^[A-Z0-9-]+$`, không cần bịa mã mới).
    `title` không có sẵn trong content-draft.json — viết ngắn gọn dựa trên `fanpage.hook` (diễn đạt
    lại, không copy nguyên câu). `platform` = "TIKTOK", `aspect_ratio` = "9:16" (kịch bản B6 vốn viết
    cho TikTok dọc). `target_audience`: nếu có chan-dung-khach-hang.md, dùng đúng mô tả khớp mã
    `chan_dung`; nếu không có file, viết ngắn từ chính `fanpage.noi_dung` và ghi trong
    content-validation-report.md rằng đây là suy luận, không phải nguồn B6 gốc. `brand_style`: tương tự,
    ưu tiên brand-voice.md; nếu không có, suy từ giọng văn `fanpage.noi_dung`, ghi rõ là suy luận.
    `forbidden_elements`: gom các điều cấm xuất hiện rải rác trong từng `hinh_anh` (vd "không quay mặt
    trẻ em thật") thành một danh sách chung ở đầu video-script.json.
3. Nếu MANUAL: đọc input mẫu, không tự thêm claim/số liệu.
4a. Chuẩn hóa thành video-script.json có 6–9 scene. Bốn block HOOK/PROBLEM/SOLUTION/CTA có thể
    tách thành nhiều scene nhưng mỗi scene phải giữ source_block.
4b. B6 luôn ra đúng 4 khối và B7 luôn cần tối thiểu 6 scene, nên việc tách KHÔNG phải tuỳ chọn — hầu
    hết trường hợp bắt buộc phải tách ít nhất một khối. Cách tách, theo thứ tự ưu tiên:
    - Chia `duration_seconds` của các scene con sao cho tổng đúng bằng đúng bề rộng giây của khối gốc
      (đọc từ `thoi_gian`, vd khối "10-35s" rộng 25 giây), mỗi scene vẫn nằm trong khoảng schema cho
      phép (3-10 giây/scene).
    - Lời thoại (`dialogue`) của các scene con phải lấy TỪ đúng `loi_thoai` gốc của khối đó, chia theo
      từng câu hoặc từng vế câu tự nhiên (dấu phẩy, liên từ) — KHÔNG được viết thêm câu mới mang thông
      tin/số liệu ngoài những gì khối gốc đã có, vì đó là nội dung đã qua (hoặc sắp qua) duyệt ở B6.
    - Nếu số scene cần tách nhiều hơn số câu/vế câu có sẵn trong khối gốc, những scene còn dư được
      phép để `dialogue` là chuỗi rỗng `""` (scene hình-không-lời, b-roll) — KHÔNG được bịa lời thoại
      mới để lấp đầy. Không được để CẢ khối chỉ toàn scene rỗng — phải giữ ít nhất một scene mang đúng
      lời thoại gốc.
5. Tạo storyboard.json: một style_bible dùng chung; một **voice_bible** dùng chung (1 mô tả giọng
   duy nhất — giới tính, chất giọng, tốc độ, phong cách — sẽ lặp lại y nguyên ở mọi clip, không đổi
   theo scene, để giọng đồng nhất xuyên suốt video); mỗi scene có một frame chính. image_prompt
   phải mô tả bố cục, chủ thể, hành động, camera, ánh sáng, tỷ lệ và continuity anchor.
6. Ban đầu mọi frame status=DRAFT, image_asset_ref=null.
7. Trước khi tạo video-plan.json: nếu công cụ sinh video thật của lớp chỉ nhận vài giá trị
   duration cố định (kiểm tài liệu công cụ, không đoán), **ép tròn duration_seconds của từng
   clip về giá trị gần nhất được chấp nhận NGAY LÚC NÀY** — trước khi viết dialogue/video_prompt ở
   bước 8, để lời chú thích số giây (nếu có) trong prompt khớp đúng giá trị thật sẽ gửi đi.
8. Tạo video-plan.json cho cùng danh sách scene. Video Generator tổng chạy SEQUENTIAL.
   Vì frame chưa duyệt, clip ban đầu status=BLOCKED và image_asset_ref=null.
9. Mỗi clip phải có motion cho subject/camera/environment và audio đầy đủ (voice_profile PHẢI
   giống hệt voice_bible.description, không tự viết riêng theo scene). video_prompt phải hợp nhất
   hình + chuyển động + lời thoại + ambience/SFX/music/negative audio — nếu công cụ hỗ trợ audio
   gốc (không TTS rời), video_prompt BẮT BUỘC chứa nguyên văn 3 phần: (a) câu chỉ dẫn narration
   off-screen (người đọc không xuất hiện trong khung hình, vd "OFF-SCREEN VOICE-OVER NARRATION
   ONLY, narrator never shown on screen"), (b) voice_bible.description lặp lại y nguyên, (c) lời
   thoại trong ngoặc kép. Mỗi clip cũng cần negative_prompt riêng (khác negative_prompt của frame
   ảnh) liệt kê tối thiểu: visible speaker/narrator/person, human face, hands entering frame,
   on-screen text — chặn công cụ tự vẽ thêm người đọc thoại vào khung hình.
10. Ước lượng lời thoại phù hợp duration_seconds (đã ép tròn ở bước 7); nếu dài, rút gọn mà không
    đổi thông điệp.
11. Validate ba artifact theo schema; kiểm chéo project_id, scene_id, frame_id, clip_id.
12. Ghi content-validation-report.md. Nếu lỗi chất lượng không thuộc schema, ghi vào checklist,
    không tuyên bố schema đã đảm bảo nghệ thuật.

TIÊU CHUẨN BÀN GIAO:
- video-script.json, storyboard.json, video-plan.json.
- 6–9 scene.
- Không có reference mồ côi.
- Nếu B6_APPROVED: brief_id/source_angle_id trong video-script.json khớp đúng content-draft.json
  (không null); tổng duration_seconds các scene bằng đúng tiktok.tong_thoi_luong_giay.
- Nêu rõ dữ kiện nào kế thừa B6 và dữ kiện nào do MANUAL cung cấp.
```

**Chaining line:** TH3 chỉ cập nhật asset reference/status sau khi chạy media; không sinh lại kịch bản hay đổi ID.

