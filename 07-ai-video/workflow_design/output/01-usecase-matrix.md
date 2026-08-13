# W1 — Ma trận Hiệu quả × Độ phức tạp

> Input: `00-intake.md`. Nguồn use-case: bước 1–7 chu trình dựng video trong `../../luong-nghiep-vu.md`, cụ thể hoá theo minh hoạ Sunrise Kids (đồng bộ với `v2.0-workflow-mindset/Output_B7/01-usecase-impact-matrix.md`, đã hiệu chỉnh lại phạm vi cho khớp `../../lab.md`).
> Output feeds W2 (`02-as-is-tobe.md`).

## 1. Bảng đánh giá use-case

| # | Use-case | Impact (1-5) | Difficulty (1-5) | Góc ma trận | Lý do ngắn |
|---|---|:---:|:---:|---|---|
| 1 | Chuẩn hoá 2 đường input (B6_APPROVED/MANUAL) + sinh 3 schema qua prompt (TH1) | 5 | 2 | 🟢 LÀM NGAY | Kịch bản đã duyệt sẵn từ B6; đây là bước chia nhỏ có luật rõ, kiểm được bằng schema — `additionalProperties:false` chặn trường lạ. |
| 2 | Chia kịch bản → 6–9 scene có ID + style bible dùng chung (TH2) | 5 | 2 | 🟢 LÀM NGAY | Thay "tự hình dung trong đầu" bằng scene có ID, thời lượng, và một style bible giữ nhân vật/bối cảnh/tông màu nhất quán. |
| 3 | Sinh ảnh storyboard cho từng scene (TH2/TH3) | 5 | 2 | 🟢 LÀM NGAY | Xem trước toàn bộ video bằng ảnh tĩnh trước khi tiêu một credit video nào; ảnh rẻ hơn clip nhiều lần. |
| 4 | Cổng duyệt ảnh trước khi dựng clip — HITL bắt buộc (TH3) | 5 | 2 | 🟢 LÀM NGAY | Rẻ nhất để làm, đắt nhất nếu thiếu — một clip sai style tốn credit gấp nhiều lần một ảnh sai, phát hiện muộn hơn. |
| 5 | Canary 2 scene trước khi chạy cả batch (TH3) | 4 | 2 | 🟢 LÀM NGAY | Gần như không tốn công thêm, nhưng cắt phần lớn chi phí hỏng cả loạt; báo trước số lượt tạo ảnh/video dự kiến. |
| 6 | Sinh clip có native audio từ frame Approved, chạy tuần tự (TH3) | 5 | 3 | 🟡 LÊN KẾ HOẠCH | Tốn credit và thời gian thật; cần per-clip state, retry riêng từng clip, không bắn một lượt. |
| 7 | Đóng gói Content/Video Engine spec độc lập công cụ (TH4A) | 5 | 3 | 🟡 LÊN KẾ HOẠCH | Node/port/edge, hai input adapter, approval gate, cost guard, test case — đổi công cụ chỉ thay adapter, không viết lại logic. |
| 8 | Build app node-based hỗ trợ vận hành (TH4B) | 4 | 3 | 🟡 LÊN KẾ HOẠCH | Canvas/node/edge/status/preview đọc từ engine spec; giao diện đẹp không giải quyết nút thắt gì nếu engine chưa chạy ổn. |
| 9 | Ghép clip + chèn chữ + đăng video (bước 6 `luong-nghiep-vu.md`) | 5 | 3 | 🟡 LÊN KẾ HOẠCH | Kỹ thuật không khó (nối clip, chèn chữ, gọi API đăng) nhưng **chủ đích KHÔNG làm trong lab** — buổi học dừng ở bộ clip + run log, người ghép/chèn chữ/đăng. |
| 10 | Đo lường hiệu quả video sau đăng & rút kinh nghiệm (bước 7 `luong-nghiep-vu.md`) | 5 | 4 | 🟡 LÊN KẾ HOẠCH | Cần dữ liệu chạy thật một thời gian mới đo được, phụ thuộc API nền tảng — **ngoài phạm vi lab hiện tại**, nối lại vòng lặp về content calendar B6. |

## 2. Ma trận 2×2

| | HIỆU QUẢ CAO (Impact ≥4) | HIỆU QUẢ THẤP (Impact ≤3) |
|---|---|---|
| **DỄ LÀM (Difficulty ≤2)** | 🟢 LÀM NGAY — UC1, UC2, UC3, UC4, UC5 | *(không có)* |
| **KHÓ LÀM (Difficulty ≥3)** | 🟡 LÊN KẾ HOẠCH — UC6, UC7, UC8, UC9, UC10 | *(không có)* |

## 3. Top-3 nên automate TRƯỚC

1. **Kịch bản → 6–9 scene → ảnh storyboard, style bible dùng chung (UC1+UC2+UC3) — ƯU TIÊN #1, đúng phạm vi TH1→TH2.** Biến một trang chữ thành thứ nhìn được, kiểm chứng hoàn toàn bằng schema và bằng mắt, chưa tốn một credit video nào.
2. **Cổng duyệt ảnh + canary trước khi dựng clip (UC4+UC5) — đúng phạm vi TH3 phần đầu.** Chỗ chặn lãng phí lớn nhất của cả quy trình: chỉ frame `APPROVED` mới mở clip `READY_TO_GENERATE`, và không batch 6–9 cảnh khi canary 2 scene chưa PASS.
3. **Sinh clip có audio + đóng gói engine (UC6+UC7) — đúng phạm vi TH3 phần sau + TH4A.** Đích đến thật của quy trình, nhưng phải chạy sau hai nhóm trên, per-clip state để một clip lỗi không làm hỏng cả lượt.

**👉 Use-case chọn cho W2:** kết hợp UC1–UC8 = đúng chuỗi `../../lab.md` TH1→TH2→TH3→TH4A→TH4B, dừng ở bộ clip đã dựng + run log. UC9 (ghép/chèn chữ/đăng) và UC10 (đo lường) ghi nhận là **mở rộng ngoài phạm vi lab hiện tại** — nêu ở `06-leadership-deck.md` như bước tiếp theo do người thực hiện, không đưa vào to-be W2/hardening W3.

> ⚠️ **Ghi chú quan trọng (không phải use-case, là ràng buộc xuyên suốt):** clone mặt/giọng người thật cho nhân vật trong video — dù kỹ thuật khả thi — **không được đưa vào bất kỳ nhánh automation nào**. Đây là vấn đề quyền và đạo đức, không phải độ khó kỹ thuật; không có consent bằng văn bản thì tuyệt đối không làm (xem compliance note `00-intake.md`).
