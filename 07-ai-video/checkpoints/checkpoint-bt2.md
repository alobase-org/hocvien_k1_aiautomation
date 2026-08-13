# Checkpoint TH2 — Content artifact

- [ ] `video-script.json`, `storyboard.json`, `video-plan.json` PASS.
- [ ] 6–9 scene; project ID khớp.
- [ ] Không có scene/frame/clip mồ côi.
- [ ] Frame ban đầu DRAFT; clip ban đầu BLOCKED.
- [ ] Style bible dùng chung.
- [ ] Prompt video có hình, motion và audio.
- [ ] Không bịa claim/dữ kiện thiếu.
- [ ] Nếu `B6_APPROVED`: `brief_id`/`source_angle_id` khớp `content-draft.json`, không null (schema chặn cứng). Tổng `duration_seconds` các scene bằng đúng `tiktok.tong_thoi_luong_giay`. Đã hỏi và xác nhận nội dung đã Approved ở B6 TH4b trước khi dùng.

Rescue quan trọng: `Đọc lại schema vừa sinh. Không đổi ID hay chia lại nội dung từ đầu; sửa đúng artifact đang FAIL.`

| Lỗi thường gặp (B6_APPROVED) | Câu cứu hộ |
|---|---|
| Một khối B6 (vd SOLUTION 25s) cần tách ≥3 scene nhưng chỉ có 2 câu thoại gốc | `Chia thời lượng cho đủ số scene, giữ nguyên 2 câu thoại gốc ở 2 scene, scene còn lại để dialogue rỗng (b-roll) — không bịa câu thoại mới.` |
| Agent tự bịa `target_audience`/`brand_style` không có căn cứ | `Không có chan-dung-khach-hang.md/brand-voice.md của B6 thì viết ngắn từ chính fanpage.noi_dung và ghi rõ đây là suy luận trong content-validation-report.md, đừng bịa mô tả không có căn cứ.` |
| Kẹt quá thời gian | Dùng `checkpoints/video-script-b6-approved-sample.json` (ví dụ B6_APPROVED đã tách đúng, validate PASS) làm tham chiếu. |

