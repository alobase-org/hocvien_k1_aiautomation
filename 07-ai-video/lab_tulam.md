# 🧑‍💻 Lab Tự Làm — Buổi 07: AI Video Production cho kịch bản của bạn

> Dành cho học viên tự thực hành ngoài giờ học với **kịch bản, sản phẩm và phong cách hình ảnh của chính bạn** thay vì kịch bản mẫu trên lớp.
> Khác với `lab.md` (chạy trên lớp, có GV dẫn và có sẵn checkpoint), bản này được thực hiện trong **repo GitHub riêng của bạn**.
> Mục tiêu không chỉ là tạo một video đẹp. Bạn phải chứng minh được chuỗi dữ liệu và ba cổng duyệt: **Script Review → Storyboard Review → Clip Review**.

---

## ⚠️ Cảnh báo dữ liệu, bản quyền và chi phí

- Repo dùng để nộp bài có thể là **public**. Không đưa API key, webhook riêng, credential n8n, dữ liệu khách hàng hoặc chiến lược kinh doanh chưa công bố lên repo.
- Chỉ sử dụng hình ảnh, giọng nói, logo và tài sản mà bạn có quyền sử dụng. Không clone giọng hoặc gương mặt người thật khi chưa có sự đồng ý rõ ràng.
- Không mô tả đặc điểm nhận dạng của trẻ em hoặc người thật cụ thể trong prompt. Ưu tiên nhân vật minh họa hoặc bối cảnh không nhận diện cá nhân.
- Công cụ sinh ảnh/video có thể tính phí theo lượt. Đặt ngân sách tối đa trước khi chạy; luôn canary 2 scene trước khi batch 6–9 scene.
- Video/ảnh thường có dung lượng lớn. Không commit file media quá lớn vào GitHub. Có thể lưu trên Drive/object storage rồi đưa link vào `media-run-log.json`; bảo đảm quyền truy cập phù hợp.
- Watermark hoặc nhãn nội dung AI do công cụ gắn cứng không phải lỗi prompt. Ghi nhận trong review; không tìm cách xóa trái điều khoản dịch vụ.

---

## 🤖 Cách nhanh — để Coding Agent hỗ trợ

Mở Coding Agent tại một **thư mục trống, mới, tách biệt** khỏi repo khóa học, rồi dán nguyên văn file `lab_tulam.md` này và yêu cầu Agent thực hiện tuần tự các bước bên dưới.

Agent phải dừng lại hỏi bạn trước khi:

1. Tạo hoặc đẩy dữ liệu lên repo GitHub public.
2. Gọi API/công cụ sinh ảnh hoặc video có thể phát sinh phí.
3. Dùng hình ảnh hoặc giọng nói của người thật.
4. Đánh dấu `APPROVED` tại bất kỳ cổng duyệt nào — AI không được tự duyệt output của chính nó.

Bạn vẫn phải tự xem, nghe và quyết định tại ba cổng HITL. Coding Agent chỉ chuẩn bị dữ liệu, chạy validation và ghi lại bằng chứng.

---

## Cách thức làm bài

### Bước 1 — Tạo repo và workspace riêng

Tạo repo GitHub mới, ví dụ `<ten-ban>-k1-buoi07-tulam`. Tạo thư mục cục bộ mới, không lồng bên trong repo khóa học.

Copy từ Student Kit Buổi 7:

```text
prompts/
templates/
lab.md
README.md
```

Tạo thêm:

```text
schemas/
samples/
output_tulam/
output_tulam/media/
```

### Bước 2 — Chọn một trong hai nguồn đầu vào

#### Lựa chọn A — `B6_APPROVED`

Sử dụng `content-draft.json` của chính bạn từ Buổi 6.

- Xác nhận nội dung đã được người thật duyệt ở B6.
- Giữ nguyên `brief_id`, `source_angle_id` và lời thoại đã duyệt.
- Không tự thêm claim hoặc số liệu mới.
- Khi tách 4 block B6 thành 6–9 scene, tổng thời lượng các scene con phải khớp block nguồn; scene b-roll có thể không có thoại nhưng không được bịa lời mới.

#### Lựa chọn B — `MANUAL`

Copy `templates/manual-script-input.md` thành `templates/my-script-input.md`, rồi thay bằng kịch bản thật của bạn.

Kịch bản tối thiểu phải có:

- Tiêu đề và mục tiêu video.
- Nền tảng, tỷ lệ khung hình và đối tượng xem.
- Phong cách hình ảnh/brand style.
- Nội dung HOOK, PROBLEM, SOLUTION, CTA.
- Điều cấm xuất hiện.
- CTA có nguồn rõ ràng, không bịa ưu đãi hoặc cam kết.

Nếu chưa có dữ liệu thật, dùng nguyên `manual-script-input.md`; ghi rõ `FALLBACK_INPUT` trong báo cáo.

### Bước 3 — Chạy TH1 đến TH4A trong cùng phiên chat

Chạy đúng thứ tự:

```text
prompts/bt1-prompt.md
prompts/bt2-prompt.md
prompts/bt3-prompt.md
prompts/bt4a-prompt.md
```

Output bước trước là input bước sau. Không mở phiên chat mới giữa chừng và không để Agent âm thầm đổi schema chỉ để output PASS.

### Bước 4 — Tự kiểm tra và ghi review

- Validate schema/sample và ba content artifact.
- Tự duyệt kịch bản chi tiết trước khi sinh ảnh.
- Chỉ sinh clip từ frame đã Approved.
- Clip tạo được file phải vào `NEEDS_REVIEW`; bạn tự xem/nghe rồi quyết định.
- Chỉ clip `APPROVED` mới được coi là đủ điều kiện ghép.

### Bước 5 — Commit và push

Trước khi commit, xóa secret và kiểm tra kích thước media.

```bash
git init
git add .
git commit -m "buoi 07: ai video production tu lam"
git branch -M main
git remote add origin https://github.com/<github-username>/<ten-repo-cua-ban>.git
git push -u origin main
```

Không commit `.env`, API key, credential export hoặc URL webhook có quyền truy cập riêng.

---

## Cấu trúc thư mục đề xuất

```text
<ten-repo-cua-ban>/
├── templates/
│   └── my-script-input.md
├── prompts/
│   ├── bt1-prompt.md
│   ├── bt2-prompt.md
│   ├── bt3-prompt.md
│   └── bt4a-prompt.md
├── schemas/
│   ├── video-script.schema.json
│   ├── storyboard.schema.json
│   ├── video-plan.schema.json
│   └── engine-spec.schema.json
├── samples/
│   ├── video-script.sample.json
│   ├── storyboard.sample.json
│   └── video-plan.sample.json
└── output_tulam/
    ├── video-script.json
    ├── storyboard.json
    ├── video-plan.json
    ├── script-review.md
    ├── media-run-log.json
    ├── clip-review.md
    ├── engine-spec.json
    ├── engine-spec.md
    ├── schema-validation-report.md
    ├── content-validation-report.md
    ├── engine-validation-report.md
    └── media/
        ├── storyboard-canary-01.png
        ├── storyboard-canary-02.png
        └── clip-canary-01.mp4
```

Nếu media lưu ngoài repo, thư mục `media/` có thể chỉ chứa `README.md` ghi link, quyền truy cập và checksum/tên asset.

---

## TH1 — Prompt sinh schema và sample (bắt buộc)

Chạy `prompts/bt1-prompt.md` để Agent tự sinh ba schema và ba sample. Không copy schema reference trước khi tự làm.

### Deliverable

- `schemas/video-script.schema.json`
- `schemas/storyboard.schema.json`
- `schemas/video-plan.schema.json`
- Ba file tương ứng trong `samples/`
- `output_tulam/schema-validation-report.md`

### Nghiệm thu

- Ba schema parse được, dùng JSON Schema Draft 2020-12.
- Object nghiệp vụ có `additionalProperties: false`.
- Video script có 6–9 scene.
- Chuỗi ID `project_id → scene_id → frame_id → clip_id` kiểm tra được.
- Storyboard có `style_bible`, `voice_bible` và trạng thái duyệt ảnh.
- Video plan có motion, native audio, negative prompt và trạng thái từng clip.
- Report nói rõ phần schema kiểm được và phần bắt buộc con người review.

Nếu sau thời gian tự đặt ra vẫn chưa PASS, bạn có thể xem reference schema trong checkpoint, nhưng phải ghi `FALLBACK_SCHEMA` và file nào đã dùng.

---

## TH2 — Tạo content artifact 6–9 scene (bắt buộc)

Chạy `prompts/bt2-prompt.md` với `SOURCE_MODE` đã chọn.

### Deliverable

- `output_tulam/video-script.json`
- `output_tulam/storyboard.json`
- `output_tulam/video-plan.json`
- `output_tulam/content-validation-report.md`
- `output_tulam/script-review.md`

### Script Review bắt buộc

Trong `script-review.md`, lập bảng cho từng clip:

| clip_id | dialogue đúng nguồn? | vừa duration? | off-screen narration? | voice bible đúng? | negative prompt đủ? | quyết định | ghi chú |
|---|---|---|---|---|---|---|---|

Chỉ khi bạn ghi quyết định `APPROVED` cho kịch bản chi tiết mới được sang TH3.

### Nghiệm thu

- Có 6–9 scene và không có reference mồ côi.
- Mỗi scene giữ đúng `source_block`.
- Một style bible và một voice bible dùng xuyên suốt.
- `audio.voice_profile` của mọi clip khớp nguyên văn voice bible.
- `video_prompt` có off-screen narration, lời thoại trong ngoặc kép và chỉ dẫn âm thanh.
- Negative prompt của clip chặn tối thiểu visible speaker/narrator/person, face, hands và on-screen text.
- Duration được chốt theo giá trị công cụ thật chấp nhận **trước** khi viết lời thoại/prompt.

---

## TH3 — Media canary và ba cổng duyệt (bắt buộc để hoàn thành đầy đủ)

Chạy `prompts/bt3-prompt.md`. Chỉ chọn hai scene: SC-01 và một scene SOLUTION.

### Giới hạn chi phí trước khi chạy

Ghi vào đầu `media-run-log.json`:

- Công cụ/model dự kiến.
- Số lượt sinh ảnh tối đa.
- Số lượt sinh video tối đa.
- Ngân sách/credit tối đa.
- Điều kiện dừng.

### Ba cổng HITL

1. **Script Review:** đã hoàn thành ở TH2.
2. **Storyboard Review:** sinh đúng hai ảnh, tự kiểm tra và chọn `APPROVED` hoặc `NEEDS_REVIEW`; AI không tự duyệt.
3. **Clip Review:** chỉ sinh clip từ frame Approved. Khi API trả asset, trạng thái là `NEEDS_REVIEW`, không phải Approved.

Trong `clip-review.md`, kiểm tra:

- Đúng `scene_id`, `frame_id`, `clip_id`.
- Đúng frame nguồn và continuity.
- Không tự thêm người, mặt hoặc tay lạ.
- Chuyển động chủ thể/camera/bối cảnh hợp lý.
- Lời thoại đúng, rõ, đúng ngôn ngữ.
- Giọng khớp voice bible.
- Ambience/SFX/music không lấn thoại; không có lời dẫn thừa.
- Watermark/nhãn AI đã được ghi nhận.
- Quyết định: `APPROVED`, `NEEDS_RETRY` hoặc `REJECTED`.

### Phân biệt trạng thái

```text
SUCCESS kỹ thuật = công cụ tạo được asset có thể mở
APPROVED nghiệp vụ = con người đã xem/nghe và chấp nhận
```

Chỉ clip `APPROVED` mới đủ điều kiện assemble. Nếu `NEEDS_RETRY`, giữ nguyên ID, tăng `retry_count`, ghi lý do và chỉ sửa phần prompt liên quan.

### Nếu không có công cụ/credit video

- Vẫn hoàn thành TH1, TH2 và Script Review.
- Có thể hoàn thành Storyboard Review bằng công cụ ảnh bạn có quyền sử dụng.
- Ghi TH3 là `BLOCKED_NO_VIDEO_RUNTIME` hoặc `NOT_RUNTIME_TESTED`.
- Không dùng URL giả/placeholder và không tuyên bố đã hoàn thành media canary.
- Bài vẫn có thể nộp để nhận phản hồi về dataflow, nhưng chưa được tính là hoàn thành đầy đủ Buổi 7.

---

## TH4A — Đóng gói engine spec (bắt buộc)

Chạy `prompts/bt4a-prompt.md`. Bước này không yêu cầu bạn phải có n8n.

`engine-spec.json` phải mô tả:

- Hai input adapter `B6_APPROVED` và `MANUAL`.
- Scene Planner và chuỗi ID.
- Script Review trước Storyboard Generator.
- Storyboard Generator và Storyboard Review.
- Một Video Generator tổng chạy tuần tự, state/retry/error riêng từng clip.
- Clip Review tách khỏi technical success.
- Chỉ clip Approved mới được Export/Assemble.
- Run log, cost guard, test cases và known limitations.

Validate theo `engine-spec.schema.json` và ghi `engine-validation-report.md`.

---

## TH4B — Workflow n8n và app hỗ trợ (nâng cao, không bắt buộc)

Phần này cần n8n, credential và dịch vụ sinh media của riêng bạn. Không sử dụng credential của GV.
Student Kit **không phát sẵn file workflow n8n để import** — bạn tự dựng từ `engine-spec.json`,
đúng tinh thần "không phát sẵn phần mềm để bấm nút" của cả khóa.

Nếu thực hiện:

1. Dùng n8n Cloud hoặc self-host.
2. Đọc kỹ `output_tulam/engine-spec.json` (node, port, edge, execution_policy, approval_gates,
   retry_policy) và tự thiết kế node/kết nối tương ứng trong n8n của bạn — không có file starter
   để import, engine-spec chính là bản thiết kế bạn phải hiện thực hóa.
3. Bốn webhook cần có: `POST /b7/plan`, `POST /b7/generate-image`, `POST /b7/generate-clip`,
   `POST /b7/assemble`. Hard gate (`script_approved`, `frame_status === 'APPROVED'`, mọi clip gửi
   vào assemble phải `review_decision === 'APPROVED'`) phải chặn ở backend n8n, không chỉ ở app.
4. Chỉ sau khi bốn webhook đã hoạt động và ba negative test (chặn đúng khi thiếu duyệt) PASS mới
   chạy `prompts/bt4b-prompt.md` để build app.
5. App phải tách Script Review, Storyboard Review và Clip Review.
6. Nút assemble chỉ mở khi mọi clip cần dùng đã Approved.
7. Trước khi export/commit workflow, xóa credential ID, Drive/Sheet ID, domain riêng và mọi secret;
   thay bằng placeholder rõ ràng (`REPLACE_...`). Không commit file workflow còn giữ credential thật.

Nếu không có điều kiện chạy n8n, bỏ qua TH4B. `engine-spec` ở TH4A vẫn là deliverable bắt buộc.

---

## Checklist trước khi nộp

- [ ] Ba schema và ba sample parse được, validate PASS.
- [ ] `video-script.json`, `storyboard.json`, `video-plan.json` cùng `project_id`.
- [ ] Có 6–9 scene; scene/frame/clip reference khớp.
- [ ] Không bịa claim, ưu đãi hoặc số liệu ngoài nguồn.
- [ ] Có một style bible và một voice bible dùng chung.
- [ ] Đã hoàn thành `script-review.md` trước khi sinh ảnh.
- [ ] Hai ảnh canary có asset reference và quyết định Storyboard Review.
- [ ] Clip chỉ được sinh từ frame Approved.
- [ ] Nếu có clip runtime: đã hoàn thành `clip-review.md`; không dùng SUCCESS kỹ thuật thay APPROVED nghiệp vụ.
- [ ] `media-run-log.json` ghi tool/model, thời gian, retry, chi phí, technical status và review decision.
- [ ] `engine-spec.json` có đủ ba cổng HITL, retry, cost guard và test case.
- [ ] Không commit API key, credential, webhook riêng hoặc dữ liệu nhạy cảm.
- [ ] Có quyền sử dụng hình ảnh, giọng nói và tài sản xuất hiện trong bài.
- [ ] Media lớn được lưu phù hợp; link nộp có thể truy cập nhưng không mở quyền quá mức cần thiết.

---

## 📮 Hướng dẫn nộp bài

1. Push repo cá nhân sau khi đã kiểm tra secret và dữ liệu nhạy cảm.
2. Copy link repo và link media ngoài repo nếu có.
3. Điền vào form nộp bài: **[Form Nộp Bài Buổi 7](https://forms.gle/CKwnibtXZjnjhD9a9)**.
4. Trong phần ghi chú nộp bài, khai báo một trong các trạng thái:
   - `FULL_RUNTIME`: có clip thật, đã Clip Review.
   - `STRUCTURE_ONLY`: hoàn thành TH1, TH2, TH4A nhưng TH3 chưa runtime-test.
   - `WITH_FALLBACK`: có dùng schema/sample/media fallback; liệt kê rõ file.

---

## Câu hỏi phản tư

1. Trong ba cổng Script Review, Storyboard Review và Clip Review, cổng nào giúp bạn tiết kiệm credit nhiều nhất? Vì sao?
2. Clip của bạn có lỗi nào mà schema không thể phát hiện nhưng con người phát hiện được khi xem/nghe?
3. `SUCCESS` kỹ thuật và `APPROVED` nghiệp vụ đã được ghi tách biệt thế nào trong run log?
4. Nếu chạy đủ 6–9 scene, continuity nào dễ hỏng nhất: nhân vật, bối cảnh, ánh sáng, giọng hay nhịp dựng?
5. Nếu đưa engine vào production, bạn sẽ đặt cost guard, retry limit và nơi lưu media như thế nào?
6. Bạn đã xử lý quyền hình ảnh/giọng nói và dữ liệu nhạy cảm ra sao trước khi đưa bài lên repo?
