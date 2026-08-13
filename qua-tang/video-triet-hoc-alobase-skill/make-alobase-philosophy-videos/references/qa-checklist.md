# Checklist bàn giao

## Hình

- Đúng 1080×1920, 30 fps, 75–85 giây.
- Không có frame đen ngoài chủ ý, lỗi font, chữ tràn hoặc caption ngoài safe area.
- Contact sheet cho thấy nhịp cảnh hợp lý và kết thúc đủ thời gian đọc.

## Âm

- Có AAC stereo 48 kHz và giải mã được toàn bộ.
- Voice khoảng −16 LUFS, rõ phụ âm trên loa điện thoại.
- Piano có giai điệu rõ; không hiss/drone/noise; thấp hơn voice khoảng 7–10 LU trước ducking.
- Master −16 đến −15 LUFS integrated; true peak ≤ −1 dBTP; không NaN/Inf/clipping.
- Không có khoảng im lặng bất thường dài hơn 1,5 giây ngoài chủ ý.

## Đồng bộ

- Kiểm tra caption ở đầu, giữa, cuối bằng timestamp thực tế.
- Câu cuối khớp hình kết và còn ít nhất 2 giây để người xem đọc.
- Nếu chỉ sửa âm thanh, hash video stream phải trùng bản trước.

## File

- Chạy `scripts/verify_video.py` và yêu cầu kết quả PASS.
- Mở/giải mã toàn file bằng FFmpeg.
- Test ZIP bằng `unzip -t`.
- Tạo tên file ngắn, không dấu cho thiết bị di động.
- Xác nhận bản mobile giữ nguyên audio packet stream của master bằng hash khi chỉ nén lại hình.
- Kiểm tra `production-manifest.json` đã lưu voice ID/cấu hình. Nếu provider chưa trả voice ID ổn định, phải lưu voice stem đã duyệt và SHA-256; lý do đơn thuần không đủ.
- Kiểm tra font được nhúng từ file trong dự án và hash khớp manifest.
- Kiểm tra manifest đã điền phiên bản Remotion, FFmpeg, libx264 cùng package version/hash của Skill; không để `null`.
- Chạy SHA-256 cho toàn bộ script (`captions`, `piano`, `mobile`, `master`, `verify`) và yêu cầu khớp `skill.scriptSha256` trong manifest.
