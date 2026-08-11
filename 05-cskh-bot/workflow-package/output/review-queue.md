# HITL Review Queue — CSKH Bot Workflow Design Package

> Danh sách các điểm bắt buộc con người (Human-in-the-loop) kiểm tra và duyệt trong quy trình CSKH Bot.

| ID | Bước / Hạng mục | Điều kiện kích hoạt | Người phụ trách | Hành động cần làm |
|---|---|---|---|---|
| **REV-01** | Yêu cầu Hoàn tiền / Đổi trả | Intent = `khieu_nai` hoặc `hoan_tien` | Nhân viên CSKH | Kiểm tra thông tin đơn hàng trên ERP/Sheets, liên hệ xác nhận với khách. |
| **REV-02** | Trả lời nghi vấn Hallucination | LLM Judge Confidence < 0.7 | Nhân viên CSKH | Đọc câu hỏi + nguồn trả lời, duyệt tin nhắn thủ công hoặc gọi trực tiếp hỗ trợ. |
| **REV-03** | Truy vấn ngoài phạm vi dịch vụ | Scope Status = `ngoai_pham_vi` | Nhân viên CSKH | Đánh giá nhu cầu khách hàng, chuyển tiếp thông tin tới đúng bộ phận phụ trách. |
| **REV-04** | Cảnh báo Prompt Injection nguy hiểm | Risk Flag = True | Trưởng nhóm CSKH / IT | Kiểm tra vết tin nhắn, chặn IP/User nếu cố tình tấn công hệ thống. |
