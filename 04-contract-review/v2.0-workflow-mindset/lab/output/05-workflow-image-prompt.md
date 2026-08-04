# Mẫu Prompt Sinh Ảnh Sơ Đồ Quy Trình (Bước 5)

Dưới đây là các prompt được điền sẵn thông tin thực tế cho use-case **Tự động tổ chức tài liệu (Document Organization)** bằng tiếng Việt ở mức độ chi tiết cực cao (đầy đủ tất cả các bước nhỏ và nhánh rẽ từ MermaidJS). Học viên có thể copy một trong các phương án dưới đây dán vào các công cụ sinh ảnh AI (như Imagen 3, Gemini, Midjourney, v.v.) để lấy hình ảnh minh họa bằng tiếng Việt cho slide.

---

## 📸 PHƯƠNG ÁN 1: Sơ đồ Infographic Ngang (Dựa trên Mermaid)
*Phù hợp cho slides kỹ thuật mô tả ngang, chứa toàn bộ các bước của quy trình.*

```text
A professional, premium horizontal business process flowchart infographic diagram on a clean, light gray background (#F8FAFC). The design uses crisp technical line-art with subtle pastel color fills and a distinct isometric 3D perspective for icons, structured like a high-end slide.

LAYOUT & STRUCTURE (Left to Right):
- Main Title at the top center: "QUY TRÌNH TỰ ĐỘNG HÓA TÀI LIỆU HYBRID CHI TIẾT" in Vietnamese.
- The diagram flows strictly from left to right, segmented into 4 vertical stages separated by thin elegant vertical dividers:
  1. Giai đoạn 1 (Blue Theme): "1. DATA WATCHER - Thu thập & Quét dữ liệu"
     - Steps (vertical flow within the stage): 
       * "1. Phát hiện file mới" (folder icon)
       * "2. Thư mục trống?" (conditional check). Branch: "Trống" -> "Graceful Exit (Kết thúc êm)"; "Có file" -> "3. Đọc Metadata & MD5" -> "4. Kiểm tra trùng MD5" (conditional check). Branch: "Trùng" -> "Di chuyển sang /TrungLap/ & Ghi log"; "Mới" -> (arrow pointing to Giai đoạn 2).
  2. Giai đoạn 2 (Orange Theme): "2. ROUTING & OCR - Phân luồng & Tiền xử lý"
     - Steps (vertical flow within the stage):
       * "1. Kiểm tra định dạng?". Branch: "Ảnh PNG/JPG" -> "Local OCR" -> "OCR thành công?". Branch: "Không" -> "Vibe App Cảnh báo đỏ"; "Có" -> "Gọi API LLM". Branch: "Văn bản PDF/DOCX" -> "Gọi API LLM".
       * "2. Gọi API LLM (Retry 3 lần)" (icon of API request). Branch: "Lỗi API" -> "Di chuyển sang /LoiHeThong/ & Báo Slack"; "Thành công" -> (arrow pointing to Giai đoạn 3).
  3. Giai đoạn 3 (Purple Theme): "3. AI ANALYSIS - AI Phân tích & Đổi tên"
     - Steps (vertical flow within the stage):
       * "1. AI Phân loại" (brain/robot icon) -> "2. Chuẩn hóa tên theo Policy" -> "3. Tạo đề xuất & Confidence" -> "4. Điểm tin cậy >= 80%?". Branch: ">= 80%" -> "Tab Pending (Duyệt)"; "< 80%" -> "Tab Cảnh báo đỏ (Check tay)" (arrows pointing to Giai đoạn 4).
  4. Giai đoạn 4 (Yellow Theme): "4. HITL & EXECUTION - Kiểm duyệt & Thực thi"
     - Steps (vertical flow within the stage):
       * "1. Người dùng duyệt (HITL)" (user review dashboard icon). Branch: "Reject (Từ chối)" -> "Di chuyển sang /TuChoi/ & Ghi log"; "Approve (Duyệt)" -> "2. Trùng tên đích?". Branch: "Trùng" -> "Đổi tên thêm hậu tố _v1, _v2"; "Không" -> "3. Copy sang thư mục đích" -> "4. So khớp MD5 Checksum?". Branch: "Lệch" -> "Rollback file đích & Báo lỗi"; "Khớp MD5" -> "Xóa file gốc & Báo Slack thành công".

DESIGN & AESTHETICS & LANGUAGE:
- Style: Tech-focused, horizontal flowchart layout, clean studio lighting, vector graphics.
- CRITICAL: All labels, descriptions, titles, and paths inside the diagram must render correctly in Vietnamese, without font errors or spelling mistakes.
```

---

## 📸 PHƯƠNG ÁN 2: Ảnh so sánh Trước - Sau (Before-After Diagram)
*Thuyết phục ban giám đốc bằng cách đối lập sự hỗn loạn thủ công cũ và sự tinh gọn tự động hóa mới.*

```text
A premium, tech-focused Before-After diagram illustrating a process transformation, isometric system architecture illustration, 3D vector style, clean white background.

LAYOUT & STRUCTURE:
- Top Title: "BẢN ĐỒ CHUYỂN ĐỔI: TỰ ĐỘNG HÓA TÀI LIỆU AI HYBRID" in Vietnamese.
- Left Side (Trước - Quy trình thủ công): Depicts the original manual process before applying ESIA. Labeled "TRƯỚC: Quy trình thủ công lộn xộn". Steps include:
  1. Nhận file rời rạc qua email, Zalo, Drive.
  2. Mở đọc từng file thủ công mất thời gian.
  3. Tự quyết định thư mục lưu mà không có quy chuẩn.
  4. Đặt tên file tùy ý, trùng lặp phiên bản.
  5. Di chuyển file bằng tay dễ thất lạc.
  6. Tìm kiếm tài liệu thủ công mất hơn 30 phút.
- Right Side (Sau - Quy trình tự động hóa AI): Depicts the streamlined, highly detailed automated process after optimization, structured into 4 clear vertical columns (Xanh dương, Cam, Tím, Vàng) representing the ESIA framework:
  1. "DATA WATCHER" (I - Tích hợp): Quét tự động phát hiện file mới, Check thư mục trống (nếu trống dừng êm), Tính MD5 Hash, Check file trùng MD5 (trùng di chuyển sang /TrungLap/).
  2. "ROUTING & OCR" (S - Đơn giản hóa): Nhận diện định dạng, chạy OCR nếu là ảnh (OCR lỗi báo Cảnh báo đỏ), Gọi API LLM có retry 3 lần, xử lý lỗi hệ thống qua thư mục `/LoiHeThong/` & báo Slack.
  3. "AI ANALYSIS" (A - Tự động hóa): AI Agent phân loại tài liệu (Category), chuẩn hóa tên file theo quy chuẩn đặt tên, lập Proposed Plan và Confidence Score (tin cậy >= 80% chuyển Pending, < 80% chuyển Cảnh báo đỏ).
  4. "HITL & EXECUTION" (HITL - Người dùng duyệt): Người dùng duyệt trên Dashboard Vibe App (Approve / Reject). Reject di chuyển sang `/TuChoi/`. Approve check trùng tên ở đích (nếu trùng đổi tên thêm _v1, _v2), copy file, so khớp MD5 Checksum (nếu lệch rollback, nếu khớp xóa file gốc).

DESIGN & AESTHETICS & LANGUAGE:
- Style: Isometric view, soft shadows, shades of blue, orange, purple, and yellow.
- Clean typography using a modern sans-serif font (Inter or Segoe UI) with high contrast and legible, clear text labels.
- CRITICAL: All titles, labels, step numbers, and explanations inside the diagram must be in clear, readable Vietnamese.
```

---

## 📸 PHƯƠNG ÁN 3: Ảnh quy trình kể chuyện (Storytelling Infographic)
*Phù hợp cho slide thuyết trình chính, thể hiện trải nghiệm hàng ngày của nhân viên được AI hỗ trợ.*

```text
A premium, modern, and clean business storytelling infographic on a minimalist light gray (#F8FAFC) background. The theme is "Hành trình: Trợ lý Sắp xếp Tài liệu AI" illustrating how the new AI-powered workflow transforms daily operations and benefits key stakeholders. The infographic is designed for a professional business presentation deck.

1. Layout & Structure:
- Labeled cleanly in Vietnamese: "QUY TRÌNH MỚI: Tự động hóa Sắp xếp Tài liệu" with a smaller subtitle: "Phối hợp n8n × AI Agent × Vibe App".
- The design is structured as a sequential storytelling journey of 4 detailed sequential panels (comic-style blocks), colored in Blue, Orange, Purple, and Yellow.

2. Panels & Story Steps (All text in Vietnamese):
- Panel 1 - Giai đoạn Thu thập (Blue Theme):
  - Visual: Folder watcher scans Google Drive and Local folders.
  - Steps: "1. Quét file mới" -> "2. Check trống (nếu trống kết thúc)" -> "3. Đọc Metadata & MD5 Hash" -> "4. Check trùng MD5 (nếu trùng di chuyển sang /TrungLap/)".
- Panel 2 - Giai đoạn Phân luồng & OCR (Orange Theme):
  - Visual: n8n routing files and processing OCR.
  - Steps: "1. Kiểm tra định dạng file" -> "2. Chạy local OCR nếu là ảnh (lỗi chuyển Cảnh báo đỏ)" -> "3. Gọi API LLM (thử lại 3 lần, lỗi chuyển /LoiHeThong/ & báo Slack)".
- Panel 3 - Giai đoạn AI Phân tích (Purple Theme):
  - Visual: A sleek AI mascot processing document content.
  - Steps: "1. AI đọc hiểu & Phân loại category" -> "2. Đổi tên theo Policy" -> "3. Chấm điểm tin cậy (>= 80% sang Pending, < 80% sang Cảnh báo đỏ)".
- Panel 4 - Giai đoạn Duyệt & Thực thi (Yellow Theme):
  - Visual: User reviewing dashboard and files moving to folders.
  - Steps: "1. HITL Duyệt trên Vibe App (Approve/Reject)" -> "2. Check trùng tên tại đích" -> "3. Copy file" -> "4. MD5 Checksum match (Rollback nếu lệch, Xóa file gốc nếu khớp)".

3. Design & Aesthetics Style & Language:
- Use a professional modern flat vector illustration style, storytelling comic strip design, subtle drop shadows, studio lighting, vector graphics.
- Clean typography using a modern sans-serif font (Inter or Segoe UI) with high contrast and legible, clear text labels.
- CRITICAL: All titles, step labels, and descriptions must render in Vietnamese correctly.
```

---

## 📸 PHƯƠNG ÁN 4: Sơ đồ kiến trúc hệ thống (System Architecture Diagram)
*Thuyết phục bộ phận hạ tầng & IT bằng cách trình bày chính xác sơ đồ mạng, bảo mật và kết nối các tầng.*

```text
A professional, modern system architecture diagram illustrating a hybrid AI Automation workflow on a clean, light gray background (#F8FAFC). The design uses clean vector illustration with subtle pastel color fills and a distinct isometric 3D perspective for system components.

LAYOUT FLOW (Left to Right):
- Input Source Layer: On the far left, cloud and local storage icons labeled "Nguồn tài liệu lộn xộn" (including Google Drive, OneDrive, Local Folder) with arrows pointing to the next layer.
- Orchestration Layer (n8n): In the center-left, a large gear and workflow node connector icon labeled "n8n (Bộ điều phối & OCR)" that triggers on new files, extracts MD5, runs local OCR if needed, and routes them.
- Cognitive AI Layer: On the top-middle, a glowing brain/robot icon labeled "AI Agent (Claude/Hermes)" that connects bidirectionally to n8n to classify files and propose standardized names.
- HITL Review Layer (Vibe App & User): On the bottom-middle, a sleek dashboard screen interface labeled "Vibe App (Giao diện HITL)" with a mock pending-list and a green checkmark button, connecting to a person icon labeled "Người dùng (Duyệt kế hoạch)". n8n sends proposals to the Vibe App, and the User's approvals trigger actions back in n8n.
- Output & Storage Layer: On the far right, two paths branching from n8n:
  1. Neat, organized folder stack icons labeled "Thư mục đích chuẩn hóa" (e.g. /HopDong/, /HoaDon/, /BaoCao/).
  2. Fallback folder icons labeled "Thư mục Dự phòng & Lỗi" (e.g. /TrungLap/, /LoiHeThong/, /TuChoi/).
  - A small log table icon on the bottom right labeled "Nhật ký (CSV & Slack)".

DESIGN & AESTHETICS & LANGUAGE:
- Use a professional, harmonious modern pastel color palette (soft blue, warm gold, fresh green, light purple) with distinct isometric 3D vector graphics.
- Clean flat vector illustration style, subtle drop shadows, studio lighting, vector graphics.
- Clean typography using a modern sans-serif font (Inter or Segoe UI) with high contrast and legible, clear text labels.
- Avoid cluttered or messy details, keeping the layout perfectly aligned and balanced with plenty of white space.
- CRITICAL: All labels, text descriptions, and titles in this system architecture diagram must render in Vietnamese correctly.
```
