# Validation Report v2 — Audit simulation vòng 4+5 (Khánh/Thảo/Hùng)

> /vibe-validate-orchestrator · 18/08/2026 · Deterministic-first: mọi check bằng re-run code, không LLM self-score.

## Verdict tổng: **VERIFIED — simulation chạy thật** (với 2 phát hiện nhỏ, 0 hallucination nghiêm trọng)

## Kết quả 5 nhóm kiểm

### V1. Artifact tồn tại ✅
| Package | Files | Ghi chú |
|---|---|---|
| khanh-capstone | 29 | đủ 4 deliverable + 5 runtime-responses files |
| thao-capstone | 21 | đủ |
| hung-capstone | 23 | đủ |

### V2. Exec-log verifier re-run ✅ 3/3 PASS
- Khánh: 57 dòng · 8 STUCK resolved · coverage 100%
- Thảo: 34 dòng · 3 STUCK resolved · coverage 100%
- Hùng: 35 dòng · 2 STUCK resolved · coverage 100%

### V3. Logic re-run (deterministic) ✅
| Check | Kết quả |
|---|---|
| Khánh D1 re-run 3 TC (alias + classify) | **3/3 PASS** |
| Thảo D1 tc2 re-run (đúng baseline w_prev=2.1t) | **-14.3% PASS** — khớp file output |
| Hùng D1 re-run 5 TC + khớp file output | **5/5 PASS** |
| Khánh D3 app re-run (reply "sạc 65w") | **P02 + hết hàng PASS** |
| Thảo D3 app re-run (so + parse dấu phẩy) | **5/5 PASS** (sau khi sửa harness auditor) |
| Hùng D3 app re-run (review thanh toán 100%) | **CAO-A1 PASS** |

**2 lỗi harness của AUDITOR (không phải lỗi HV)** — lần đầu re-run: (1) Thảo tc2 dùng sai baseline (w1 thay w_prev) → -22.1% giả; sửa đúng baseline → -14.3% khớp. (2) Thảo hàm so() gọi sai cách (Function constructor) → FAIL giả; sửa → PASS. **Bài học: 2 "FAIL" đầu đều là lỗi auditor, không phải lỗi simulation.**

### V4. Run-log claim vs evidence ✅
- Khánh runtime `content-type: application/json` ✓, response chứa `candidates` (bằng chứng AI Gemini chạy thật) ✓, chứa `KHAC` (lỗi phân loại khai đúng) ✓
- Workflow IDs thật (cKlsHwHKcZJCQ9JA, VBwikDatGTW0kQlz...) — 5 file runtime-responses tồn tại
- Điểm grading khớp dry-run-report: Khánh 95.4 · Thảo 90.0 · Hùng 90.0 ✓

### V5. Verbatim evidence ✅ 7/7
- Khánh 5/5: evidence trong `cskh-log.csv` (TC5,KHAC,None,PASS — verbatim)
- Thảo -14.3% trong output tc2-summary.json (verbatim)
- Hùng KHONG_RO trong output tc5-review.json (verbatim)
- F16 áp đúng: cả 3 workflow đều 0 connection tới node Extract/Redaction B4 ✓

## 2 PHÁT HIỆN (không nghiêm trọng)

### P1 (LOW): Khánh thiếu `d1-agent-skill/test/test-run.md`
- Dry-run-report claim "5/5 PASS có output JSON thật + CSV log" — **đúng** (CSV có đủ 5 dòng PASS + 5 output JSON), nhưng format test-run.md (mà Thảo, Hùng có) bị thiếu.
- Nguyên nhân: exec-log Khánh ghi DONE cskh-log.csv + 5 output JSON nhưng không ghi test-run.md riêng.
- **Không phải hallucination** — claim "5/5 + CSV" khớp evidence thật. Gap format nhỏ.
- Đề xuất: thêm file test-run.md cho Khánh (mô tả kết quả đã có trong CSV).

### P2 (INFO): Auditor 2 lần suýt falsely-flag FAIL do lỗi harness
- Re-run thiếu đúng baseline / sai cách gọi hàm → kết quả âm giả.
- Xác nhận thêm giá trị nguyên tắc "deterministic nhưng phải ĐÚNG input" — auditor cũng cần self-check.

## Kết luận
**hallucination_risk = LOW.** Simulation vòng 4+5 chạy thật: mọi artifact tồn tại, logic re-run PASS, exec-log PASS verifier, runtime evidence thật (JSON responses từ n8n docker), điểm số khớp grading. 2 phát hiện nhỏ (P1 gap format, P2 lỗi harness auditor) không ảnh hưởng kết luận.
