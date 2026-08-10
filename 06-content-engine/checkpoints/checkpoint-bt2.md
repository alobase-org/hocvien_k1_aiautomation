# Checkpoint TH2 — Bài Fanpage + kịch bản TikTok (GV/TA)

## Expected state

- [ ] Agent đã đọc `content-angles.json`, không nghĩ lại ý tưởng từ brief.
- [ ] Workspace có `content-draft.json`.
- [ ] `brief_id` khớp TH1; `source_angle_id` là angle học viên chọn và có trong danh sách TH1.
- [ ] Bài Fanpage 120–200 từ, hook không mở bằng tên trung tâm, đúng 1 CTA.
- [ ] Kịch bản TikTok đủ 4 khối HOOK / PROBLEM / SOLUTION / CTA, tổng 30–45 giây.
- [ ] Cột `hinh_anh` ghi rõ quay gì — Buổi 7 sẽ dựng video từ đây.
- [ ] `thieu_thong_tin` **không rỗng**. Brief thiếu học phí và ngày khai giảng.

## Đếm lại số từ — luôn làm

`so_tu` là con số agent tự khai và hay sai. Đếm lại độc lập:

```bash
python -c "import json,re,sys; sys.stdout.reconfigure(encoding='utf-8'); d=json.load(open('content-draft.json',encoding='utf-8')); t=d['fanpage']['noi_dung']; print('khai',d['fanpage']['so_tu'],'| đếm lại',len(re.findall(r'\S+',t)))"
```

## Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Agent bóc lại brief, không dùng angle | `Đọc content-angles.json, lấy đúng angle A-0X. Bài viết phải bám angle đó, không được đổi góc.` |
| `brief_id` khác TH1 | `brief_id phải giữ y nguyên giá trị trong content-angles.json. Sửa lại.` |
| `thieu_thong_tin` rỗng | `Brief không có học phí và ngày khai giảng. Kiểm lại bài: chỗ nào cần hai thông tin đó phải ghi [cần bổ sung] và liệt kê vào thieu_thong_tin.` |
| Bịa ưu đãi, bịa số học viên | `Bỏ mọi con số không tra được về brief. Thay bằng [cần bổ sung].` |
| Kịch bản TikTok viết thành văn xuôi | `Trả về đúng 4 khối, mỗi khối có ten_khoi, thoi_gian, hinh_anh, loi_thoai. ten_khoi dùng HOOK, PROBLEM, SOLUTION, CTA.` |
| Cột `hinh_anh` chung chung hoặc trống | `Cột hinh_anh phải ghi quay cái gì, đủ để người khác dựng được video. Viết lại cả 4 khối.` |
| Lời thoại nghe như văn viết | `Lời thoại viết để nói ra miệng. Bỏ "đồng thời", "bên cạnh đó". Câu ngắn, mỗi khối tối đa 2 câu, số đọc thành chữ.` |
| Bài quảng cáo, nhiều tính từ khen | `Bỏ hết tính từ khen. Thay bằng việc cụ thể diễn ra trong buổi học.` |
| Có câu hứa kết quả | `Bỏ mọi cam kết kết quả. Trung tâm không cam kết điểm số hay chứng chỉ — xem brand-voice.md.` |
| Số từ ngoài khoảng | `Bài đang X từ. Viết lại cho vào khoảng 120-200 từ, giữ nguyên angle và CTA.` |
| Kẹt quá thời gian | Dùng `checkpoints/content-draft-sample.json` để tiếp tục TH3. |
