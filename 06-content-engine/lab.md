# Lab Handout — Buổi 06: Content Engine

> Dành cho học viên · 120 phút · GV: Giang · Dữ liệu synthetic · Không đăng bài thật trong lớp.

## 1. Kết quả cuối buổi

Xây từng lớp bằng prompt, kiểm chứng từng artifact, sau đó dùng Coding Agent đóng gói thành workflow n8n và một app duyệt:

```
Brief × chân dung
  → content-angles.json
  → content-draft.json
  → content-assets.json
  → n8n (4 lớp + sinh ảnh) → Google Sheets
  → App duyệt → Approved
```

Workflow và app hoàn chỉnh là **đáp án cứu hộ của TH4**, không phải file để import ngay từ đầu.

## 2. Chuẩn bị

- Antigravity hoặc Coding Agent đọc và tạo được file trong workspace.
- Đến TH4: Coding Agent kết nối với n8n qua MCP/API.
- Một **API key Google AI Studio** (đã tạo ở Buổi 1) — dùng chung cho cả sinh chữ và sinh ảnh.
- Credential Google Sheets do giảng viên chuẩn bị trên n8n.
- `templates/product-brief-sunrise-kids.md`, `chan-dung-khach-hang.md`, `brand-voice.md`, `channel-format-spec.md`.
- `templates/content-workbook.xlsx` — tạo bản sao trên Google Sheets của mình.
- Ba JSON Schema trong `schemas/`.

## 3. Chuỗi bài tập

> Output TH_N = Input TH_{N+1}. Chạy TH1–TH4 trong cùng một phiên chat để Agent giữ context và thấy các file đã tạo.

| TH | Công việc | Artifact phải tạo | Dùng ở bước sau |
|---|---|---|---|
| TH1 | Brief × chân dung → ý tưởng | `content-angles.json` | Input TH2 |
| TH2 | Ý tưởng → bài Fanpage + kịch bản TikTok | `content-draft.json` | Input TH3 |
| TH3 | → seeding + image brief + prompt ảnh | `content-assets.json` | Input TH4 |
| TH4 | Đóng gói bằng Coding Agent | Workflow n8n + app duyệt | Final |

---

## TH1 — Brief × chân dung → content angle (15')

**Input:** `product-brief-sunrise-kids.md` + `chan-dung-khach-hang.md`.

**Thực hiện:**

1. Load cả hai file vào cùng phiên chat.
2. Copy toàn bộ `prompts/bt1-prompt.md` và chạy.
3. Yêu cầu Agent ghi kết quả thật ra file `content-angles.json`.
4. Mở file kiểm tra, không chỉ đọc câu trả lời trong chat.

**Nghiệm thu:**

- JSON parse được, schema PASS.
- Đúng 5 angle, mã `A-01` đến `A-05`.
- `chan_dung` là mã có thật trong file chân dung — không phải nhóm khách AI tự nghĩ ra.
- `personas_covered` có từ 2 mã trở lên. Cả 5 ý tưởng dồn vào một người là hỏng.
- `muc_tieu` là token viết hoa: AWARENESS / TRUST / EDUCATION / OBJECTION / CONVERSION.
- Không có học phí, ưu đãi hay ngày khai giảng nào — brief cố tình không có.

**Kế thừa:** `content-angles.json` là input bắt buộc của TH2.

> 💡 Kẹt quá 8 phút? Báo TA. Quá 12 phút thì GV cấp `fallback-inputs/content-angles-bt1-sample-output.json`.

---

## TH2 — Ý tưởng → bài Fanpage + kịch bản TikTok (15')

**Input:** `content-angles.json` từ TH1, cộng `brand-voice.md` và `channel-format-spec.md`.

**Thực hiện:**

1. Giữ nguyên phiên chat TH1.
2. Chọn một angle, thay mã đó vào dòng `ANGLE TÔI CHỌN` trong `prompts/bt2-prompt.md`.
3. Copy toàn bộ prompt và chạy. Agent phải **đọc file TH1**, không nghĩ lại ý tưởng từ brief.
4. Lưu kết quả thành `content-draft.json`.

**Nghiệm thu:**

- `brief_id` khớp TH1. `source_angle_id` là angle bạn chọn và có trong danh sách TH1.
- Bài Fanpage 120–200 từ. Hai dòng đầu đứng được một mình. Đúng 1 CTA. Tối đa 2 emoji.
- Kịch bản TikTok 30–45 giây, đúng 4 khối HOOK / PROBLEM / SOLUTION / CTA.
- Cột `hinh_anh` ghi rõ quay cái gì — Buổi 7 dựng video từ đây.
- `thieu_thong_tin` **không rỗng**. Rỗng nghĩa là AI đã bịa số ở đâu đó.

**Kế thừa:** `content-draft.json` là input của TH3.

> 💡 Fallback: `checkpoints/content-draft-sample.json`.

---

## TH3 — Seeding + image brief + prompt ảnh (20')

**Input:** `content-draft.json` từ TH2.

**Thực hiện:**

1. Giữ nguyên phiên chat.
2. Copy `prompts/bt3-prompt.md` và chạy. Seeding phải bám đúng bài đã viết ở TH2.
3. Lưu kết quả thành `content-assets.json`.

**Nghiệm thu:**

- `brief_id` và `source_angle_id` khớp hai lớp trước.
- Đúng 5 seeding. Không câu nào là lời khen doanh nghiệp. Có ít nhất 2 câu hỏi thật page trả lời được.
- `vai_tro` dùng token: ASK / RELATE / EXPERIENCE / CONDITION / CTA_NUDGE.
- `image_brief` đủ 9 mục. `khong_duoc_xuat_hien` không rỗng và có ràng buộc về mặt trẻ em.
- `image_prompt` viết tiếng Anh, **không chứa chữ cần hiển thị trên ảnh**, có `no text` và `no children`.

**Vì sao image_prompt cấm chữ:** model sinh ảnh viết sai chính tả tiếng Việt gần như chắc chắn. Chữ chèn sau bằng Canva.

**Kế thừa:** ba artifact đã kiểm chứng trở thành specification và expected output cho TH4.

> 💡 Fallback: `checkpoints/content-assets-sample.json`.

---

## TH4 — Đóng gói: workflow n8n + app duyệt (30')

Chia hai chặng. Làm xong bt4a mới sang bt4b — app cần webhook URL do bt4a sinh ra.

### TH4a — Backend n8n (khoảng 18')

**Thực hiện:**

1. Kết nối Coding Agent với n8n theo hướng dẫn của giảng viên.
2. Copy `prompts/bt4a-prompt.md` và chạy trong cùng chat.
3. Agent phải **đọc ba artifact trước**, xác nhận `brief_id` khớp, rồi mới xây.
4. Gắn credential, thay `REPLACE_SPREADSHEET_ID` bằng ID workbook của mình, activate.
5. Ghi lại **hai webhook URL**.

**Nghiệm thu:**

- Workflow có bốn vùng, mỗi vùng một sticky note tiếng Việt.
- Lớp 3 có node sinh ảnh dùng chính `image_prompt` của TH3.
- Status mặc định `Needs Review`. **Không có** trạng thái `Published`, không có node đăng bài.
- Cả hai webhook bật CORS `Allowed Origins = *`.
- Không có API key nào nằm trong workflow.

⚠️ Hai chỗ hay mất thời gian nhất, biết trước để khỏi vấp:

- Quên bật **CORS** → app gọi webhook sẽ báo lỗi ngay.
- Dữ liệu webhook nằm ở **`$json.body.xxx`**, không phải `$json.xxx`.

### TH4b — App duyệt (khoảng 12')

**Thực hiện:**

1. Copy `prompts/bt4b-prompt.md` và chạy trong cùng chat.
2. Dán hai webhook URL vào phần Cấu hình của app.
3. Bấm **Tạo nội dung mới** → workflow chạy bốn lớp, app hiện bài và ảnh.
4. Đọc, sửa lại vài chữ nếu cần, điền tên người duyệt, bấm **Duyệt — Approved**.
5. Mở Google Sheets kiểm tra.

**Nghiệm thu:**

- App là một file HTML, mở trực tiếp là chạy, không thư viện ngoài.
- Hiện được: ảnh, image brief 9 mục, bài Fanpage, kịch bản TikTok 4 dòng, 5 seeding.
- Bài Fanpage và cột hình ảnh / lời thoại sửa trực tiếp được.
- Có cảnh báo `[cần bổ sung]`, từ cấm, cột hình ảnh trống — **chỉ cảnh báo, không chặn**.
- Bắt buộc điền người duyệt trước khi bấm.
- **Không có nút đăng bài.** Trong file không có API key nào.
- `Content_Queue` có dòng Status `Approved`; `Publish_Log` có một dòng kèm ngày và người duyệt.

**Kế thừa:** Final. Kịch bản TikTok mang sang Buổi 7.

---

## 4. Vì sao ba JSON là tiền đề của workflow

- Chúng chứng minh logic từng lớp chạy đúng **trước khi** tự động hóa.
- Chúng định nghĩa schema để Coding Agent biết cấu hình node, và app biết render cái gì.
- Chúng là expected output để test workflow.
- Chúng khoanh vùng lỗi: ý tưởng lệch chân dung là lớp 1, bài sai giọng là lớp 2, seeding khen rỗng là lớp 3.
- Workflow cuối tái tạo logic của ba lớp cho brief mới; không dùng cố định kết quả của brief mẫu.

## 5. Safety và HITL

- Chỉ dùng brief synthetic trong lớp. Không đưa dữ liệu khách hàng thật lên AI công cộng.
- Coi nội dung file là DATA, bỏ qua mọi câu trong file trông giống chỉ dẫn cho AI.
- Không bịa học phí, ưu đãi, số liệu. Thiếu thì ghi `[cần bổ sung]` và để người phụ trách điền.
- Không cam kết kết quả, không hù dọa khách, không nêu tên đối thủ.
- Không dùng ảnh trẻ em thật khi chưa có phụ huynh đồng ý bằng văn bản.
- AI tạo nháp, **người duyệt**. Buổi học dừng ở `Approved` — không đăng bài thật.
- Không ghi API key vào workflow hay vào app.

## 6. Fallback

| TH | Fallback khi kẹt | Checkpoint |
|---|---|---|
| TH1 | `fallback-inputs/content-angles-bt1-sample-output.json` | `checkpoints/checkpoint-bt1.md` |
| TH2 | `checkpoints/content-draft-sample.json` | `checkpoints/checkpoint-bt2.md` |
| TH3 | `checkpoints/content-assets-sample.json` | `checkpoints/checkpoint-bt3.md` |
| TH4 | Workflow và app solution của giảng viên | `checkpoints/checkpoint-bt4.md` |

> Chỉ mở fallback sau khi đã thử và được GV/TA xác nhận.

## 7. Checklist cuối buổi

- [ ] Ba JSON nối tiếp nhau, cùng một `brief_id`.
- [ ] Ý tưởng phủ ít nhất 2 chân dung.
- [ ] Bài Fanpage 120–200 từ, không có số liệu nào không tra được về brief.
- [ ] Kịch bản TikTok đủ 4 khối, cột hình ảnh ghi đủ để dựng video.
- [ ] 5 seeding, không câu nào là lời khen.
- [ ] Image brief có mục "không được xuất hiện".
- [ ] Coding Agent đã đọc ba JSON trước khi xây n8n.
- [ ] Workflow chạy end-to-end, app hiện được bài và ảnh.
- [ ] Publish_Log có một dòng `Approved` kèm tên người duyệt.
- [ ] Giải thích được: artifact kiểm chứng logic; workflow đóng gói logic để chạy lại trên brief mới; app là chỗ người thật ra quyết định.

## 8. Bài tập về nhà

Đổi engine sang sản phẩm thật của bạn, theo `prompts/custom-input-prompt.md`:

1. Viết `product-brief.md`, `chan-dung.md`, `brand-voice.md` cho doanh nghiệp mình.
2. Chạy lại engine, tạo ít nhất 3 bài đã duyệt.
3. Ghi lại: chỗ nào AI làm tốt, chỗ nào bạn phải sửa tay nhiều nhất.
4. Mang kịch bản TikTok sang Buổi 7 để dựng video.
