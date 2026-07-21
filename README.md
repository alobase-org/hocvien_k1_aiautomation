# Tài liệu khóa học — K1 AI Automation & Vibe Coding

Chào mừng bạn đến với kho tài liệu chính thức của khóa **K1 AI Automation & Vibe Coding**.
Toàn bộ slide, bài thực hành, prompt và template đều nằm trong repo này.

> Repo này là **bản dành cho học viên**. Mọi nội dung đã được tinh gọn — không kèm đáp án,
> không kèm script giảng dạy. Bạn lấy gì, làm nấy, nộp bài đúng hạn là xong.

---

## Cách lấy tài liệu về máy

**Cách 1 — Tải ZIP (đơn giản nhất):** nút `Code` (góc phải) → `Download ZIP`.

**Cách 2 — Clone (khuyên dùng, để cập nhật mỗi buổi):**
```bash
git clone https://github.com/alobase-org/hocvien_k1_aiautomation.git
```
Khi GV cập nhật tài liệu, bạn chỉ cần:
```bash
git pull
```
Chưa cài Git? Xem hướng dẫn ở buổi khai giảng, hoặc dùng Cách 1.

---

## Cấu trúc folder — đi theo số buổi

Mỗi folder là **một buổi học**, đặt tên `BB-tên-buổi` (BB = số buổi):

| Folder | Buổi |
|---|---|
| `00-khai-giang` | Khai giảng — cách học, cách nộp bài |
| `01-onboarding-automation` | B1 — Làm quen automation |
| `02-advanced-automation` | B2 — Automation nâng cao |
| `03-hr-screening` | B3 — Sàng lọc CV ứng viên |
| `04-contract-review` | B4 — Rà soát hợp đồng |
| `05-cskh-bot` | B5 — Chatbot chăm sóc khách hàng |
| `06-content-engine` | B6 — Engine sản xuất nội dung |
| `07-ai-video` | B7 — Sản xuất video AI |
| `08-capstone` | B8 — Đồ án tốt nghiệp |

---

## Trong mỗi buổi có gì?

Mở folder buổi học, bạn sẽ thấy:

- **`README.md`** — tổng quan buổi: mục tiêu, mục tiêu đầu ra, flow bài học. **Đọc cái này đầu tiên.**
- **`buoi-BB-*.pptx`** — slide giảng dạy. Mở để ôn lại lý thuyết và demo.
- **`lab.md`** — đề bài thực hành chi tiết. Đây là **trục chính** để bạn làm bài.
- **`prompts/`** — các prompt đã soạn sẵn, **copy-paste** thẳng vào Claude / ChatGPT / n8n.
  - `bt1-prompt.md`, `bt2-prompt.md`... theo từng bài tập.
  - `custom-input-prompt.md` — khi bạn muốn dùng dữ liệu của chính mình.
- **`templates/`** — file mẫu (input, rubric, JD, workbook...) để bạn điền vào.
- **`schemas/`** (một số buổi) — schema JSON để kiểm tra output đúng cấu trúc trước khi nộp.

---

## Quy trình làm bài chuẩn (mỗi buổi)

1. **Đọc `README.md`** của buổi → nắm mục tiêu.
2. **Làm theo `lab.md`** từng bước.
3. Khi gặp bài tập, mở **`prompts/btX-prompt.md`** → copy → dán vào công cụ AI.
4. Lấy input từ **`templates/`** (hoặc dùng dữ liệu thật của bạn qua `custom-input-prompt.md`).
5. Nếu có **`schemas/`**, validate output của bạn khớp schema trước khi nộp.
6. **Nộp bài** theo hướng dẫn trong `lab.md` (thường là nộp link output / file kết quả).

> 💡 Mẹo: làm đúng thứ tự bài tập (bt1 → bt2 → ...). Các bài sau thường dựng trên kết quả bài trước.

---

## Buổi khai giảng — đọc kỹ trước khi bắt đầu

Vào `00-khai-giang/` để biết:
- Cách học khóa này hiệu quả
- Cách nộp bài và tiêu chuẩn chấm
- Công cụ cần cài đặt

---

## Cập nhật tài liệu

GV có thể bổ sung / chỉnh sửa tài liệu trong quá trình học. **Mỗi trước buổi học, chạy lại:**
```bash
git pull
```
để đảm bảo bạn đang dùng phiên bản mới nhất.

---

## Cần hỗ trợ?

- Câu hỏi về bài tập → đặt trong nhóm lớp / kênh hỗ trợ của buổi.
- Lỗi tài liệu (link hỏng, nội dung sai) → báo lại GV hoặc comment trên folder buổi đó.

Chúc bạn học tốt — và biến từng bài tập thành automation thật sự chạy được trong công việc. 🚀
