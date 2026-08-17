# W1 — Ma trận Hiệu quả × Độ phức tạp

> Input: `00-intake.md`. Nguồn 10 use-case: 7 bước chu trình nội dung trong `../../luong-nghiep-vu.md`, cụ thể hoá theo minh hoạ Sunrise Kids (đồng bộ với `v2.0-workflow-mindset/lab_6/output/01-usecase-impact-matrix.md`, đã hiệu chỉnh lại phạm vi cho khớp `../../lab.md`).
> Output feeds W2 (`02-as-is-tobe.md`).

## 1. Bảng đánh giá use-case

| # | Use-case | Impact (1-5) | Difficulty (1-5) | Góc ma trận | Lý do ngắn |
|---|---|:---:|:---:|---|---|
| 1 | Chuẩn hoá brief + chân dung + brand voice tái sử dụng | 5 | 2 | 🟢 LÀM NGAY | Chỉ cần gom dữ kiện đã có sẵn thành 1 bộ nguồn cố định, không cần hạ tầng mới — đúng `templates/product-brief-sunrise-kids.md` đã có sẵn. |
| 2 | Sinh ý tưởng nội dung theo chân dung (TH1 — content-angles) | 5 | 2 | 🟢 LÀM NGAY | AI sinh 5 angle bám ≥2 chân dung, có schema kiểm cấu trúc + kế thừa. |
| 3 | Viết bài Fanpage + kịch bản TikTok có kiểm chứng (TH2 — content-draft) | 5 | 3 | 🟡 LÊN KẾ HOẠCH | Cần nghiệm thu văn phong ngoài schema (số từ đếm lại, 4 khối đúng thứ tự, không bịa số) — đã có `validate-b6-artifacts.py` làm việc này. |
| 4 | Sinh seeding + image brief + ảnh (TH3 — content-assets) | 4 | 3 | 🟡 LÊN KẾ HOẠCH | Cùng AI Agent làm thêm, nhưng seeding không sáo rỗng + tiêu đề ngắn trong ảnh (nếu có) đúng dự kiến cần kiểm kỹ (ảnh AI sinh được phép có người/trẻ em và ≤1 dòng chữ ngắn). |
| 5 | Cổng duyệt chuẩn hoá (App duyệt thay chat lộn xộn) | 5 | 2 | 🟢 LÀM NGAY | Một dashboard hiện bài + ảnh + nút Approved/Needs Review là đủ, không cần hệ thống phức tạp. |
| 6 | Đóng gói workflow n8n 4 lớp + webhook duyệt (TH4a+TH4b) | 5 | 3 | 🟡 LÊN KẾ HOẠCH | Kỹ thuật rõ ràng (n8n + webhook + Sheets) nhưng nhiều điểm dễ vấp thật (CORS, `$json.body`, credential) — xem `checkpoint-bt4.md`. |
| 7 | Content calendar theo kỳ | 4 | 3 | 🟡 LÊN KẾ HOẠCH | Cần thống nhất mùa vụ + ngân sách với chủ doanh nghiệp trước khi máy gợi ý được — bước 1 của `luong-nghiep-vu.md`, **ngoài phạm vi lab hiện tại**. |
| 8 | Lên lịch & đăng bài tự động sau khi Approved | 5 | 3 | 🟡 LÊN KẾ HOẠCH | Kỹ thuật đơn giản (gọi API nền tảng) nhưng **chủ đích KHÔNG làm trong lab** (`../../lab.md` §5: "buổi học dừng ở Approved") — cần độ tin cậy đủ cao ở cổng duyệt trước khi cân nhắc bật. |
| 9 | Trực page trả lời comment thật sau khi đăng | 2 | 4 | 🔴 BỎ (tạm thời) | Việc liên tục cần người thật theo dõi hàng giờ — không phải bài toán tự động hoá một lần, khác seeding có kiểm soát. |
| 10 | Đo lường hiệu quả & rút kinh nghiệm kỳ sau | 5 | 4 | 🟡 LÊN KẾ HOẠCH | Cần dữ liệu chạy thật một thời gian mới đo được, phụ thuộc API các nền tảng — bước 7 của `luong-nghiep-vu.md`, **ngoài phạm vi lab hiện tại**, hiện không ai làm ở as-is. |

## 2. Ma trận 2×2

| | HIỆU QUẢ CAO (Impact ≥4) | HIỆU QUẢ THẤP (Impact ≤3) |
|---|---|---|
| **DỄ LÀM (Difficulty ≤2)** | 🟢 LÀM NGAY — UC1, UC2, UC5 | *(không có)* |
| **KHÓ LÀM (Difficulty ≥3)** | 🟡 LÊN KẾ HOẠCH — UC3, UC4, UC6, UC7, UC8, UC10 | 🔴 BỎ — UC9 |

## 3. Top-3 nên automate TRƯỚC

1. **Content Engine 3 lớp có kiểm chứng (UC1+UC2+UC3+UC4) — ƯU TIÊN #1, đúng phạm vi TH1→TH2→TH3.** Giải quyết gốc rễ: nội dung chung chung vì brief viết lại từ đầu và không chân dung cố định. Gộp sinh angle, bài, kịch bản, seeding, ảnh vào một luồng có schema + nghiệm thu văn phong kiểm tra được trước khi tới người duyệt.
2. **Cổng duyệt chuẩn hoá + đóng gói n8n (UC5+UC6) — đúng phạm vi TH4a+TH4b.** Thay chat lộn xộn bằng một App duyệt duy nhất, có cảnh báo tự động (không tự chặn), Approved/Needs Review rõ ràng, audit trail trong Publish_Log.
3. **Content calendar theo kỳ (UC7)** — tiền đề để Content Engine "có gì mà chạy", nhưng cần thống nhất mùa vụ với chủ doanh nghiệp trước → LÊN KẾ HOẠCH, không phải quick win kỹ thuật thuần.

**👉 Use-case chọn cho W2:** kết hợp UC1–UC6 = đúng chuỗi `../../lab.md` TH1→TH2→TH3→TH4a→TH4b, dừng ở "Approved". UC7 (content calendar), UC8 (đăng tự động), UC10 (đo lường) ghi nhận là **mở rộng ngoài phạm vi lab hiện tại** — nêu ở `06-leadership-deck.md` như đề xuất giai đoạn sau, không đưa vào to-be W2/hardening W3.
