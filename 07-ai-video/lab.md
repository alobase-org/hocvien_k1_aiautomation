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
- Style bible dùng chung; **voice bible dùng chung** (1 mô tả giọng cho cả video, lặp lại y nguyên ở `audio.voice_profile` mọi clip — không đổi giọng theo từng scene); không tự đổi nhân vật/bối cảnh.
- Lời thoại vừa thời lượng; `video_prompt` có cả hình và audio — nếu công cụ sinh video hỗ trợ audio gốc (không TTS rời), `video_prompt` phải tự chứa đủ: chỉ dẫn narration off-screen (người đọc không xuất hiện trong khung hình), voice bible lặp lại nguyên văn, và lời thoại trong ngoặc kép.
- Mỗi clip có `negative_prompt` riêng (khác `negative_prompt` của frame ảnh) — tối thiểu chặn: visible speaker/narrator/person, human face, hands, on-screen text.
- `duration_seconds` của mỗi clip đã ép về đúng giá trị công cụ sinh video thật sự chấp nhận (vd một số model chỉ nhận vài giá trị cố định, không phải dải tự do) — **ép tròn TRƯỚC khi viết lời thoại/`video_prompt`**, không phải sau, để tránh lệch giữa số giây model nhận và số giây (nếu có) ghi trong prompt.

**Nếu chạy `B6_APPROVED`:** B6 luôn ra đúng 4 khối, B7 luôn cần tối thiểu 6 scene — nên gần như luôn phải tách ít nhất một khối. Đã hỏi và xác nhận nội dung được đưa vào **đã Approved ở B6 TH4b** chưa (`content-draft.json` không tự mang trạng thái duyệt). `brief_id`/`source_angle_id` trong `video-script.json` phải khớp đúng `content-draft.json`, không được null (schema chặn cứng phần này khi `source_mode=B6_APPROVED`). Khi tách một khối thành nhiều scene: tổng `duration_seconds` các scene con phải bằng đúng bề rộng giây của khối gốc; lời thoại lấy từ đúng `loi_thoai` gốc (chia theo câu/vế câu), không bịa câu mới; scene dư được phép `dialogue` rỗng (b-roll) nhưng không được để cả khối rỗng hoàn toàn. Xem ví dụ đã chạy đúng ở `checkpoints/video-script-b6-approved-sample.json`.

**Cổng bắt buộc trước khi sang TH3: Duyệt kịch bản chi tiết.** Người dạy/học viên đọc lại toàn bộ dialogue + `video_prompt` + `negative_prompt` của từng clip trong `video-plan.json`, xác nhận đúng ý trước khi cho phép sinh ảnh/video. Đây là cổng HITL riêng, tách khỏi cổng duyệt ảnh và cổng duyệt clip ở TH3 — sai sót ở kịch bản (lời thoại sai, thiếu chỉ dẫn narration) mà không bắt ở đây sẽ tốn credit sinh ảnh/video sai.

## TH3 — Media canary (22')

Chạy `prompts/bt3-prompt.md`.

0. Xác nhận kịch bản chi tiết đã được duyệt (bước trên) — nếu công cụ/app có cổng chặn kỹ thuật (vd flag `script_approved`), xác nhận nó đã bật.
1. Chọn 2 scene đại diện.
2. Tạo 2 ảnh storyboard.
3. Duyệt ít nhất 1 ảnh; ghi asset reference và status.
4. Video Generator tổng chỉ nhận frame Approved.
5. Sinh 1 clip có audio — nếu dùng công cụ hỗ trợ audio gốc, kiểm tra thêm: (a) không có người/tay lạ xuất hiện trong khung hình so với ảnh đã duyệt (mô hình có thể tự vẽ thêm "người đọc thoại" nếu prompt không cấm rõ), (b) mọi công cụ sinh video AI thường có watermark/nhãn xác thực nội dung AI-sinh không xoá được bằng prompt — nếu gặp, đây là đặc tính của công cụ, không phải lỗi cần sửa; ghi rõ vào báo cáo, không cố xoá bằng prompt.
6. **Clip Review:** clip sinh xong phải vào `NEEDS_REVIEW`, chưa được coi là nội dung đã duyệt. Người dùng xem cả hình lẫn tiếng và chọn `APPROVED`, `NEEDS_RETRY` hoặc `REJECTED`.
7. Chỉ clip `APPROVED` mới được đưa vào danh sách ghép video cuối. Ghi quyết định duyệt, lý do retry/reject và asset reference vào `media-run-log.json`.

### Ba cổng HITL không được gộp

| Cổng | Duyệt cái gì | Đứng trước | Lỗi cần bắt |
|---|---|---|---|
| Script Review | `dialogue`, `video_prompt`, `negative_prompt` | Sinh ảnh | Sai thông điệp, lời thoại quá dài, thiếu off-screen narration, thiếu điều cấm |
| Storyboard Review | Ảnh, bố cục, nhân vật, bối cảnh, continuity | Sinh clip | Sai khung hình, đổi nhân vật/bối cảnh, chữ/logo/hình ảnh không phù hợp |
| Clip Review | Hình động + native audio của clip thật | Ghép video | Biến dạng, người/tay lạ, sai giọng/lời thoại, âm thanh lấn, lời dẫn thừa, watermark ngoài dự kiến |

`API SUCCESS` chỉ có nghĩa tác vụ kỹ thuật đã tạo được file. Nó **không đồng nghĩa** clip đã được con người duyệt:

```text
READY_TO_GENERATE → GENERATING → NEEDS_REVIEW
                                      ├─ APPROVED → được phép ASSEMBLE
                                      ├─ NEEDS_RETRY → sửa prompt và sinh lại
                                      └─ REJECTED → loại khỏi video
```

Không chạy đủ 6–9 cảnh trước khi canary PASS.

## TH4A — Content/Video Engine (15')

Chạy `prompts/bt4a-prompt.md`.

Đầu ra `engine-spec.json` phải mô tả:

- Node/port/edge;
- Hai input adapter;
- Scene planning;
- **Script Review** — cổng duyệt kịch bản chi tiết, đứng TRƯỚC Storyboard Generator, tách khỏi Storyboard Review;
- Storyboard generation + approval;
- Một Video Generator tổng chạy tuần tự;
- Per-clip state, retry, progress, error;
- Clip Review tách khỏi trạng thái thành công kỹ thuật; chỉ clip `APPROVED` mới được export/assemble;
- Run log và chi phí dự kiến;
- Test case.

## TH4B — Build app hỗ trợ (12')

Chạy `prompts/bt4b-prompt.md` — sau khi TH4A đã activate workflow và có đủ 4 webhook URL
(`/b7/plan`, `/b7/generate-image`, `/b7/generate-clip`, `/b7/assemble`). App là một file HTML tĩnh
gọi thẳng 4 webhook đó, không dùng nền tảng ngoài, không tự đổi data contract. App phải có màn hình
Script Review riêng (dialogue/video_prompt/negative_prompt từng clip, nút Duyệt kịch bản) trước khi
cho phép sinh ảnh — không gộp vào màn hình duyệt ảnh storyboard. Ở bước clip, app phải cho xem/nghe
kết quả thật và ghi quyết định `APPROVED`/`NEEDS_RETRY`/`REJECTED`; nút ghép video chỉ mở khi mọi clip
cần dùng đều đã `APPROVED`.

## Checklist cuối buổi

- [ ] Prompt TH1 thực sự sinh schema; không dùng schema viết tay từ trước.
- [ ] Ba sample PASS.
- [ ] Hai đường input về cùng `video-script.json`.
- [ ] Có 6–9 scene.
- [ ] Kịch bản chi tiết (dialogue + video_prompt + negative_prompt từng clip) đã được duyệt TRƯỚC khi sinh ảnh — cổng riêng, không lẫn với duyệt ảnh.
- [ ] Storyboard được duyệt trước video.
- [ ] Clip sinh thành công kỹ thuật đã qua Clip Review; chỉ clip Approved mới được ghép.
- [ ] Một Video Generator tổng, log riêng từng clip.
- [ ] Ít nhất 1 clip runtime từ đúng frame, có audio.
- [ ] Có `engine-spec.json` độc lập công cụ.
- [ ] App/master prompt không tuyên bố chạy được nếu chưa runtime-test.

## Bài tập về nhà

Chạy đủ 6–9 cảnh, ghi số lần retry, credit/thời gian, lỗi continuity và quyết định sửa. Mang engine spec + media proof sang B8 làm prototype capstone.
