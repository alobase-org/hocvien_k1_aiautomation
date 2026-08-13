# Style Bible — Nguyễn Minh Cường / Alobase

## Tư tưởng

- Đi từ nguyên lý gốc đến ứng dụng lãnh đạo.
- Nhìn tổ chức như một hệ thống: năng lượng, cấu trúc, dữ liệu, phản hồi và khả năng tự điều chỉnh.
- Tạo cảm giác suy tưởng, không lên lớp; sắc sảo, không phô trương.
- Câu kết phải cô đọng thành một mệnh đề có thể đứng độc lập.

## Cấu trúc kể chuyện

1. Nêu khái niệm bằng một câu đơn giản.
2. Cho hai hình ảnh đời thường không thể phủ nhận.
3. Mở rộng sang con người hoặc tổ chức.
4. Chỉ ra điểm nghẽn của lãnh đạo.
5. Đưa ra chuyển dịch hệ thống.
6. Kết bằng một câu đối lập hoặc nghịch lý.

## Giọng văn

- Tiếng Việt hiện đại, tự nhiên, có chiều sâu.
- Câu 5–15 từ; đan xen một vài câu dài để tạo dòng suy nghĩ.
- Dùng khoảng nghỉ sau ý quan trọng; không lạm dụng dấu ba chấm.
- Tránh: “trong thời đại ngày nay”, “chìa khóa thành công”, “hành trình vươn tới”, “không ngừng nỗ lực”.
- Không viết như quảng cáo hoặc văn bản AI.

## Hình ảnh

- Nền đen/xám than `#090A0C`; chữ trắng ngà `#F1EBDD`; vàng đồng `#B9914B`.
- Chuyển động chậm, mềm, có chủ đích; hạt phim rất nhẹ.
- Ưu tiên: hạt sáng, mạng lưới, đường lực, ánh sáng gom trật tự, vật thể nứt/vỡ, dữ liệu liên kết, typography lớn.
- Mỗi cảnh chỉ có một ý thị giác chính. Giữ khoảng trống âm.
- Không dùng stock cliché: bắt tay, người đứng trên đỉnh núi, bóng đèn ý tưởng, văn phòng cười nhìn camera.

## Chữ và phụ đề

- Mặc định sao chép và nhúng `assets/AlobaseSerif.ttf` cho tiêu đề, `assets/AlobaseSans.ttf` cho nội dung/caption; khai báo bằng `@font-face` để kết quả không phụ thuộc máy. Hai font hỗ trợ tiếng Việt và có giấy phép kèm tại `assets/FONT-LICENSE.txt`.
- Phụ đề ở vùng dưới nhưng cách đáy ít nhất 260 px; cách hai cạnh ít nhất 72 px.
- Caption 48–52 px, line-height 1,28–1,32; tối đa hai dòng và tối đa 42 ký tự mỗi dòng. Mục tiêu thường là 28–40 ký tự, nhưng ngắt theo cụm nghĩa quan trọng hơn số ký tự. Không quá 4,5 giây một caption.
- Dùng vàng đồng để nhấn một từ khóa, không tô cả câu.

## Chuyển động và hạt phim

- Easing mặc định: `cubic-bezier(0.16, 1, 0.3, 1)`; dùng ease-in-out `cubic-bezier(0.45, 0, 0.55, 1)` cho biến đổi trạng thái.
- Transition mềm trong 12–18 frame; tránh whip-pan, flash và chuyển cảnh phô diễn.
- Grain phải là lớp hình đơn sắc nhẹ, khoảng 4–5,5% opacity hiệu dụng; tuyệt đối không ghép thêm noise âm thanh.

## Âm nhạc

- Mặc định: piano độc tấu felt/soft, 68–76 BPM, giọng thứ hoặc hợp âm add9/maj7.
- Giai điệu thưa, có nốt và khoảng nghỉ rõ; không cần trống.
- Không dùng noise bed, drone, pad, synth pulse, riser hoặc âm gió liên tục.
- Cao trào đến từ register, hòa âm và lực phím, không đến từ tăng dày lớp âm thanh.

## Giọng thương hiệu

- Nam Việt Nam baritone, cảm giác 40–50 tuổi, bình tĩnh và có chiều sâu; broadcaster nhưng không giống đọc bản tin.
- Tốc độ khởi điểm 0,96; nghỉ 0,3–0,45 giây giữa ý và 0,6–0,8 giây trước câu kết.
- Khi đã chọn được voice ID tốt, ghi ID, engine, speed và ngày chọn vào `production-manifest.json`; các video sau ưu tiên tái dùng cấu hình này.

## Dấu ấn tùy chọn

- Có thể dùng định vị “Thiết kế lại cách con người làm việc” khi phù hợp với chủ đề Alobase.
- Không chèn logo/tagline nếu người dùng không yêu cầu hoặc không có tài sản chuẩn.
