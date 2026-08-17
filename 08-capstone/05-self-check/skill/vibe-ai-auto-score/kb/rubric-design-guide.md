# Hướng dẫn thiết kế Rubric chuyên nghiệp

Tham chiếu cho Phase 1. Mục tiêu: rubric khả thi, khách quan, chấm nhất quán giữa các giám khảo.

## 1. Cấu trúc 2 tầng

```
Tiêu chí chính (criterion) — chiều đánh giá lớn, vd: "Chất lượng kỹ thuật"
└── Tiêu chí con (subcriterion) — đo lường được, vd: "Hiệu năng", "Bảo mật", "Code sạch"
      └── 5 mức định tính — mỗi mức CÓ MÔ TẢ cụ thể
```

**Tại sao 2 tầng:** Tiêu chí chính quá rộng để chấm trực tiếp; tiêu chí con đủ hẹp để có descriptor
khách quan. Điểm tổng = tổng hợp có trọng số các tiêu chí con.

## 2. Trọng số (weight)

- Phản ánh độ quan trọng, không cần cộng đủ 1 — aggregator chuẩn hóa.
- Nguyên tắc: tiêu chí phản ánh mục tiêu cốt lõi → trọng số cao nhất.
- Thường: tiêu chí con trong 1 nhóm có thể cộng đủ trọng số của nhóm đó.
- Tránh "mọi tiêu chí đều trọng số bằng" trừ khi thực sự đúng.

## 3. Mô tả 5 mức (level descriptors) — yếu tố quyết định

**Đây là phần quan trọng nhất.** Descriptor mơ hồ → chấm không nhất quán.

❌ Tệ: `5 = Tốt, 3 = Trung bình, 1 = Kém` (không biết "tốt" là gì)

✅ Tốt (ví dụ tiêu chí "Hiệu năng"):
```
5: Thời gian phản hồi <100ms ở p99; xử lý được 10k req/s; có benchmark kèm số liệu
4: <300ms p99; 1k req/s; có số liệu nhưng thiếu benchmark đầy đủ
3: <1s p99; chịu tải vừa phải; số liệu ít
2: >1s thường xuyên; không có số liệu
1: Không chạy được / treo / không đo lường
```

Mỗi mức nên có **điều kiện quan sát được** (số liệu, hành vi cụ thể), không phải tính từ.

## 4. Đánh dấu `needs_research`

Đặt `needs_research: true` + `research_query` cho tiêu chí con mà việc chấm đòi hỏi fact bên ngoài
mà giám khảo thông thường không chắc:
- Đúng chuẩn luật/quy định (vd: "tuân thủ NĐ 30")
- Đúng best-practice ngành (vd: "kiến trúc microservices chuẩn")
- So sánh với benchmark ngành

Tại sao: chấm những tiêu chí này "bằng cảm tính" = chấm sai. Cần research làm tham chiếu khách quan.

## 5. Checklist trước khi chấm

- [ ] Mỗi tiêu chí con có đủ 5 descriptor cụ thể (quan sát được)
- [ ] Trọng số phản ánh mục tiêu (không đều nhau vô cớ)
- [ ] Tiêu chí cần fact → đã đánh `needs_research` + `research_query`
- [ ] Không có descriptor chồng lấn (mức 4 và 5 phải khác biệt rành mạch)
- [ ] Đã validate `rubric.json` qua `validator.py`

## 6. Thang điểm

```
5 → Xuất sắc   (≥90 tổng)
4 → Tốt/Khá    (≥75)
3 → Đạt        (≥60)
2 → Yếu        (≥40)
1 → Kém        (<40)
```

`total_100 = Σ(level_i / 5 × 100 × weight_i) / Σ(weight_i)` — aggregator tự tính, KHÔNG tự ghi.
