---
title: Student Grading Calibration — chấm nương tay, động viên học viên
muc-tich: Hiệu chỉnh rubric và cách chấm cho bối cảnh đào tạo: học viên làm 70% so với bài mẫu giảng viên thì đạt ~7/10.
nguon-hoc: Định hướng giáo dục "động viên trước, khắt khe sau" — ưu tiên giữ động lực học viên.
---

# Student Grading Calibration

> **"Học viên làm được 70% so với bài mẫu của giảng viên → đạt khoảng 7/10. Mục tiêu là động viên, không phải gạt."**

Skill này dùng để **chấm bài học viên** dựa trên tài liệu một buổi dạy. Bài "mẫu/giảng viên" là
chuẩn 10/10 (level 5). Học viên không cần vượt bằng giảng viên — chỉ cần làm được phần lớn yêu cầu
cốt lõi là đã đạt. Hướng dẫn này hiệu chỉnh (calibrate) rubric và cách chọn level cho đúng tinh thần đó.

---

## 1. Mô hình tham chiếu: "bài giảng viên = 10/10"

| Mức làm so với bài mẫu GV | Điểm dự kiến | Level trung bình | Band |
|---|---|---|---|
| 100% — sánh ngang/gần bằng GV | 9–10 | 5 | Xuất sắc |
| ~85% — làm đầy đủ, chỉ thiếu điểm tinh tế | 8 | 4 | Tốt |
| **~70% — làm được phần lớn yêu cầu cốt lõi** | **7** | **3.5** | **Đạt (khäng khích)** |
| ~50% — làm được một nửa, còn thiếu chính | 5–6 | 3 | Đạt/Yếu |
| ~30% — mới khởi động, còn nhiều khoảng trống | 3–4 | 2 | Yếu |
| <20% — gần như chưa làm | <3 | 1 | Kém |

**Quy tắc vàng:** "70% của giảng viên" = **mốc ĐẠT**, không phải mốc "yếu". Học viên chạm được 70%
yêu cầu cốt lõi đã đáng được 7/10.

---

## 2. Hiệu chỉnh level descriptors (BẮT BUỘC khi thiết kế rubric)

Khi viết 5 mức cho mỗi tiêu chí con, **căn cứ vào bài mẫu giảng viên** (từ `checkpoints/`, `prompts/`,
`lab.md` của buổi đó):

- **Level 5 (Xuất sắc ≈ 100%):** sánh ngang bài GV — đầy đủ, đúng, có điểm tinh tế/vượt yêu cầu.
  *(Dành cho số ít — không kỳ vọng mọi học viên.)*
- **Level 4 (Tốt ≈ 85%):** làm đầy đủ yêu cầu, chỉ thiếu 1–2 điểm tinh tế hoặc độ hoàn thiện.
- **Level 3 (Đạt ≈ 70%):** **làm được phần lớn yêu cầu CỐT LÕI**, có thể còn sai sót nhỏ hoặc thiếu
  điểm phụ. **Đây là mốc kỳ vọng cho đa số học viên chăm chỉ.**
- **Level 2 (Yếu ≈ 50%):** làm được một nửa, còn bỏ trống phần chính.
- **Level 1 (Kém ≈ <30%):** gần như chưa làm, chỉ có ý định/skeleton.

❌ Đừng đặt mức "Đạt" = "làm đúng 100% như GV" → sẽ ép mọi bài về 5–6/10, mất tính động viên.
✅ Đặt mức "Đạt" = "làm được phần lớn cốt lõi" → bài 70% tự nhiên về 7/10.

### Ví dụ hiệu chỉnh (tiêu chí "Workflow có chạy đúng luồng")
- **Tệ (không động viên):**
  `5 = đầy đủ mọi nhánh + error handling · 3 = đúng luồng chính · 1 = không chạy`
  → ở đây "Đạt" đòi hỏi quá nhiều, bài 70% dễ rớt về level 2.
- **Tốt (động viên):**
  `5 = sánh ngang bài GV (đủ nhánh + xử lý lỗi + polish) · 4 = đúng luồng chính + 1 nhánh phụ · 3 = đúng luồng chính, thiếu nhánh phụ/xử lý lỗi (ĐẠT ~70%) · 2 = luồng chính còn thiếu bước · 1 = không chạy`
  → bài làm được luồng chính = level 3 ≈ 7/10.

---

## 3. Nới lỏng level-ceiling cho bối cảnh học viên

`kb/scoring-integrity-guide.md §2` định nghĩa level-ceiling chống "chấm phồng" — rất đúng cho thi
cử/production. Nhưng khi **chấm học viên**, áp dụng tinh thần nới lỏng sau (vẫn giữ evidence, chỉ bớt
khắt khe):

| Tình huống | Capstone/production (gốc) | Chấm học viên (này) |
|---|---|---|
| Không có verbatim quote | max L2 | **max L3** (nếu nội dung rõ ràng trong bài) |
| Evidence chung chung, không đặc hiệu | max L3 | **vẫn cho L3–L4 nếu đúng ý cốt lõi** |
| Không có output chạy thử/log/test | max L4 | **không cap cứng** — mô tả logic đúng vẫn tính |
| L5 cần ≥2 dấu hiệu độc lập | giữ | giữ (L5 vẫn phải xứng đáng) |

**Nguyên tắc:** vẫn KHÔNG bịa evidence (BR-01 giữ nguyên), nhưng khi evidence hợp lý, **chọn level
cao hơn** thay vì thấp hơn khi phân vân. "Nâng tay" cho học viên, không "ghim".

> Ngoại lệ: nếu bài có dấu hiệu **lười/ảo thật sự** (placeholder trống, copy nguyên mẫu không sửa,
> AI-slop) → vẫn áp penalty theo §3 scoring-integrity-guide. Động viên người chăm chỉ, không bao che
> người lười.

---

## 4. Trọng số ưu tiên "hiểu và làm được" hơn "polish"

Khi gán `weight` cho tiêu chí con, ưu tiên:
- **Cao:** hiểu đúng yêu cầu, làm được cốt lõi, workflow chạy đúng luồng chính, nộp đủ deliverable.
- **Trung bình:** hoàn thiện, xử lý edge-case, tinh tế.
- **Thấp:** polish thẩm mỹ, ghi chú formatting.

→ Tránh phạt nặng vì thiếu polish — học viên mới chưa giỏi phần đó.

---

## 5. Checklist "chấm nương tay" trước khi chốt 1 bài

- [ ] Level descriptors đã căn cứ bài GV, mức 3 = "phần lớn cốt lõi" (không phải "đúng 100%").
- [ ] Khi phân vân giữa 2 mức → **chọn mức cao hơn** cho học viên (trừ khi rõ ràng yếu).
- [ ] Không cap cứng vì thiếu test output/log — mô tả logic đúng vẫn được tính.
- [ ] Bài 70% cốt lõi → điểm thực tế rơi ~7/10, không bị kéo về 5–6.
- [ ] Penalty chỉ áp cho lười/ảo thật sự, không áp cho "chưa hoàn thiện".
- [ ] Phần feedback ghi rõ **điều làm tốt trước**, rồi mới gap — để học viên có động lực sửa.

---

## 6. Lưu ý về "đạt tầm 7/10"

Công thức tổng điểm vẫn là `total_100 = Σ(level_i/5 × 100 × weight_i) / Σ(weight_i)` (aggregator tự
tính, KHÔNG tự ghi). KhiDescriptors đã hiệu chỉnh đúng (mức 3 ≈ 70%), một bài "làm phần lớn cốt lõi"
sẽ **tự nhiên** ra quanh 70/100 = 7/10. Không cần nhân hệ số ẩn — hiệu chỉnh nằm ở descriptors, không
phải ở công thức.

*Living guide. Cập nhật khi có phản hồi từ lớp học.*
*"Chấm nương tay — để học viên còn muốn học tiếp buổi sau."*
