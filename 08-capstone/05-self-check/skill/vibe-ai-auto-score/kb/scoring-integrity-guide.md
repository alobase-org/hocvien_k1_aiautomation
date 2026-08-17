---
title: Scoring Integrity — chống chấm phồng & chấm thành thật
muc-tich: Hướng dẫn thiết kế điểm minh bạch, tái lập được, chống hallucination ở tầng chấm.
nguon-hoc: cham_bai_capstone_v2 (capstone-rubric-v2 §0.4 §0.7 §0.8) — triết lý "điểm cộng lại phải thành thật"
---

# Scoring Integrity Guide

> **"Điểm công bố phải cộng lại thành thật — không chấm cao rồi ép về khung ở bước cuối, không cộng/trừ khi không có bằng chứng."**

Skill generic này học 3 cơ chế từ `cham_bai_capstone_v2` (skill chấm Capstone Viettel đã đạt chuẩn) —
đã được **generalize** để dùng cho MỌI rubric, không phải riêng Capstone:

1. **Honest additive scoring** — base + bonus − penalty, không hệ số nhân ẩn.
2. **Level-ceiling anti-inflation** — rule cấm nâng level khi evidence không đủ đặc hiệu.
3. **Adjustment trigger gate** — penalty chỉ trừ khi đủ điều kiện khách quan, chống trừ bừa.

---

## 1. Honest additive scoring — KHÔNG nhân hệ số ẩn

### Vấn đề nó giải quyết
Một số rubric cũ chấm từng mục 90-100 rồi nhân `× 0.8` ép về ≤80 ở bước cuối → candidate/giám khảo
cảm thấy bị "cố tình chấm thấp". Điểm công bố không khớp điểm từng mục → mất niềm tin.

### Nguyên tắc (vibe-ai-auto-score)
- **Base score** = weighted-average của levels — đây là điểm cốt lõi, luôn minh bạch.
- **Adjustments** (TUỲ CHỌN) là lớp cộng/trừ **công khai**, mỗi mục có evidence:
  - `bonus` (+) thưởng nỗ lực vượt yêu cầu
  - `penalty` (−) phạt hành vi lười/ảo
- **Final** = `clamp(base + Σbonus − Σpenalty, 0, 100)`.
- **Không có phép nhân hệ số ẩn nào ở cuối.** Mỗi điểm cộng/trừ đều có lý do + evidence ghi rõ.

### Khi nào DÙNG adjustments
- Khi rubric cần **phân biệt** bài "làm vừa đủ" vs "vượt trội" vs "lười/ảo".
- Khi có hành vi cụ thể đáng thưởng/phạt mà weighted-average không bắt được (vd: AI-slop, placeholder
  chưa điền, diagram xuất sắc, tri thức chuyên môn sâu).

### Khi nào KHÔNG dùng
- Rubric đơn thuần định tính, không có yếu tố thưởng/phạt → để trống `adjustments`. Khi đó
  `final_score == base_score` (skill tự xử lý backward-compat).

---

## 2. Level-ceiling anti-inflation — chống chấm phồng

### Vấn đề nó giải quyết
Giám khảo (LLM hoặc người) dễ "chấm phồng": thấy bài có ý tưởng đúng, có tài liệu dài → nâng level.
Kết quả: mọi bài đều 4-5, mất khả năng phân loại, và vi phạm nguyên tắc "không có bằng chứng verbatim —
không có điểm".

### Các rule cấm nâng level (kế thừa v4.2, generalize)

| Tình huống evidence | Level tối đa |
|---|---|
| Không tìm được `verbatim_quote` trong source | **2** (+ confidence ≤ 0.5, need_review=true) |
| Evidence chỉ khẳng định chung chung, KHÔNG cho thấy cách làm cụ thể | **3** |
| Tiêu chí cần số liệu/owner/ngưỡng nghiệm thu/schema/test/rollback/log/Q&A nhưng bài chỉ nêu tên hạng mục, không có nội dung | **3** |
| Evidence từ file nhị phân (.pptx/.pdf/.docx) chỉ xác nhận tệp tồn tại, không đọc nội dung | **3** |
| Tiêu chí vận hành/kiểm thử nhưng KHÔNG có output chạy thử/log/test result/lệnh chạy/file cấu hình | **4** (dù mô tả thiết kế tốt) |
| Level **5** (khi tiêu chí có nhiều thành phần) | cần **≥2 dấu hiệu kiểm chứng độc lập** |

### Nguyên tắc nền
- **KHÔNG nâng level dựa trên:** ý định tốt · độ dài tài liệu · mô tả miệng · "có vẻ đúng".
- Khi evidence không thể kiểm tra → tối đa level 2.
- Level 5 là đặc quyền của bài có minh chứng **đầy đủ, cụ thể, vận hành được** — không phải mặc định cho "bài khá".

### Cách áp trong workflow
Trong Phase 5 (GRADE), khi chọn level cho mỗi tiêu chí con, giám khảo phải:
1. Đọc descriptor từng mức (1-5).
2. Tìm evidence verbatim **đặc hiệu** cho mức đó.
3. Áp rule ceiling ở trên — nếu evidence không đủ đặc hiệu cho mức N → chốt mức thấp hơn.

---

## 3. Adjustment trigger gate — chống trừ bừa

### Vấn đề nó giải quyết
Penalty (−) nguy hiểm hơn bonus (+): giám khảo có thể lạm quyền trừ điểm theo cảm tính để "ép điểm thấp",
phá tính công bằng. Cần cơ chế ép penalty phải **khách quan, có điều kiện**.

### Nguyên tắc
- **Mỗi penalty BẮT BUỘC có `trigger_condition`** — điều kiện khách quan phải thoả mới được trừ.
  VD: "bài thiếu ≥2 dấu hiệu tri thức chuyên môn/thực tế" · "còn ≥1 placeholder chưa điền" · "copy-paste
  ≥2 file gần identical".
- Validator (`score_aggregator.py`) **CHỈ tính penalty khi `trigger_met == true`**.
  - `trigger_met` thiếu/`false` → penalty bị BỎ QUA (bảo vệ candidate).
- **Mục đích penalty là PHÂN BIỆT** "làm đàng hoàng" vs "lười/ảo" — KHÔNG phải để ép điểm thấp.
  Trừ vừa đủ, có evidence, công khai.

### Bonus thì sao?
- Bonus không cần trigger (luôn được tính khi có evidence) — vì thưởng là chủ động, không gây hại.
- Nhưng vẫn BẮT BUỘC có evidence: "không chứng minh được thì không cộng".

### Thiết kế trigger_condition cho penalty — checklist
- [ ] Khách quan, đếm được (số placeholder, số file identical, số dấu hiệu chuyên môn).
- [ ] Không phụ thuộc ý kiến chủ quan của giám khảo.
- [ ] Có evidence verbatim trỏ về file gốc.
- [ ] Mức trừ tỉ lệ với mức độ vi phạm, không trừ quá mức.

---

## 4. Confidence gate 3 tầng — quyết định flow

| Verdict | Confidence | Hành xử |
|---|---|---|
| **PASS** | ≥ 0.85 | Chấp nhận chấm tự động, vào xếp hạng. |
| **NEED_REVIEW** | 0.60 – 0.85 | Đẩy review queue, chờ human xác nhận rồi mới chốt. |
| **REJECT** | < 0.60 | Dừng, exit, **KHÔNG xếp hạng** — human xử lý thủ công (BR-08). |

- Overall confidence = `min` across tất cả fields/tiêu chí (nơi yếu nhất quyết định toàn bài).
- Gate chạy **sau** recompute, **trước** xếp hạng. REJECT = candidate bị loại khỏi summary ranking.

---

## 5. Tổng kết — checklist "điểm thành thật"

Trước khi chốt 1 bài:

- [ ] Mỗi tiêu chí con có ≥1 `verbatim_quote` CÓ THẬT trong source (BR-01).
- [ ] Level đã áp rule ceiling ở §2 — không phồng.
- [ ] Mọi bonus/penalty có evidence; penalty có `trigger_condition` + `trigger_met=true`.
- [ ] `final_score` = clamp(base + bonus − penalty) — KHÔNG nhân hệ số ẩn.
- [ ] `confidence_gate` verdict đã tính; REJECT/NEED_REVIEW chưa vào xếp hạng chính thức.
- [ ] Aggregate recompute bằng `score_aggregator.py --verify` (BR-03).

*Living guide. Cập nhật khi có pattern chấm sai mới.*
*"Điểm thành thật — công khai, tái lập được, có bằng chứng cho từng con số."*
