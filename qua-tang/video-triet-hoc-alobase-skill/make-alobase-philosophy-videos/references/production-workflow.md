# Quy trình sản xuất

## 1. Kịch bản và thời lượng

- Chọn 8–10 beat hình ảnh cho 75–85 giây.
- Viết 160–220 từ như ước lượng; timeline chỉ được khóa bằng thời lượng và timestamp của TTS thật.
- Đặt 1,5–2 giây mở nhạc trước voice và 3–4 giây kết nhạc sau câu cuối.

## 2. Voice-over

- Dùng HeyGen TTS-only khi có; chọn nam Vietnamese hoặc multilingual broadcaster có phát âm Việt tốt.
- Tốc độ khởi điểm 0,96. Tạo mẫu ngắn với 2–3 giọng khi chưa có giọng chuẩn; tự chọn mẫu baritone rõ phụ âm nhất, rồi lưu `voice_id`, `engine`, `speed` và ngày chọn trong `production-manifest.json`.
- Dùng timestamp từng từ từ phản hồi TTS. Chuẩn hóa voice bằng high-pass 60–70 Hz, presence nhẹ 2–3 kHz, nén 2:1 và loudness gần −16 LUFS.

## 3. Piano

Tạo score nguyên bản:

```bash
python3 scripts/generate_piano_score.py \
  --output public/music-piano.wav \
  --duration 81.045 \
  --bpm 72 \
  --target-lufs -24
```

Nghe/đo riêng track piano. Phải nghe thành nốt nhạc và hợp âm ngay trên loa điện thoại. Nếu nghe như nền nhiễu, bỏ bản đó và tạo lại; không cứu bằng EQ.

## 4. Phụ đề

Chuẩn bị `words.json` từ timestamp TTS và `segments.json` là mảng chuỗi caption theo đúng thứ tự lời đọc:

```bash
python3 scripts/captions_from_words.py \
  --words words.json \
  --segments segments.json \
  --output public/captions.json \
  --offset-ms 2000
```

Script phải báo lỗi nếu từ caption không khớp transcript; sửa text thay vì ép timing.

## 5. Remotion

- 1080×1920, 30 fps, 9:16.
- Sao chép `assets/AlobaseSerif.ttf` và `assets/AlobaseSans.ttf` vào `public/fonts/`, khai báo `@font-face`; không dựa vào font cài sẵn trên máy.
- Dựng từng scene theo beat, dùng `Sequence`/`TransitionSeries` và animation theo frame.
- Giữ subtitle trong safe area. Render contact sheet ít nhất tại mở đầu, 1/3, 2/3 và kết.
- Với sửa audio-only, dùng video stream hiện có và remux để tránh thay đổi hình.

## 6. Mix và master

```bash
bash scripts/master_video.sh \
  --video video-with-captions.mp4 \
  --music public/music-piano.wav \
  --voice public/voiceover.wav \
  --output final.mp4 \
  --duration 81.045 \
  --voice-offset-ms 2000
```

Mặc định dùng ducking nhẹ lên piano khi voice xuất hiện, sau đó loudness-normalize master. Không nén mạnh làm piano bơm/phập phồng.

Cấu hình khởi điểm: ratio 1,8:1, attack 24 ms, release 320 ms; mục tiêu duck 2–3 dB khi có voice. Đo voice/piano bằng LUFS/LU và true peak bằng dBTP.

## 7. Bàn giao

- MP4 master H.264/AAC, faststart; CRF 17 là mặc định cho master dựng lại.
- Bản mobile 1080×1920 mặc định CRF 25, maxrate 2,8 Mbps và giữ nguyên audio AAC từ master.
- Tạo bản mobile bằng `bash scripts/make_mobile.sh final.mp4 final-mobile.mp4`; script phải dừng nếu hash audio thay đổi.
- ZIP dự án không chứa `node_modules` hoặc file render tạm.
- Lưu deliverable bền vững và đưa link tải có tên ngắn, không dấu.
- Kèm `production-manifest.json` ghi voice, palette, font file/hash, audio targets, seed/BPM piano, phiên bản công cụ và hash các asset/stem/script để lần sau tái lập được.
