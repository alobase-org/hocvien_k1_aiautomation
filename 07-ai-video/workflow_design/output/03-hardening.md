# W3 — Production Hardening (4 lớp + kiểm chứng bằng checklist thật)

> Input: `02-as-is-tobe.md`. Nguồn fallback/edge case thật: `../../checkpoints/checkpoint-bt1.md` đến `checkpoint-bt4.md` (rescue map GV/TA), `../../checkpoints/reference-schemas/` (fallback schema), `../../fallback-inputs/video-script-sample.json`. Đối chiếu kiến trúc: `v2.0-workflow-mindset/Output_B7/03-production-hardening.md`.
> Output feeds W4 (`04-mermaid.mmd`).

## 1. Bảng hardening theo từng bước to-be

| Bước to-be | Fallback | Execution log | Edge case | HITL | Kiểm chứng bằng |
|---|---|---|---|---|---|
| Sinh 3 schema + sample (TH1) | Chỉ in JSON trong chat → ép ghi file thật; kẹt >10' → cấp `checkpoints/reference-schemas/*.schema.json` (`checkpoint-bt1.md`) | `schema_validation: PASS/FAIL`, số lần sinh lại | Schema khoá tiêu chí nghệ thuật bằng regex → tách thành `quality_checklist`, không kiểm bằng schema; thiếu native audio → bổ sung dialogue/language/voice_profile/delivery/ambient/sound_effects/music/negative_audio | Không | **KHÔNG CÓ test tự động** — checklist thủ công `checkpoint-bt1.md` (4 mục) |
| Chia 6–9 scene + storyboard + video plan (TH2) | Fallback `fallback-inputs/video-script-sample.json` (`checkpoint-bt2.md`) | `project_id`, số scene/frame/clip, ID cross-reference | Scene/frame/clip mồ côi (tham chiếu ID không tồn tại) → FAIL, không cho đi tiếp; frame ban đầu phải `DRAFT`, clip ban đầu phải `BLOCKED` | Không bắt buộc ở lớp JSON | **KHÔNG CÓ test tự động** — checklist thủ công `checkpoint-bt2.md` (7 mục), rescue quan trọng: "sửa đúng artifact đang FAIL, không đổi ID hay chia lại từ đầu" |
| Media canary — sinh ảnh + duyệt + sinh clip (TH3) | Video chậm → dùng clip fallback nhưng bắt buộc ghi `NOT_RUNTIME_TESTED`, không được ghi `SUCCESS` (`checkpoint-bt3.md`) | `media-run-log.json`: chỉ chạy 2 scene trước, ảnh/asset ref, clip nào lấy đúng `image_asset_ref` của frame nào | Ảnh API lỗi/quota → coi là chưa PASS canary, không tự chuyển sang clip; người dùng chưa duyệt ảnh nào → không có clip nào được sinh | **Bắt buộc** — người duyệt ≥1 ảnh trước khi cho phép sinh clip; đây là cổng chặn chi phí quan trọng nhất | **KHÔNG CÓ test tự động** — checklist thủ công `checkpoint-bt3.md` (6 mục) |
| Đóng gói `engine-spec.json` (TH4A) | Canary chưa tạo được clip thật → ghi `BLOCKED` trong engine spec, không tự suy diễn là chạy được | `engine-validation-report.md`, sơ đồ Mermaid ngắn trong `engine-spec.md` | Engine mô tả tính năng chưa từng chạy thật → đánh dấu `NOT_RUNTIME_TESTED`, không ghi là đã chạy | Có — người rà lại trước khi chốt spec | **KHÔNG CÓ test tự động** — checklist thủ công `checkpoint-bt4.md` mục "4A bắt buộc" (6 mục) |
| Build app node-based (TH4B) | Hết giờ → ưu tiên hoàn thành 4A, nộp master prompt 4B + sơ đồ node, **không cắt engine spec để cố hoàn thiện giao diện** | Không tự ghi log — app đọc `engine-spec.json`, log thật nằm ở lớp n8n/Agent phía sau | App hardcode API key/pseudo API → bỏ, dùng adapter thật hoặc ghi `NOT_RUNTIME_TESTED`; giao diện render đẹp nhưng chưa chạy được → không tuyên bố hoàn thành | Không bắt buộc riêng — kế thừa 2 cổng HITL đã có ở TH3 | **KHÔNG CÓ test tự động** — checklist thủ công `checkpoint-bt4.md` mục "4B hỗ trợ" (6 mục) |

## 2. Compliance note

- Không clone mặt/giọng người thật khi chưa có consent bằng văn bản — ràng buộc pháp lý, kiểm bằng checklist ở khâu duyệt ảnh (TH3) và duyệt clip (TH3), không có nhánh automation nào bỏ qua bước này.
- Không dùng logo bên thứ ba, không dùng hình/nhạc/giọng thiếu quyền; nhạc nền phải có license rõ ràng.
- Với nội dung liên quan trẻ em (kế thừa Buổi 6): không dùng hình ảnh học viên/trẻ em thật khi chưa có đồng ý của phụ huynh — ảnh trong lab là AI sinh, style reference synthetic.
- Không bịa dữ kiện hay cam kết hiệu suất trong lời thoại, kể cả khi câu nghe hay hơn — thiếu thì ghi `[cần bổ sung]`, kế thừa nguyên tắc Buổi 6.
- Chữ trên hình: model không sinh chữ hiển thị — `image_prompt`/`video_prompt` cấm chữ, chữ chèn ở khâu dựng.
- Log tối giản: ghi tham chiếu asset + trạng thái, không log toàn văn prompt, không log khoá API.
- **Kỷ luật báo cáo — chỗ dễ tự lừa mình nhất:** phân biệt rõ phần nào chạy thật (`runtime_evidence` có bằng chứng), phần nào dùng fallback, phần nào chưa runtime-test. `media-run-log.json` bắt buộc có `runtime_evidence`; thiếu bằng chứng thì status không được ghi `SUCCESS` (AT2 giáo án B7).

## 3. Mức độ tin cậy (6 thuộc tính, tự đánh giá thẳng thắn)

| Thuộc tính | Đạt? | Nhận xét |
|---|:---:|---|
| Fault-tolerant | Một phần | Per-clip state + retry riêng từng clip, một clip lỗi không xóa kết quả scene khác — nhưng chưa test thật trường hợp hết credit giữa batch trên instance thật. |
| Observable | Một phần | `media-run-log.json` ghi start/end/retry_count/output ref theo thiết kế — nhưng chưa có lần chạy thật nào để xác nhận log này thực sự được ghi đúng khi có lỗi. |
| Auditable | Đạt | ID nối xuyên suốt `project_id→scene_id→frame_id→clip_id`; `runtime_evidence` chống báo cáo khống theo thiết kế schema (TH1). |
| Workable | Đạt | Người duyệt chỉ cần xem ảnh/nghe clip và bấm; không phải viết prompt hay đụng vào engine. |
| Idempotent | Một phần | Các bước kiểm (validate schema, cổng duyệt) idempotent hoàn toàn; sinh ảnh/clip thì không — chạy lại ra kết quả khác và tốn credit thật, cần khoá `project_id+scene_id+version` để chống chạy trùng — **chưa có cơ chế khoá này được build/test thật**. |
| Scalable | Thiếu | Video Generator chạy tuần tự nên thời gian tăng tuyến tính theo số scene; chưa test trên instance thật với batch 6–9 scene đầy đủ, mới dừng ở canary 2 scene trong giờ lab. |

**Tổng: 2 đạt / 4 một phần / 0 thiếu hoàn toàn về mặt thiết kế — nhưng khác B6, package này CHƯA có lần chạy thật trên instance ngoài giờ lab được ghi nhận lại** (B6 có `checkpoint-bt4.md` "✅ Đã validate trên instance thật"; B7 hiện chỉ có checklist thiết kế + checkpoint rescue, chưa có nhật ký chạy thật tương đương). Đây là việc cần làm trước khi coi package này là production-ready — xem đề xuất Tuần 1-3 ở `06-leadership-deck.md`.
