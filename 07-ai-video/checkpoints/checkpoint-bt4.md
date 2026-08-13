# Checkpoint TH4 — Engine và app hỗ trợ

## 4A bắt buộc

- [ ] `engine-spec.json` + schema PASS.
- [ ] Hai input adapter về một contract.
- [ ] Một Video Generator tổng chạy tuần tự.
- [ ] Retry một scene không reset scene khác.
- [ ] Có approval, log, cost guard và test cases.
- [ ] Độc lập công cụ.

## 4B hỗ trợ

- [ ] App đọc engine spec, không tự nghĩ lại nghiệp vụ.
- [ ] Canvas/node/edge/status/preview hoạt động.
- [ ] 6–9 storyboard cards.
- [ ] Progress tổng + state từng clip.
- [ ] Không hardcode key/pseudo API.
- [ ] Phân biệt UI rendered với runtime success.

Mốc chặn: ưu tiên hoàn thành 4A. Nếu hết giờ, nộp master prompt 4B và sơ đồ node; không cắt engine spec.

## ✅ Đã validate trên instance thật — REV2, kiến trúc hiện tại (2026-08-12)

**Đổi hướng so với REV1 (xem lịch sử bên dưới):** REV1 dùng Kling sinh hình câm + OpenRouter TTS rời + mux bằng ffmpeg — gặp 2 vấn đề thật khi dùng lại: (1) mỗi lần TTS đọc một kiểu, không đồng nhất giữa các clip dù cùng `voice_preset`, (2) độ dài audio do TTS tự quyết, không khớp `duration_seconds` của clip. Sau khi test thật, chuyển sang **Veo sinh audio GỐC kèm video** (không TTS rời, không mux) — giải quyết cả 2 vấn đề, đổi lại chấp nhận watermark cứng của Veo (xem mục "Đánh đổi đã chấp nhận" bên dưới) và giới hạn `duration` chỉ 4/6/8 giây.

`checkpoints/n8n-video-engine-solution.json` (43 node) — workflow `B7 K1 - Video Engine` (id `0elgaDRlwTBu13IS`) trên `n8n-qns0.srv1741374.hstgr.cloud`.

**Kiến trúc:** 1 workflow, 4 webhook stateless:

1. `POST /b7/plan` — 3 bước AI nối tiếp (Gemini `gemini-3.1-flash-lite`):
   - **Scene Planner** — sinh `video_script.scenes[]`.
   - **Storyboard Generator** — sinh `storyboard.frames[]` (composition/image_prompt) VÀ **`storyboard.voice_bible`** — 1 mô tả giọng DUY NHẤT (giới tính/chất giọng/tốc độ/phong cách, tiếng Anh) dùng LẶP LẠI Y NGUYÊN ở mọi clip để giữ giọng đồng nhất xuyên suốt video (khác REV1 vốn để mỗi scene tự chọn 1 giọng preset khác nhau).
   - **Video Plan Generator** — sinh `video_plan.clips[]`, mỗi clip có sẵn `video_prompt` GỬI THẲNG cho Veo (đã nhúng: chuyển động tiếp nối đúng frame + câu bắt buộc "OFF-SCREEN VOICE-OVER NARRATION ONLY, narrator never shown on screen" + `voice_bible.description` y nguyên + dialogue trong ngoặc kép + ghi chú nhịp đọc), `negative_prompt` (luôn có visible speaker/person/face/hands/on-screen text + `style_bible.forbidden_elements`), và `audio` (8 field theo đúng `video-plan.schema.json`, dùng để người đọc duyệt kịch bản — không dùng để gọi TTS nữa). **Duration mỗi clip bị ép về giá trị gần nhất trong {4, 6, 8}** (giới hạn cứng API Veo — xem mục lỗi bên dưới) ngay trong node Code gộp kết quả, không phải do AI tự chọn.
   - Trả `{video_script, storyboard, video_plan}`.
2. `POST /b7/generate-image` — **cổng mới**: chặn (HTTP 400) nếu `script_approved !== true` — bắt buộc người đã duyệt kịch bản chi tiết (đọc dialogue + video_prompt từng clip trong app) trước khi được sinh ảnh. Qua cổng: GeminiGen `nano-banana-pro`, vòng lặp Wait 55s → Poll → IF (tối đa 3 lần). Trả `image_asset_ref` + status `NEEDS_REVIEW` — KHÔNG tự APPROVE.
3. `POST /b7/generate-clip` — cổng cứng IF chặn nếu `frame_status !== 'APPROVED'`. Qua cổng: **GeminiGen Veo (`veo-3.1-fast`)**, gửi thẳng `video_prompt`/`negative_prompt`/`duration` đã dựng sẵn từ Vùng 1, vòng lặp Wait 30s × tối đa 10 lần (~5 phút, Veo chậm hơn Kling). Trả `clip_asset_ref` — **video ĐÃ CÓ audio thật**, `status: SUCCESS` trực tiếp — không còn bước preview/duyệt-audio/mux riêng như REV1 vì không còn gì để mux.
4. `POST /b7/assemble` — tải N `clip_asset_ref` (đã có audio) → base64 → `ffmpeg-helper-b7` `/concat` → trả `final_video_ref`. Không mux, chỉ nối.

**Test thật ngày 2026-08-12 (REV2):**
- `/b7/plan`: `voice_bible.description` là 1 mô tả duy nhất (không đổi theo scene); mỗi clip có `duration_seconds` ∈ {4,6,8} đúng luật; `video_prompt` có đủ câu "OFF-SCREEN VOICE-OVER NARRATION ONLY..." + voice_bible + dialogue.
- Cổng `script_approved`: gọi `/b7/generate-image` với `script_approved:false` → HTTP 400 đúng.
- `/b7/generate-clip` (Veo): **status SUCCESS thật**, tải `clip_asset_ref` xuống — video 1080×1920, H.264+AAC, đúng 4.0s (khớp duration đã ép). Tách audio bằng ffmpeg, transcribe bằng `faster-whisper` (model `small`, chạy local, không đoán mò): phát hiện ngôn ngữ **tiếng Việt, độ tin cậy 99.76%**, transcript khớp sát dialogue gốc (sai lệch nhỏ do Whisper nghe nhầm âm gần giống, không phải Veo đọc sai).
- Trích khung hình giữa clip: xác nhận **không có người/tay xuất hiện** (giữ đúng bố cục ảnh đã duyệt — chỉ có màn hình + con trỏ, đúng chỉ dẫn off-screen narration + negative_prompt), watermark Veo (sparkle + "Veo", góc dưới phải) **vẫn còn** — đã xác nhận không prompt bỏ được (xem mục "Đánh đổi đã chấp nhận").
- App test `app-video-engine-test.html` viết lại: thêm card "Bước 2 — Duyệt kịch bản chi tiết" (hiện voice_bible + dialogue + delivery + video_prompt từng clip, khoá cho tới khi bấm Duyệt), bỏ hẳn UI duyệt-audio-riêng. Verify qua Playwright: card duyệt kịch bản hiện đúng, bấm Duyệt → `state.scriptApproved=true`, card sinh ảnh/clip mở khoá đúng lúc, 0 lỗi console.

**Lỗi/giới hạn thật phát hiện khi build REV2:**
1. **API Veo chỉ nhận `duration` ∈ {4, 6, 8} giây** (`INVALID_DURATION` nếu gửi giá trị khác, đã bắt được qua test thật) — khác Kling nhận tự do 3-10s. Đã xử lý bằng ép tròn về giá trị gần nhất ngay khi gộp kế hoạch, KHÔNG để lệch tới lúc gọi video-gen mới phát hiện.
2. **Veo khi nhận mô tả lời thoại trong prompt có xu hướng tự vẽ thêm 1 người đang nói vào khung hình** dù ảnh tham chiếu không có người — phá vỡ tính nhất quán với ảnh đã duyệt. Đã sửa bằng cách bắt buộc câu "OFF-SCREEN VOICE-OVER NARRATION ONLY, narrator never shown on screen" + `negative_prompt` liệt kê rõ visible speaker/person/face/hands — test lại xác nhận hết người thừa.
3. **Watermark Veo (sparkle icon + chữ "Veo") không xoá được bằng prompt/negative_prompt** — đã thử cả hai lần test, cùng xuất hiện. Xác nhận đây là nhãn xác thực nội dung AI-sinh Google cố tình gắn cứng, không phải lỗi ngẫu nhiên. **Đánh đổi đã được người ra quyết định (Giang) chấp nhận ngày 2026-08-12**: dùng Veo để đổi lấy audio đồng bộ + giọng đồng nhất, chấp nhận watermark như nhãn AI-sinh minh bạch — phù hợp bài giảng, cần cân nhắc lại nếu dùng cho sản phẩm thương mại cuối cùng.
4. **`video_prompt` do LLM sinh đôi khi tự ghi số giây cụ thể** (vd "fit exactly 5 seconds") dựa trên `duration_seconds` GỐC của scene, trong khi giá trị GỬI THẬT cho Veo đã bị ép tròn khác đi (vd 4s) ở bước sau — lệch nhẹ giữa lời chú thích trong prompt và duration thật gửi API. CHƯA sửa (cần ép tròn duration TRƯỚC khi cho LLM viết video_prompt, không phải sau).
5. **[ĐÃ SỬA 2026-08-13]** `/b7/assemble` (Vùng 4) chưa từng được test thật trong REV2 (mục test 2026-08-12 ở trên chỉ dừng ở `/b7/generate-clip`) — khi test thật (execution `1063` trên instance thật, 2026-08-13 13:26) lộ lỗi **preview video cuối hỏng ở frontend**. Đã kiểm bằng cách curl thẳng n8n REST API (`GET /api/v1/executions/1063?includeData=true`) đọc `runData` từng node thay vì đoán — root cause thật (đã loại bỏ giả thuyết ban đầu về `-c copy` lệch codec, kiểm tra thực tế cho thấy KHÔNG phải vậy):
   - Node `Chuẩn hoá kết quả clip (đã lưu Drive)` (mới thêm cùng ngày 2026-08-13, xem sticky note "Lưu ảnh + clip lẻ vào Drive") ghi đè `clip_asset_ref` bằng `https://drive.google.com/file/d/{id}/preview` — URL này chỉ dùng được cho `<iframe>` xem trên trình duyệt (cần phiên đăng nhập Google), KHÔNG phải link tải file trực tiếp.
   - Node `Tải từng clip` ở Vùng 4 gọi HTTP GET thẳng vào URL đó để tải về ghép — xác nhận qua execution 1063: **cả 7/7 clip tải về đều là `text/html` ~72KB** (trang xem trước của Drive), không phải MP4 thật.
   - `ffmpeg-helper-b7 /concat` nhận 7 file HTML giả làm `.mp4` → lỗi thật `moov atom not found` / `Invalid data found when processing input` → trả 502 kèm JSON lỗi.
   - Node HTTP `Nối clip (ffmpeg-helper-b7 /concat)` có `neverError:true` + `responseFormat:'file'`, nên khi 502 xảy ra, body lỗi (JSON) vẫn bị nhét vào `binary.final` y như file video thật; node Code `Video cuối -> base64` chỉ check `binary.final` có tồn tại (không check mimeType) → đóng gói JSON lỗi (`{"detail":"ffmpeg concat failed:..."}`) thành `data:video/mp4;base64,...`, trả `assemble_ok:true` giả (đã giải mã base64 xác nhận đúng nội dung này). Frontend tin `assemble_ok`, gán thẳng `<video src>` → trình duyệt không phát được, lỗi âm thầm không rõ nguyên nhân.
   - Sửa gốc: node `Chuẩn hoá kết quả clip (đã lưu Drive)` — `clip_asset_ref` trả về link tạm GeminiGen (`$('Kiểm trạng thái video (GeminiGen)').item.json.generated_video[0].video_url`, tải trực tiếp được, đúng thiết kế cũ trước khi thêm lưu Drive), tách link Drive `/preview` ra field `clip_drive_ref` riêng (app đã có sẵn chỗ nhận field này ở `ghepVideoCuoi()`, trước đó luôn `null` vì backend chưa từng set).
   - Sửa an toàn (giữ lại phòng hờ lỗi tương tự tái diễn ở nguồn khác): `n8n-video-engine-solution.json` node `Video cuối -> base64` thêm check `binary.final.mimeType` phải bắt đầu bằng `video/` trước khi coi là thành công, nếu không trả lỗi thật (trích nội dung lỗi) thay vì `assemble_ok` giả; `ffmpeg-helper-b7-app.py` `/concat` thêm fallback re-encode (`-c:v libx264 -c:a aac`) khi `-c copy` fail vì lý do khác (vẫn hữu ích dù không phải nguyên nhân lần này).
   - **Chưa làm:** import lại workflow đã sửa vào instance `n8n-qns0.srv1741374.hstgr.cloud` (sửa file trong repo không tự cập nhật workflow đang chạy) và rebuild lại container `ffmpeg-helper-b7`, rồi test lại `/b7/assemble` thật để xác nhận hết lỗi preview.
   - Ngoài phạm vi assemble: cùng phiên kiểm tra qua API phát hiện thêm 2 việc trên instance thật — (a) node `Scene Planner` gọi Gemini `gemini-3.1-flash-lite` từng lỗi thật `503 Service Unavailable` (Google quá tải, không phải lỗi cấu hình) ở execution `1064`, node này KHÔNG có `retryOnFail` nên 1 lần 503 thoáng qua là chết cả `/b7/plan` — nên bật retry tự động; (b) node fallback `Sinh ảnh qua OpenRouter` từng lỗi `Credential REPLACE_CREDENTIAL_ID does not exist` ở 6 execution liên tiếp (13:09-13:11) — đã tự sửa (credential `Openrouter` thật đã được gắn trước 13:35), không cần làm gì thêm.

**Vẫn CHƯA làm (REV2):**
- Mục 4 ở trên (ép duration trước khi LLM viết prompt, tránh lệch chú thích giây).
- Chưa nghe thử toàn bộ 8 giọng có thể có trong `voice_bible` — mới nghe-xác-nhận qua Whisper 2 giọng khác nhau (2 lần test), chưa test toàn bộ dải mô tả giọng nam/nữ mà voice_bible có thể sinh ra.
- `ref_images` gửi Veo dùng link tạm GeminiGen (hết hạn ~7 ngày).
- Response trả base64 inline trong JSON — chấp nhận cho demo/lab, sản xuất thật nên đổi sang lưu Drive.
- Chưa có script validate tĩnh tương đương `validate-b6-n8n-app.py`.
- `checkpoints/app-video-engine-test.html` là test harness tuyến tính, CHƯA phải app node-based đúng chuẩn TH4B.
- Chưa build bước loop tự động gọi `/b7/generate-image` + `/b7/generate-clip` cho đủ 6-9 scene liên tiếp — hiện phải bấm tay từng nút trên app test cho mỗi clip.
- Container `ffmpeg-helper-b7` vẫn còn endpoint `/mux` từ REV1 (không dùng nữa vì Veo không cần mux) — để lại không gây hại, có thể dọn sau.

---

## 📜 REV1 — lịch sử (đã thay thế bởi REV2 ở trên, giữ lại để biết đã thử và tại sao đổi hướng)

`checkpoints/n8n-video-engine-solution.json` (51 node) đã chạy thật end-to-end trên instance n8n thật (cùng instance với B6: `n8n-qns0.srv1741374.hstgr.cloud`, workflow `B7 K1 - Video Engine`, id `0elgaDRlwTBu13IS`), khác với TH1-TH4A vốn chỉ chạy qua prompt/agent không giữ trạng thái. Workflow này là bản hiện thực hoá kiến trúc hybrid n8n từ `workflow_design/output/workflow-design-doc.md` mục 2 (n8n lo điều phối/cổng cứng, AI Agent lo sinh nội dung, App lo HITL) — KHÔNG thay thế TH1-TH4B của lab, là bản production tham khảo thêm.

**Kiến trúc:** 1 workflow, 5 webhook stateless (không giữ state phía server — client/app tự lưu và gửi lại, đúng tinh thần "engine độc lập công cụ" của `bt4a-prompt.md`):

1. `POST /b7/plan` — 3 bước AI nối tiếp: **Scene Planner** (chainLlm, sinh scenes) → **Storyboard Generator** (chainLlm, sinh frames + image_prompt) → **Video Plan Generator** (chainLlm, sinh `video_plan.clips[]` — mỗi clip có `video_prompt` VÀ audio directive riêng: `dialogue` giữ nguyên văn, `voice_profile`/`delivery` mô tả cách đọc PHÙ HỢP NGỮ CẢNH từng scene, `voice_preset` chọn 1 trong 8 giọng preset cố định của model — không còn hardcode 1 giọng chung cho mọi clip). Cả 3 dùng Gemini `gemini-3.1-flash-lite`. Trả `{video_script, storyboard, video_plan}`.
2. `POST /b7/generate-image` — GeminiGen `nano-banana-pro`, vòng lặp Wait 55s → Poll → IF (tối đa 3 lần, giống B6). Trả `image_asset_ref` + status `NEEDS_REVIEW` — KHÔNG tự APPROVE.
3. `POST /b7/generate-clip` — cổng cứng IF chặn nếu `frame_status !== 'APPROVED'` (test xác nhận: trả đúng HTTP 400 kèm lý do). Qua cổng: GeminiGen Kling (`kling-video-3-0`) sinh video, vòng lặp Wait 30s × tối đa 8 lần (~4 phút); song song sinh thoại tiếng Việt qua OpenRouter `openai/gpt-audio-mini` — **dùng đúng `audio.voice_preset` do AI Video Plan Generator chọn** (không còn cứng `alloy`). Trả `status: NEEDS_REVIEW` (KHÔNG tự mux nữa), `video_asset_ref` (video câm), `audio_asset_ref` (data URI WAV riêng), `audio_transcript`.
4. `POST /b7/approve-clip` — **cổng HITL thứ 2** (mới thêm): người nghe/xem preview từ bước 3 rồi mới quyết định. `decision !== 'APPROVED'` → trả `NEEDS_REVIEW`, không mux. `decision === 'APPROVED'` → ghép (mux) audio vào video qua service `ffmpeg-helper-b7` → trả `muxed_clip_ref` (data URI MP4 đã có tiếng, `status: SUCCESS`) — dùng cái này cho bước ráp cuối.
5. `POST /b7/assemble` — nhận mảng `muxed_clip_refs` (đúng thứ tự scene, N clip 6-9) → nối thành 1 video hoàn chỉnh qua `ffmpeg-helper-b7` `/concat`. Trả `final_video_ref` (data URI MP4).

**Sửa 3 lỗ hổng phát hiện qua review 2026-08-12 (trước đó pipeline "chạy được" nhưng sai thiết kế):**
- Audio directive (voice/delivery/ambient...) trước đây do **client tự bịa giống nhau cho mọi clip** (không AI sinh, không phân biệt HOOK/CTA) → sửa bằng bước Video Plan Generator ở trên.
- `voice` gửi OpenRouter trước đây hardcode `'alloy'` bất kể `voice_profile` mô tả gì → sửa dùng `audio.voice_preset` động. Test thật: 6 scene ra 6 preset khác nhau (`ash/echo/sage/alloy/shimmer/ballad`), delivery bám đúng ngữ cảnh (HOOK nhấn mạnh, CTA truyền cảm hứng).
- Audio sinh xong trước đây **tự mux luôn**, không ai nghe qua — đúng lúc đó lộ lỗi model tự thêm lời dẫn thừa ("Tất nhiên, tôi sẽ đọc theo yêu cầu của bạn:...") lọt thẳng vào clip cuối. Sửa bằng cổng `/b7/approve-clip` — tách generate (preview) khỏi mux (chỉ chạy sau khi người duyệt Approved). Tác dụng phụ: prompt audio siết lại rõ hơn ("KHÔNG tự thêm lời dẫn") cũng giúp transcript sạch hơn hẳn ở lần test lại.

**Service `ffmpeg-helper-b7` (mới, container riêng trên server n8n):**

Server n8n (`31.97.220.195`) vốn đã có 1 container `ffmpeg-helper` (FastAPI + ffmpeg 7.1.5) chạy trên mạng docker `n8n-qns0_default`, nhưng nó dựng cho việc khác (ghép audio tải từ URL Facebook vào video quay — endpoint `/merge`), không khớp việc B7 cần (ghép 2 file mình tự có). Đã dựng **container riêng** `ffmpeg-helper-b7` (không đụng vào container cũ đang phục vụ workflow khác), build từ `/opt/ffmpeg-helper-b7/` trên cùng server, cùng mạng docker (n8n gọi thẳng qua `http://ffmpeg-helper-b7:8080`, không cần expose port ra ngoài). 2 endpoint:
- `POST /mux` — multipart 2 file `video` + `audio` → ffmpeg `-map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` → trả MP4.
- `POST /concat` — JSON `{videos_base64: [...]}` (đổi từ multipart nhiều file cùng tên sang JSON vì n8n không dễ gộp nhiều item thành 1 multipart request nhiều field cùng tên) → ffmpeg `-f concat -safe 0 -c copy` → trả MP4.

**Test thật ngày 2026-08-12** (canary scene SC-01/FR-01/CLIP-01, chủ đề "Không phải cứ AI Automation là n8n"):
- `/b7/plan`: nhiều lần chạy ra 5-6 scene (HOOK/PROBLEM/SOLUTION×2-3/CTA) + frame với image_prompt đúng schema; `video_plan.clips[]` có `voice_preset` khác nhau theo ngữ cảnh (vd lần chạy 6 scene ra `ash/echo/sage/alloy/shimmer/ballad`), `delivery` bám đúng block (HOOK nhấn mạnh, CTA truyền cảm hứng) — xem mục "3 lỗ hổng" bên trên.
- `/b7/generate-image`: ảnh PNG thật 1536×2752, tải xuống xác nhận đúng nội dung (màn hình workflow rối như prompt yêu cầu).
- `/b7/generate-clip` (gate DRAFT bị chặn đúng, HTTP 400): trả `status: NEEDS_REVIEW`, video MP4 câm thật 716×1284 5.04s H.264 (`video_asset_ref`), audio WAV thật 24kHz mono PCM16 6.6s (`audio_asset_ref`) — transcript SẠCH, không còn lời dẫn thừa sau khi dùng `voice_preset` động + prompt siết lại.
- `/b7/approve-clip` (`decision: NEEDS_REVIEW` → trả `NEEDS_REVIEW`, không mux — test xác nhận đúng): với `decision: APPROVED` → ghép qua `ffmpeg-helper-b7`, trả `muxed_clip_ref` thật có cả 2 track (H.264+AAC), 5.04s — tải + ffprobe xác nhận.
- `/b7/assemble` (2 bản của cùng 1 muxed clip, giả lập 2 scene): trả video cuối 10.13s (~2×5.04s) — tải + ffprobe xác nhận nối đúng, không hỏng.
- Thử thêm ngoài phạm vi B7 gốc: gọi Veo 3.1 (`veo-3.1-fast`) qua GeminiGen với **chỉ 1 ảnh tham chiếu** (không cần 2 frame start/end như tài liệu `Agent_Video_AI` mô tả cho ca dùng khác) — ra video 1080p thật, 8s, nhưng chậm hơn Kling (~135s so với ~90s) và **nghi có watermark** dù field `has_watermark:0` — chưa dùng chính thức trong workflow, cần kiểm kỹ trước khi đổi mặc định.
- App test `checkpoints/app-video-engine-test.html` — verify qua Playwright (headless), gọi thật `/b7/plan`, render đúng frame card + voice_preset, 0 lỗi console (screenshot lưu trong quá trình review, không commit vào repo).

**Lỗi thật đã gặp và sửa (đáng biết trước khi dạy hoặc tái sử dụng):**
1. **`responseCode` phải nằm trong `options`, không phải gốc `parameters`** — giống hệt gotcha #9 của B6, lặp lại đúng lỗi cũ. Node "Trả lỗi — frame chưa duyệt" ban đầu trả sai HTTP 200 dù body đúng nội dung lỗi.
2. **Gửi JSON body trong node httpRequest phải dùng `specifyBody: "json"`, không phải `contentType: "json"`** — dùng sai tên field khiến OpenRouter nhận request rỗng ("Input required: specify prompt or messages").
3. **OpenRouter `openai/gpt-audio-mini` bắt buộc `stream: true` để có audio output**, và khi `stream: true` thì `audio.format` CHỈ nhận `pcm16` (không phải `mp3`). Response trả về là SSE (`data: {...}\n\n` nhiều dòng), không phải 1 JSON. Phải thêm Code node parse từng dòng SSE, gộp base64 PCM16 chunks, tự dựng header WAV 44-byte (24000Hz/mono/16-bit) — n8n không có node dựng sẵn cho việc này.
4. **[ĐÃ SỬA]** Audio model đôi khi tự thêm lời dẫn ("Tất nhiên, tôi sẽ đọc theo yêu cầu của bạn:...") trước khi đọc thoại thật — sửa bằng cách siết prompt Video Plan Generator ("KHÔNG tự thêm lời dẫn/lời chào") + thêm cổng duyệt `/b7/approve-clip` để bắt được nếu vẫn lọt.
5. **`/concat` ban đầu thiết kế multipart nhiều file cùng tên field** (`videos`) — n8n's httpRequest node chạy 1 request/item, không tự gộp N item thành 1 multipart nhiều field cùng tên. Đổi endpoint sang nhận JSON `{videos_base64: [...]}`, đơn giản và chắc chắn hơn hẳn.

**Vẫn CHƯA làm (ghi rõ để không lẫn với đã xong):**
- **Scene Planner đôi khi ra ngoài khoảng 6-9 scene yêu cầu của schema** (1 lần test ra đúng 5) — chưa có validate/retry tự động ép đúng khoảng, hiện chỉ phát hiện khi người đọc kết quả.
- Chưa xác nhận danh sách đầy đủ giọng preset thật của `openai/gpt-audio-mini` qua OpenRouter — mới test thật 1 giọng (`ash`), 5 giọng còn lại AI chọn (`echo/sage/alloy/shimmer/ballad`) mới dừng ở việc model trả về hợp lệ theo enum, CHƯA nghe thử để xác nhận đúng đặc điểm mô tả (nam/nữ, trầm/cao) như `voice_profile` yêu cầu.
- `ref_images` gửi sang Kling/Veo dùng link tạm GeminiGen (hết hạn ~7 ngày) — đủ cho một buổi học nhưng không nên coi là lưu trữ lâu dài; nên tải về/lưu Drive như B6 đã làm cho ảnh.
- Response trả base64 inline trong JSON (vài MB/clip, ~11MB cho `/b7/assemble` 2 clip) — chấp nhận được cho demo/lab, sản xuất thật nên đổi sang lưu Drive/object storage rồi trả link.
- Chưa có script validate tĩnh tương đương `validate-b6-n8n-app.py`.
- `checkpoints/app-video-engine-test.html` là test harness tuyến tính (form → gọi webhook → xem kết quả), CHƯA phải app node-based đúng chuẩn TH4B (chưa có canvas/pan/zoom/minimap).
- Chưa kết luận watermark Veo — nếu xác nhận có thật, cần loại Veo khỏi lựa chọn mặc định (đang dùng Kling).
- Chưa build bước loop tự động gọi `/b7/generate-clip` + `/b7/approve-clip` cho đủ 6-9 scene liên tiếp — hiện phải gọi tay/từng nút bấm trên app test cho mỗi clip.

