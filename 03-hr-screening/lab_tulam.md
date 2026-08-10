# 🧑‍💻 Lab Tự Làm — Buổi 03: HR Screening Workflow 4 lớp

> Dành cho học viên tự thực hành ngoài giờ học, với **CV/JD thật của công ty bạn** thay vì dữ liệu synthetic trên lớp.
> Khác với `lab.md` (chạy trên lớp, có GV dẫn, dùng CV mẫu, nộp theo quy trình riêng của buổi học) — bản này bạn tự làm ở nhà và **nộp trên repo GitHub của chính bạn**, không phải repo `hocvien_k1_aiautomation`.

---

## ⚠️ Cảnh báo dữ liệu cá nhân (đọc trước khi bắt đầu)

- Repo bạn dùng để nộp bài là **public** — bất kỳ ai có link đều xem được, kể cả sau này bạn xóa file thì lịch sử git vẫn có thể còn giữ lại.
- Nếu CV bạn dùng chứa thông tin thật của một ứng viên (tên, số điện thoại, email, link LinkedIn...), thông tin đó sẽ **công khai vĩnh viễn**.
- Đây là lựa chọn và trách nhiệm của bạn. Gợi ý an toàn: đổi tên ứng viên thành "Ứng viên A", xóa số điện thoại/email thật trước khi dán CV vào Agent — giữ nguyên phần kinh nghiệm/kỹ năng để bài tập vẫn phản ánh đúng tình huống thật.
- JD và rubric của công ty thường ít nhạy cảm hơn CV cá nhân, có thể giữ nguyên nếu công ty bạn không yêu cầu bảo mật riêng.

---

## 🤖 Cách nhanh — để Coding Agent tự làm

Bạn có thể mở Coding Agent (Claude Code/Antigravity/Cline...) tại một **thư mục trống, mới, tách biệt** khỏi folder đã clone `hocvien_k1_aiautomation`, dán nguyên văn file `lab_tulam.md` này vào và yêu cầu Agent thực hiện toàn bộ 8 bước bên dưới tuần tự — kể cả tạo repo, sửa CV/JD, chạy TH1–TH4, `git init`/`commit`/`push`. Agent nên dừng lại hỏi bạn xác nhận trước khi: tạo repo GitHub công khai, và trước khi `git push` (vì đây là hành động công khai không dễ đảo ngược). Bạn vẫn nên đọc qua các bước dưới để biết Agent đang làm gì và tự kiểm tra kết quả.

## Cách thức làm bài (theo đúng thứ tự thực thi)

1. Tạo một repo GitHub mới (public) cho riêng bạn: bấm **New repository** trên GitHub → đặt tên (vd. `<ten-ban>-k1-buoi03-tulam`) → chọn **Public** → **Create repository** (không tick "Add README", để repo trống).
2. Tạo một **thư mục cục bộ mới, tách biệt** khỏi folder đã clone `hocvien_k1_aiautomation` (tránh lồng 2 git repo). Copy các folder `templates/`, `prompts/`, `schemas/` từ Student Kit buổi 3 vào thư mục mới này, thêm folder rỗng `output_tulam/`.
3. Sửa nội dung `templates/cv-b2b-junior-input.md` và `templates/JD-nhan-vien-kinh-doanh-B2B-junior.md` thành CV/JD thật của bạn (xem cảnh báo PII ở trên). Nếu chưa có dữ liệu thật, cứ **dùng nguyên hai file mẫu có sẵn** — bài tập vẫn chạy tốt. **Giữ nguyên** `templates/rubric-kinh-doanh-B2B-100.json` — nếu vai trò bạn chọn không phải Sales B2B, rubric có thể không khớp hoàn toàn, bài vẫn chạy được nhưng điểm số chỉ mang tính minh họa, không phải rubric chuẩn cho vai trò đó.
4. Mở Coding Agent tại thư mục mới này. Chạy đúng 4 prompt có sẵn `prompts/bt1-prompt.md` → `bt4-prompt.md` — **không cần sửa nội dung prompt**, prompt đã được viết để đọc CV/JD bất kỳ có trong workspace, không hardcode dữ liệu mẫu.
5. Lưu toàn bộ kết quả (`candidate-profile.json`, `data-quality.json`, `scoring-result.json`, `run-log.jsonl`) vào folder `output_tulam/`.
6. Tự kiểm tra theo checklist bên dưới.
7. Commit và đẩy lên repo vừa tạo:

```bash
git init
git add .
git commit -m "buoi 03: tu lam voi du lieu cua toi"
git branch -M main
git remote add origin https://github.com/<github-username>/<ten-repo-cua-ban>.git
git push -u origin main
```

Kiểm tra: mở `https://github.com/<github-username>/<ten-repo-cua-ban>` trên trình duyệt, thấy đủ file trong `output_tulam/` là đã đẩy thành công. Mỗi lần cập nhật thêm, chạy lại `git add .` / `git commit -m "..."` / `git push`.

8. Nộp bài theo hướng dẫn ở mục cuối.

### Cấu trúc thư mục đề xuất trong repo riêng của bạn

```
<ten-repo-cua-ban>/
├── templates/              <- copy từ Student Kit, đã sửa CV/JD thật của bạn
├── prompts/                 <- copy nguyên bản 4 prompt, không sửa
├── schemas/                  <- copy nguyên bản, dùng để tự validate output
└── output_tulam/
    ├── candidate-profile.json   <- kết quả TH1
    ├── data-quality.json         <- kết quả TH2
    ├── scoring-result.json       <- kết quả TH3
    ├── run-log.jsonl               <- log 3 dòng TH1–TH3, cùng run_id
    └── workflow-export.json      <- (nếu làm TH4) export workflow n8n
```

---

## Chi tiết TH1–TH3 (bắt buộc) — chạy trong cùng phiên chat

Làm đúng theo mô tả TH1, TH2, TH3 trong `lab.md` (mục "TH1 — Bóc tách và chuẩn hóa CV", "TH2 — Rà soát chất lượng dữ liệu", "TH3 — Áp rubric 100 điểm"), chỉ khác đầu vào là CV/JD thật của bạn thay vì file mẫu. Tiêu chí nghiệm thu giữ nguyên như `lab.md`.

**Deliverable bắt buộc:** `candidate-profile.json`, `data-quality.json`, `scoring-result.json` cùng một `candidate_id`, và `run-log.jsonl` có đúng 3 dòng TH1–TH3 cùng một `run_id`, đều PASS schema trong `schemas/`.

---

## Chi tiết TH4 (nâng cao, không bắt buộc) — Đóng gói thành workflow n8n

TH4 cần một **n8n instance của riêng bạn** (không dùng credential Google AI Studio mà GV cấp trên lớp — credential đó chỉ hoạt động trong buổi học). Nếu muốn làm bước này ở nhà:

1. Tạo tài khoản [n8n Cloud](https://n8n.io) (có gói free/trial) hoặc self-host n8n.
2. Tạo API key riêng tại [Google AI Studio](https://aistudio.google.com) (miễn phí), cấu hình credential Header Auth trên n8n của bạn.
3. Chạy `prompts/bt4-prompt.md` như hướng dẫn trong `lab.md`, dùng n8n/credential của chính bạn.
4. Export workflow ra `output_tulam/workflow-export.json`.

Nếu không có điều kiện tự dựng n8n, **bỏ qua TH4** — nộp bài với TH1–TH3 vẫn được tính hợp lệ cho phần tự làm.

---

## Checklist tự kiểm tra trước khi nộp

- [ ] `candidate-profile.json`, `data-quality.json`, `scoring-result.json` đều JSON parse được và PASS đúng schema tương ứng trong `schemas/`.
- [ ] Cả ba file cùng một `candidate_id`.
- [ ] `run-log.jsonl` có đúng 3 dòng TH1–TH3, cùng một `run_id`.
- [ ] Rubric trong `scoring-result.json` cộng đúng tổng tối đa 100.
- [ ] Không có secret/API key nào bị commit vào repo (kiểm tra lại trước khi push).
- [ ] Đã cân nhắc cảnh báo PII ở đầu bài — dữ liệu ứng viên thật (nếu có) đã được xử lý theo lựa chọn của bạn.

---

## 📮 Hướng dẫn nộp bài

> ⚠️ Bản nháp — quy trình này viết trực tiếp ở đây để dùng ngay cho buổi 3. Khi quy ước nộp bài chung của khóa (`00-khai-giang`) được hoàn thiện, phần này sẽ được đồng bộ lại/rút gọn thành link tới đó.

1. Đảm bảo repo GitHub cá nhân của bạn ở chế độ **Public**.
2. Copy link repo.
3. Điền vào form nộp bài: **[Form Nộp Bài Buổi 3](https://forms.gle/GbuW4NH58s4PnCbD8)**.
4. Sau khi nộp, GV sẽ chấm và phản hồi theo tiêu chí ở `lab.md` (áp dụng tương đương cho TH1–TH3; TH4 nếu có sẽ được cộng điểm thêm).

---

## Câu hỏi phản tư

1. Rubric mẫu (B2B Sales Junior) có thực sự phù hợp với vai trò bạn chọn không? Nếu không, tiêu chí nào bạn sẽ đổi trước khi dùng thật?
2. Nếu workflow này chạy production cho công ty bạn, lớp hardening nào (fallback/log/edge/HITL) bạn lo nhất?
3. Bạn đã xử lý dữ liệu ứng viên thật (nếu có) như thế nào trước khi đưa vào repo public?
