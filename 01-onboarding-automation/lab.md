# Lab Handout — Buổi 01 (onboarding-automation)

> File dành cho HỌC VIÊN (sẽ sync sang `studentkit/`). Đáp án/expected output để ở `checkpoints/`.

## Workflow
Cài đặt Hybrid AI Agents (Antigravity 2.0 / Codex / Claude Code) → Gọi Nhân sự số → Quản lý Skill (.md) → Đồng bộ GitHub Repository (`hocvien_k1_aiautomation.git`).

## KPI / Sản phẩm đầu ra
1. Cài đặt thành công ít nhất 2/3 ứng dụng Hybrid AI trên máy tính (Antigravity 2.0, Codex, Claude Code).
2. Tạo & kích hoạt được Nhân sự số AI trên máy tính, sẵn sàng thực thi câu lệnh.
3. Cài đặt trình xem Markdown (Markdown View) và đọc/quản lý thành công file Skill định dạng `.md`.
4. Git clone thành công kho bài tập `hocvien_k1_aiautomation.git` từ GitHub về thư mục làm việc cục bộ `K1-HOCVIEN-AIAT`.

## Điều kiện tiên quyết
- Máy tính cá nhân (macOS hoặc Windows) đã cài đặt Git và VS Code / Terminal.
- Tài khoản GitHub cá nhân và kết nối Internet ổn định.

## Công cụ
Hybrid AI Agents (Antigravity 2.0 · Codex · Claude Code/CLI) · Markdown View · Git / GitHub (`https://github.com/alobase-org/hocvien_k1_aiautomation.git`)

## Các phân đoạn thực hành (TH1 → TH4 = pipeline)
> Output TH_N = Input TH_{N+1}.

### TH1 — Phân đoạn 1 — Cài đặt Siêu trợ lý AI trên máy tính (Hybrid AI)
- **Mô tả kỹ thuật (Input → Action → Output):** 
  - *Lý thuyết:* Hiểu 3 cách dùng AI phổ biến (Web-based, Local, Hybrid). Tránh rủi ro rò rỉ dữ liệu của Web-based và tối ưu chi phí hạ tầng so với Pure Local bằng giải pháp Hybrid AI.
  - *Thực hành:* Học viên tiến hành tải và cài đặt THÀNH CÔNG 2/3 ứng dụng AI ở môi trường trên máy tính: **Antigravity 2.0**, **Codex**, hoặc **Claude Code / CLI**.
- **Công cụ:** Antigravity 2.0 / Codex / Claude Code CLI
- **Đầu ra:** ★ Ứng dụng Hybrid AI cài đặt thành công trên máy tính

### TH2 — Phân đoạn 2 — Tạo & Gọi Nhân viên AI (Nhân sự số) trên máy tính
- **Mô tả kỹ thuật (Input → Action → Output):** 
  - *Thực hành:* Mở ứng dụng AI đã cài đặt, tiến hành khởi tạo và thiết lập không gian làm việc cho Trợ lý AI.
  - Thực hành gọi "Nhân sự số" ra bằng câu lệnh (Codex / Antigravity), gán vai trò trợ lý vận hành chuyên trách cho doanh nghiệp.
- **Công cụ:** Codex / Antigravity
- **Đầu ra:** ★ Nhân viên AI được kích hoạt và sẵn sàng nhận lệnh

### TH3 — Phân đoạn 3 — Cài đặt Markdown Viewer & Quản lý File Skill (.md)
- **Mô tả kỹ thuật (Input → Action → Output):** 
  - *Lý thuyết:* Hiểu Markdown là ngôn ngữ đánh dấu đơn giản giúp AI hiểu cấu trúc văn bản. Nắm vững cấu trúc chuẩn 4 phần của một Skill Doanh nghiệp: **Bối cảnh → Dữ liệu đầu vào → Quy trình xử lý → Tiêu chuẩn đầu ra**.
  - *Thực hành:* Cài đặt trình duyệt/tiện ích mở rộng **Markdown View** (tương tự trình đọc PDF) để xem và trực quan hóa các file Skill đuôi `.md`. Mở file `.md` bài tập để kiểm tra thể thức văn bản chuẩn.
- **Công cụ:** Markdown View / VS Code / Antigravity
- **Đầu ra:** ★ Trình xem Markdown hoạt động chuẩn, đọc & làm chủ file Skill `.md`

### TH4 — Phân đoạn 4 — Đồng bộ dữ liệu Nhân viên AI với GitHub
- **Mô tả kỹ thuật (Input → Action → Output):** 
  - *Thực hành:* Mở Terminal/VS Code tại thư mục làm việc `K1-HOCVIEN-AIAT`.
  - Thực hiện lệnh clone repository chính thức của khóa học:
    ```bash
    git clone https://github.com/alobase-org/hocvien_k1_aiautomation.git
    ```
  - Kiểm tra toàn bộ tài liệu, slide, template và lab handout đã được đồng bộ về máy. Thực hành lệnh `git pull` để nhận các cập nhật mới nhất từ giảng viên.
- **Công cụ:** Git / Terminal / GitHub
- **Đầu ra:** ★ Kho lưu trữ `hocvien_k1_aiautomation` đồng bộ thành công về máy local

## Bài tập về nhà
- Hoàn thiện cài đặt đủ 3/3 ứng dụng Hybrid AI trên máy tính.
- Tự viết 01 file Skill dạng Markdown (`.md`) chuẩn 4 phần theo nghiệp vụ thực tế tại doanh nghiệp của bạn và lưu vào folder bài tập.

## Checklist nghiệm thu
- [ ] Cài đặt thành công ít nhất 2/3 ứng dụng (Antigravity 2.0, Codex, Claude Code).
- [ ] Mở ứng dụng và gọi thành công Nhân viên AI bằng câu lệnh.
- [ ] Cài đặt thành công trình duyệt/extension Markdown View và xem được file `.md`.
- [ ] Lệnh `git clone` kho `hocvien_k1_aiautomation.git` chạy thành công không có lỗi.
