# Prompt TH2 — Rà soát chất lượng dữ liệu

> Chạy trong cùng phiên chat TH1. Input bắt buộc là file `candidate-profile.json` vừa tạo.

```text
BỐI CẢNH:
Đây là LỚP 2 trong hệ thống HR Screening 4 lớp. Lớp này chỉ kiểm tra chất lượng dữ liệu trước khi chấm điểm; không bóc lại CV và không đánh giá ứng viên tốt/xấu.

INPUT:
- candidate-profile.json từ TH1.
- schemas/data-quality.schema.json.
- schemas/run-log-entry.schema.json.

CHỈ DẪN:
1. Đọc candidate-profile.json từ workspace và kiểm tra JSON hợp lệ.
2. Kiểm tra bốn trường bắt buộc: candidate_name, full_time, months_sales, communication_evidence.
3. Mỗi trường bắt buộc thiếu trừ 20 điểm completeness.
4. Nếu months_b2b lớn hơn months_sales, thêm cảnh báo và trừ 10 điểm.
5. ready_for_scoring chỉ true khi completeness_score >= 60 và không có cảnh báo.
6. source_candidate_id phải lấy đúng candidate_id của TH1.
7. Ghi kết quả thật ra file data-quality.json; không sửa candidate-profile.json.
8. Validate file theo schemas/data-quality.schema.json. Nếu sai schema hoặc kiểu dữ liệu, tự sửa rồi validate lại.
9. Giữ nguyên run_id của TH1 và append một dòng vào run-log.jsonl: step=TH2_DATA_QUALITY. Dùng SUCCESS nếu đủ điều kiện chấm, NEEDS_REVIEW nếu artifact hợp lệ nhưng dữ liệu cần HR xác minh, ERROR nếu lỗi kỹ thuật/schema. Nếu ERROR thì dừng, không chạy TH3.

TIÊU CHUẨN ĐẦU RA:
{
  "source_candidate_id": "",
  "completeness_score": 0,
  "missing_fields": [],
  "warnings": [],
  "ready_for_scoring": false,
  "review_note": ""
}

Sau khi ghi file, đọc lại và xác nhận schema PASS, source_candidate_id khớp TH1, completeness_score nằm trong 0–100 và log entry hợp lệ. Không xây node n8n ở bước này.
```

**Chaining line:** `candidate-profile.json` + `data-quality.json` là input TH3.
