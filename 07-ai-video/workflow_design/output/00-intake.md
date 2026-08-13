# W0 — Intake (Use-case làm rõ)

> Workflow Design Package — Buổi 7 AI Video Production.
> Nguồn sự thật: `../../lab.md` (lab handout B7), `../../luong-nghiep-vu.md` (as-is nghiệp vụ gốc — nối tiếp bước 3 của `06-content-engine/luong-nghiep-vu.md`). Anonymize: use-case synthetic (tiếp nối Sunrise Kids ở Buổi 6), zero PII thật.

## Use-case

**Video Production Engine — biến kịch bản TikTok đã duyệt (Buổi 6) thành storyboard ảnh có cổng duyệt, rồi clip có native audio, bằng AI 4 lớp (schema → content artifact → media canary → engine spec).**

Cùng SME tiếp nối từ Buổi 6 (marketing 1 người kiêm nhiệm), giờ có kịch bản đã duyệt nhưng không dựng được video: không có người quay chuyên trách, không có diễn viên, không được dùng mặt trẻ em thật. Nghiệp vụ dựng video gốc (`../../luong-nghiep-vu.md`) đòi hỏi một đội chuyên trách (đạo diễn, quay phim, editor) mà SME nhỏ không có — nên thực tế của họ thường suy biến thành cách làm tự phát: gõ thẳng prompt vào công cụ sinh video, xem ra gì sửa nấy, không có bản thiết kế trước, không đếm chi phí.

## Phòng ban

Marketing/Content — người dùng cuối là người phụ trách content (thường kiêm nhiệm, tiếp nối vai trò ở Buổi 6), người duyệt ảnh/clip là chính người đó hoặc chủ doanh nghiệp.

## Ràng buộc compliance (constraint)

- Không clone mặt hoặc giọng người thật khi chưa có consent bằng văn bản — ràng buộc pháp lý, không phải tùy chọn kỹ thuật (`../../checkpoints/checkpoint-bt3.md`, `../../giao-an` AT3).
- Không dùng logo bên thứ ba, không dùng hình/nhạc/giọng thiếu quyền.
- Với nội dung liên quan trẻ em, kế thừa nguyên tắc Buổi 6: không dùng hình ảnh học viên/trẻ em thật khi chưa có đồng ý của phụ huynh — ảnh storyboard trong lab là AI sinh, style reference synthetic.
- Không bịa dữ kiện hay cam kết hiệu suất trong lời thoại — thiếu thì ghi `[cần bổ sung]`, kế thừa nguyên tắc Buổi 6.
- Chữ hiển thị trên hình: model không sinh — `image_prompt`/`video_prompt` cấm chữ, chữ chèn ở khâu dựng (giống Buổi 6: model viết sai chính tả tiếng Việt).
- **Không sinh video từ storyboard chưa duyệt** (AT1 giáo án B7) — cổng cứng: chỉ frame `APPROVED` mới cho clip chuyển `READY_TO_GENERATE`.
- **Không tuyên bố thành công nếu mới validate cấu trúc hoặc render UI** (AT2) — `media-run-log.json` bắt buộc có `runtime_evidence`, thiếu thì không được ghi `SUCCESS`.
- Kiểm soát chi phí trước batch run (AT3) — canary 2 scene, báo trước số lượt tạo ảnh/video dự kiến, trước khi chạy cả 6–9 cảnh.

## Mục tiêu đo được (KPI — từ lab.md + luong-nghiep-vu.md)

Chưa có số liệu vận hành thật (lab mới chạy trong lớp, chưa pilot ngoài đời) — các số dưới đây là khung tham chiếu để so sánh, không phải KPI đã đo:

- As-is (as chronicled trong `../../luong-nghiep-vu.md`): dựng video cần một chuỗi vai trò (đạo diễn/quay phim/diễn viên/editor) SME nhỏ không có; suy biến thực tế là tự phát dùng công cụ AI không quy trình — retry nhiều lần mỗi cảnh, không đếm chi phí, mất continuity giữa các cảnh, phần lớn video bỏ dở.
- To-be trong phạm vi lab: pipeline 4 lớp (schema → 6–9 scene có ID → storyboard ảnh có cổng duyệt → clip có audio chạy tuần tự) đóng gói thành `engine-spec.json` độc lập công cụ.
- Số giờ/video, credit/video, tỉ lệ clip cần dựng lại → **`[cần đo]`** sau khi chạy đủ 6–9 cảnh ngoài giờ lớp (bài tập về nhà, `../../lab.md` "Bài tập về nhà").

## Tool (theo lab.md)

- **Coding Agent** (Antigravity/Claude Code) có quyền ghi file và chạy JSON validation — sinh 3 schema, 3 content artifact, engine spec.
- **Google Flow** (demo chính cho TH3/TH4B) hoặc công cụ sinh ảnh/video khác (n8n/API, AI Studio, app nội bộ) — engine phải độc lập công cụ.
- Tài khoản có credit cho sinh ảnh và video có audio — GV chuẩn bị trước.

## Data contract (chain N→N+1, ID xuyên suốt `project_id → scene_id → frame_id → clip_id`)

`content-draft.json (B6_APPROVED) hoặc manual-script-input.md (MANUAL) → 3 schema + 3 sample (TH1) → video-script.json + storyboard.json + video-plan.json (TH2) → media canary 2 scene, ≥1 ảnh Approved, ≥1 clip có audio (TH3) → engine-spec.json (TH4A) → app/master prompt (TH4B)`.

Kế thừa bắt buộc: mỗi frame tham chiếu đúng một `scene_id` có thật; mỗi clip tham chiếu đúng `frame_id` đã `APPROVED`; clip chưa duyệt ảnh giữ trạng thái `BLOCKED`, không có đường vòng.

## Anonymizer note

Use-case dùng kịch bản `content-draft.json` synthetic của Sunrise Kids (từ Buổi 6) hoặc `../../templates/manual-script-input.md` (synthetic) → KHÔNG cần chạy `anonymizer.py`.
Nếu HV đổi sang sản phẩm thật của mình: không đưa dữ liệu khách hàng/hình ảnh thật (đặc biệt trẻ em) lên AI công cộng khi chưa có consent bằng văn bản.
