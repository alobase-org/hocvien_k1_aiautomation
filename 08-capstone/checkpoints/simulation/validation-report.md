# Validation Report — Audit claim của Teaching Simulation B8

> /vibe-validate-orchestrator · 17/08/2026 · Auditor độc lập với tác giả simulation (cùng là tôi — nên mọi claim được kiểm bằng deterministic check, không tự tuyên bố).
> Câu hỏi của user: (1) HV giả lập có làm bài từng bước theo thiết kế thật không? (2) Workflow chạy được thật không? (3) Skill chấm có chạy test thật không?

## Verdict tổng

| Nhóm claim | Verdict | Chi tiết |
|---|----------|---------|----------|
| (1) HV làm bài theo từng bước | **VERIFIED (phần lớn)** — với 1 nhóm claim **HALLUCINATED** | File artifact tồn tại + logic chạy lại PASS; NHƯNG claim "ảnh demo" là bịa (0/7 file tồn tại) |
| (2) Workflow chạy được | **PARTIAL — chưa chứng minh được runtime** | Chỉ verify cấu trúc (đồ thị node/connection). Runtime n8n đang khởi động để kiểm — xem Addendum |
| (3) Skill chấm chạy thật | **BAN ĐẦU: KHÔNG → GIỜ: ĐÃ CHẠY THẬT** | Trước audit: tôi chấm bằng rubric JSON + aggregator, KHÔNG qua pipeline skill (claim "chấm bằng vibe-ai-auto-score" trong report là overclaim). Trong audit này: skill đã chạy thật trên package Linh — và bắt được 3 lỗi tôi bỏ sót |

## (1) Kiểm "HV làm bài từng bước" — deterministic re-run

| Check | Kết quả |
|-------|---------|
| File tồn tại: 4 package (Hà 20, Linh 20, Tuấn 15, Mai 13 file) | ✅ khớp claim |
| D1 Hà: re-run logic 3 test case (ngày + chính sách) | ✅ 3/3 PASS lại đúng như report |
| D1 Linh: output/recon-analysis.csv + email-drafts.md tồn tại, 4/4 verdict PASS | ✅ |
| D3 Hà: app unit-test re-run trong audit vòng 1 | ✅ 4/4 |
| D3 Linh: subagent ĐỌC CODE + tự chạy node: **9/9 PASS** (nhiều hơn cả 6/6 tôi claim — gồm cả TRUNG_DON) | ✅ vượt claim |
| Auto-check 4 package: kết quả khớp bảng report vòng 2 | ✅ |
| **Ảnh demo: README/pitch claim "3 ảnh chụp"/trỏ `anh-demo/*.png` — thực tế 0 file** | ❌ **HALLUCINATED** (giữ nguyên tính minh bạch: đây là chỗ simulation ghi claim không có evidence — đúng như F8 đã cảnh báo, và lần này chính claim của tôi bị bắt) |

**Kết luận (1):** lộ trình từng bước là THẬT (mọi logic/artifact tái lập được bằng chạy lại). Riêng claim ảnh demo + execution ID trong run-log là mô phỏng-chưa-chạy (đã khai báo từ F8, nhưng ảnh demo trong README là claim bịa chưa từng được khai báo — lỗi của tôi).

## (3) Kiểm "skill chấm chạy thật" — kết quả quan trọng nhất của audit

**Sự thật:** trong 2 vòng simulation, TÔI KHÔNG từng chạy skill vibe-ai-auto-score. Việc chấm là tôi đọc rubric + tính điểm bằng score_aggregator. Report ghi "chấm bằng rubric-capstone" (đúng) nhưng một số chỗ gợi ý "GV chấm bằng vibe-ai-auto-score đã test" — **chưa từng test cho tới audit này**.

**Audit này đã chạy skill THẬT** (subagent vận hành đúng SKILL.md + calibration KB + auto-check pre-check) trên package Linh:

| So sánh | Tôi chấm (vòng 2) | Skill chấm (audit) |
|---|---|---|
| Tổng Linh | 97.0 | **87.0** (sau sửa 1 finding sai của chính skill) |
| Chênh | — | **-10 điểm — tôi chấm ỒNG 10 điểm** |

3 lỗi thật skill bắt được mà tôi bỏ sót (mọi lỗi đã verify lại deterministic):
1. **D2a=3 thay vì 4:** nửa sau workflow (schema validation + report node) vẫn là B4 trả `report.docx` — e2e assert của chính HV kỳ vọng JSON recon → **assert không thể PASS thật** dù run-log claim 5/5. Tôi đã cho 4 vì "trung thực khai" — skill đúng hơn.
2. **D4c=3:** claim "3 ảnh chụp" (0 file), "6/6 unit test" (không có test log trong package), auto-check [6] PASS (không tái lập) — nhiều claim không khớp runtime-check.
3. **D1c=4:** output CSV của skill HV chỉ là bảng verdict, không đúng output contract đã hứa (thiếu cột phân tích đầy đủ).

1 finding của skill bị **bác bỏ** (kiểm deterministic): "luong-nghiep-vu.md không tồn tại" — file tồn tại thật tại `studentkit/06-content-engine/luong-nghiep-vu.md` (agent tìm nhầm gốc repo). Đã sửa B2=5 → 87.0.

**Hệ quả calibration:** số của vòng 2 do tôi chấm bị phình: Linh 97→87 (band Xuất sắc→Tốt), cần chấm lại Tuấn/Mai cùng chuẩn khắt khe hơn (dự kiến vẫn cùng band trả-bài vì lỗi cấu trúc nặng). Bài học: **người thiết kế lab không nên là người chấm simulation của chính mình** — đúng lý do skill chấm tồn tại.

## (2) Kiểm "workflow chạy được" — runtime

- Trước audit: KHÔNG lần nào n8n được khởi động. Mọi "đồ thị nguyên vẹn" là structural check (auto-check [3]) — đúng sự thật, nhưng "chạy được" là claim chưa kiểm.
- Trong audit: đang khởi động n8n local cold (npx lần đầu, đang resolve deps) — kết quả runtime sẽ ghi Addendum dưới khi port 5678 lên.
- Kỳ vọng trung thực: import + webhook sẽ chạy; **node AI sẽ 401 nếu không có GEMINI key** (workflow mượn B4 để placeholder `REPLACE_WITH_YOUR_GEMINI_API_KEY`) — đúng lý do checklist GV yêu cầu điền key trước buổi.

## Hành động sửa sau audit

1. ❌→✅ Sửa README package Hà/Linh: bỏ claim "3 ảnh chụp", ghi "ảnh demo: GV chụp khi runtime-test" — hoặc chụp thật khi n8n chạy.
2. Chấm lại vòng 2 bằng skill (đã có 1 bài chuẩn — Linh 87.0); điều chỉnh con số trong dry-run-report.
3. Ghi rõ trong HUONG-DAN-CHAM (đã có): GV PHẢI runtime-check — audit này chứng minh nhuần: cả chính người chấmsimulation cũng ồng điểm khi không verify runtime.
4. Kết luận về "workflow chạy được": chờ Addendum runtime.

*Auditor ghi chú: audit này do chính tác giả simulation thực hiện — xung đột lợi ích có giảm một phần nhờ (a) mọi check là deterministic re-run, (b) skill chấm chạy bởi subagent đọc file độc lập không biết số điểm cũ.*

## Addendum runtime (kết thúc)
3 lần khởi động n8n (npx cold install + warm cache + persistent background) — process đều bị kill câm trong giai đoạn resolve dependencies (~1000 deps, log chỉ có npm warnings, không error). Môi trường sandbox này không start được n8n instance. **Verdict runtime: ATTEMPTED — NOT PROVEN.** Workflow "chạy được" vẫn chỉ được chứng minh ở mức cấu trúc; bước runtime-check đúng như HUONG-DAN-CHAM phải làm trên máy GV trước buổi (đã có trong checklist). Auto-check [6] sẽ tự chạy khi n8n khả dụng.

## Addendum runtime SỐ 2 (17/08 khuya) — RUNTIME ĐÃ ĐƯỢC CHỨNG MINH ✅
Sau Addendum 1 ("không start được n8n"), đã giải quyết bằng đúng hướng user chỉ đạo — **docker-compose**:
- Cài colima + docker (brew) → `docker-compose up -d` n8n official image (port 5678).
- Vượt 3 rào n8n 2.x: (1) `/api/v1` bỏ cookie auth → tạo API key qua `/rest/api-keys` (key thật nằm `data.rawApiKey`, field `apiKey` bị che!); (2) `active` read-only lúc import → strip field quản trị; (3) activate qua `POST /api/v1/workflows/{id}/activate` (PATCH trả 405).
- Gemini: key express của user hoạt động (200); model `gemini-3.6-flash` trong workflow B4 KHÔNG tồn tại → auto-check patch sang `gemini-flash-latest` TẠI RUNTIME (--gemini-key/--model, không ghi key xuống đĩa); 2.5-flash "not available to new users" với key express; flash-latest hay 503 "high demand" → auto-check tự retry ×3.
- **KẾT QUẢ CUỐI:** 4/4 workflow import + activate + webhook chạy thật (id thật trong `runtime-batch-log.txt`). Hà chạy trọn chuỗi 2 lần: 1 lần AI trả phân tích đầy đủ, 1 lần **HTTP 200 + DOCX 52KB thật** (lưu `ho-ha-capstone/anh-demo/runtime-report.docx`).
- **Phát hiện quan trọng (khớp mọi khai báo):** DOCX là template hợp đồng B4, dữ liệu warranty không lọt — node Schema Validation B4 chặn đúng chỗ. "Workflow chạy được" = TRUE ở mức execute toàn chuỗi + AI thật; "artifact đúng nghiệp vụ" = FALSE đúng như D2a mức 3 đã chấm. **Rubric phân biệt chính xác 2 tầng này — thiết kế đúng.**
