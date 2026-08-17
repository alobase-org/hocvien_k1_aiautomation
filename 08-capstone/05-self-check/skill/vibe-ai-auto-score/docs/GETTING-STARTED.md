# Getting Started — vibe-ai-auto-score

> Sinh rubric chấm bài học viên TỰ ĐỘNG từ tài liệu một buổi dạy, chấm nương tay.

## 30 giây đầu tiên

1. Cài skill (xem `docs/INSTALL.md`).
2. Trỏ vào folder buổi dạy + folder bài nộp, ví dụ:
   ```
   /vibe-ai-auto-score
   Buổi: giao_trinh/giang-day/05-thuc-hanh/05-cskh-bot
   Bài nộp học viên: bai_nop/buoi-05/
   ```
3. Skill tự parse buổi dạy → sinh rubric → chấm từng bài → xuất docx + báo cáo lớp.

## Input bắt buộc

| Input | Bắt buộc | Ví dụ |
|---|---|---|
| Folder buổi dạy | **CÓ** | `05-thuc-hanh/05-cskh-bot/` (lab.md + thuc-hanh-N + prompts/ + checkpoints/) |
| Thư mục bài nộp HV | **CÓ** | `bai_nop/buoi-05/<ten-hv>/` |
| Rubric có sẵn | KHÔNG (tự sinh) | `output/rubric.json` |

**Quy ước cốt lõi:** `checkpoints/` = bài mẫu giảng viên = chuẩn 10/10. Skill dùng nó để hiệu chỉnh
mức điểm sao cho "học viên làm 70% cốt lõi → 7/10".

## Triết lý chấm — NƯƠNG TAY

Khác với bản chấm capstone khắt khe, skill này **động viên**:
- Mức 3 (Đạt) = "làm phần lớn cốt lõi ≈ 70% bài GV" — KHÔNG phải "đúng 100%".
- Khi phân vân giữa 2 mức → chọn mức **cao hơn** cho học viên.
- Không cap cứng vì thiếu test/log/output — mô tả logic đúng vẫn tính.
- KHÔNG phạt "chưa hoàn thiện/thiếu polish" — chỉ penalty cho lười/ảo thật sự.
- Feedback: nêu **điều làm tốt TRƯỚC**, gap SAU.

Chi tiết: `kb/student-grading-calibration.md`.

## Workflow 6 phase

```
Phase 0  Parse folder buổi dạy → session-brief.md
Phase 1  Sinh rubric (nương tay) từ lab.md + prompts + checkpoints
Phase 2  Định nghĩa unified schema
Phase 3  Convert từng bài nộp → unified + validate evidence/confidence
Phase 4  (optional) Deep-research cho tiêu chí khó
Phase 5  Chấm nương tay + adjustments + confidence gate + validate grounding
Phase 6  Xuất docx từng HV + báo cáo lớp (docx/html-dashboard/slide)
```

## Cần tùy chỉnh?

- **Mức nương tay:** chỉnh ngưỡng descriptors trong `kb/student-grading-calibration.md §1,§2`.
- **Trọng số ưu tiên:** sửa `§4` (hiểu+core vs polish) nếu lớp trình độ khác.
- **Feedback tone:** sửa template markdown trong `prompt/grade-prompt.md`.
- **Band:** sửa `BANDS` trong `script/score_aggregator.py` nếu muốn ngưỡng khác.

## Output điển hình

```
output/
├── session-brief.md           # tóm tắt buổi (Phase 0)
├── rubric.json                # rubric sinh ra (Phase 1)
├── candidates/
│   ├── <hv1>.unified.json     # trích evidence (Phase 3)
│   ├── <hv1>.grading.json     # điểm + gate (Phase 5)
│   └── ...
├── research/                  # (nếu có tiêu chí needs_research)
├── reports/<hv1>.docx         # phiếu chấm từng HV (Phase 6)
└── summary-report.json        # báo cáo lớp (xếp hạng + thống kê)
```

## Troubleshooting

| Lỗi | Nguyên nhân | Khắc phục |
|---|---|---|
| "Input không phải folder buổi dạy" | Thiếu lab.md/checkpoints/ | Kiểm lại cấu trúc folder (BR-10) |
| evidence.missing_count > 0 | Trích dẫn bịa/paraphrase | Sửa verbatim_quote cho khớp file gốc |
| confidence_gate REJECT | Overall confidence < 0.6 | Xem trường yếu nhất, bổ sung evidence hoặc human review |
| Điểm toàn lớp偏低 | descriptors mức 3 quá khắt | Rà `kb/student-grading-calibration §2`, nới mức 3 |
