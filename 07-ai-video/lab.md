# Lab Buổi 07 — Video Production Workflow

## Mục tiêu

Biến kịch bản B6 hoặc kịch bản nhập tay thành 6–9 cảnh, storyboard ảnh và các clip có native audio; sau đó đóng gói logic thành engine độc lập công cụ và tùy chọn app node-based.

## TH1 — Prompt sinh schema (18')

Chạy `prompts/bt1-prompt.md`.

Đầu ra:

```text
schemas/video-script.schema.json
schemas/storyboard.schema.json
schemas/video-plan.schema.json
samples/video-script.sample.json
samples/storyboard.sample.json
samples/video-plan.sample.json
schema-validation-report.md
```

Nghiệm thu:

- Sample validate PASS.
- `additionalProperties: false` ở các object nghiệp vụ.
- 6–9 scene.
- Có `project_id`, `scene_id`, `frame_id`, `clip_id`.
- Có image approval và trạng thái từng clip.
- Audio có dialogue/language/voice/ambient/SFX/music/negative audio.

## TH2 — Schema sinh content artifact (18')

Chạy `prompts/bt2-prompt.md`, chọn `B6_APPROVED` hoặc `MANUAL`.

Đầu ra:

- `video-script.json`
- `storyboard.json`
- `video-plan.json`

Nghiệm thu:

- 6–9 scene; tổng thời lượng hợp lý.
- Mỗi scene thuộc một block nguồn.
- Mỗi frame tham chiếu scene có thật.
- Mỗi clip tham chiếu đúng frame.
- Style bible dùng chung; không tự đổi nhân vật/bối cảnh.
- Lời thoại vừa thời lượng; video prompt có cả hình và audio.

## TH3 — Media canary (22')

Chạy `prompts/bt3-prompt.md`.

1. Chọn 2 scene đại diện.
2. Tạo 2 ảnh storyboard.
3. Duyệt ít nhất 1 ảnh; ghi asset reference và status.
4. Video Generator tổng chỉ nhận frame Approved.
5. Sinh 1 clip có audio.
6. Ghi `media-run-log.json`.

Không chạy đủ 6–9 cảnh trước khi canary PASS.

## TH4A — Content/Video Engine (15')

Chạy `prompts/bt4a-prompt.md`.

Đầu ra `engine-spec.json` phải mô tả:

- Node/port/edge;
- Hai input adapter;
- Scene planning;
- Storyboard generation + approval;
- Một Video Generator tổng chạy tuần tự;
- Per-clip state, retry, progress, error;
- Run log và chi phí dự kiến;
- Test case.

## TH4B — Build app hỗ trợ (12')

Chạy `prompts/bt4b-prompt.md`.

Google Flow là đường demo chính. Có thể dùng nền tảng khác. Phần app phải đọc `engine-spec.json`, không tự đổi data contract.

## Checklist cuối buổi

- [ ] Prompt TH1 thực sự sinh schema; không dùng schema viết tay từ trước.
- [ ] Ba sample PASS.
- [ ] Hai đường input về cùng `video-script.json`.
- [ ] Có 6–9 scene.
- [ ] Storyboard được duyệt trước video.
- [ ] Một Video Generator tổng, log riêng từng clip.
- [ ] Ít nhất 1 clip runtime từ đúng frame, có audio.
- [ ] Có `engine-spec.json` độc lập công cụ.
- [ ] App/master prompt không tuyên bố chạy được nếu chưa runtime-test.

## Bài tập về nhà

Chạy đủ 6–9 cảnh, ghi số lần retry, credit/thời gian, lỗi continuity và quyết định sửa. Mang engine spec + media proof sang B8 làm prototype capstone.
