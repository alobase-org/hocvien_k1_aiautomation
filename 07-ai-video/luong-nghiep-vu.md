# Luồng nghiệp vụ — Sản xuất video marketing (nguyên bản)

## Bối cảnh

Với cùng một SME đã xuất hiện ở Buổi 6 (trung tâm Anh ngữ, hay bất kỳ ngành nào có sản phẩm/dịch vụ định kỳ cần bán), **quay dựng video** không phải một nghề tách rời khỏi content — nó là **bước 3 "Sản xuất nội dung theo kênh"** trong chu trình marketing đã trình bày ở Buổi 6, cụ thể là nhánh video của bước đó. Buổi 6 dừng lại ở việc kịch bản TikTok (`content-draft.json`) được duyệt xong phần *chữ*; luồng nghiệp vụ thật vẫn còn nguyên phần *hình* phía sau — phần tốn thời gian nhất và ít khi do một người làm trọn vẹn.

## Actors thật trong một đội sản xuất video SME

| Vai trò                                           | Việc thật họ làm                                                                                                                                                                                                                    |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chủ doanh nghiệp / trưởng phòng marketing     | Duyệt kịch bản trước khi quay (tránh quay xong mới sửa — tốn kém), duyệt bản dựng cuối, chịu trách nhiệm về hình ảnh thương hiệu/con người xuất hiện trong video                                            |
| Content lead (người viết kịch bản ở Buổi 6) | Bàn giao kịch bản đã duyệt kèm ý định hình ảnh cho từng cảnh (`tiktok.khoi[].hinh_anh` — mới là ý định, chưa phải bản vẽ storyboard)                                                                          |
| Đạo diễn / người dựng storyboard             | Chuyển ý định hình ảnh thành storyboard cụ thể: khung hình, góc quay, chuyển động, bối cảnh —**là người dịch chữ sang hình**, thường là điểm nghẽn vì phải tưởng tượng ra thứ chưa tồn tại |
| Quay phim / diễn viên                            | Set bối cảnh thật, quay nhiều lần (retake) tới khi khớp storyboard — tốn nhiều giờ, phụ thuộc lịch người và địa điểm                                                                                               |
| Editor hậu kỳ                                    | Cắt ghép, đồng bộ lời thoại/nhạc/SFX, chèn phụ đề, chuẩn hóa màu — thường mất nhiều giờ cho một clip ngắn                                                                                                        |
| Đội CSKH / sales                                 | Không trực tiếp trong chu trình video, nhưng là nguồn phản hồi thật sau khi video đăng (khách có hiểu đúng thông điệp không)                                                                                       |

## Chu trình đầy đủ (nối tiếp bước 3 của Buổi 6, lặp lại theo từng kịch bản)

**Bước 1 — Nhận kịch bản đã duyệt**
Input: `content-draft.json` (Buổi 6) — kịch bản TikTok 4 khối HOOK/PROBLEM/SOLUTION/CTA, đã qua cổng duyệt nội dung.
Output: kịch bản được xác nhận là **input cố định**, không viết lại thông điệp ở bước sau.
Đây là ranh giới bàn giao: từ đây, không ai được tự ý đổi lời thoại hay claim đã duyệt.

**Bước 2 — Storyboard hóa**
Input: kịch bản + ý định hình ảnh sơ bộ trong từng khối.
Output: storyboard — mỗi cảnh có mô tả khung hình, góc máy, chuyển động, nhân vật/bối cảnh nhất quán xuyên suốt (style bible).
Đây là bước quyết định **video có giống một bộ phim hay là 8 cảnh rời rạc** — thiếu style bible là nguyên nhân phổ biến nhất khiến nhân vật/bối cảnh đổi giữa chừng.

**Bước 3 — Chuẩn bị & Quay (bối cảnh thật)**
Input: storyboard đã chốt.
Output: footage thô cho từng cảnh.
Ở quy trình truyền thống: đặt lịch diễn viên, thuê địa điểm, quay nhiều lần tới khi khớp storyboard. Đây là khâu **tốn chi phí và thời gian nhất**, và là lý do nhiều SME bỏ dở video giữa chừng.

**Bước 4 — Dựng hậu kỳ**
Input: footage thô + audio (lời thoại, nhạc, SFX).
Output: bản dựng hoàn chỉnh có hình + tiếng đồng bộ.
Editor ghép cảnh, đồng bộ thoại, chèn nhạc/SFX theo đúng ý đồ kịch bản — không phải chỉ "làm cho đẹp" mà phải khớp lại đúng thông điệp gốc.

**Bước 5 — Duyệt nội bộ**
Input: bản dựng.
Output: bản Approved hoặc yêu cầu sửa (sai continuity, sai thông điệp, hình ảnh nhạy cảm).
Giống bước 4 của Buổi 6: **không có nút đăng tự động** ở đây — người thật phải xem trước khi video ra khỏi nội bộ. Với video có con người/trẻ em xuất hiện, đây còn là cổng kiểm tra quyền hình ảnh.

**Bước 6 — Xuất bản & đăng**
Input: video đã duyệt.
Output: video **thật sự xuất hiện** trên TikTok/Fanpage, đúng lịch content calendar.
Đây là bước tạo giá trị kinh doanh — mọi bước trước chỉ là chi phí cho tới khi video được đăng.

**Bước 7 — Đo lường & rút kinh nghiệm**
Input: dữ liệu view, completion rate, share, comment từ video đã đăng.
Output: bài học cho kịch bản/storyboard kỳ sau (cảnh nào giữ chân người xem, cảnh nào bị lướt).
Đóng vòng lặp về lại content calendar của Buổi 6 — thiếu bước này, đội sản xuất lặp lại đúng lỗi cũ.

```
[Buổi 6] Kịch bản đã duyệt
        │
        ▼
[1] Nhận kịch bản (ranh giới bàn giao — không sửa thông điệp)
        │
        ▼
[2] Storyboard hóa ◄─────────────────┐
        │                             │
        ▼                             │
[3] Chuẩn bị & Quay (bối cảnh thật)   │  (điểm nghẽn: chi phí + thời gian)
        │                             │
        ▼                             │
[4] Dựng hậu kỳ                       │
        │                             │
        ▼                             │
[5] Duyệt nội bộ ─── chưa đạt ────────┘
        │ đạt
        ▼
[6] Xuất bản & đăng
        │
        ▼
[7] Đo lường & rút kinh nghiệm ───► quay lại content calendar Buổi 6
```

## Buổi 7 thay thế đoạn nào

Workshop Buổi 7 (TH1–TH4B) dùng AI để nén **Bước 2–5** (Storyboard hóa → Quay → Dựng hậu kỳ → Duyệt) từ việc cần một đội (đạo diễn, quay phim, diễn viên, editor) và nhiều giờ/ngày, thành một pipeline sinh ảnh + sinh video có audio, vẫn giữ nguyên cổng duyệt ở từng lớp (`scene_id → frame_id → clip_id`, ảnh phải Approved trước khi sinh clip).

Cố ý **không chạm Bước 6 (đăng)** và **Bước 7 (đo lường)** — đúng nguyên tắc "AI tạo nháp, người duyệt" đã học ở Buổi 6, chỉ khác đối tượng nháp là video thay vì bài viết.
