# W2 — Workflow Design: As-is → ESIA To-be

> Input: `01-usecase-matrix.md`. As-is nguồn sự thật duy nhất: `../../luong-nghiep-vu.md` (7 bước nghiệp vụ gốc, không rút gọn). To-be map vào chuỗi thật `../../lab.md` TH1→TH2→TH3→TH4A→TH4B.
> Output feeds W3 (`03-hardening.md`).

## 1. As-is — 7 bước (nguyên bản từ `luong-nghiep-vu.md`)

| # | Bước | Người thực hiện | Input | Output | Điểm nghẽn / Lỗi lặp |
|---|---|---|---|---|---|
| 1 | Nhận kịch bản đã duyệt | Content lead (B6) → Đạo diễn/dựng storyboard | `content-draft.json` (B6) — kịch bản TikTok 4 khối | Kịch bản xác nhận là input cố định | Ranh giới bàn giao thường bị phá — người dựng sau tự sửa lại lời thoại "cho hay hơn", làm sai lệch bản đã duyệt. |
| 2 | Storyboard hóa | Đạo diễn / người dựng storyboard | Kịch bản + ý định hình ảnh sơ bộ (`tiktok.khoi[].hinh_anh`) | Storyboard: khung hình, góc máy, chuyển động, style bible | SME nhỏ (marketing 1 người kiêm nhiệm) không có đạo diễn riêng — bước này thường **bị bỏ qua hoàn toàn**, nhảy thẳng sang bước 3. |
| 3 | Chuẩn bị & Quay (bối cảnh thật) | Quay phim / diễn viên | Storyboard đã chốt | Footage thô | Không đủ ngân sách thuê đội quay chuyên trách → thực tế suy biến thành **gõ thẳng prompt vào công cụ sinh video**, xem ra gì sửa nấy, retry 4–6 lần/cảnh, không ai đếm đã tốn bao nhiêu credit. |
| 4 | Dựng hậu kỳ | Editor hậu kỳ | Footage thô + audio | Bản dựng có hình + tiếng đồng bộ | Vì bước 2–3 đã suy biến (không storyboard, không style bible), **mỗi cảnh ra một nhân vật/bối cảnh/tông màu khác nhau** — ghép lại không ra một video; lời thoại đọc không kịp trong cảnh ngắn chỉ lộ ra ở bước này, đã dựng xong hết mới biết. |
| 5 | Duyệt nội bộ | Chủ doanh nghiệp / trưởng phòng marketing | Bản dựng | Approved hoặc yêu cầu sửa | Góp ý kiểu "cảnh đầu chưa cuốn" ở mức cả video, không ở mức từng cảnh → sửa gì cũng thành dựng lại gần hết; không lưu quan hệ scene→ảnh→clip nên không truy vết được. |
| 6 | Xuất bản & đăng | Content lead | Video đã duyệt | Video xuất hiện trên TikTok/Fanpage | Đăng tay, có kỳ quên đúng khung giờ vàng. |
| 7 | Đo lường & rút kinh nghiệm | *(không ai làm)* | View, completion rate, share, comment | Bài học cho kịch bản/storyboard kỳ sau | Không ai tổng hợp — mỗi video lại lặp lại đúng lỗi continuity/chi phí cũ. |

> Nguồn: `../../luong-nghiep-vu.md` — tài liệu nghiệp vụ gốc, giữ nguyên 7 bước, không rút gọn. Chi tiết "suy biến thực tế" (retry mù, mất continuity, không đếm chi phí) đối chiếu với ghi nhận thật ở `v2.0-workflow-mindset/Output_B7/02a-workflow-as-is.md`.

## 2. To-be — ESIA (chỉ trong phạm vi lab: Bước 1–5 của as-is → TH1→TH2→TH3→TH4A→TH4B)

| Bước to-be | E/S/I/A | Chi tiết tối ưu & HITL | Ai làm | Nhánh automation |
|---|---|---|---|---|
| Chuẩn hoá 2 đường input về `video-script.json` (bước 1) | **I** | `B6_APPROVED` và `MANUAL` đi qua 2 adapter khác nhau, về CÙNG một cấu trúc — phần sau không cần biết nguồn nào | AI+Người | n8n (2 input adapter) |
| Sinh 3 schema + 3 sample, validate PASS (TH1) | **A** | Do prompt sinh ra rồi validate, **không dùng schema viết tay từ trước**; `additionalProperties:false` chặn trường lạ | AI Agent | AI Agent |
| Chia kịch bản → 6–9 scene có ID + thời lượng, thay bước 2 (TH2) | **A** | Thay "tự hình dung trong đầu" hoặc bỏ hẳn khâu storyboard; mỗi scene thuộc đúng 1 block nguồn, có `scene_id` | AI Agent | AI Agent |
| Kiểm lời thoại vừa thời lượng | **A** | Luật cứng số từ/giây, deterministic — sai thì viết lại lời, không kéo dài cảnh | n8n (không LLM) | n8n (Code node) |
| Nạp style bible dùng chung (thay việc mỗi cảnh tự sinh thế giới riêng) | **S** | 1 file nhân vật/bối cảnh/tông màu/9:16, nạp vào mọi `image_prompt`+`video_prompt` | n8n | n8n (Set node) |
| Sinh `storyboard.json` + ảnh từng frame, thay bước 2-3 (TH2/TH3) | **A** | Mỗi frame tham chiếu 1 scene có thật; `image_prompt` không chứa chữ hiển thị, không mô tả người thật cụ thể | AI Agent + API ảnh | AI Agent |
| **Người duyệt từng ảnh: APPROVED/NEEDS_REVIEW** (thay bước 5 ở mức ảnh) | **HITL** | AI không được tự APPROVE; kiểm continuity, bố cục, an toàn/quyền, mục cấm — cổng chặn chi phí quan trọng nhất | **Người** | App duyệt |
| Cổng cứng: chỉ frame Approved mới mở clip | **A** | `APPROVED` → clip `READY_TO_GENERATE` + chép `image_asset_ref`; chưa duyệt → `BLOCKED`, không có ngoại lệ | n8n | n8n (IF node) |
| Canary 2 scene trước khi batch | **A** | Báo trước số lượt tạo ảnh/video dự kiến; canary chưa PASS thì không batch 6–9 | n8n + Người | n8n (nhánh canary) |
| Video Generator tổng, chạy tuần tự, thay bước 3-4 (TH3) | **I** | 1 node xử lý tuần tự danh sách `READY_TO_GENERATE`; `video_prompt` có cả hình và audio (dialogue/language/voice/ambient/SFX/music/negative audio) | n8n + API video | n8n (Loop) |
| Per-clip state + retry riêng | **A** | `BLOCKED→READY_TO_GENERATE→RUNNING→DONE/FAILED`; một clip lỗi không xóa kết quả scene khác | n8n | n8n (Code node) |
| **Người kiểm clip: hình, thoại, âm nền** (thay bước 5 ở mức clip) | **HITL** | Nghe rõ lời thoại, đúng giọng/ngôn ngữ, ambience không lấn thoại, không âm thanh cấm — máy không tự chấm được | **Người** | App duyệt |
| Ghi `media-run-log.json` + sổ chi phí | **A** | run_id, scene, status, retry_count, `runtime_evidence` bắt buộc — không có bằng chứng thì không ghi `SUCCESS` | n8n | n8n (ghi file) |
| Đóng gói `engine-spec.json` độc lập công cụ (TH4A) | **S** | Node/port/edge, 2 input adapter, per-clip state, test case, cost guard — đổi công cụ chỉ thay adapter | AI Agent + Người | AI Agent |
| App node-based hỗ trợ vận hành (TH4B) | **S** | Đọc `engine-spec.json`, không tự đổi data contract; canvas/node/edge/status/preview | AI Agent | App vibe coding |

**HITL note (kế thừa nguyên tắc B6, viết lại đúng cho buổi 7):** Hai cổng người quyết định KHÔNG thể bỏ qua — duyệt ảnh trước khi dựng clip (rẻ hơn, phát hiện sớm) và nghe/xem clip trước khi coi là xong. AI không được tự APPROVE ở cả hai cổng. Bước 6–7 (đăng, đo lường) **không nằm trong to-be này** — engine kết thúc ở bộ clip + run log, người ghép/chèn chữ/đăng, đúng nguyên tắc "AI tạo nháp, người duyệt" đã học ở B6 (`../../lab.md` §AT1-AT2).

## 3. Phạm vi bị cắt — ghi rõ, không giả vờ đã thiết kế

| Bước as-is | Vì sao KHÔNG có trong to-be trên | Xử lý |
|---|---|---|
| 6 — Xuất bản & đăng | Chủ đích của lab: engine kết thúc ở bộ clip đã dựng + run log; ghép/chèn chữ/đăng do người thực hiện (`../../lab.md` "Bài tập về nhà"; giáo án AT1/AT2) | Ghi nhận là **mở rộng giai đoạn sau** trong `06-leadership-deck.md`, không đưa vào hardening/mermaid ở package này |
| 7 — Đo lường & rút kinh nghiệm | Cần dữ liệu chạy thật một thời gian, phụ thuộc API nền tảng — ngoài phạm vi 120 phút của lab, giống bước 7 của Buổi 6 | Ghi nhận là **mở rộng giai đoạn sau**, đề xuất ở leadership deck, không bịa số liệu đo lường chưa có |
| Clone mặt/giọng người thật | Vấn đề quyền và đạo đức, không phải độ khó kỹ thuật — không có consent bằng văn bản thì không làm | Cấm tuyệt đối trong ràng buộc dự án (`00-intake.md`), kiểm ở checklist duyệt ảnh/clip, không có nhánh automation nào cho việc này |
