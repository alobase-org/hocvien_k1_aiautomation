# B6 Foundation — Content Engine: n8n + Hybrid AI Automation (nền 4 TH)

> NỀN buổi 6. Tool chính = **n8n** (orchestrator) + **AI Agent** (Gemini qua HTTP Request) + **Vibe-coded App** (HITL dashboard). Track A/B móc vào đây.
> Tư duy mới: **Hybrid Architecture (3 trụ)** + **Schema kế thừa** (harness nhẹ, khác cấp với B4) + **Cổng duyệt dừng cứng ở Approved** (không đường tắt publish).

## 0. Use-case (doanh nghiệp minh hoạ)

SME 1 sản phẩm/dịch vụ định kỳ cần bán (minh hoạ: trung tâm Anh ngữ trẻ em Sunrise Kids, 2 cơ sở), marketing 1 người kiêm nhiệm. Workflow: brief+chân dung → 3 lớp AI (schema+kế thừa kiểm được) → n8n ghi `Content_Queue` → App duyệt (HITL) → `Publish_Log`.
Kết quả đo: **`[cần đo]`** — lab mới chạy trong lớp học (`../../lab.md`), chưa pilot với dữ liệu thật ngoài đời.

## 1. ESIA

### Steps (4 TH = 4 tư duy, n8n+AI+App)

1. **TH1 — Sinh ý tưởng** (harness nhẹ: schema+kế thừa): AI Gemini sinh 5 angle bám ≥2 chân dung → `content-angles.json` schema-valid.
2. **TH2 — Viết bài + kịch bản** (harness: kế thừa + nghiệm thu văn phong): AI viết từ angle đã chọn, đọc file TH1 chứ không nghĩ lại từ brief → `content-draft.json`, kiểm bằng `validate-b6-artifacts.py`.
3. **TH3 — Sinh seeding + ảnh** (harness: ràng buộc an toàn): `content-assets.json`, ảnh được phép có người/trẻ em (AI sinh hoàn toàn, không tham chiếu ai thật) và tối đa 1 dòng tiêu đề/CTA ngắn ≤8 từ (test thật: model render dấu tiếng Việt đúng — Judge ảnh vẫn kiểm chữ có khớp dự kiến không).
4. **TH4 — Đóng gói hybrid**: TH4a n8n 4 lớp (điều phối + gọi AI + ghi Sheets) + TH4b Vibe App (HITL duyệt) chạy end-to-end, dừng ở `Approved`.

### Exceptions (n8n IF/Code node + App)

- Schema/kế thừa FAIL → cần thử lại, không chặn các brief khác đang chạy song song.
- Ảnh lỗi/vi phạm chính sách → placeholder + gắn nhãn "cần thay tay" (`checkpoint-bt4.md`: "chưa runtime-test").
- `thieu_thong_tin` rỗng nhưng brief thật sự thiếu dữ kiện → nghi AI bịa số — **đề xuất** cảnh báo riêng ở App, **chưa triển khai** (xem `03-hardening.md`).
- Webhook `/b6/approve` gọi 2 lần cùng Post ID (double-submit) → kiểm Post ID đã có trong `Publish_Log` chưa trước khi ghi thêm.

### Inputs

- Brief + chân dung + brand-voice + spec kênh (`../../templates/product-brief-sunrise-kids.md`, `chan-dung-khach-hang.md`, `brand-voice.md`, `channel-format-spec.md`).
- Ba JSON Schema (`../../schemas/content-angles.schema.json`, `content-draft.schema.json`, `content-assets.schema.json`).

### Outputs (data contract, chain N→N+1, `brief_id`)

`content-angles.json → content-draft.json → content-assets.json → Content_Queue (n8n, Status=Needs Review) → Publish_Log (webhook /b6/approve, khi Approved)`.

### Accountability (RACI)

| Vai trò | Trách nhiệm |
|---|---|
| n8n (Orchestrator) | Điều phối 4 lớp, gọi AI, ghi `Content_Queue`/`Publish_Log` — tất định ở phần ghi sổ |
| AI Agent (Gemini) | Sinh angle/bài/kịch bản/seeding/ảnh — **đề xuất**, KHÔNG quyết định duyệt |
| Vibe App | Hiển thị + cảnh báo tự động (không chặn) + nhận thao tác người |
| Người phụ trách marketing (HITL) | Xem, sửa, nhập tên, bấm Approved/Needs Review — **quyết định cuối** |

## 2. Hybrid Architecture (tư duy mới — chi tiết)

### 2a. Vì sao không để 1 trụ làm hết

Không để LLM làm tất cả (đắt, chậm, không tất định); không để n8n làm tất cả (thiếu trí tuệ ngôn ngữ để viết bài đúng giọng thương hiệu) — chia 3 trụ:

| Trụ | Vai trò |
|---|---|
| **n8n** | Orchestration: gọi API, ghi Sheets, xử lý webhook, IF/logic tất định |
| **AI Agent (Gemini)** | Cognitive: sinh ý tưởng, viết bài/kịch bản, seeding, ảnh |
| **Vibe-coded App** | HITL dashboard — nơi người thật ra quyết định cuối |

### 2b. Schema + kế thừa (harness nhẹ — khác cấp với B4)

- Mọi output 3 lớp phải pass JSON Schema (`../../schemas/*.schema.json`, Draft 2020-12).
- `brief_id`/`source_angle_id`/`chan_dung` phải khớp xuyên suốt — kiểm bằng `validate-b6-artifacts.py` mục "2. KẾ THỪA".
- **Khác B4** (Code node Python validate schema ngay trong n8n runtime, tất định trong workflow): ở B6, `validate-b6-artifacts.py` là script kiểm **ngoài** (chạy tay khi chấm bài/kiểm bản mẫu), **CHƯA gắn vào runtime n8n** — nếu Coding Agent sinh JSON sai ngay trong workflow thật, không có Code node nào tự chặn như B4. Đây là khoảng cách thật giữa "harness" của B4 và "schema kiểm ngoài" của B6, không nên nói hai buổi có cùng mức tất định.

### 2c. Cổng duyệt dừng ở Approved — không đường tắt

Không có node/nút đăng bài trong cả n8n lẫn App, dù chỉ là đề xuất kỹ thuật. Muốn đăng thật là **một workflow riêng, có kiểm soát riêng** — ngoài phạm vi package này (`../../prompts/custom-input-prompt.md`: "Status dừng ở Approved — Cố ý không có Published").

## 3. Diagram (n8n + AI + App)

Xem `04-mermaid.mmd` (flowchart LR, 8 node, 1 node AI, 1 node HITL, 2 node fallback).

## 4. Handover

`Content_Queue`: Post ID, Angle ID, Kênh, Nội dung, Status, Người duyệt, Ghi chú. `Publish_Log`: Log ID, Post ID, Kênh, Status, Ngày duyệt, Người duyệt, Ghi chú. KHÔNG auto đăng/gửi — cao nhất ghi được là `Approved`.

## Mapping + tư duy mới

- Track A = HV build đúng TH1→TH4a→TH4b theo `esia-usecase.md`. Track B = HV đổi use-case theo `../../prompts/custom-input-prompt.md`, giữ nguyên 3 schema + cấu trúc 4 lớp + cổng duyệt dừng ở Approved.
- **Tư duy mới B6:** TH1-TH3 = schema+kế thừa (harness nhẹ, kiểm ngoài runtime), TH4a = orchestration n8n, TH4b = HITL App — đúng 3 trụ hybrid + cổng duyệt dừng cứng mà user yêu cầu.
