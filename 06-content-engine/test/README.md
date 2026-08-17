# Hướng dẫn chạy live E2E test cho buổi 6 (Content Engine) — dành cho AI agent

Tài liệu này viết cho một agent (Claude Code hoặc tương đương) mới nhận việc, chưa có context về
phiên làm việc trước. Đọc hết trước khi chạy bất kỳ lệnh nào.

## 0. Việc này là gì

Thư mục `test/` chứa bộ kiểm thử **live E2E** cho workflow n8n buổi 6 — gọi thẳng webhook n8n **THẬT**,
không mock. Có 2 công cụ, cùng đọc chung `../checkpoints/test-cases.json`:

| File | Dùng khi |
|---|---|
| `interactive_b6_runner.py` | Chạy nhanh qua CLI, có exit code để CI/script khác kiểm tra pass/fail |
| `06_content_engine_lab_demo.ipynb` | Trình chiếu từng bước có diễn giải (GV lên lớp), cần Jupyter kernel |

Cả hai gọi 3 webhook: `/b6/angles` (sinh ý tưởng), `/b6/generate` (viết bài + ảnh), `/b6/approve` (duyệt).

## 1. Điều kiện cần trước khi chạy

**Bắt buộc — 1 instance n8n đang chạy thật, đã import/dựng workflow buổi 6 và Activate.**
Không có docker-compose tự-launch n8n cục bộ như buổi 4/5 (lý do: workflow này gọi LLM Gemini thật +
sinh ảnh thật qua GeminiGen.ai trả phí + ghi Google Sheets qua OAuth thật — không tự động hoá được
credential trong container dùng-rồi-bỏ).

Lấy workflow từ `../checkpoints/n8n-content-engine-solution.json` (đã gỡ credential thật, thay bằng
`REPLACE_CREDENTIAL_ID`) — import vào n8n, gắn lại 3 credential thật (Google Gemini AI Studio,
GeminiGen.ai `httpHeaderAuth`, Google Sheets OAuth), Activate, rồi copy 3 URL production của 3 webhook
node (`Webhook: Sinh nội dung`, `Webhook: Sinh ý tưởng`, `Webhook: Duyệt`).

Nếu người giao việc đã có sẵn 1 instance đang chạy (thường là trường hợp thật), chỉ cần hỏi lấy 3 URL,
không cần tự dựng lại từ đầu.

## 2. Chạy qua CLI (cách nhanh nhất, khuyên dùng để tự kiểm)

```bash
# Bash / Git Bash (Windows) hoặc macOS/Linux
cd giao_trinh/giang-day/05-thuc-hanh/06-content-engine/test
PYTHONUTF8=1 PYTHONIOENCODING=utf-8 \
B6_WEBHOOK_ANGLES="https://<n8n-cua-ban>/webhook/b6/angles" \
B6_WEBHOOK_GENERATE="https://<n8n-cua-ban>/webhook/b6/generate" \
B6_WEBHOOK_APPROVE="https://<n8n-cua-ban>/webhook/b6/approve" \
python interactive_b6_runner.py
```

PowerShell (Windows) tương đương:
```powershell
$env:PYTHONUTF8=1; $env:PYTHONIOENCODING="utf-8"
$env:B6_WEBHOOK_ANGLES="https://<n8n-cua-ban>/webhook/b6/angles"
$env:B6_WEBHOOK_GENERATE="https://<n8n-cua-ban>/webhook/b6/generate"
$env:B6_WEBHOOK_APPROVE="https://<n8n-cua-ban>/webhook/b6/approve"
python interactive_b6_runner.py
```

- **Không cần cài gì thêm** — chỉ dùng thư viện chuẩn Python (`urllib`, `json`, `argparse`). Python 3.8+ là đủ.
- Exit code `0` = tất cả case đạt. Exit code `1` = có case fail, đọc dòng `CHƯA ĐẠT (...)` cuối output.
- Mặc định **KHÔNG** chạy TC05 (đường đầy đủ Lớp 2→3→4, tốn phí sinh ảnh thật + ~2 phút). Thêm `--full`
  vào cuối lệnh nếu cần chạy cả case đó — chỉ làm khi người giao việc yêu cầu rõ, vì tốn tiền thật.

## 3. Chạy qua Notebook (cần cài thêm)

Chỉ cần khi người giao việc muốn **xem trực quan từng bước** (không cần cho việc kiểm tra tự động).

1. Cài extension **Jupyter** (nhà xuất bản `ms-toolsai`) trong VSCode/Antigravity/Cursor — các extension
   khác trong marketplace (Jupytext Sync, JupyterHub, Jupyter Export, Vscodium Jupyter, DataFrame Viewer,
   Cloud Studio Jupyter Server Provider) đều **không cần** cho việc này.
2. Cài gói Python: `pip install ipykernel` (môi trường mặc định thường CHƯA có `IPython`/`ipykernel` —
   nếu bỏ qua bước này, mở notebook sẽ báo `ModuleNotFoundError: No module named 'IPython'` ở cell cuối).
3. Mở `06_content_engine_lab_demo.ipynb`, chọn kernel Python 3 ở góc phải trên.
4. Sửa Step 0 (cell thứ 3 trong notebook) — bỏ comment 3 dòng `os.environ['B6_WEBHOOK_...']` và điền URL
   thật của bạn. **Notebook không có URL mặc định nào** — thiếu dòng nào, cell này sẽ raise lỗi rõ ràng
   ngay tại đó, không âm thầm gọi nhầm vào instance của người khác.
5. Run All. Cell Step 4 (đường đầy đủ) mặc định `CHAY_FULL = False` — im lặng bỏ qua, không tốn phí.

## 4. Tác dụng phụ cần biết trước khi chạy

Mọi lần chạy (CLI hay notebook) đều ghi **dòng thật** vào Google Sheets `Content_Queue`/`Publish_Log`
của instance đang test (qua 3 case loại `approve` trong `test-cases.json`, post_id tiền tố `AUTOTEST-`
hoặc `NOTEBOOK-DEMO-`) — dễ nhận ra và xoá tay sau nếu cần, không tự dọn.

Case `generate`/`generate_full` gọi LLM thật — luôn tốn 1 lượt gọi Gemini, dù rẻ. Chỉ `generate_full`
(TC05, cần `--full`) mới tốn thêm phí sinh ảnh GeminiGen.ai (~vài chục nghìn VNĐ/lần) + ~2 phút chờ.

## 5. Nếu case fail

Đọc trực tiếp dòng `✗` in ra — mỗi dòng đã tự giải thích kỳ vọng vs thực tế. Nếu nghi là bug thật trong
workflow (không phải lỗi test), xem `../checkpoints/checkpoint-bt4.md` gotcha #15 để biết ví dụ thật đã
từng xảy ra (case thiếu `angle` từng làm LLM tự bịa `angle_id` thay vì báo lỗi — đã sửa bằng node IF
`Có angle hợp lệ?` trong workflow, không sửa bằng cách nới lỏng test).

Nếu nghi ngờ chính `n8n-content-engine-solution.json` không khớp workflow đang chạy live (ai đó đã sửa
qua n8n UI mà chưa đồng bộ lại), đọc `checkpoint-bt4.md` gotcha #13 — n8n KHÔNG merge khi 2 nơi sửa cùng
lúc, ai save sau đè hoàn toàn bản trước, không cảnh báo.

## 6. Việc KHÔNG nên làm

- Đừng nới lỏng `ky_vong` trong `test-cases.json` chỉ để case pass — nếu thấy `ky_vong` sai, sửa nó,
  nhưng phải nêu rõ vì sao trong commit/báo cáo, không âm thầm sửa cho xanh.
- Đừng thêm docker-compose n8n cục bộ để "giống buổi 4/5 hơn" — đã cân nhắc và quyết định không làm vì
  lý do credential thật ở mục 1. Nếu người giao việc yêu cầu khác, hỏi lại trước khi tự làm.
- Đừng sửa workflow qua n8n UI trong lúc agent khác (hoặc phiên trước) đang sửa qua API — xem gotcha #13.
