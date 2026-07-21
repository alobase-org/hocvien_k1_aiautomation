# Prompt TH3 — Áp rubric 100 điểm

> Chạy trong cùng phiên chat. Input là hai JSON trước, JD và rubric cố định.

```text
BỐI CẢNH:
Đây là LỚP 3 trong hệ thống HR Screening 4 lớp cho Nhân viên Kinh doanh B2B Junior. Mục tiêu là áp rubric cố định, không tự thay trọng số và không tự quyết định tuyển dụng.

INPUT:
- candidate-profile.json từ TH1.
- data-quality.json từ TH2.
- templates/JD-nhan-vien-kinh-doanh-B2B-junior.md.
- templates/rubric-kinh-doanh-B2B-100.json.
- schemas/scoring-result.schema.json.
- schemas/run-log-entry.schema.json.

CHỈ DẪN:
1. Đọc cả bốn file từ workspace.
2. Xác nhận candidate_id của TH1 khớp source_candidate_id của TH2.
3. Chấm đúng tám tiêu chí và max_points trong rubric; tổng max_points phải đúng 100.
4. Chỉ cho điểm khi có evidence trong candidate-profile.json. Không có evidence thì 0 điểm.
5. Mỗi criteria phải có id, name, score, max_points, evidence và scoring_note.
6. total_score phải bằng tổng score của criteria và nằm trong 0–100.
7. Nếu ready_for_scoring=false, result phải là NEEDS_REVIEW.
8. Nếu đủ dữ liệu: từ 75 STRONG_REVIEW; 60–74 REVIEW; dưới 60 LOW_PRIORITY_REVIEW.
9. Tạo interview_questions gồm 2–4 câu hỏi phỏng vấn bằng tiếng Việt. Mỗi câu phải dùng để xác minh dữ liệu thiếu, evidence yếu hoặc một thành tích/kinh nghiệm quan trọng; không hỏi thuộc tính nhạy cảm.
10. Ghi kết quả thật ra scoring-result.json; không sửa hai JSON trước.
11. Validate file theo schemas/scoring-result.schema.json. Nếu sai schema hoặc kiểu dữ liệu, tự sửa rồi validate lại.
12. Giữ nguyên run_id từ TH1–TH2 và append một dòng vào run-log.jsonl: step=TH3_SCORING_RESULT. SUCCESS khi artifact hợp lệ và ready_for_scoring=true; NEEDS_REVIEW khi artifact hợp lệ nhưng cần HR xác minh; ERROR khi lỗi kỹ thuật/schema. Nếu ERROR thì không chạy TH4.

TIÊU CHUẨN ĐẦU RA:
{
  "source_candidate_id": "",
  "criteria": [],
  "total_score": 0,
  "result": "NEEDS_REVIEW",
  "human_review_required": true,
  "scoring_summary": "",
  "interview_questions": []
}

Sau khi ghi file, đọc lại và tự kiểm tra: schema PASS, đủ 8 criteria, tổng max_points = 100, tổng score = total_score, có 2–4 interview_questions và source_candidate_id khớp hai lớp trước. Không xây workflow n8n ở bước này.
```

**Chaining line:** Ba JSON đã kiểm chứng + JD + rubric trở thành specification và expected output cho TH4.
