# 🧑‍💻 Lab Tự Làm — Buổi 06: Content Engine cho sản phẩm của bạn

> Dành cho học viên tự thực hành ngoài giờ học, với **brief/chân dung/brand voice thật của công ty bạn** thay vì dữ liệu synthetic Sunrise Kids trên lớp.
> Khác với `lab.md` (chạy trên lớp, có GV dẫn, dùng brief mẫu, nộp theo quy trình riêng của buổi học) — bản này bạn tự làm ở nhà và **nộp trên repo GitHub của chính bạn**, không phải repo `hocvien_k1_aiautomation`.
> Khác với `prompts/custom-input-prompt.md` (dùng để **sửa tiếp** engine đã dựng sẵn trên lớp) — bản này bạn **dựng lại từ đầu**, trong repo riêng, với dữ liệu riêng. `custom-input-prompt.md` chỉ dùng lại ở bước nâng cao cuối bài, sau khi engine riêng của bạn đã chạy được.

---

## ⚠️ Cảnh báo dữ liệu (đọc trước khi bắt đầu)

- Repo bạn dùng để nộp bài là **public** — bất kỳ ai có link đều xem được, kể cả sau này bạn xóa file thì lịch sử git vẫn có thể còn giữ lại.
- Nếu `product-brief.md` của bạn chứa số liệu kinh doanh thật (học phí, doanh thu, chiến lược giá chưa công bố), số liệu đó sẽ **công khai vĩnh viễn**. Chỉ đưa vào những gì bạn đã sẵn sàng cho đối thủ nhìn thấy; chỗ nào nhạy cảm thì ghi `[ẩn — không đưa vào bài công khai]` thay vì số thật.
- Đừng dán nguyên văn phản hồi/khiếu nại của khách hàng thật vào `chan-dung.md` hay dùng làm gợi ý seeding — dùng dưới dạng khái quát hóa ("khách hay hỏi về...") thay vì trích dẫn có thể lần ra danh tính người thật.
- Ảnh do AI sinh trong TH3 không dùng ảnh tham chiếu thật, nhưng đừng viết `image_prompt` mô tả đặc điểm nhận dạng của một người cụ thể (kể cả bạn hoặc nhân viên bạn) — giữ nguyên tinh thần "nhân vật minh họa", không phải ảnh thật.
- Đây là lựa chọn và trách nhiệm của bạn. `brand-voice.md` (giọng nói + danh sách cấm) thường ít nhạy cảm, có thể giữ nguyên.

---

## 🤖 Cách nhanh — để Coding Agent tự làm

Bạn có thể mở Coding Agent (Claude Code/Antigravity/Cline...) tại một **thư mục trống, mới, tách biệt** khỏi folder đã clone `hocvien_k1_aiautomation`, dán nguyên văn file `lab_tulam.md` này vào và yêu cầu Agent thực hiện tuần tự các bước bên dưới — kể cả tạo repo, viết brief/chân dung/brand voice, chạy TH1–TH3, `git init`/`commit`/`push`. Agent nên dừng lại hỏi bạn xác nhận trước khi: tạo repo GitHub công khai, trước khi `git push`, và trước khi tạo tài khoản/credential trả phí cho phần TH4 nâng cao (n8n Cloud, API sinh ảnh). Bạn vẫn nên đọc qua các bước dưới để biết Agent đang làm gì và tự kiểm tra kết quả.

## Cách thức làm bài (theo đúng thứ tự thực thi)

1. Tạo một repo GitHub mới (public) cho riêng bạn: bấm **New repository** trên GitHub → đặt tên (vd. `<ten-ban>-k1-buoi06-tulam`) → chọn **Public** → **Create repository** (không tick "Add README", để repo trống).
2. Tạo một **thư mục cục bộ mới, tách biệt** khỏi folder đã clone `hocvien_k1_aiautomation` (tránh lồng 2 git repo). Copy các folder `templates/`, `prompts/`, `schemas/` từ Student Kit buổi 6 vào thư mục mới này, thêm folder rỗng `output_tulam/`.
3. Viết ba file nguyên liệu thật của bạn — đúng theo mô tả ở `prompts/custom-input-prompt.md` mục "Trước khi bắt đầu" (`product-brief.md`, `chan-dung.md`, `brand-voice.md`; xem cảnh báo dữ liệu ở trên). Nếu chưa có dữ liệu thật, cứ **dùng nguyên bộ mẫu Sunrise Kids có sẵn** trong `templates/` — bài tập vẫn chạy tốt.
4. Mở Coding Agent tại thư mục mới này. Chạy đúng 3 prompt có sẵn `prompts/bt1-prompt.md` → `bt3-prompt.md` — **không cần sửa nội dung prompt**, prompt đã được viết để đọc brief/chân dung/brand voice bất kỳ có trong workspace, không hardcode Sunrise Kids.
5. Lưu toàn bộ kết quả (`content-angles.json`, `content-draft.json`, `content-assets.json`) vào folder `output_tulam/`, đúng tên file như trên (không đổi tên) — script kiểm tra ở bước sau cần đúng tên này.
6. Tự kiểm tra:

```bash
python giao_trinh/scripts/validate-b6-artifacts.py output_tulam/
```

   (chạy lệnh này từ thư mục gốc repo `hocvien_k1_aiautomation` đã clone, trỏ đường dẫn tới `output_tulam/` trong thư mục lab tự làm của bạn — hai thư mục tách biệt nên cần đường dẫn tuyệt đối hoặc tương đối chính xác)

7. Commit và đẩy lên repo vừa tạo:

```bash
git init
git add .
git commit -m "buoi 06: content engine voi du lieu cua toi"
git branch -M main
git remote add origin https://github.com/<github-username>/<ten-repo-cua-ban>.git
git push -u origin main
```

Kiểm tra: mở `https://github.com/<github-username>/<ten-repo-cua-ban>` trên trình duyệt, thấy đủ file trong `output_tulam/` là đã đẩy thành công. Mỗi lần cập nhật thêm, chạy lại `git add .` / `git commit -m "..."` / `git push`.

8. Nộp bài theo hướng dẫn ở mục cuối.

### Cấu trúc thư mục đề xuất trong repo riêng của bạn

```
<ten-repo-cua-ban>/
├── templates/              <- copy từ Student Kit, product-brief.md/chan-dung.md/brand-voice.md đã đổi thành thật
├── prompts/                 <- copy nguyên bản (bt1-bt3 bắt buộc; bt4a/bt4b nếu làm phần nâng cao)
├── schemas/                  <- copy nguyên bản, dùng để tự validate output
└── output_tulam/
    ├── content-angles.json     <- kết quả TH1
    ├── content-draft.json       <- kết quả TH2
    ├── content-assets.json      <- kết quả TH3
    └── n8n-workflow-export.json <- (nếu làm TH4a/TH4b) export workflow n8n
```

---

## Chi tiết TH1–TH3 (bắt buộc) — chạy trong cùng phiên chat

Làm đúng theo mô tả TH1, TH2, TH3 trong `lab.md` (mục "TH1 — Brief × chân dung → ý tưởng", "TH2 — Ý tưởng → bài + kịch bản", "TH3 — Seeding + image brief + prompt ảnh"), chỉ khác đầu vào là brief/chân dung/brand voice thật của bạn thay vì Sunrise Kids. Tiêu chí nghiệm thu giữ nguyên như `lab.md`.

**Deliverable bắt buộc:** `content-angles.json`, `content-draft.json`, `content-assets.json` cùng một `brief_id`, `content-draft.json.source_angle_id` khớp một `angle_id` có trong `content-angles.json`, đều PASS schema trong `schemas/`. Không bịa số liệu — chỗ nào brief chưa có (học phí, ưu đãi, ngày cụ thể...) phải giữ `[cần bổ sung]`, không tự điền cho đẹp.

---

## Chi tiết TH4a + TH4b (nâng cao, không bắt buộc) — Đóng gói thành workflow n8n + app duyệt

TH4 cần một **n8n instance của riêng bạn** và **API key sinh ảnh của riêng bạn** (không dùng credential GV cấp trên lớp — credential đó chỉ hoạt động trong buổi học và không nên chia sẻ lại). Nếu muốn làm bước này ở nhà:

1. Tạo tài khoản [n8n Cloud](https://n8n.io) (có gói free/trial) hoặc self-host n8n.
2. Tạo API key riêng tại [Google AI Studio](https://aistudio.google.com) (miễn phí, dùng cho sinh chữ TH1-TH3) và một tài khoản dịch vụ sinh ảnh riêng (dùng cho node ảnh trong TH4a — có thể phát sinh phí, đọc kỹ bảng giá trước khi chạy).
3. Tạo bản sao Google Sheets riêng từ `templates/content-workbook.xlsx` (upload lên Google Drive của bạn → mở bằng Google Sheets), dùng làm sổ cái `Content_Queue`/`Publish_Log` cho n8n của bạn — không dùng chung Sheet với lớp học.
4. Chạy `prompts/bt4a-prompt.md` rồi `prompts/bt4b-prompt.md` như hướng dẫn trong `lab.md`, dùng n8n/credential/Sheet của chính bạn, lấy `content-angles.json`/`content-draft.json`/`content-assets.json` bạn vừa tạo ở TH1-TH3 làm đầu vào — không cần chạy lại "đổi nguyên liệu" vì engine mới dựng đã sẵn dữ liệu của bạn ngay từ đầu.
5. Export workflow ra `output_tulam/n8n-workflow-export.json`.
6. **Nghiệm thu:** `Content_Queue` có ít nhất 1 dòng, app duyệt bấm được Approved, `Publish_Log` ghi được 1 dòng kèm tên người duyệt — giống tiêu chí TH4 trên lớp.

Nếu không có điều kiện tự dựng n8n hoặc không muốn phát sinh chi phí, **bỏ qua TH4a/TH4b** — nộp bài với TH1–TH3 vẫn được tính hợp lệ cho phần tự làm.

**Sau khi TH4a/TH4b chạy được**, nếu muốn mở rộng tiếp (đổi kênh đăng, chạy nhiều brief cùng lúc, sửa giao diện app duyệt), quay lại dùng `prompts/custom-input-prompt.md` — file đó viết riêng cho việc **sửa tiếp** một engine đã chạy, đúng tình huống bạn đang ở lúc này.

---

## Checklist tự kiểm tra trước khi nộp

- [ ] `content-angles.json`, `content-draft.json`, `content-assets.json` đều JSON parse được và PASS đúng schema tương ứng (`python giao_trinh/scripts/validate-b6-artifacts.py output_tulam/` không báo lỗi schema).
- [ ] Cả ba file cùng một `brief_id`; `source_angle_id` trong `content-draft.json` khớp một `angle_id` có thật trong `content-angles.json`.
- [ ] `content-angles.json` phủ ít nhất 2 mã chân dung khác nhau trong `personas_covered`.
- [ ] `content-draft.json.thieu_thong_tin` không bịa lấp — nếu brief của bạn có đủ thông tin thì mảng này có thể rỗng thật (khác Sunrise Kids cố ý thiếu), nhưng phải đúng với brief thật, không phải do AI quên đánh dấu.
- [ ] `content-assets.json` có seeding không khen rỗng, `image_prompt` có `no text`/`no children` nếu bạn giữ nguyên ràng buộc gốc.
- [ ] Không có secret/API key nào bị commit vào repo (kiểm tra lại trước khi push).
- [ ] Đã cân nhắc cảnh báo dữ liệu ở đầu bài — số liệu kinh doanh nhạy cảm (nếu có) đã được xử lý theo lựa chọn của bạn (`[ẩn]` hoặc bỏ qua).

---

## 📮 Hướng dẫn nộp bài

> ⚠️ Bản nháp — quy trình này viết trực tiếp ở đây để dùng ngay cho buổi 6. Khi quy ước nộp bài chung của khóa (`00-khai-giang`) được hoàn thiện, phần này sẽ được đồng bộ lại/rút gọn thành link tới đó.

1. Đảm bảo repo GitHub cá nhân của bạn ở chế độ **Public**.
2. Copy link repo.
3. Điền vào form nộp bài: **[Form Nộp Bài Buổi 6](https://forms.gle/Un7QjLm2U7RA59c19)**.
4. Sau khi nộp, GV sẽ chấm và phản hồi theo tiêu chí ở `lab.md` (áp dụng tương đương cho TH1–TH3; TH4a/TH4b nếu có sẽ được cộng điểm thêm).

---

## Câu hỏi phản tư

1. `brand-voice.md` của Sunrise Kids cấm "cam kết đầu ra", "nêu tên đối thủ". Với ngành/sản phẩm thật của bạn, danh sách cấm nào bạn sẽ thêm mà Sunrise Kids không có?
2. Nếu engine này chạy production cho công ty bạn, lớp hardening nào (CORS/`$json.body`/API key, hay thứ khác) bạn lo nhất — và vì sao?
3. Bạn đã xử lý số liệu kinh doanh/dữ liệu khách hàng thật (nếu có) như thế nào trước khi đưa vào repo public?
4. *(mở rộng thêm, không bắt buộc)* Nếu áp khung thiết kế workflow tổng quát (`workflow_design/README.md`, xem lại slide "Tổng kết ngược" cuối buổi) cho đúng bài toán bạn vừa làm ở đây, use-case của bạn rơi vào góc nào trong ma trận Impact × Difficulty — "làm ngay" hay "lên kế hoạch"?
