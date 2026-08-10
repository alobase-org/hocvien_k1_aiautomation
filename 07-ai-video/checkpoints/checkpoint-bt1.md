# Checkpoint TH1 — Schema do prompt sinh

## Expected state

- [ ] Có 3 schema + 3 sample + validation report.
- [ ] Sample PASS Draft 2020-12.
- [ ] Script có 6–9 scene; ID pattern rõ.
- [ ] Storyboard có approval và asset ref.
- [ ] Video plan chạy SEQUENTIAL, có audio và per-clip state.
- [ ] Agent phân biệt schema với quality checklist.

## Rescue

| Lỗi | Câu cứu hộ |
|---|---|
| Chỉ in JSON trong chat | `Ghi toàn bộ schema/sample thành file thật rồi đọc lại và validate.` |
| Schema khóa prompt nghệ thuật bằng regex | `Bỏ tiêu chí nghệ thuật khỏi schema; chuyển thành quality checklist.` |
| Thiếu native audio | `Bổ sung dialogue, language, voice_profile, delivery, ambient, sound_effects, music, negative_audio vào clip contract.` |
| Quá 10 phút chưa PASS | Dùng `checkpoints/reference-schemas/` và ghi rõ FALLBACK. |

