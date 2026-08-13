# Simulation log — đường B6_APPROVED (B7 bt1/bt2-prompt.md) chạy trên dữ liệu B6 thật

Ngày chạy: 2026-08-12. Dry-run bằng tay (không gọi LLM thật) theo ĐÚNG chữ hiện có trong
`prompts/bt1-prompt.md` + `prompts/bt2-prompt.md` (SOURCE_MODE=B6_APPROVED), dùng input thật:
`giao_trinh/giang-day/05-thuc-hanh/06-content-engine/run-output/content-draft.json`
(brief_id `SUNRISE-KIDS-TUYENSINH-2026-08`, source_angle_id `A-01`, 4 khối HOOK/PROBLEM/SOLUTION/CTA,
tổng 45s). Mục tiêu: dựng `video-script.json` y như một học viên/agent làm nếu chỉ có đúng những gì
prompt hiện tại nói — không thêm hiểu biết ngoài văn bản prompt.

## Kết quả đo được

| Điều kiện | Kỳ vọng nghiệp vụ | Kết quả dry-run "literal minimal" | Schema có bắt được không? |
|---|---|---|---|
| `brief_id`/`source_angle_id` truy vết về content-draft.json | Phải khớp `SUNRISE-KIDS-TUYENSINH-2026-08` / `A-01` | Để `null` — schema cho phép `["string","null"]` không điều kiện | **KHÔNG** — validate PASS dù mất hoàn toàn traceability |
| `target_audience` mô tả thật | Cần mô tả persona PH1 (Mẹ bé mới vào tiểu học, sợ con chán học...) | Chỉ có `"PH1"` — content-draft.json không mang mô tả, prompt B7 không yêu cầu mang theo `chan-dung-khach-hang.md` | **KHÔNG** — `minLength:1` vẫn PASS với chuỗi "PH1" |
| `brand_style` có nguồn thật | Cần giọng thương hiệu từ `brand-voice.md` (B6) | Bịa "chuyên nghiệp, gần gũi" — không sai chính tả nhưng không có căn cứ | **KHÔNG** — chỉ cần `minLength:1` |
| Tổng `duration_seconds` các scene | Phải bằng 45 (khớp `tong_thoi_luong_giay`) | 3+7+8+8+9+10 = 45 | Không có ràng buộc chéo trong schema — khớp là do tự tính tay, không có gì bắt nếu sai |
| Khối SOLUTION (10-35s, 25 giây, 2 câu thoại gốc) | Tách thành scene mà **không bịa lời thoại mới ngoài B6 đã duyệt** | Bắt buộc tách ≥3 scene (mỗi scene tối đa 10s theo schema), nhưng chỉ có 2 câu gốc → 1 scene phải để `dialogue: ""` (rỗng) | **KHÔNG** — field `dialogue` không có `minLength`, chuỗi rỗng vẫn PASS |
| `project_id`, `title` | Cần định danh dự án nhất quán | Tự bịa `"TEMP-001"` / `"Video quang cao Sunrise Kids"` — không có bất kỳ nguồn nào trong content-draft.json hay hướng dẫn prompt | Không kiểm được bằng schema (chỉ cần đúng pattern/minLength) |

**Kết luận đo được:** file `video-script.json` dựng theo đúng chữ hiện tại của prompt PASS schema
100% (0 lỗi) trong khi vẫn: mất traceability về B6, có scene lời thoại rỗng, và 4 field quan trọng
(`target_audience`, `brand_style`, `project_id`, `title`) không có nguồn dữ liệu thật nào được chỉ ra.
Schema hiện tại không phải chỗ sai — nó đúng vai trò "khóa cấu trúc, không khóa nghệ thuật" theo đúng
triết lý đã ghi trong bt1-prompt.md của cả B6 lẫn B7. Vấn đề nằm ở **prompt nghiệp vụ thiếu bước**, không
phải schema thiếu ràng buộc.

## Phát hiện cụ thể, xếp theo mức ảnh hưởng

1. **Tách khối bắt buộc nhưng không có hướng dẫn cách tách** (mức cao nhất — xảy ra ở MỌI lần chạy
   B6_APPROVED, không phải edge case). B6 luôn xuất đúng 4 khối (`content-draft.schema.json` khóa cứng
   `minItems=maxItems=4`); B7 luôn cần 6-9 scene. Với ví dụ thật, khối SOLUTION rộng 25s nhưng chỉ có
   2 câu thoại — cần tối thiểu 3 scene (giới hạn 10s/scene) nhưng không đủ câu gốc để chia mà không
   bịa hoặc để trống. `bt2-prompt.md` bước 4 chỉ nói "có thể tách thành nhiều scene" mà không nói:
   chia thời lượng thế nào, xử lý thế nào khi số câu ít hơn số scene cần, có được viết thêm lời thoại
   mới hay không.
2. **`target_audience`/`brand_style` không có nguồn trong B6_APPROVED mode.** content-draft.json chỉ
   mang mã persona (`chan_dung: "PH1"`), không mang mô tả. Mô tả thật và giọng thương hiệu nằm ở
   `chan-dung-khach-hang.md`/`brand-voice.md` của B6 — hai file này **không** có trong danh sách INPUT
   của `bt2-prompt.md` (B7) khi SOURCE_MODE=B6_APPROVED. So sánh: mode MANUAL có hẳn
   `templates/manual-script-input.md` với đủ Tiêu đề/Nền tảng/Tỷ lệ/Đối tượng/Phong cách/CTA — B6_APPROVED
   không có gì tương đương.
3. **`title`, `project_id` không có nguồn và không được hướng dẫn.** content-draft.json không có field
   tiêu đề; MANUAL mode có sẵn "Tiêu đề" trong template, B6_APPROVED thì không.
4. **Câu kiểm `status` trong bt2-prompt.md là tử lệnh chết.** "Nếu có status mà khác Approved, dừng và
   báo" — `content-draft.schema.json` không có field `status` ở bất kỳ đâu; trạng thái Approved chỉ tồn
   tại ở Google Sheets `Content_Queue` (do workflow n8n của B6 TH4a tạo ra), một tầng sau file JSON. Học
   viên dùng thẳng `content-draft.json` (là output TH2 của B6, TRƯỚC khi qua cổng duyệt TH4b) sẽ không
   bao giờ có gì để câu điều kiện này kiểm — có thể đưa nội dung CHƯA được duyệt ở B6 sang thẳng B7.
5. **Schema `video-script.schema.json` không ép buộc traceability cho B6_APPROVED.** `brief_id`/
   `source_angle_id` có type `["string","null"]` không điều kiện — không có ràng buộc kiểu
   `if source_mode==B6_APPROVED then brief_id != null`. Không phải lỗi nghiêm trọng (schema cố tình
   không khóa nghệ thuật) nhưng đây là một bất biến CÓ THỂ khóa bằng schema (không phải chất lượng nghệ
   thuật) mà hiện chưa khóa.
6. **`prompts/bt4a-prompt.md` và `prompts/bt4b-prompt.md` chưa cập nhật theo hướng đi mới** (native audio +
   voice_bible + cổng duyệt kịch bản chi tiết, chốt trong phiên làm việc trước). `bt4a` bước 3 liệt kê
   pipeline bắt buộc vẫn là `Input Adapter → Scene Planner → Storyboard Generator → Storyboard Review →
   Video Generator tổng → Clip Review/Export` — thiếu hẳn bước "Duyệt kịch bản chi tiết" đã thêm vào
   `lab.md` và `workflow-design-doc.md`. `bt4b` bước 4 chỉ mô tả card ảnh storyboard, không nhắc màn hình
   duyệt kịch bản (dialogue/video_prompt/negative_prompt) — trong khi app thật (`app-video-engine-test.html`)
   đã build và test đúng màn hình này.

## Việc CHƯA làm trong log này

- Không sửa bất kỳ file nghiệp vụ nào (`bt1/bt2-prompt.md`, `content-draft.schema.json`,
  `video-script.schema.json`, `bt4a/bt4b-prompt.md`) — đây là log mô phỏng, chờ xác nhận phạm vi sửa.
- Không chạy LLM thật; toàn bộ dry-run làm bằng tay theo đúng chữ prompt để kết quả tái lập được, không
  phụ thuộc một lần sinh ngẫu nhiên của model.
