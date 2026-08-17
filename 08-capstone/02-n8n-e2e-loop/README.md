# Lab 02 — Deliverable D2: Workflow n8n theo vòng e2e-test-first

## Mục tiêu
Xây workflow n8n chạy trên use case của bạn bằng **vòng lặp test-first**: viết e2e test TRƯỚC, rồi sửa workflow tới khi test PASS. Mỗi vòng ghi run-log. Đây là mindset implementation: nghiệm thu đi trước sản phẩm.

## File input cần cung cấp
- `input/INPUT-CHECKLIST.md` — chuẩn bị trước khi chạy
- `input/e2e-test.template.md` — khung viết test
- `input/run-log.template.md` — khung ghi vòng lặp
- `usecase-brief.md` (lab 00) + 2–3 input mẫu của use case

## Prompt để chạy

| Prompt | Input | Output |
|--------|-------|--------|
| `prompt/05-write-e2e-test.prompt.md` | brief + input mẫu | `e2e-test.md` (định nghĩa PASS/FAIL) |
| `prompt/06-adapt-workflow.prompt.md` | e2e-test + workflow mượn | `workflow-plan.md` (bản đồ node cần sửa) |
| `prompt/07-run-loop.prompt.md` | workflow-plan + e2e-test | `run-log.md` ≥2 vòng (≥1 FAIL) |

## Các bước
1. Viết e2e test trước (prompt 05): input mẫu → gọi workflow → assert output. Test phải FAIL khi workflow chưa sửa gì (vì còn là workflow buổi cũ).
2. Nhập workflow mượn vào n8n (mở n8n local → Import File), chạy prompt 06 để có bản đồ sửa: node nào giữ, node nào sửa, node nào thêm cho use case bạn.
3. Sửa workflow theo bản đồ. Chạy test. Ghi run-log vòng 1 (kỳ vọng FAIL hoặc partial).
   - **Cảnh báo (từ simulation):** ĐỪNG đổi tên node trực tiếp trong UI n8n rồi save — connection vẫn trỏ tên cũ, workflow chết câm không báo lỗi. Nếu vẫn muốn đổi tên: đổi xong chạy ngay `capstone_auto_check.py` (lab 05) check [3] để bắt connection đứt, rồi nối lại từng connection.
   - **Cảnh báo 2 (F16):** khung B4 có 2 node tiền xử lý ("Extract .docx", "Redaction") là **logic đặc thù hợp đồng** — khi mượn khung cho use case khác, BỎ chúng khỏi luồng (Webhook nối thẳng node AI). Giữ lại sẽ mất dữ liệu input.
   - **Ghi chú (F17):** webhook n8n bọc body trong `$json.body` — trong expression node AI dùng `$json.body.data` (không phải `$json.data`). Kiểm tra nhanh bằng cách tạo workflow debug: Webhook → Respond `{{ JSON.stringify($json) }}`.
4. Sửa tiếp, chạy lại. Lặp tối đa 5 vòng. Ghi mọi vòng vào run-log.

## Cách chạy test (không cần code nếu chưa sẵn)
- Đơn giản nhất: manual e2e — trigger workflow với input mẫu, soi output sinh ra, đối chiếu assert trong `e2e-test.md`, ghi PASS/FAIL.
- Nâng cao (khuyến khích): mở `04-contract-review/test/` xem `interactive_e2e_runner.py` + notebook — gọi n8n qua REST API (`http://localhost:5678/api/v1/`), trigger execution và đọc artifact tự động. Có thể mượn nguyên cấu trúc script này, sửa cho use case của bạn.

## Tự chạy E2E + debug từ terminal (không cần chờ GV)
Sau mỗi vòng sửa workflow, chạy 1 lệnh để biết workflow có chạy thật không — ngay tại máy bạn:
```bash
# 1 lần duy nhất: khởi n8n (nếu chưa có) — cần Docker Desktop (hoặc colima) đang mở:
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n

# Lần đầu vào http://localhost:5678 tạo tài khoản, rồi Settings > n8n API > Create API key (lưu lại)

# 2. Chạy auto-check (thay KEY_N8N và KEY_GEMINI bằng key của bạn):
python3 05-self-check/tool/capstone_auto_check.py <thư-mục-đồ-án-của-bạn> \
  --n8n-api-key KEY_N8N --gemini-key KEY_GEMINI --model gemini-flash-latest \
  --input "1 tin nhập mẫu của bạn"
```
Script tự: import workflow vào n8n → activate → gửi input qua webhook → in response → dọn workflow test. Key chỉ điền tại runtime, không ghi vào file.

**Đọc kết quả:**
| Output | Nghĩa là gì | Làm gì tiếp |
|---|---|---|
| `[FAIL] đồ thị nguyên vẹn` | Connection đứt (thường do đổi tên node) | Nối lại connection, chạy lại |
| `200 — response OK` | Workflow chạy trọn chuỗi | Soi response có đúng nghiệp vụ không |
| `200 NHƯNG response chứa error` + "503/high demand" | Model AI quá tải — bình thường | Chạy lại sau 1 phút (script đã tự retry) |
| `200 NHƯNG response chứa error` + "API Key/Quota" | Key sai hoặc hết hạn ngạch | Kiểm tra key Gemini |
| Response là DOCX/template "hợp đồng" | Node sau AI (schema/report) còn của B4 | Đó là phần "chưa chuyển" — vòng loop tiếp theo của bạn (xem run-log khai báo) |
| HTTP 404 webhook | Workflow chưa activate | Activate trong UI rồi chạy lại |

Mỗi lần chạy xong: ghi 1 dòng vào run-log (kết quả + lỗi + sửa gì) — đó chính là vòng e2e của bạn.

## Nghiệm thu (đếm được)
- [ ] Workflow import được vào n8n, chạy không lỗi node đỏ
- [ ] Chạy trên input mẫu **của use case bạn** → sinh artifact output đúng tên file trong test
- [ ] `e2e-test.md` có ≥3 assert, mỗi assert PASS/FAIL rõ
- [ ] `run-log.md` có ≥2 vòng, trong đó **≥1 vòng FAIL** (chứng minh đã loop thật, không copy nguyên)
- [ ] Có node ghi log/hoặc file run-log ghi rõ phần nào chưa runtime-test

## Tài nguyên mượn (mở thật ra xem trước)
- `04-contract-review/checkpoints/n8n-contract-review-solution.json` — workflow n8n hoàn chỉnh: mượn khung trigger → xử lý → validate → output
- `04-contract-review/test/interactive_e2e_runner.py` + `04_contract_review_lab_demo.ipynb` — pattern e2e qua n8n REST API (login → inspect node → trigger → verify artifact)
- `04-contract-review/templates/clause.schema.json` — mẫu schema validation output
- `03-hr-screening/` (lab_tulam.md + schemas/) — workflow chấm điểm thứ 2 để tham khảo cấu trúc scoring
- `05-cskh-bot/` — nếu use case bạn cần webhook nhận tin nhắn
