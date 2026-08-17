# Prompt 12 — Tự chấm package theo rubric (Evaluate)

> Chạy SAU khi auto-check đã PASS hết [1]–[5]. Đây là bản FALLBACK cho AI thường — nếu bạn dùng Claude Code, dùng luôn skill `vibe-ai-auto-score` (kèm trong lab này) sẽ chấm đầy đủ hơn.

---

Bạn là trợ lý chấm bài trung thực. Giúp tôi tự chấm package đồ án capstone của chính tôi theo rubric dưới đây. Nguyên tắc: **tôi là người chấm, bạn là người đối chiếu evidence** — đừng nể tôi, đừng chấm hộ rồi xong.

## Bối cảnh
Đây là đồ án capstone AI Automation K1: 4 deliverable (D1 skill, D2 n8n e2e, D3 MVP, D4 package+pitch). GV sẽ chấm bằng đúng rubric này và sẽ runtime-check lại (import workflow chạy input, mở app). Tự chấm trung thực giờ rẻ hơn bị phát hiện claim ảo lúc chấm.

## Chỉ dẫn
1. Đọc rubric (5 nhóm criterion, mỗi criterion có mô tả 5 mức). Đọc mô tả package tôi dán.
2. Với TỪNG sub-criterion: đề xuất mức (1–5) + 1 câu lý do + trích verbatim 1 chỗ trong package làm evidence. Không tìm được evidence → mức ≤2 và ghi "[thiếu evidence]".
3. Phân biệt rõ: cái nào trong package CHẠY THẬT (có bằng chứng: test PASS, run-log, ảnh) vs cái nào chỉ MỚI MÔ TẢ — mức của cái thứ hai tối đa 3.
4. Tính điểm nhóm = trung bình mức theo trọng số; điểm tổng /100.
5. Cuối: liệt kê TOP 3 gap đáng fix nhất (trọng số × khoảng cách tới mức 4), mỗi gap ghi: fix gì, ở lab nào, ước lượng phút.

## Tiêu chuẩn đầu ra
- File `self-grading.md`: bảng chấm đủ mọi sub-criterion (mức + lý do + evidence verbatim) + tổng điểm + top 3 gap
- Không khen chung chung; không nâng mức khi thiếu evidence
- Nếu tôi bảo "cho điểm cao hơn" trong chat sau đó — từ chối, chỉ chấp nhận khi tôi đưa evidence mới

## Rubric

[DÁN nội dung checkpoints/rubric-capstone.json]

## Package của tôi (mô tả + các file chính)

[DÁN: README package + usecase-brief + kết quả auto-check + các đoạn SKILL.md / run-log / spec-kit / improve-log chính]
