# W0 — Intake (Use-case làm rõ)

> Workflow Design Package — Buổi 6 Content Engine.
> Nguồn sự thật: `../../lab.md` (lab handout B6), `../../luong-nghiep-vu.md` (as-is nghiệp vụ gốc). Anonymize: use-case synthetic (Sunrise Kids), zero PII thật.

## Use-case

**Content Engine — sản xuất nội dung bán hàng đa kênh (Fanpage + TikTok) bằng AI 3 lớp + n8n + App duyệt.**

SME một sản phẩm/dịch vụ định kỳ cần bán (minh hoạ: trung tâm Anh ngữ trẻ em "Sunrise Kids", 2 cơ sở), marketing chỉ 1 người kiêm nhiệm. Sản xuất nội dung không phải sự kiện rời rạc mà là chu trình lặp theo kỳ (`../../luong-nghiep-vu.md`), hiện làm thủ công: brief hỏi lại mỗi lần, không chân dung khách hàng cố định, duyệt qua chat lộn xộn không audit trail.

## Phòng ban

Marketing/Content — người dùng cuối là người phụ trách content (thường kiêm nhiệm), người duyệt cuối là chủ doanh nghiệp/trưởng phòng marketing.

## Ràng buộc compliance (constraint)

- Chỉ dùng brief **synthetic** trong lớp học; không đưa dữ liệu khách hàng thật lên AI công cộng (`../../lab.md` §5).
- Không bịa học phí/ưu đãi/số liệu — thiếu thì ghi `[cần bổ sung]`, để người phụ trách điền (`brand-voice.md` — 8 điều cấm).
- Không cam kết kết quả, không hù doạ khách, không nêu tên đối thủ.
- Không dùng ảnh trẻ em THẬT khi chưa có phụ huynh đồng ý bằng văn bản — nhưng ảnh trong lab này là AI sinh hoàn toàn (không tham chiếu ai thật) nên được phép có người/trẻ em, và được phép có tối đa 1 dòng tiêu đề/CTA ngắn ≤8 từ (test thật: model render dấu tiếng Việt đúng); ràng buộc còn giữ trong `image_prompt`: `image_brief.khong_duoc_xuat_hien` không rỗng, nội dung dài hơn 1 dòng vẫn để trống cho Canva.
- Không ghi API key vào workflow n8n hay vào app duyệt.
- **Quyết định "Approved" luôn thuộc người phụ trách marketing** — hệ thống dừng đúng ở trạng thái này, **không có trạng thái `Published`, không có node/nút đăng bài** (mạnh hơn cả BR-W2 của buổi 4: ở đây không tồn tại đường tắt tự động ra công chúng, dù chỉ là đề xuất).

## Mục tiêu đo được (KPI — từ lab.md + luong-nghiep-vu.md)

Chưa có số liệu vận hành thật (lab mới chạy trong lớp, chưa pilot ngoài đời) — các số dưới đây là khung tham chiếu để so sánh, không phải KPI đã đo:

- As-is (as chronicled trong `luong-nghiep-vu.md`): production 1 bộ nội dung phụ thuộc 2 người làm song song (copywriter + designer), TikTok cần quay+dựng thật tốn nhiều giờ không gọn trong 1 bước; duyệt nội bộ thường không có cổng hình thức (Zalo/Slack).
- To-be trong phạm vi lab: 3 lớp AI (angle → draft → assets+ảnh) đều có schema + nghiệm thu văn phong kiểm chứng được (`giao_trinh/scripts/validate-b6-artifacts.py`), gộp vào 1 cổng duyệt (Vibe App) thay vì rải rác nhiều kênh trao đổi.
- Số giờ/tháng tiết kiệm thực tế, tỉ lệ nội dung bị `Needs Review`, thời gian trung bình từ ý tưởng tới "Approved" → **`[cần đo]`** sau khi pilot thật với brief thật (bài tập về nhà, `../../prompts/custom-input-prompt.md`).

## Tool (theo lab.md)

- **n8n** (điều phối 4 lớp, Code node + HTTP Request tới AI, ghi Google Sheets).
- **AI Agent (Gemini qua HTTP Request/API)** — sinh angle, draft, assets, ảnh.
- **Vibe-coded App** (1 file HTML, không thư viện ngoài) — cổng duyệt HITL.
- Coding Agent (Antigravity/Claude Code) — sinh 3 JSON qua prompt, sau đó đóng gói thành n8n + app ở TH4.

## Data contract (chain N→N+1, `brief_id` xuyên suốt)

`product-brief + chân dung → content-angles.json (TH1) → content-draft.json (TH2) → content-assets.json (TH3) → n8n 4 lớp (Content_Queue, Status mặc định Needs Review) → App duyệt (HITL) → Publish_Log (Approved + người duyệt + ngày)`.

Kế thừa bắt buộc: `brief_id` giống nhau cả 3 lớp; `source_angle_id`/`chan_dung` khớp xuyên suốt (kiểm bằng `validate-b6-artifacts.py` — xem `03-hardening.md`).

## Anonymizer note

Use-case dùng `templates/product-brief-sunrise-kids.md` + `chan-dung-khach-hang.md` (synthetic, zero PII thật) → KHÔNG cần chạy `anonymizer.py`.
Track B (HV đổi sang sản phẩm thật của mình qua `../../prompts/custom-input-prompt.md`) → phải tự viết `product-brief.md`/`chan-dung.md`/`brand-voice.md` riêng, không đưa dữ liệu khách hàng thật (tên, SĐT, ảnh cá nhân) lên AI công cộng khi triển khai thật.
