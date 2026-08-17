# Prompt TH1 — Từ yêu cầu nghiệp vụ sinh schema + sample

> Chạy trong Coding Agent có quyền ghi file. Đây là bước **sinh schema**, không dùng schema viết sẵn.

```text
BỐI CẢNH:
Tôi đang thiết kế Video Production Workflow: nhận kịch bản từ Buổi 6 hoặc nhập tay, chuẩn hóa
thành 6–9 cảnh, tạo storyboard ảnh, duyệt ảnh, rồi một Video Generator tổng lần lượt sinh
clip có native audio cho từng cảnh. Build app là lớp hỗ trợ, engine phải độc lập công cụ.

INPUT NGHIỆP VỤ:
- templates/manual-script-input.md để hiểu một input tối thiểu.
- Hai source_mode: B6_APPROVED và MANUAL.
- Chuỗi ID bắt buộc: project_id → scene_id → frame_id → clip_id.

CHỈ DẪN:
1. Phân tích nghiệp vụ và tự đề xuất đúng ba data contract:
   a) video-script: project + 6–9 scene chuẩn hóa;
   b) storyboard: style bible + frame cho từng scene + approval;
   c) video-plan: clip plan, motion, native audio, execution state.
2. Tạo thư mục schemas/ và samples/ trong workspace.
3. Sinh ba JSON Schema Draft 2020-12:
   - schemas/video-script.schema.json
   - schemas/storyboard.schema.json
   - schemas/video-plan.schema.json
4. Mọi object nghiệp vụ dùng additionalProperties=false. Dùng required/type/enum/pattern phù hợp.
5. video-script phải cho phép source_mode B6_APPROVED hoặc MANUAL; trường brief_id và
   source_angle_id được null khi MANUAL; scenes có minItems=6, maxItems=9.
6. Mỗi scene có scene_id dạng SC-01, source_block, duration_seconds, visual và dialogue.
7. storyboard giữ project_id; mỗi frame có frame_id, scene_id, image_prompt, negative_prompt,
   status DRAFT/NEEDS_REVIEW/APPROVED, image_asset_ref có thể null.
8. video-plan có một execution_mode SEQUENTIAL; mỗi clip có clip_id, scene_id, frame_id,
   image_asset_ref, duration, visual motion, audio, video_prompt, status và video_asset_ref.
   Audio bắt buộc có dialogue, language, voice_profile, delivery, ambient, sound_effects,
   music và negative_audio.
9. Status clip hợp lệ: BLOCKED, READY_TO_GENERATE, GENERATING, SUCCESS, ERROR, NEEDS_REVIEW,
   APPROVED. Chỉ frame APPROVED mới làm clip READY_TO_GENERATE.
10. Sinh ba sample JSON có cùng project_id, đủ 6 scene và các reference khớp.
11. Viết script validation nhỏ hoặc dùng validator có sẵn để validate cả ba sample.
12. Nếu FAIL, tự sửa schema/sample đến khi PASS. Ghi schema-validation-report.md gồm đường dẫn,
    kết quả, số scene/frame/clip và các invariant đã kiểm tra chéo.

PHÂN BIỆT:
- Schema khóa cấu trúc, ID, enum, số lượng.
- Không cố khóa chất lượng nghệ thuật bằng regex/schema. Continuity, prompt hay, lời thoại vừa
  thời lượng và audio hợp lý phải ghi thành quality_checklist trong sample hoặc report.

TIÊU CHUẨN BÀN GIAO:
- 3 schema parse được.
- 3 sample parse được và PASS.
- Không chỉ in code trong chat; phải ghi file thật.
- Báo rõ phần nào schema kiểm được và phần nào phải kiểm bằng checklist.
```

**Chaining line:** TH2 phải đọc chính schema vừa sinh; không dựng lại data contract trong prompt mới.

