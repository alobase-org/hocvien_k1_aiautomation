# W5 — Infographic (3 ảnh đã render)

> Input: `04-mermaid.mmd` + `02-as-is-tobe.md`.
> **Trạng thái ảnh:** khác Buổi 6 (tái sử dụng PNG có sẵn), package này ban đầu không có công cụ sinh ảnh ở phiên thiết kế — ba prompt dưới đây (đối chiếu, hiệu chỉnh nhỏ từ `v2.0-workflow-mindset/Output_B7/05-workflow-image-prompt.md`) đã được chạy sau đó và **cả 3 ảnh đã render xong**, lưu tại thư mục này (xem mục 1).
>
> 📌 **Đừng nhầm hai loại prompt ảnh:** prompt ở đây là ảnh minh hoạ **quy trình nội bộ** cho slide tham mưu (cần chữ tiếng Việt). Khác hoàn toàn với `image_prompt` trong `storyboard.json` của engine (TH2/TH3) — prompt đó **cấm chữ hiển thị** và **cấm mô tả nhận dạng người thật**.

## 1. Ảnh đã render

| File | Dùng cho | Trạng thái |
|---|---|---|
| [05-workflow-before-after.png](05-workflow-before-after.png) | Slide 1 deck — nền cover + so sánh Trước/Sau | `[đã render]` |
| [05-workflow-storytelling.png](05-workflow-storytelling.png) | Ảnh phụ, dễ hiểu cho người không kỹ thuật | `[đã render]` |
| [05-workflow-system-architecture.png](05-workflow-system-architecture.png) | Slide 3 deck — kiến trúc hybrid n8n+AI Agent+App | `[đã render]` |

![Before/After](05-workflow-before-after.png)

![System Architecture](05-workflow-system-architecture.png)

![Storytelling](05-workflow-storytelling.png)

## 2. Phương án 1 — Trước–Sau (Before–After Isometric)

→ Lưu thành `05-workflow-before-after.png`

```text
A premium, tech-focused Before-After diagram illustrating a short-form video production transformation, isometric system architecture illustration, 3D vector style, clean white background.

LAYOUT & STRUCTURE:
- Top Title: "BẢN ĐỒ CHUYỂN ĐỔI: CỖ MÁY DỰNG VIDEO NGẮN" in Vietnamese.
- Left Side (Trước): Labeled "TRƯỚC: Đốt credit mù - phần lớn video bỏ dở". A frustrated content creator facing mismatched video clips in different art styles, a burning credit counter, a pile of discarded takes.
- Right Side (Sau - Engine 4 lớp): 4 vertical columns (Xanh dương/Cam/Tím/Vàng):
  1. "LỚP 1 - SCHEMA": Sinh 3 schema + 3 sample, validate PASS trước. ID nối xuyên suốt dự án → cảnh → khung hình → clip.
  2. "LỚP 2 - CHIA CẢNH": 6-9 cảnh có thời lượng rõ. Style bible dùng chung giữ nhân vật/bối cảnh. Kiểm lời thoại vừa số giây.
  3. "LỚP 3 - STORYBOARD ẢNH": Sinh ảnh xem trước cả video, trước khi tốn credit video. Prompt ảnh cấm chữ hiển thị.
  4. "LỚP 4 - DUYỆT VÀ DỰNG CLIP": Người duyệt từng ảnh. Chỉ khung hình đã duyệt mới dựng clip. Canary 2 cảnh trước batch.
- Red gate icon giữa cột 3-4, nhãn: "CỔNG CỨNG: CHƯA DUYỆT ẢNH THÌ KHÔNG DỰNG CLIP".
- Stamp badge góc dưới phải bên "Sau": "XEM TRƯỚC BẰNG ẢNH - NGƯỜI DUYỆT - RỒI MỚI TIÊU CREDIT".

DESIGN: Isometric, soft shadows, blue/orange/purple/yellow. Modern sans-serif (Inter/Segoe UI), high contrast. CRITICAL: mọi nhãn/tiêu đề phải là tiếng Việt đọc đúng dấu.
```

## 3. Phương án 2 — Kể chuyện (Storytelling, 4 panel)

→ Lưu thành `05-workflow-storytelling.png`

```text
A premium, modern, clean business storytelling infographic on minimalist light gray (#F8FAFC) background. Theme: "Hành trình một kịch bản: từ trang chữ tới video có tiếng" — 4 sequential comic-style panels (Blue/Orange/Purple/Yellow).

- Panel 1 (Blue — Nền móng): hai đường input (kịch bản đã duyệt + kịch bản nhập tay) hợp về 1 cấu trúc. Steps: "Hai đường đầu vào" → "Về cùng một cấu trúc dữ liệu" → "Sinh 3 schema + 3 sample, kiểm PASS trước" → "ID nối xuyên suốt: dự án, cảnh, khung hình, clip".
- Panel 2 (Orange — Chia cảnh): kịch bản chia thành 6-9 thẻ cảnh trên timeline, kèm style guide ghim phía trên. Steps: "Chia 6-9 cảnh theo khối kịch bản" → "Style bible dùng chung: nhân vật, bối cảnh, tông màu, khung dọc 9:16" → "Kiểm lời thoại vừa số giây" → "Quá dài thì viết lại lời, không kéo dài cảnh".
- Panel 3 (Purple — Storyboard): lưới ảnh storyboard xem như truyện tranh, tem giá cho thấy ảnh rẻ hơn clip nhiều. Steps: "Sinh ảnh từng cảnh" → "Xem trước cả video bằng ảnh tĩnh" → "Prompt ảnh cấm chữ hiển thị" → "Chưa tiêu một credit video nào".
- Panel 4 (Yellow — Duyệt & Dựng): người duyệt từng ảnh với nút approve/reject, cổng khoá, rồi bộ sinh clip tuần tự với chip trạng thái từng clip. Steps: "Người duyệt từng ảnh: liền mạch, bố cục, quyền, mục cấm" → "Chỉ khung hình đã duyệt mới dựng clip" → "Canary 2 cảnh trước khi chạy cả loạt" → "Một clip lỗi không hỏng các cảnh đã xong" → "Ghi nhật ký và sổ chi phí".

DESIGN: flat vector illustration, comic strip, subtle drop shadow, modern sans-serif. CRITICAL: toàn bộ nhãn tiếng Việt đọc đúng dấu.
```

## 4. Phương án 3 — Kiến trúc hệ thống (System Architecture)

→ Lưu thành `05-workflow-system-architecture.png`

```text
A professional system architecture diagram illustrating a hybrid AI video production engine, light gray background (#F8FAFC), isometric 3D perspective, pastel color fills. Layout left→right:

- Input Source Layer: hai icon tài liệu hợp thành một, nhãn "Hai đường đầu vào": "Kịch bản đã duyệt từ Buổi 6" và "Kịch bản nhập tay". Caption: "Hai adapter, cùng một cấu trúc".
- Orchestration Layer (n8n): gear + workflow node, nhãn "n8n - Bộ điều phối 4 lớp", 4 sub-block: "Lớp 1 Schema", "Lớp 2 Chia cảnh", "Lớp 3 Storyboard", "Lớp 4 Dựng clip". Chip xám: "Kiểm lời thoại vừa giây" và "Cổng cứng: chỉ ảnh đã duyệt", caption "luật cứng, không dùng AI".
- Cognitive AI Layer: icon não phát sáng, nhãn "AI Agent - Sinh schema, chia cảnh, viết prompt hình và audio". Card ghim bên cạnh: "Style bible - nhân vật, bối cảnh, tông màu" kèm icon khoá.
- Media Generation Layer: 2 icon API: "API sinh ảnh - cấm chữ hiển thị" và "API sinh video - có tiếng thoại, tiếng nền, hiệu ứng". Badge cấm đỏ: "Không clone mặt hoặc giọng người thật".
- HITL Review Layer: màn hình app "App duyệt - đọc engine spec, không tự đổi cấu trúc dữ liệu" với lưới storyboard + nút approve/reject + trình phát clip có waveform. Nối tới icon người "Người duyệt - duyệt ảnh và nghe clip". Vạch chắn đỏ phía sau: "Automation dừng tại đây".
- Output & Storage Layer: 3 khối xếp chồng: "Bộ clip đã dựng" (chip Xong/Đang chạy/Bị chặn), "Nhật ký chạy - có bằng chứng runtime" (cảnh báo "Không có bằng chứng thì không ghi thành công"), "Sổ chi phí - credit và số lần thử lại". Bên dưới: icon file spec "engine-spec - độc lập công cụ, đổi nền tảng chỉ thay adapter".

DESIGN: pastel isometric, modern sans-serif, high contrast, không rối. CRITICAL: mọi nhãn tiếng Việt đọc đúng dấu.
```

## 5. Ghi chú khi sinh ảnh

- Nếu công cụ render sai dấu tiếng Việt, rút ngắn nhãn 3–5 từ rồi sinh lại; ưu tiên Imagen 3 hoặc Nano Banana cho tiếng Việt.
- Giữ lại thông điệp cốt lõi ở mọi phương án: **"Xem trước bằng ảnh — người duyệt — rồi mới tiêu credit"** — đây là điểm khác biệt lớn nhất và là thứ lãnh đạo quan tâm nhất (tiền).
- Ảnh khuyến nghị làm chính (Phương án 1 — Trước/Sau) dùng cho Slide 2, Phương án 3 (System Architecture) dùng cho Slide 3 của `06-leadership-deck.md`.
- Sơ đồ kỹ thuật chính xác từng node: dán `04-mermaid.mmd` (bản 8 node, đúng BR-W6) vào [mermaid.live](https://mermaid.live) — không dùng làm nguồn cho 3 prompt ảnh trên (3 prompt trên minh hoạ khái niệm 4 lớp, không phải render đúng-từng-node).
