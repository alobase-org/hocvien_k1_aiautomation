# Studentkit — K1 AI Automation & Vibe Coding

> ⚠️ **Đây là folder BUILD** — sinh tự động bởi `scripts/sync-studentkit.py`.
> KHÔNG sửa tay tại đây. Sửa ở `giao_trinh/giang-day/` rồi chạy sync lại.

## Đây là gì?

Bản tài liệu **dành cho học viên** — cắt giảm từ workspace giảng viên, loại bỏ:
- Script giảng dạy, lời dẫn, timeline (`04-script-giang-day/`)
- Checkpoint / đáp án / expected output (`05-thuc-hanh/*/checkpoints/`)
- Slide design spec, rubric, governance (`02-slide-design/`, `00-admin/`)

HV nhận được: **slide PPTX + lab handout + prompt copy-paste + template starter + capstone**.

## Sinh lại

```bash
cd giao_trinh
python3 scripts/sync-studentkit.py --clean      # xoá cũ + sync toàn bộ
python3 scripts/sync-studentkit.py --buoi 03     # sync riêng 1 buổi
python3 scripts/sync-studentkit.py --dry-run     # preview
```

Rule include/exclude: [`../giang-day/studentkit-manifest.json`](../giang-day/studentkit-manifest.json)
