---
name: make-alobase-philosophy-videos
description: "Sản xuất và chỉnh sửa video triết học/leadership tiếng Việt theo phong cách Nguyễn Minh Cường – Alobase: cinematic tối giản, tư duy hệ thống, voice-over nam sâu, motion graphics Remotion, phụ đề an toàn, piano nhẹ và master âm thanh rõ trên điện thoại. Dùng khi người dùng yêu cầu video triết lý, video tư duy hệ thống, video lãnh đạo, video dọc TikTok/Reels, hoặc muốn lặp lại phong cách video ENTROPY đã thống nhất."
---

# Video triết học Alobase

Tạo sản phẩm hoàn chỉnh, không chỉ viết kịch bản. Tự quyết định trong phạm vi brief; chỉ hỏi khi thiếu tài sản bắt buộc hoặc quyền truy cập.

## Quy trình bắt buộc

1. Chốt một luận đề duy nhất và cấu trúc: hiện tượng → quy luật → ẩn dụ đời thường → hệ quả tổ chức → vai trò lãnh đạo → câu kết ám ảnh.
2. Viết lời đọc tiếng Việt tự nhiên, dùng 160–220 từ như ước lượng ban đầu cho video 75–85 giây. Dùng câu ngắn, nhịp nghỉ có chủ ý; tránh sáo ngữ truyền động lực. Chỉ khóa timeline sau khi có TTS và timestamp thật; nếu lệch thời lượng, sửa lời hoặc scene boundary theo audio, không ép tốc độ máy móc.
3. Tạo voice-over nam Việt Nam quãng baritone, khoảng 40–50 tuổi, trầm, rõ, bình tĩnh nhưng có lực; tốc độ khởi điểm 0,96. Ưu tiên chất broadcaster, phát âm phụ âm rõ, không đều đều hoặc thì thầm. Nếu dự án chưa có voice ID đã duyệt, tự tạo 2–3 mẫu ngắn, chọn mẫu tốt nhất và lưu voice ID/cấu hình vào manifest dự án để tái sử dụng.
4. Dựng Remotion 1080×1920, 30 fps. Dùng motion graphics và hình ảnh ẩn dụ; không dùng avatar hoặc talking head nếu người dùng không yêu cầu.
5. Tạo phụ đề từ timestamp từng từ. Đặt trong safe area, tối đa hai dòng, tối đa 42 ký tự mỗi dòng, ưu tiên ngắt theo cụm nghĩa và không che điểm nhìn chính.
6. Dùng piano độc tấu nhẹ làm nhạc mặc định. Cấm drone, ambient hiss, pink noise, pad kéo dài hoặc pulse tổng hợp giả nhạc.
7. Master voice gần −16 LUFS integrated; piano thường −25 đến −23 LUFS integrated trước ducking và thấp hơn voice 7–10 LU; master −16 đến −15 LUFS integrated, true peak không vượt −1 dBTP.
8. Kiểm tra toàn bộ file trước bàn giao: thông số, giải mã, audio track, loudness, clipping, khoảng im lặng, phụ đề và contact sheet.
9. Bàn giao MP4 chất lượng cao, bản mobile nhẹ khi hữu ích, và ZIP dự án chỉnh sửa.

## Tài nguyên

- Đọc [references/style-bible.md](references/style-bible.md) trước khi viết kịch bản hoặc thiết kế hình.
- Đọc [references/production-workflow.md](references/production-workflow.md) khi sản xuất từ đầu hoặc sửa audio/caption.
- Đọc [references/qa-checklist.md](references/qa-checklist.md) trước khi bàn giao.
- Chạy `scripts/generate_piano_score.py` để tạo score piano nguyên bản, không bản quyền.
- Chạy `scripts/captions_from_words.py` để chuyển timestamp HeyGen thành phụ đề Remotion.
- Chạy `scripts/master_video.sh` để mix voice/piano và master MP4.
- Chạy `scripts/make_mobile.sh` để tạo bản tải nhẹ mà vẫn giữ nguyên audio của master.
- Chạy `scripts/verify_video.py` để kiểm định file cuối.
- Sao chép `assets/style-tokens.json` vào dự án khi cần khóa màu sắc, safe area và chuẩn âm thanh.
- Sao chép `assets/AlobaseSerif.ttf`, `assets/AlobaseSans.ttf` và giấy phép font vào dự án; luôn nhúng bằng `@font-face`.
- Sao chép `assets/production-manifest.template.json` thành `production-manifest.json`, rồi điền voice ID hoặc hash voice stem, hash asset/stem/script và thông số công cụ thực tế để tái lập video sau này.

## Nguyên tắc sửa đổi

- Khi người dùng chỉ yêu cầu thay audio, giữ nguyên luồng hình; xác nhận bằng hash video stream.
- Khi tăng nhạc, đo chênh lệch loudness bằng LU và kiểm tra true peak bằng dBTP. Không dựa vào cảm giác hoặc chỉ nhìn waveform.
- Nếu nhạc bị nhận xét là “tiếng ồn”, thay hoàn toàn bản phối bằng piano có cao độ, tiết tấu và khoảng nghỉ rõ ràng; không chỉ EQ hoặc tăng giảm volume.
- Luôn ưu tiên chất lượng nghe trên loa điện thoại: giọng rõ, piano hiện diện nhưng không che phụ âm.
