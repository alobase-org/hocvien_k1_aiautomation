# Lab — Workflow Mindset: Thiết kế quy trình đáng tin cậy trước khi tự động hóa

> 6 bước móc nối. Output Bước N = input Bước N+1. HV build dần 1 Workflow Design Doc hoàn chỉnh + deck tham mưu lãnh đạo 30 ngày.
> Thời lượng demo: 30 phút (GV demo). 15 phút cuối HV tự chạy 1 bài.

## Mục tiêu lab
- Chọn use-case tối ưu theo ma trận Hiệu quả × Độ phức tạp.
- Thiết kế workflow mới theo ESIA, phân nhánh 3 giải pháp automation.
- Harden workflow cho production (fallback/log/edge/HITL).
- Mô tả workflow bằng Mermaid + render ảnh infographic.
- Dựng deck tham mưu lãnh đạo 30 ngày bằng NotebookLM.

## Mô tả tình huống & Bài toán đặt ra
- **Tình huống thực tế:** Dữ liệu doanh nghiệp của bạn có rất nhiều, tổ chức lộn xộn trên cả máy tính lẫn các kho dữ liệu cloud khác nhau (Google, OneDrive, iCloud...).
- **Vấn đề gặp phải:**
  - **Mất thời gian tìm kiếm:** Khi cần tài liệu, bạn phải tìm kiếm thủ công qua nhiều thư mục/nền tảng khác nhau, có khi mất cả tiếng đồng hồ mà vẫn không thấy.
  - **Rác dữ liệu & Trùng lặp:** Các file được tải xuống nhiều lần, đặt tên tùy tiện (`Document(1).pdf`, `baocao_final_final.docx`), chồng chéo nhiều phiên bản mà không biết bản nào mới nhất.
  - **Thiếu nhất quán:** Không có cấu trúc thư mục rõ ràng hay quy chuẩn đặt tên file, khiến việc chia sẻ và phối hợp trong team gặp khó khăn.
- **Nhu cầu áp dụng AI Automation:**
  - **Tự động phân loại & Sắp xếp:** Sử dụng AI để đọc hiểu nội dung file, tự động nhận diện loại tài liệu, chuẩn hóa tên file theo quy chuẩn và di chuyển/sao chép vào đúng thư mục thích hợp.
  - **Tìm kiếm thông minh:** Xây dựng quy trình tự động trích xuất từ khóa, tìm kiếm và tập hợp nhanh các tài liệu liên quan đến một chủ đề hoặc dự án mới khi cần thiết.
- **Use-case chính xuyên suốt lab:** **Tự động tổ chức tài liệu + Tìm kiếm tài liệu tham khảo**.

> File dữ liệu: `synthetic-data/company-dong-duong-thuongmai.md` (folder lộn xộn mẫu + 10 vấn đề).
> Workflow được giữ **đơn giản (dumb)**: AI Agent chạy các script Python có sẵn để copy/đổi tên file, không cần hệ thống phức tạp.

---

## Bước 0 · Setup môi trường — Antigravity & Extensions (3 phút)

- **🎯 Mục tiêu:** Chuẩn bị và cài đặt các công cụ, extension bổ trợ trên Antigravity IDE nhằm tối ưu hóa việc đọc tài liệu dự án và preview trực quan sơ đồ Mermaid.
- **💡 Vì sao làm bước này:** 
  - Sử dụng **Antigravity IDE** làm môi trường pair-programming với AI trợ lý để thực hiện trực tiếp các bài lab.
  - Cài đặt **Office Viewer** giúp xem trực tiếp các file tài liệu Word/Powerpoint có sẵn trong bài học mà không cần mở ứng dụng ngoài.
  - Cài đặt **Mermaid Preview** giúp xem trực quan, hiển thị sơ đồ quy trình (workflow) dạng Mermaid vẽ bằng code ngay trên IDE.
- **📋 Quy trình tóm tắt:** Thiết lập IDE -> Cài đặt extension Office Viewer -> Cài đặt extension Mermaid Preview.

**🎯 Deliverable:** 
- Môi trường Antigravity sẵn sàng, đọc được tài liệu Office và xem được preview sơ đồ Mermaid trực tiếp trên màn hình code.

### Bước thực hành
1. **(1')** Khởi động Antigravity IDE và mở thư mục chứa mã nguồn lab (`v2.0-workflow-mindset`).
2. **(1')** Truy cập kho tiện ích mở rộng (Extensions Marketplace), tìm và cài đặt:
   - **Office Viewer** (để mở xem trực tiếp các tài liệu `.docx`, `.pptx` của bài học).
   - **Mermaid Preview** / **Mermaid Chart** (để hiển thị sơ đồ từ file `.mmd`).
3. **(1')** Kiểm tra thử nghiệm: Mở một file sơ đồ Mermaid mẫu (ví dụ: [sample-mermaid.mmd](output/sample-mermaid.mmd)), nhấn tổ hợp phím hoặc click nút **Preview** để kiểm tra hình ảnh sơ đồ hiển thị thành công.

---

## Bước 1 · Usecase design — Ma trận ưu tiên & Chi tiết Usecase (7 phút)

- **🎯 Mục tiêu:** Xác định và xếp hạng các vấn đề cần tự động hóa bằng ma trận Hiệu quả × Độ phức tạp, chọn ra use-case tối ưu nhất và thiết kế tổng quan (Usecase Design) để sẵn sàng tự động hóa.
- **💡 Vì sao làm bước này:** Để tránh lãng phí nguồn lực vào các quy trình quá phức tạp nhưng mang lại giá trị thấp. Việc thiết kế chi tiết use-case trước giúp định hình rõ ràng Input, Output, Value kỳ vọng, các rủi ro và điểm HITL cốt lõi từ đầu.
- **📋 Quy trình tóm tắt:** Liệt kê danh sách vấn đề -> Sử dụng AI để phân tích và xếp hạng trên ma trận -> Chọn use-case ưu tiên -> Chạy prompt sinh thiết kế chi tiết `01b-usecase-design.md`.

**🎯 Deliverable:** 
- 1 ma trận Hiệu quả × Độ phức tạp + top-3 use-case nên automate trước.
- 1 file `01b-usecase-design.md` mô tả thiết kế chi tiết của use-case được chọn.
**📊 SLI/SLO:** 
- Ma trận có đủ 4 góc · top-3 use-case ghi rõ lý do.
- File `01b-usecase-design.md` có đầy đủ 6 mục (mô tả, input/output, value, risk, HITL, ràng buộc).

**Prompt:** 
- Ma trận ưu tiên: `prompts/01-usecase-impact-matrix.md`
- Thiết kế chi tiết: `prompts/01b-usecase-design.md`

### Bước thực hành
1. **(1')** Mở `synthetic-data/company-dong-duong-thuongmai.md`, copy list 10 vấn đề (hoặc tự list vấn đề phòng bạn).
2. **(2')** Sử dụng Antigravity, dán prompt `01-usecase-impact-matrix.md`, thay `[LIST VẤN ĐỀ]`.
3. **(1')** Xem ma trận AI đề xuất. Điều chỉnh nếu AI chấm sai use-case bạn rành.
4. **(2')** Chọn use-case ưu tiên số 1 (Tổ chức tài liệu), dán prompt `01b-usecase-design.md` để sinh thiết kế chi tiết. Lưu kết quả ra file `output/01b-usecase-design.md`.

**Đầu ra:** Ma trận 4 góc + top-3 use-case + file [01b-usecase-design.md](output/01b-usecase-design.md). → Input Bước 2.

**📸 Expected result:** 
- Ma trận 2×2 + bảng top-3 (xem [Kết quả chạy BT 1](output/01-usecase-impact-matrix.md) hoặc file thô [sample-problems-list.md](output/sample-problems-list.md)).
- File thiết kế chi tiết: [01b-usecase-design.md](output/01b-usecase-design.md).

---

## Bước 2 · Workflow design — As-is → ESIA to-be (7 phút)

- **🎯 Mục tiêu:** Phân tích quy trình hiện tại (As-is) và thiết kế quy trình mới (To-be) sử dụng khung tư duy ESIA, chỉ rõ vai trò của AI/người và các nhánh công nghệ phù hợp.
- **💡 Vì sao làm bước này:** Nếu tự động hóa một quy trình thủ công tồi tệ và lộn xộn, bạn chỉ nhận được một quy trình tồi tệ chạy nhanh hơn. Thiết kế lại quy trình (ESIA) giúp đơn giản hóa và tối ưu hóa trước khi áp dụng công nghệ.
- **📋 Quy trình tóm tắt:** Lấy tài liệu thiết kế chi tiết `01b-usecase-design.md` từ Bước 1 làm đầu vào -> Đưa vào prompt để AI mô tả quy trình As-is hiện trạng quy trình hiện tại và lưu thành file `02a-workflow-as-is.md` -> Người dùng review và chỉnh sửa file `02a-workflow-as-is.md` để đảm bảo phản ánh đúng thực trạng hiện tại -> Áp dụng khung tư duy ESIA để đề xuất quy trình To-be -> Tách biệt vai trò con người (HITL) và AI, phân loại nhánh công nghệ.

**🎯 Deliverable:** 
- 1 file [02a-workflow-as-is.md](output/02a-workflow-as-is.md) mô tả hiện trạng quy trình hiện tại (bảng 5 cột) đã qua con người review/hiệu chỉnh.
- 1 file Workflow Design Doc [02b-workflow-design-esia.md](output/02b-workflow-design-esia.md).
**📊 SLI/SLO:** as-is ≥5 bước · mỗi bước to-be có 1 ký hiệu E/S/I/A · ≥1 bước A ghi nhánh automation.
**🧩 Use-case demo:** Tự động tổ chức tài liệu (folder lộn xộn → folder đúng chuẩn).

**Prompt:** `prompts/02-workflow-design-esia.md`

### Bước thực hành
1. **(1')** Đọc và sử dụng file thiết kế chi tiết [01b-usecase-design.md](output/01b-usecase-design.md) được tạo ra ở Bước 1 làm input cho Bước 2.
2. **(2')** Sử dụng prompt `prompts/02-workflow-design-esia.md` (trong đó đã được tích hợp trực tiếp toàn bộ nội dung của `01b-usecase-design.md` để chạy luôn). AI sẽ dựa trên thiết kế use-case để mô tả quy trình As-is (đang sắp tài liệu tay). Lưu bảng hiện trạng này thành file [02a-workflow-as-is.md](output/02a-workflow-as-is.md) (tham khảo file mẫu [sample-as-is.md](output/sample-as-is.md)).
3. **(1') [Quan trọng - HITL]** Người dùng đọc và review lại file [02a-workflow-as-is.md](output/02a-workflow-as-is.md), chỉnh sửa thủ công trực tiếp nếu cần thiết để đảm bảo nó phản ánh chính xác thực trạng hiện tại của doanh nghiệp bạn (ví dụ: các ngoại lệ, các thói quen lưu trữ thủ công đặc thù).
4. **(2')** Từ quy trình As-is đã được con người review và chỉnh sửa ở trên, áp dụng khung tư duy ESIA để AI đề xuất quy trình mới To-be (AI Agent chuẩn hóa tên + lên kế hoạch + người dùng duyệt + script copy file).
5. **(1')** Rà soát: bước xóa file / di chuyển file rủi ro → bắt buộc phải có Human-in-the-loop (người dùng xác nhận kế hoạch trước khi thực thi). Xác định rõ nhánh công nghệ tự động hóa.

**Đầu ra:** File [02a-workflow-as-is.md](output/02a-workflow-as-is.md) + Design Doc to-be [02b-workflow-design-esia.md](output/02b-workflow-design-esia.md). → Input Bước 3.

**📸 Expected result:** 
- File hiện trạng đã review: [02a-workflow-as-is.md](output/02a-workflow-as-is.md)
- File thiết kế to-be: [02b-workflow-design-esia.md](output/02b-workflow-design-esia.md)

---

## Bước 3 · Tái thiết kế quy trình hiện đại: Kết hợp Node Automation (n8n) × Agentic × Vibe-coded App & Hardening (5 phút)

- **🎯 Mục tiêu:** Tái tổ chức quy trình To-be theo mô hình hiện đại (phân rã trách nhiệm giữa n8n, AI Agent và Vibe-coded App) đồng thời bổ sung 4 lớp thiết kế an toàn Hardening (Fallback, Log, Edge case, HITL) để sẵn sàng chạy production.
- **💡 Vì sao làm bước này:** 
  - Một hệ thống tự động hóa hiện đại không để LLM làm tất cả (vừa đắt vừa chậm) hay n8n làm tất cả (thiếu trí tuệ). Mô hình chuẩn: **n8n** đóng vai trò điều phối xương sống (gọi API, triggers, routers, loops); **AI Agent** (Claude/Hermes/OpenClaw/Antigravity/Codex) làm bộ não nhận thức (đọc hiểu, lập kế hoạch, phân loại); **Vibe-coded App** (các app dựng nhanh bằng vibe coding) làm cổng kiểm duyệt HITL (dashboard duyệt/sửa file) giúp vận hành mượt mà.
  - Kết hợp thêm 4 lớp phòng thủ Hardening giúp hệ thống không bị sập khi mất mạng, gặp file lỗi hoặc AI ảo tưởng.
- **📋 Quy trình tóm tắt:** Lấy quy trình To-be từ Bước 2 -> Đưa vào prompt để thiết kế mô hình hybrid (n8n, Agent, App) và bổ sung các lớp hardening thích hợp -> Rà soát và cập nhật vào tài liệu thiết kế.

**🎯 Deliverable:** Design doc kiến trúc hybrid & hardening [03-production-hardening.md](output/03-production-hardening.md) (gồm kiến trúc n8n-Agent-App và 4 lớp fallback/log/edge/HITL).

**Prompt:** `prompts/03-production-hardening.md`

### Bước thực hành
1. **(1')** Lấy quy trình To-be từ Bước 2.
2. **(3')** Dán prompt `03-production-hardening.md` vào AI để phân rã quy trình thành mô hình 3 trụ cột (n8n làm điều phối, AI Agent xử lý nhận thức, Vibe-coded App làm UI duyệt kế hoạch) đồng thời thiết kế 4 lớp hardening bảo vệ.
3. **(1')** Rà soát sự phân chia trách nhiệm và các điểm chạm giữa n8n, AI Agent và Vibe-coded App (ví dụ: Vibe-coded App nhận dữ liệu đề xuất từ n8n qua webhook, hiển thị giao diện duyệt cho người dùng bấm Approve). Lưu kết quả ra file [03-production-hardening.md](output/03-production-hardening.md).

**Đầu ra:** File [03-production-hardening.md](output/03-production-hardening.md) kiến trúc hybrid và hardening. → Input Bước 4.

**📸 Expected result:** [03-production-hardening.md](output/03-production-hardening.md) (hoặc xem mẫu kiến trúc hybrid trong [sample-design-doc.md](output/sample-design-doc.md)).

---

## Bước 4 · Vẽ quy trình — Mermaid activity/sequence (5 phút)

- **🎯 Mục tiêu:** Trực quan hóa toàn bộ quy trình To-be kèm các lớp phòng thủ Hardening bằng ngôn ngữ ký hiệu sơ đồ Mermaid.
- **💡 Vì sao làm bước này:** Sơ đồ quy trình trực quan giúp lập trình viên hiểu chính xác cách viết code, và giúp các bên liên quan dễ dàng nhìn nhận, đánh giá lại luồng vận hành mà không cần đọc hàng trang tài liệu chữ.
- **📋 Quy trình tóm tắt:** Đưa thiết kế To-be và Hardening từ Bước 2 & 3 vào AI -> AI tạo mã sơ đồ Mermaid -> Render và kiểm tra hiển thị sơ đồ trên `mermaid.live`.

**🎯 Deliverable:** 1 Mermaid diagram [04-mermaid-diagram.mmd](output/04-mermaid-diagram.mmd).

**Prompt:** `prompts/04-mermaid-diagram.md`

### Bước thực hành
1. **(1')** Lấy to-be + hardening từ Bước 2, Bước 3.
2. **(2')** Dán prompt `04-mermaid-diagram.md` vào AI → nhận mã Mermaid.
3. **(2')** Mở `mermaid.live`, paste mã → xem render. Chỉnh nếu lỗi.

**Đầu ra:** 1 Mermaid diagram code: [04-mermaid-diagram.mmd](output/04-mermaid-diagram.mmd). → Input Bước 5.

**📸 Expected result:** [04-mermaid-diagram.mmd](output/04-mermaid-diagram.mmd)

---

## Bước 5 · Generate ảnh workflow — Prompt infographic (4 phút)

- **🎯 Mục tiêu:** Tạo ra hình ảnh infographic giới thiệu quy trình tự động hóa đẹp mắt, rõ ràng và dễ hiểu bằng công cụ tạo ảnh AI bằng tiếng Việt.
- **💡 Vì sao làm bước này:** Sơ đồ kỹ thuật Mermaid có thể khó hiểu đối với bộ phận kinh doanh hoặc các cấp quản lý phi kỹ thuật. Việc chuyển đổi thành ảnh đồ họa (Before-After hoặc Storytelling) giúp truyền thông quy trình mới hiệu quả hơn và thu hút sự ủng hộ của các bên liên quan.
- **📋 Quy trình tóm tắt:** Lựa chọn phương án vẽ ảnh sơ đồ -> Sử dụng các mẫu prompt AI tương ứng để thiết lập mô tả bằng tiếng Việt -> Chạy prompt trên các mô hình sinh ảnh (Codex, Imagen 3, Midjourney, v.v.).

**🎯 Deliverable:** 
- 1 prompt render ảnh [05-workflow-image-prompt.md](output/05-workflow-image-prompt.md)
- 3 ảnh sơ đồ workflow tiếng Việt tương ứng với 3 phương án:
  - Sơ đồ Trước-Sau: [05-workflow-before-after.png](output/05-workflow-before-after.png)
  - Sơ đồ Kể chuyện: [05-workflow-storytelling.png](output/05-workflow-storytelling.png)
  - Sơ đồ Kiến trúc hệ thống: [05-workflow-system-architecture.png](output/05-workflow-system-architecture.png)
- 1 ảnh workflow infographic chính [05-workflow-infographic.png](output/05-workflow-infographic.png) (sử dụng một trong các ảnh trên để làm slide thuyết trình ở Bước 6).

**Prompt:** `prompts/05-generate-workflow-image.md`

### Bước thực hành
Học viên thực hành và sinh ảnh theo cả 3 phương án chính trong tài liệu prompt:
1. **Phương án 1 (Before-After):** So sánh trực quan quy trình trước khi tối ưu (lộn xộn, thủ công) và sau khi tối ưu bằng AI (gọn gàng, tự động hóa theo ESIA) bằng tiếng Việt.
2. **Phương án 2 (Storytelling):** Vẽ sơ đồ kể chuyện "A Day in the Life" qua các khung tranh mô tả trải nghiệm người dùng và vai trò của AI trợ lý bằng tiếng Việt.
3. **Phương án 3 (System Architecture):** Vẽ sơ đồ kiến trúc hệ thống mô tả hạ tầng các tầng (Edge, Entry, Application Zone, Data Zone, Storage & Analytics) phục vụ cho quy trình bằng tiếng Việt.

**Thao tác thực hành:**
1. **(1')** Mở file prompt mẫu [prompts/05-generate-workflow-image.md](prompts/05-generate-workflow-image.md).
2. **(2')** Chọn phương án phù hợp, thay thế các thông tin trong ngoặc vuông `[...]` bằng dữ liệu thực tế của use-case của bạn dưới dạng tiếng Việt ngắn gọn. Dán vào công cụ sinh ảnh AI để tạo ảnh.
3. **(1')** Kiểm tra hình ảnh đầu ra, tinh chỉnh text tiếng Việt ngắn gọn và xúc tích để AI render chữ sắc nét, tránh bị méo chữ hoặc lỗi font. Lưu 3 ảnh sơ đồ tương ứng thành các file [05-workflow-before-after.png](output/05-workflow-before-after.png), [05-workflow-storytelling.png](output/05-workflow-storytelling.png), [05-workflow-system-architecture.png](output/05-workflow-system-architecture.png) và lưu ảnh infographic chính thành [05-workflow-infographic.png](output/05-workflow-infographic.png).

**Đầu ra:** Đủ 3 ảnh workflow tiếng Việt và 1 ảnh infographic chính trong folder `output`. → Input Bước 6.

---

## Bước 6 · NotebookLM deck — Tham mưu lãnh đạo 30 ngày (5 phút)

- **🎯 Mục tiêu:** Tạo slide deck và tài liệu đề xuất thuyết phục để tham mưu lãnh đạo về kế hoạch hành động triển khai AI Automation trong vòng 30 ngày. Trong đó đề xuất cử nhân sự đi học khóa AI Automation K1 do Alobase tổ chức, khai giảng 16/07/2026 để học cách triển khai workflow thành automation workflow chạy được thực sự, hướng tới tương lai dài hạn xây dựng đội ngũ Forward Deploy Engineer ngay trong tổ chức.
- **💡 Vì sao làm bước này:** Kế hoạch hay đến mấy cũng cần được lãnh đạo phê duyệt để cấp ngân sách và nhân lực. NotebookLM hỗ trợ tổng hợp nhanh toàn bộ tài liệu thiết kế trước đó thành một slide thuyết trình chặt chẽ để thuyết phục ban quản trị.
- **📋 Quy trình tóm tắt:** Chuẩn bị các file nguồn PDF (bằng cách convert các file markdown sang PDF và lưu trữ tại thư mục `output/notebooklm_input/`) -> Tải các file PDF này vào NotebookLM làm nguồn -> Sử dụng prompt CRAFT để sinh nội dung slide (bao gồm đề xuất đào tạo Alobase K1 và xây dựng đội ngũ Forward Deploy Engineer) -> Xem lại và tinh chỉnh số liệu.

**🎯 Deliverable:**
- Thư mục nguồn PDF cho NotebookLM: [output/notebooklm_input/](output/notebooklm_input/)
- 1 prompt NotebookLM (CRAFT) + 1 deck slide tham mưu lãnh đạo [06-leadership-deck.md](output/06-leadership-deck.md).

**Prompt:** `prompts/06-notebooklm-leadership-deck.md`

### Bước thực hành
1. **(1')** Chạy công cụ hoặc script để convert các tài liệu markdown của Bước 1, 2, 3 sang định dạng PDF và lưu trữ vào thư mục [output/notebooklm_input/](output/notebooklm_input/).
   *Vì NotebookLM không hỗ trợ tải trực tiếp các tệp `.md` từ máy tính cá nhân, việc chuyển đổi sang PDF là bắt buộc.*
2. **(1')** Truy cập [NotebookLM](https://notebooklm.google.com), tạo notebook mới.
3. **(1')** Thêm các tệp PDF nguồn từ thư mục [output/notebooklm_input/](output/notebooklm_input/) (bao gồm: `01b-usecase-design.pdf`, `02a-workflow-as-is.pdf`, `02b-workflow-design-esia.pdf`, `03-production-hardening.pdf`).
4. **(2')** Dán prompt `06-notebooklm-leadership-deck.md` (CRAFT) → generate deck.
5. **(1')** Xem deck. Chỉnh tiêu đề + số liệu lợi ích.

**Đầu ra:** Thư mục [output/notebooklm_input/](output/notebooklm_input/) chứa các tệp PDF và 1 deck tham mưu lãnh đạo [06-leadership-deck.md](output/06-leadership-deck.md). **Final output của chuỗi 6 bước.**

---


## 🔁 Workflow mở rộng — Tìm kiếm tài liệu tham khảo (tự thực hành)

> Cùng tư duy Workflow Mindset, áp dụng cho "tìm tài liệu khi bắt đầu 1 việc mới". Dùng sau webinar hoặc cho HV xong nhanh.

**🎯 Deliverable:** folder [reference/](output/reference/) + file [reference_map.md](output/reference_map.md).

**Workflow (đơn giản):**
```
Input: nội dung đang cần làm (vd: "soạn đề xuất đào tạo AI cho bệnh viện")
  → [AI] extract keyword tìm kiếm ("AI đào tạo", "bệnh viện", "y tế", "đề xuất training"...)
  → [AI] search các folder/Drive → danh sách candidate
  → [AI] rerank mức liên quan/hữu ích → top candidate
  → [AI] đọc sâu top candidate → extract điểm hữu ích → ghi vào reference_map.md
  → [AI Agent] copy file top candidate vào folder reference/
Output: folder [reference/](output/reference/) + [reference_map.md](output/reference_map.md) (bảng File | Vị trí | Điểm hữu ích | Trích đoạn liên quan)
```

**Template reference_map.md:** `templates/reference-map-template.md`

> So sánh 2 workflow: **Tổ chức** = sắp xếp input lộn xộn về đúng chỗ (1 lần / định kỳ). **Tìm kiếm** = lấy ra đúng tài liệu cần khi bắt đầu việc mới (mỗi dự án). Cả hai đều cần AI Agent đọc nội dung + HITL khi cần.


---

## Tiêu chí đánh giá & Nộp bài
- Xem tiêu chí đánh giá tại: `../nop-bai/form-nop-bai-webinar3-v2.md` (5 tiêu chí, level 1-5).
- **Link nộp bài để nhận chấm test:** [Form Nộp Bài Test](https://forms.gle/cFR5GVeJ7bcRA1ur5)

## Câu hỏi phản tư
1. Use-case bạn chọn có thực sự là quick win (giá trị cao + dễ) không?
2. Bước nào trong to-be bạn đã đánh Automate nhưng thực ra rủi ro cao → cần HITL?
3. Nếu workflow này chạy production 1 tháng, lớp hardening nào bạn lo nhất?
