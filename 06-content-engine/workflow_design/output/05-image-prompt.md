# W5 — Infographic (tái sử dụng ảnh có sẵn từ lab_6)

> Input: `04-mermaid.mmd` + `02-as-is-tobe.md`.
> Quyết định đã chốt với user: **không tự render ảnh mới** — tái sử dụng 4 PNG đã có sẵn trong `v2.0-workflow-mindset/lab_6/output/` (đúng use-case Sunrise Kids, đã xác nhận nội dung khớp: nhắc đúng `Content_Queue`/`Publish_Log`/`Approved`, kiến trúc hybrid n8n+AI Agent+Vibe App, "chưa tự động đăng"). 4 file đã copy vào thư mục này.

## 1. Ảnh đã copy vào `workflow_design/`

| File | Dùng cho | Ghi chú khớp/lệch với package này |
|---|---|---|
| `before_after_diagram.png` | Slide so sánh Trước/Sau trong `06-leadership-deck.md` | Khớp tốt — 4 cột phải đúng ESIA: NGUỒN CỐ ĐỊNH (I) / AI SINH NỘI DUNG (A) / HÀNG ĐỢI DUYỆT (S) / CỔNG DUYỆT HITL. Không nhắc bước đăng bài/đo lường — đúng phạm vi bị cắt ở W2. |
| `system_architecture_diagram.png` | Ảnh chính minh hoạ kiến trúc hybrid, dùng ở `b6-foundation-n8n-hybrid.md` | Khớp tốt — vẽ đúng n8n (điều phối 4 lớp + ghi Sheets), AI Agent (Gemini API), Vibe App (Cổng duyệt HITL), output `Content_Queue`/`Publish_Log`, và chú thích rõ "chờ đăng (chưa tự động đăng)". |
| `horizontal_infographic.png` | Ảnh phụ minh hoạ luồng ngang 4 giai đoạn | Khớp tốt cho phần kỹ thuật của deck. |
| `storytelling_infographic.png` | Ảnh phụ dạng kể chuyện, dùng nếu cần slide dễ hiểu hơn cho người không kỹ thuật | Khớp tốt. |

**Lưu ý minh bạch:** 4 ảnh này được render từ mermaid gốc phức tạp hơn của `lab_6` (`v2.0-workflow-mindset/lab_6/output/04-mermaid-diagram.mmd`, dạng `sequenceDiagram` nhiều node, có cả nhánh "đăng bài giai đoạn sau"), KHÔNG phải từ `04-mermaid.mmd` (bản ≤8 node của package này, tuân BR-W6). Nội dung minh hoạ trên ảnh (4 cột/4 giai đoạn) vẫn khớp đúng phạm vi TH1→TH4b của package này — không có mâu thuẫn — nhưng nếu sau này cần ảnh render đúng-từng-node với `04-mermaid.mmd`, phải render lại bằng 1 trong 4 prompt dưới đây.

## 2. Prompt gốc (giữ để render lại khi cần cập nhật)

Nguồn đầy đủ: `v2.0-workflow-mindset/lab_6/prompts/05-generate-workflow-image.md` và `v2.0-workflow-mindset/lab_6/output/05-workflow-image-prompt.md`. Tóm tắt 4 phương án đã dùng:

1. **Infographic ngang** — luồng trái→phải, 4 giai đoạn màu Xanh dương/Cam/Tím/Vàng, theo đúng mermaid.
2. **Before-After** — cột trái "TRƯỚC: chat lộn xộn" (6 điểm nghẽn cụ thể), cột phải "SAU: Content Engine có kiểm chứng" (4 cột theo ESIA).
3. **Storytelling 4-panel** — hành trình người phụ trách marketing 1 mình được AI hỗ trợ, phong cách comic-strip.
4. **System Architecture** — 4 lớp (Input Source / Orchestration n8n / Cognitive AI / HITL Review / Output & Storage), đúng kiến trúc hybrid.

Yêu cầu style chung (giữ nguyên khi render lại): nền xám nhạt `#F8FAFC`, isometric 3D, phông sans-serif hiện đại, **toàn bộ nhãn/tiêu đề tiếng Việt phải render đúng chính tả** — đây là lý do BR-W6 khuyên kiểm bằng mermaid.live trước khi đưa qua công cụ sinh ảnh.

## 3. Fallback nếu cần ảnh render đúng `04-mermaid.mmd`

Dán nội dung `04-mermaid.mmd` vào [mermaid.live](https://mermaid.live) để lấy ảnh sơ đồ kỹ thuật chính xác (không có style minh hoạ), hoặc dùng làm input cho prompt Phương án 1 ở trên nếu cần bản đẹp cho slide.
