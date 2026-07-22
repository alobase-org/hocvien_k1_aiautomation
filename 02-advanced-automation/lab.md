# Lab Handout — Buổi 02 (advanced-automation)

> File dành cho HỌC VIÊN (sẽ sync sang `studentkit/`). Đáp án/expected output để ở `checkpoints/`.

## Workflow
Cấu hình n8n & Credentials (OAuth2 + Gemini Key) → AI thiết kế luồng JSON → Import & Chỉnh sửa n8n Workflow → Dựng Luồng Nhắc việc & Gửi Email → Tích hợp Gemini API tự động soạn Email theo từ khóa.

## KPI / Sản phẩm đầu ra
1. Cấu hình hoàn tất n8n Cloud và kết nối thành công 3 Credentials: Google Sheets (OAuth2), Gmail (OAuth2), Google AI Studio (Gemini API Key).
2. Sử dụng AI sinh thành công file JSON workflow n8n rà soát công việc và import mượt mà vào n8n Canvas.
3. Chạy hoàn chỉnh luồng Nhắc việc tự động: Đọc Sheet CongViec (`1ViOwxqyqNoB9LUa0dJUNGoEGAyyfS-1RmsZeDDrnjgM`) → Lọc việc chưa xong → Ghi vào Sheet NhacViec → Tự động gửi Email nhắc việc. (Hiểu tư duy chuyển đổi sang Google AppsScript).
4. Dựng thành công luồng n8n tích hợp Gemini API: Đọc từ khóa từ Google Sheet (`https://docs.google.com/spreadsheets/d/1kU1hP5zpGh7DjhAee8wmfCALQwfy2fQgzCkz4Eao_HM/...`) → Gọi Gemini API tự động sinh Tiêu đề & Nội dung email → Ghi ngược vào bảng tính Google Sheet.

## Điều kiện tiên quyết
- Đã hoàn thành Buổi 01 (có kho bài tập `hocvien_k1_aiautomation`, đã cài ứng dụng AI).
- Có tài khoản n8n Cloud (hoặc self-hosted) và tài khoản Google (Gmail, Google Drive, Google AI Studio).
- Đã lưu bản sao (Make a copy) các file Google Sheet mẫu về Google Drive cá nhân.

## Công cụ
n8n Cloud / Self-hosted · Google AI Studio (Gemini API Key) · Google Sheets / Gmail (OAuth2 Credential) · AI Chatbot (ChatGPT/Claude/Antigravity) · Google AppsScript (tùy chọn)

## Các phân đoạn thực hành (TH1 → TH4 = pipeline)
> Output TH_N = Input TH_{N+1}.

### TH1 — Phân đoạn 1 — Đăng ký n8n Cloud & Cấu hình Chìa khóa kết nối (Credentials & Bảo mật)
- **Mô tả kỹ thuật (Input → Action → Output):** 
  - *Lý thuyết:* Hiểu kiến trúc n8n (Low-code/No-code, Canvas), khái niệm Trigger – Node – Action, bảo mật Credentials (OAuth2, API Key) và nguyên tắc "Human-in-the-loop" (AI chỉ soạn nháp, con người duyệt và bấm Gửi).
  - *Thực hành:* Đăng ký n8n Cloud. Cấu hình 3 bộ Chìa khóa kết nối (Credentials):
    1. Google Sheets OAuth2 (cấp quyền đọc/ghi bảng tính).
    2. Gmail OAuth2 (cấp quyền tạo nháp/gửi mail).
    3. Google AI Studio Gemini API Key (kết nối gọi mô hình LLM).
- **Công cụ:** n8n Cloud + Google AI Studio + Google Cloud Console
- **Đầu ra:** ★ 3 Credentials đã test kết nối thành công (`Connected`)

### TH2 — Phân đoạn 2 — Sử dụng AI như Trợ lý thiết kế luồng tự động & Import JSON
- **Mô tả kỹ thuật (Input → Action → Output):** 
  - *Lý thuyết:* Nắm cách truyền dữ liệu JSON trong n8n (`{{ $json["Mô tả sự cố"] }}`).
  - *Thực hành:* Soạn prompt mô tả bối cảnh & chỉ dẫn bằng ngôn ngữ tự nhiên: *"Rà soát người chưa hoàn thành công việc trong sheet CongViec và ghi vào sheet NhacViec, xuất file JSON để đưa vào n8n"*.
  - Nhận file JSON từ AI, tải (Import) lên n8n Canvas và tiến hành kiểm tra/chỉnh sửa node.
  - *Checklist điểm kiểm tra:* (1) Email n8n có trùng với email Google Drive? (2) Đã lưu file Sheet giảng viên về Drive cá nhân chưa? (3) Google Drive có bị đầy bộ nhớ không?
- **Công cụ:** ChatGPT / Claude + n8n Canvas + Google Sheets
- **Đầu ra:** ★ Workflow JSON được AI thiết kế và import thành công trên n8n

### TH3 — Phân đoạn 3 — Dựng Luồng Nhắc việc tự động & Gửi Email (n8n / Google AppsScript)
- **Mô tả kỹ thuật (Input → Action → Output):** 
  - *Thực hành:* Mở Google Sheet bài tập (ID: `1ViOwxqyqNoB9LUa0dJUNGoEGAyyfS-1RmsZeDDrnjgM`).
  - Dựng luồng n8n: Schedule/Manual Trigger → Google Sheets Read (`tab CongViec`) → IF (`Trạng thái ≠ Hoàn thành`) → Edit Fields (soạn nội dung nhắc việc) → 2 nhánh song song: Append log vào `Sheet NhacViec` + Gmail Send Email nhắc việc người phụ trách.
  - *Gợi ý nâng cao:* Tìm hiểu tư duy làm bằng Google AppsScript với logic tương tự 100% để tối ưu chi phí vận hành cho doanh nghiệp.
- **Công cụ:** n8n + Google Sheets + Gmail (Google AppsScript)
- **Đầu ra:** ★ Luồng nhắc việc và gửi email tự động chạy thành công

### TH4 — Phân đoạn 4 — Đưa AI (Gemini API) vào Luồng n8n Soạn thảo Email theo từ khóa
- **Mô tả kỹ thuật (Input → Action → Output):** 
  - *Thực hành:* Mở Google Sheet bài tập tích hợp AI (`https://docs.google.com/spreadsheets/d/1kU1hP5zpGh7DjhAee8wmfCALQwfy2fQgzCkz4Eao_HM/...`).
  - Dựng luồng n8n: Read Google Sheet (đọc từ khóa/yêu cầu) → Call Google API (Gemini Node / HTTP Request với Gemini API Key) → Code node làm sạch JSON bọc markdown (nếu có) → Update Google Sheets (ghi kết quả vào cột Tiêu đề và Nội dung).
  - *Kỹ thuật:* Sử dụng data pinning / giữ `row_number` để node Update ghi kết quả đúng dòng gốc.
- **Công cụ:** n8n + Google Gemini API + Google Sheets
- **Đầu ra:** ★ Workflow AI n8n sinh nội dung email tự động ghi vào Google Sheets

## Bài tập về nhà
- Thực hành nâng cấp workflow Buổi 02: Thêm bước Human-in-the-loop (Gemini chỉ tạo Gmail Draft + đánh dấu 'Chờ duyệt', người quản lý gõ 'Gửi' mới tiến hành gửi email chính thức).
- Viết thử nghiệm đoạn mã Google AppsScript tương đương cho luồng Nhắc việc để so sánh với n8n.

## Checklist nghiệm thu
- [ ] Cấu hình thành công 3 Credentials trên n8n (Google Sheets, Gmail, Gemini API Key).
- [ ] Import file JSON được thiết kế bởi AI vào n8n thành công không báo lỗi.
- [ ] Luồng Nhắc việc lọc chính xác công việc tồn đọng, ghi log vào Sheet NhacViec và gửi email nhắc việc.
- [ ] Luồng Gemini AI gọi thành công API và tự động điền Tiêu đề + Nội dung email vào Google Sheet.
