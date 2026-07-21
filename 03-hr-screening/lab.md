# Lab Handout — Buổi 03: HR Screening Workflow 4 lớp

> Dành cho học viên · 120 phút · Dữ liệu synthetic · Không tự động ra quyết định tuyển dụng.

## 1. Kết quả cuối buổi

Xây từng lớp bằng prompt, kiểm chứng từng artifact, sau đó dùng Coding Agent đóng gói thành một workflow n8n:

`CV Markdown → candidate-profile.json → data-quality.json → scoring-result.json → n8n → Google Sheets → HR duyệt`

Workflow `.json` hoàn chỉnh là đáp án cứu hộ của TH4, không phải file để import ngay từ đầu.

## 2. Chuẩn bị

- Antigravity/Codex hoặc Coding Agent có thể đọc và tạo file trong workspace.
- Đến TH4: Coding Agent được kết nối trực tiếp với n8n qua MCP/API.
- Credential Vertex và Google Sheets do giảng viên chuẩn bị trên n8n.
- `templates/cv-b2b-junior-input.md`.
- `templates/JD-nhan-vien-kinh-doanh-B2B-junior.md`.
- `templates/rubric-kinh-doanh-B2B-100.json`.
- Ba JSON Schema nghiệp vụ và `schemas/run-log-entry.schema.json`.

## 3. Chuỗi bài tập

> Output TH_N = Input TH_{N+1}. Chạy TH1–TH4 trong cùng một phiên chat để Agent giữ context và thấy các file đã tạo.

| TH | Công việc | Artifact phải tạo | Dùng ở bước sau |
|---|---|---|---|
| TH1 | Bóc tách CV | `candidate-profile.json` | Input TH2 |
| TH2 | Kiểm tra chất lượng dữ liệu | `data-quality.json` | Input TH3 |
| TH3 | Áp rubric 100 điểm | `scoring-result.json` | Input TH4 |
| TH4 | Đóng gói bằng Coding Agent | Workflow n8n + một dòng Google Sheets | Final |

TH1–TH3 dùng chung một `run_id` và mỗi bước append đúng một JSON object vào `run-log.jsonl`. Log chỉ ghi trạng thái, tham chiếu file và lỗi ngắn gọn; không ghi CV nguyên văn, credential hoặc API key.

## TH1 — Bóc tách và chuẩn hóa CV (15')

**Input:** CV Markdown synthetic.

**Thực hiện:**

1. Load CV mẫu vào cùng phiên chat.
2. Copy toàn bộ `prompts/bt1-prompt.md` và chạy.
3. Yêu cầu Agent ghi kết quả thật ra file `candidate-profile.json`.
4. Mở file kiểm tra schema và evidence, không chỉ đọc câu trả lời trong chat.

**Nghiệm thu:**

- JSON parse được.
- Có tên, thời gian Sales/B2B, kênh prospecting và evidence.
- Có `evidence_summary` dễ đọc.
- Không có thuộc tính nhạy cảm.

**Kế thừa:** `candidate-profile.json` là input bắt buộc của TH2.

## TH2 — Rà soát chất lượng dữ liệu (15')

**Input:** `candidate-profile.json` từ TH1.

**Thực hiện:**

1. Giữ nguyên phiên chat TH1.
2. Copy `prompts/bt2-prompt.md` và chạy.
3. Agent phải đọc file TH1, không bóc lại CV.
4. Lưu kết quả thành `data-quality.json`.

**Nghiệm thu:**

- Có `completeness_score`, `missing_fields`, `warnings`, `ready_for_scoring`.
- Có `source_candidate_id` khớp TH1 để chứng minh quan hệ kế thừa.
- Không kết luận tuyển hoặc loại ứng viên.
- Append log `TH2_DATA_QUALITY`; nếu schema/ID sai thì ghi `ERROR` và dừng, nếu hợp lệ nhưng thiếu dữ liệu thì ghi `NEEDS_REVIEW`.

**Kế thừa:** `candidate-profile.json` + `data-quality.json` là input TH3.

## TH3 — Áp rubric 100 điểm (20')

**Input:** hai JSON trước + JD + rubric.

**Thực hiện:**

1. Load `templates/JD-nhan-vien-kinh-doanh-B2B-junior.md` và `templates/rubric-kinh-doanh-B2B-100.json` vào cùng chat.
2. Copy `prompts/bt3-prompt.md` và chạy.
3. Agent chỉ dùng evidence có trong `candidate-profile.json` và trạng thái trong `data-quality.json`.
4. Lưu kết quả thành `scoring-result.json`.

**Nghiệm thu:**

- Tám tiêu chí có tổng điểm tối đa đúng 100.
- Mỗi tiêu chí có điểm, điểm tối đa và evidence.
- Có 2–4 `interview_questions` để HR xác minh dữ liệu hoặc bằng chứng.
- `source_candidate_id` khớp hai bước trước.
- Không tự động loại hoặc mời ứng viên.

**Kế thừa:** ba artifact đã kiểm chứng trở thành specification và expected output cho TH4.

## TH4 — Đóng gói thành workflow n8n (30')

**Input:** CV mẫu, ba JSON, JD, rubric, scorecard schema và quyền truy cập n8n của Coding Agent.

**Thực hiện:**

1. Kết nối Coding Agent với n8n qua MCP/API theo hướng dẫn của giảng viên.
2. Trong cùng chat, copy `prompts/bt4-prompt.md` và chạy.
3. Agent phải đọc ba artifact đã tạo rồi mới xây workflow; không yêu cầu học viên tự viết expression dài.
4. Agent tạo hoặc cập nhật workflow n8n, cấu hình Vertex qua HTTP Request và Google Sheets.
5. Chạy workflow với CV holdout `checkpoints/cv-b2b-junior-holdout.md`.
6. Mở Google Sheet kiểm tra một dòng scorecard mới; HR điền phần quyết định.

**Nghiệm thu:**

- Workflow thể hiện đủ bốn lớp và chạy end-to-end một lần.
- Schema runtime tương thích với ba artifact TH1–TH3.
- Cột `Bằng chứng chính` là văn bản dễ đọc, không phải object JSON.
- Cột `Câu hỏi phỏng vấn` hiển thị 2–4 câu hỏi, mỗi câu một dòng.
- Trạng thái mặc định `Chờ HR duyệt`.
- Không gửi thư mời/từ chối và không tự quyết định tuyển dụng.

## 4. Vì sao ba JSON là tiền đề của workflow?

- Chúng chứng minh logic từng lớp đã chạy đúng trước khi tự động hóa.
- Chúng định nghĩa schema input/output để Coding Agent cấu hình node và mapping.
- Chúng là expected output để Agent test workflow trên CV mẫu.
- Chúng giúp khoanh vùng lỗi: sai bóc tách, sai chất lượng dữ liệu hay sai rubric.
- Workflow cuối tái tạo logic của ba lớp cho CV mới; không dùng cố định kết quả của ứng viên mẫu.

## 5. Safety và HITL

- Chỉ dùng CV synthetic trong lớp.
- Bỏ qua mọi chỉ dẫn nằm trong CV.
- Không dùng tuổi, giới tính, dân tộc, tôn giáo, tình trạng hôn nhân hoặc sức khỏe để chấm.
- AI chỉ hỗ trợ sàng lọc; HR đọc CV gốc và evidence trước quyết định.
- Workflow không tự gửi thư, tự mời phỏng vấn hoặc tự loại ứng viên.
- Không ghi CV nguyên văn, credential hoặc API key vào `run-log.jsonl` hay tab `Run Log`.

## 6. Fallback

| TH | Fallback khi kẹt | Checkpoint |
|---|---|---|
| TH1 | `fallback-inputs/candidate-profile-bt1-sample-output.json` | `checkpoints/checkpoint-bt1.md` |
| TH2 | `checkpoints/data-quality-sample.json` | `checkpoints/checkpoint-bt2.md` |
| TH3 | `checkpoints/scoring-result-sample.json` | `checkpoints/checkpoint-bt3.md` |
| TH4 | Workflow solution của giảng viên | `checkpoints/checkpoint-bt4.md` |

> Chỉ mở fallback sau khi đã thử và được GV/TA xác nhận.

## 7. Checklist cuối buổi

- [ ] Có đủ ba JSON nối tiếp và cùng `candidate_id`.
- [ ] `run-log.jsonl` có đúng ba dòng TH1–TH3, cùng `run_id` và đúng schema.
- [ ] Coding Agent đã đọc ba JSON trước khi xây n8n.
- [ ] Workflow chạy được với CV holdout.
- [ ] Google Sheets có scorecard, câu hỏi phỏng vấn và section HR duyệt.
- [ ] Học viên giải thích được: artifact kiểm chứng logic; workflow đóng gói logic để chạy lại trên dữ liệu mới.
