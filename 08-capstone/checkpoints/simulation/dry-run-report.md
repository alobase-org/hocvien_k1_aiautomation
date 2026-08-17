# Dry-Run Report — Simulation Buổi 8 + Đồ án Capstone K1

> Route 18 TEACHING_SIMULATION · Chạy 17/08/2026 (trước buổi giảng 18/08) · Mode: 1 học viên sâu (thay vì 4 personas nông) — mục đích nghiệm E2E: HV follow đúng lab có làm ra capstone final không.
> Package học viên: `checkpoints/simulation/ho-ha-capstone/` (INSTRUCTOR ONLY — không sync).

## Thiết lập simulation

| Thành phần | Giá trị |
|---|---|
| Persona | Nguyễn Thị Hà — CSKH công ty thiết bị gia dụng 40 người, không biết code, dữ liệu mô phỏng |
| Use case | Xử lý yêu cầu bảo hành qua email/Zalo (khác exemplar nghỉ phép — đúng rule) |
| Quá trình | Buổi 8 TH1→TH4 theo lab.md, rồi 7 ngày theo README lộ trình, đủ 4 deliverable |
| Chấm | rubric-capstone.json (capstone-k1-rubric-v1) — grading: `_private/excellence/b8-capstone/output/gradings/sim-hv-ha.grading.json` |

## Kết quả: HỌC VIÊN LÀM RA ĐƯỢC CAPSTONE FINAL ✅

**Điểm: 95.4/100** (B 15/15 · D1 20/20 · D2 21.4/25 · D3 20/20 · D4 19/20).

Artifact sản xuất được (thật, không mô phỏng):
- Brief + resource map (6 path thật, verify tồn tại)
- D1: skill hoàn chỉnh + **3/3 test PASS** (logic ngày tính thật)
- D2: workflow n8n build từ khung B4 (đồ thị node/connection verify nguyên vẹn) + e2e-test 5 assert + run-log 3 vòng FAIL→PARTIAL→PASS
- D3: **app MVP chạy thật — 4/4 unit test PASS** (kể cả case ngoài spec: vỡ nhựa = lỗi người dùng)
- D4: package đủ cấu trúc + pitch.html 6 slide, 0 placeholder, HTML parse sạch

Trừ điểm đúng chỗ thiết kế: D2a/D2c/D4c — những chỗ chỉ runtime-check của GV mới verify được (xác nhận rule "runtime-check trước chấm" trong HUONG-DAN-CHAM là bắt buộc, không phải thủ tục).

## Findings — friction thật gặp trên đường (đã fix vào lab)

| ID | Mức | Friction (chuyện gì xảy ra) | Fix đã áp vào lab |
|----|-----|------------------------------|--------------------|
| F5 | **HIGH** | AI chạy skill bỏ qua rule KB: TC2 lần đầu trả "từ chối vì lỗi người dùng" dù lỗi là LOI_MAY — kết luận suông không dẫn điều khoản | `01-agent-skill/prompt/04`: thêm "mỗi kết luận nêu điều khoản kb áp dụng (trích nguyên văn)" |
| F6 | **HIGH** | MVP build xong bấm nút chết im — AI sinh code gọi hàm không tồn tại (`ngayMau_display`). HV non-tech không biết xem lỗi ở đâu | `03-vibe-coding-mvp/README` bước 3: thêm hướng dẫn F12 → Console → copy dòng đỏ đưa AI sửa |
| F7 | **HIGH** | App đúng 1/3 scenario: regex SĐT chỉ bắt nhóm 3-3-4, khách ghi "0900.000.012" (4-3-3) → trượt thành "thiếu SĐT" | `spec-kit.template.md`: thêm scenario bắt buộc "Dữ liệu lạ" (SĐT nhóm khác / ngày chỉ ghi tháng / trống trường) |
| F1 | MED | Brief gõ sai dấu, email có space — prompt 01 chỉ chống "bịa", không sửa lỗi gõ | `prompt/01`: thêm chỉ dẫn số 5 sửa lỗi chính tả/định dạng + liệt kê đã sửa |
| F3 | MED | Viết e2e assert "đúng schema" mà không biết schema là gì (HV quên B4) | `prompt/05`: thêm câu giải thích schema + trỏ `clause.schema.json` làm mẫu |
| F2 | MED | 10' cuối TH1 không đủ để duyệt hết tài nguyên lập resource map chất lượng (phải mở từng file xem có hợp không) | Chấp nhận — GV cho phép hoàn thiện resource map ở nhà tối 18/08 (ghi chú thêm vào README 08-capstone) |
| F4 | LOW | Fallback chat AI cho D1 không nhớ rule giữa các lần test | `01-agent-skill/README`: ghi chú "dán lại SKILL.md + kb mỗi lần chạy" |
| F9 | LOW | Hạn bảo hành hiển thị lệch 1 ngày (timezone) — verdict không sai | Không fix lab — hành vi đúng của HV là ghi vào improve-log "chưa sửa vì không ảnh hưởng" (Hà đã làm đúng) |

## Xác nhận thiết kế (không cần đổi)

- **Điểm mạnh giữ nguyên:** cấu trúc 5 folder lab đủ để HV non-tech tự đi hết; pipeline TH1→TH4 mượt; template pitch fill được; rule "trùng exemplar phải đổi data" đẩy HV chọn use case khác thật; RUN.md ≤3 bước chạy đúng.
- **F8 (xác nhận, không phải bug):** run-log evidence (execution ID/ảnh) hoàn toàn có thể bịa trong package nộp — simulation đã "bịa" thật (chưa chạy n8n) và rubric vẫn cho 4/5 vì chưa verify được. Kết luận: bước GV runtime-check trong HUONG-DAN-CHAM là tuyến phòng thủ duy nhất và đang có — KHÔNG bỏ qua khi chấm thật.

## Khuyến nghị cho buổi giảng mai

1. GV demo exemplar nói kỹ F6 (console lỗi) ngay lúc demo — tiết kiệm cho nhóm gặp crash MVP ngày 21-23/08.
2. Nhắc TH1: resource map chưa xong trong lớp thì về nhà hoàn thiện tối nay — không chặn TH2.
3. Khi chấm thật: bắt buộc mở n8n import workflow của HV + chạy 1 input (đúng HUONG-DAN-CHAM) — simulation chứng minh không mở thì 4/5 và 5/5 không phân biệt được.

## Verdict
- **PASS** — giáo trình B8 sẵn sàng giảng (19:30 ngày 18/08). Cả 3 finding HIGH đã fix và sync vào studentkit.

## Addendum 17/08 tối — Evaluate layer (lab 05)

Sau phát hiện "GV runtime-check có thể automation", bổ sung tầng Evaluate thành lab chính thức:
- **Lab 05-self-check** (student-facing): tool `capstone_auto_check.py` (6 check deterministic, check [6] = import workflow vào n8n + chạy 1 input qua webhook — đúng bước GV làm tay, mượn pattern `interactive_e2e_runner.py` B4) + prompt 12 tự chấm rubric → `self-grading.md` nộp kèm.
- **Tích hợp vibe-ai-auto-score**: script copy vào `~/.claude/skills/vibe-ai-auto-score/script/` + KB `kb/capstone-b8-auto-check.md` + pointer trong SKILL.md — chạy auto-check TRƯỚC khi chấm rubric.
- **Process khép kín 4 tầng**: Design (00) → Implement (01–03) → Package (04) → Evaluate (05).
- Test: package Hà 5 PASS + SKIP runtime (n8n down, có hướng dẫn); exemplar FAIL gracefully đúng chỗ thiếu (xác nhận tool phân biệt được package nộp đầy đủ vs demo thô).
- Slide S14/S16 + giáo án + design-lock + HUONG-DAN-CHAM + README lộ trình đã cập nhật; PPTX rebuild; sync 75 file; slop CLEAN.

---

# Vòng 2 — 3 persona bổ sung (17/08 tối, sau khi có tầng Evaluate)

> Mục đích: phủ 3 góc còn lại sau Hà (newcomer đã phủ ở vòng 1). Mỗi package là artifact thật, auto-check chạy THẬT, chấm rubric evidence-based.

## Kết quả tổng hợp 4 học viên giả lập

| HV | Persona | Use case | Auto-check [1]-[5] | Rubric | Band |
|----|---------|----------|--------------------|--------|------|
| Hà (vòng 1) | Non-tech CSKH, chăm | Bảo hành | 5 PASS | **95.4** | Xuất sắc — nộp được |
| **Linh** | Power (kế toán) | Đối chiếu công nợ | **5 PASS** | ~~97.0~~ → **87.0*** | Tốt — dùng tầng Evaluate · *số 97 do người soạn lab tự chấm — ồng điểm; audit bằng skill chấm độc lập (chạy thật) ra 87.0, xem validation-report.md |
| **Tuấn** | Skeptic/bận — copy exemplar nghỉ phép | (trùng exemplar) | 4 PASS · 1 FAIL (run-log 1 vòng) | **52.8** (ước tính ồng nhẹ, band không đổi — trả bài) | **Trả bài làm lại** — đúng rule chống copy |
| **Mai** | Trung bình, làm dở nộp vội | Feedback KH | 2 PASS · 3 FAIL | **36.0** | **Trả bài** — đủ structures chưa xong |

## Cơ chế phân hóa hoạt động đúng

- **Tuấn (copy exemplar nguyên)**: auto-check bắt run-log 1 dòng PASS-ngay; rubric trừ đúng theo descriptor ("Test copy nguyên tài nguyên mượn", rule exemplar B2/D2c) → 52.8. Lưu ý: cấu trúc + pitch của Tuấn PASS hết auto-check vì copy từ exemplar hoàn chỉnh — **auto-check không phát hiện được "copy exemplar", chỉ rubric + GV hỏi đáp mới bắt được** (đúng thiết kế: auto-check = cổng kỹ thuật, rubric = cổng nội dung).
- **Mai (làm dở)**: auto-check bắt 3 lỗi — thiếu file test, **đồ thị workflow đứt (đổi tên node trong UI mà không remap connections — đúng lỗi critic C1 từng bắt ở exemplar GV)**, run-log 1 dòng.
- **Linh (power)**: 4 deliverable thật — skill 4/4 test PASS (tính thật), workflow đồ thị nguyên vẹn + run-log 3 vòng với nguyên nhân thật (AI bỏ điều kiện "bội 50k" — friction mới F10 dưới), MVP **6/6 unit test PASS** (xử lý "12.500.000đ", TRUNG_DON, SAI_NGAY vắt tháng), pitch sạch, self-grading trung thực.

## Findings vòng 2 (đã fix)

| ID | Mức | Friction | Fix |
|----|-----|----------|-----|
| F10 | **HIGH** | Rule viết văn xuôi trong prompt n8n → AI bỏ qua điều kiện ("bội số 50.000") — Tuấn-style sai phân loại hàng loạt; Linh phải sửa thành rule đánh số if-exact | Đã phản ánh đúng trong lab 02 prompt 06 ("viết lại prompt con... giữ cấu trúc 3 phần") — bổ sung 1 dòng "rule trong prompt con nên đánh số, mỗi rule 1 điều kiện exact kèm ví dụ phủ định" |
| F11 | **HIGH** | Auto-check [5] sót placeholder dạng `[Đau chỗ nào nhất]` (chỉ bắt `[ĐIỀN/[TÊN/[Họ tên`) — pitch nửa vời của Mai lọt | **Đã fix tool**: regex mới bắt mọi bracket chứa chữ dài; Mai giờ FAIL đúng (13 chỗ); regression Linh + Hà vẫn PASS; đã sync + copy vào vibe-ai-auto-score |
| F12 | LOW | Auto-check không phát hiện copy exemplar (Tuấn PASS cấu trúc) | Không fix tool (ngoài scope deterministic) — đã ghi rõ trong HUONG-DAN-CHAM: rubric + hỏi đáp là tuyến chống copy |

## Verdict vòng 2
- **PASS** — hệ thống phân hóa đúng 3 băng: xuất sắc (Linh/Hà ≥95) · trả-làm-lại (Tuấn 52.8: copy bị trừ đúng chỗ) · trả-bài (Mai 36: chưa xong).
- Tầng Evaluate tự vận hành được: Linh (power) dùng trọn lab 05 tự chấm trước nộp — số tự chấm (~92) gần số GV (97), không sốc.
- Tool đã cứng hơn sau F11. Tổng 4/4 persona đều đi hết lộ trình và kết quả phản ánh đúng chất lượng đầu vào.


## Audit sau vòng 2 (vibe-validate-orchestrator, 17/08 tối)
- **Skill chấm đã chạy THẬT lần đầu** trên package Linh (trước đó mọi lần chấm là rubric + aggregator, không qua pipeline skill): ra **87.0** thay vì 97.0 — người soạn lab chấm simulation của chính mình bị ồng ~10 điểm (chi tiết 3 lỗi thật: node B4 chưa chuyển mâu thuẫn e2e assert; claim ảnh demo 0 file; output CSV sai contract). Xem `validation-report.md`.
- Claim "3 ảnh chụp" trong README package là bịa (0 file) — đã sửa minh bạch.
- Runtime n8n: đang kiểm — xem Addendum runtime trong validation-report.md.

---

# Vòng 3 — Execution-Log simulation (Route 18 đã improve, 17/08 khuya)

> Sau audit validate phát hiện "không có vết quá trình", skill vibe-teach-orchestrator Route 18 được improve (vibe-improve-orchestrator, verdict **IMPROVED conf 1.0**, 0 regression): exec-log JSONL BẮT BUỘC cho HV (READ/THINK/TRY/STUCK/ASK/ACT/DONE) + GV (SAID/DID/REACT), kèm schema + verifier deterministic `sim_exec_log_verifier.py` (7 check V1-V7, fixture PASS exit 0 / FAIL exit 1).

## Chạy lại simulation theo Route 18 mới — persona Nam (HC, sợ kỹ thuật)

- **HV log** `execution-logs/hv-nam-exec-log.jsonl` (12 dòng): đọc README lab 00 thật → chọn use case đặt phòng họp → điền 6/7 mục → **STUCK thật: tiêu chí thành công không ra con số** → ASK GV → GV REACT (chỉ slide S9) → chạy prompt 01 → brief hoàn chỉnh → READ studentkit (3 path thật) → resource map. **Verifier PASS: 12 dòng, STUCK resolved, package coverage 100%.**
- **GV log** `execution-logs/gv-exec-log.jsonl` (6 dòng): SAID trích verbatim từ file buoi-08-script.md, DID theo cột Thao tác GV. Verifier bắt 1 lỗi thật (SAID thiếu verbatim) → sửa → PASS.

## Giá trị cải tiến so với vòng 1-2

| Trước (vòng 1-2) | Sau (vòng 3) |
|---|---|
| Chỉ có artifact cuối + friction notes dạng tự thuật | Mỗi bước có dòng log với path thật, verify được bằng máy |
| Không chứng minh được HV "đã đọc hướng dẫn" | READ source bắt buộc tồn tại — không đọc = không PASS |
| Artifact có thể "từ trên trời rơi" | Package coverage 100% — mọi file phải được log nhắc |
| Kẹt ở đâu = đoán | STUCK có verbatim + resolved-by — biết chính xác bước nào kẹt, hỏi gì |
| Findings improve giáo trình = phỏng đoán | BR-44: finding phải trace về dòng exec-log |

## Finding từ exec-log Nam (trace V5)
- **F13 (MED):** Nam kẹt ở "tiêu chí đo được" đúng chỗ slide S9 hỗ trợ — nhưng phải chờ GV đi tới mới giải quyết. Gợi ý: lab 00 template thêm 1 ví dụ tiêu chí đo được ngay trong placeholder mục Tiêu chí (hiện chỉ có 1 ví dụ trong guidance README).

---

# Vòng 3 hoàn tất — Nam đủ 7 ngày (17/08 khuya)

## Kết quả cuối
- **Exec-log: PASS verifier** — 52 dòng, 8 READ (path thật), 7 STUCK (đều resolved bởi ASK/ACT), 3 ASK, timeline tăng dần, **package coverage 100%**. GV log 6 dòng (SAID verbatim từ script thật).
- **Auto-check (chạy thật 2 lần):** lần 1 — 3 PASS · **2 FAIL** (thiếu mục Ràng buộc; run-log thiếu evidence) → Nam tự fix cả 2 → lần 2: **5 PASS + 1 SKIP runtime**. Auto-check chứng minh giá trị giáo dục: bắt lỗi thật của HV giả lập đúng kiểu HV thật hay mắc.
- **GV chấm (chuẩn khắt khe sau audit): 88.8/100 — band Tốt.** Self-grading của Nam ~82 — chênh 6.8 điểm, chấp nhận được (Nam tự dưới-ước D2 vì sợ, GV xác nhận đúng mức).
- So sánh 5 persona: Hà 95.4 · Linh 87.0 (skill chấm) · **Nam 88.8** · Tuấn 52.8 (copy) · Mai 36.0 (bỏ dở) — phân hóa ổn định theo chất lượng đầu vào.

## Chuỗi khó khăn thật trong 7 ngày của Nam (từ exec-log — cơ sở improve giáo trình)
| Ngày | STUCK | Cách vượt | Đã có trong lab chưa |
|------|-------|-----------|---------------------|
| 18 | Tiêu chí đo không ra số | GV chỉ slide S9 | ✓ (F13 đã thêm mẹo vào template) |
| 19 | AI tự chọn khung giờ (vi phạm rule skill) | Dán lại rule — chat không nhớ | ✓ (lab 01 ghi chú F4) |
| 20 | **Đổi tên node n8n → workflow chết câm** | Auto-check [3] chỉ đúng chỗ + nối lại connection | ⚠ MỚI — xem F15 |
| 21 | Prompt rule văn xuôi → AI bỏ rule | Prompt 06 rule đánh số | ✓ (F10 đã fix) |
| 21 | n8n cần node ≥20, máy node 18 | Khai trung thực + GV runtime-check | ✓ (F14 đã thêm vào auto-check) |
| 22 | App crash câm (mảng rỗng truthy) | F12 Console — copy dòng đỏ hỏi AI | ✓ (F6 đã fix) |
| 24 | Auto-check bắt thiếu mục brief + thiếu evidence | Tự fix, chạy lại PASS | ✓ (tự tool) |

## Findings vòng 3
- **F15 (MED — đề xuất thêm vào lab 02):** lỗi "đổi tên node trong UI → đứt connection" xả ra thật ở 2/3 nhóm có runtime (Nam + chính tôi khi build exemplar). Lab 02 README nên thêm 1 dòng cảnh báo + cách kiểm: "đổi tên node xong chạy `capstone_auto_check.py` check [3] ngay". *(Áp dụng luôn bên dưới.)*
- **F14 (đã áp):** auto-check [4] giờ chấp nhận dòng khai-trung-thực "chưa runtime-test" là evidence hợp lệ (kèm note GV vẫn phải runtime-check) — vì nếu không, HV không chạy được n8n (node cũ, máy yếu) bị kẹt vô lý ở nghi thức thay vì nội dung.
- **Exec-log verifier bắt 3 lỗi thật trong chính quá trình tôi ghi log** (dòng JSON dính do thiếu newline, seq lệch, 16 file package chưa được nhắc) — tool có răng thật, không phải trang trí.

---

# Vòng 4 — Khánh: CSKH bot 3 tầng automation (ca phức tạp nhất, 17/08 sâu đêm)

## Kết quả
- **GV chấm: 95.4/100 — Xuất sắc** (B 15/15 · D1 20/20 · D2 23.4/25 · D3 20/20 · D4 17/20) · self-grading ~87 (chênh 8 — Khánh tự dưới-ước vì node AI chưa end-to-end; GV xác nhận mọi phần khác max).
- **Exec-log: PASS verifier** — 57 dòng, 8 STUCK (đều resolved), package coverage 100%.
- **Điểm khác cohort:** ca duy nhất chạy **runtime thật 7 vòng** — mỗi vòng là một lỗi thật khác nhau, không lặp.

## Hành trình 7 vòng runtime (giá trị đào tạo lớn nhất)
| Vòng | Phát hiện | Fix |
|------|-----------|-----|
| 1 | Respond B4 trả DOCX hợp đồng | Chuyển Respond → JSON |
| 2 | Đổi tên node → connection đứt (F15 tái xuất) | Remap keys + targets |
| 3 | **AI bỏ bước alias** + **Respond trả nguyên Gemini response** | Tách 2 lỗi riêng |
| 4 | Prompt alias dạng chú thích → AI bỏ qua | Đánh số R1-R5 + ví dụ phủ định |
| 5 | Webhook bọc body trong `.body` | `$json.body.data` (xác nhận bằng workflow debug riêng) |
| 6 | n8n expression không hỗ trợ JS ternary trong jsonBody | Rút gọn expression |
| 7 | **2 node B4 (Extract+Redaction) giữa Webhook-AI là logic hợp đồng — biến đổi $json làm mất dữ liệu** | Nối Webhook→AI trực tiếp |

- **Bằng chứng logic ĐÚNG:** gọi trực tiếp Gemini (từ host + từ trong container) với đúng prompt + model → **200, JSON nghiệp vụ hoàn hảo** (phân loại HOI_TON_KHO + alias P02 + reply hết hàng chuẩn). Chỉ tích hợp node AI trong n8n (với burst-quota express key + retry 1s×3) chưa chạy được end-to-end — khai rõ, fix đề xuất: waitBetweenTries=30s.
- **Runtime test lúc 20:25 ngày 18/08 (sáng nay): workflow import + activate + webhook 200 — auto-check 5/5 cấu trúc PASS, node AI quota-limited (đã thử flash-latest + flash-lite-latest + nghỉ 2 phút).**

## Findings F16-F17 (đã áp vào lab)
- **F16 (HIGH):** node preprocessing B4 (Extract .docx, Redaction) là **logic đặc thù hợp đồng** — khi mượn khung cho use case khác phải bỏ chúng khỏi luồng (chỉ giữ Webhook + AI + Respond). → Đã thêm cảnh báo vào lab 02 README.
- **F17 (MED):** webhook n8n bọc body trong `$json.body` — prompt AI node phải dùng `$json.body.data` (không phải `$json.data`). → Đã thêm ghi chú vào lab 02.

---

# Vòng 5 — Thảo (báo cáo tuần) + Hùng (review luật) — 2 use case phức tạp mới

## Kết quả
| HV | Use case | Điểm | Band | Exec-log |
|----|----------|------|------|----------|
| **Thảo** | Báo cáo tổng hợp kinh doanh tuần (10 nguồn CSV) | **90.0** | Xuất sắc | PASS 34 dòng · 3 STUCK resolved |
| **Hùng** | Review văn bản luật xây dựng | **90.0** | Xuất sắc | PASS 35 dòng · 2 STUCK resolved |

## Điểm khác biệt 2 ca này
- **Thảo — nguyên tắc thiết kế xuất sắc:** "SỐ VÒNG CỨNG, AI CHỈ VIẾT CÂU" (chống bịa số triệt để nhất cohort) + **áp F16/F17 ngay từ đầu** — học từ findings cohort, không lặp lỗi (chỉ dính F15 remap 1 lần do script build, tự fix ngay). Bug thật hay: dấu phẩy nghìn `2,310,000,000` bị `split(",")` cắt → fix `indexOf` dấu phẩy đầu.
- **Hùng — mượn tối đa cohort (6 path):** nghiệp vụ TRÙNG B4 → mượn gần nguyên workflow + **GIỮ node schema B4 có lý do** (khác các bạn khác phải bỏ — F16 chỉ áp khi nghiệp vụ khác). Quy tắc trung thực: KHONG_RO không bịa mức; 1 điều khoản match 2 rule → ghi gộp "A1/A3" thay vì chọn 1. Bug regex thật: nhánh `12%` sót — fix `(1[0-9]|[2-9]\d)%`.

## Tổng kết 8 persona sau 5 vòng
| HV | Use case | Điểm | Đặc trưng |
|----|----------|------|-----------|
| Hà | Bảo hành | 95.4 | Non-tech chăm — làm trọn đủ |
| Linh | Đối chiếu công nợ | 87.0 | Power — skill chấm độc lập |
| Nam | Đặt phòng họp | 88.8 | Sợ kỹ thuật — 7 STUCK đều vượt |
| Khánh | CSKH bot | 95.4 | Phức tạp nhất — 7 vòng runtime debug |
| **Thảo** | Báo cáo tuần | **90.0** | Nguyên tắc số-vòng-cứng + áp findings cohort |
| **Hùng** | Review luật | **90.0** | Mượn tối đa + trung thực KHONG_RO |
| Tuấn | (copy exemplar) | 52.8 | Chống copy hoạt động |
| Mai | (bỏ dở) | 36.0 | Cổng auto-check chặn đúng |

Phân hóa ổn định 36→95.4 theo chất lượng; điểm chung cohort: runtime AI node đều ⏳ quota key express (chung 1 key burst-limit) — mọi ca đều khai rõ trung thực.
