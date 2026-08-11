# Pha 3: Thiết Kế Hardening Cho Production & Đánh Giá Độ Tin Cậy

> **Mục tiêu:** Xây dựng 4 lớp gia cố an toàn (Fallback branch, Execution log, Edge case, HITL gate) và tự đánh giá 6 thuộc tính quy trình tin cậy.

---

## 1. Bảng Thiết Kế 4 Lớp Hardening

| Bước To-be | Fallback Branch (Dự phòng khi lỗi) | Execution Log (Nhật ký vận hành) | Edge Case (Trường hợp biên) | HITL (Ai duyệt / Khi nào) |
|---|---|---|---|---|
| **TB1: Guardrail** | Nếu Guard node lỗi → Coi như rủi ro cao, route thẳng tới CSKH ticket. | Log `timestamp`, `hash_input`, `risk_flag` (True/False). KHÔNG log PII thô. | Tin nhắn dài >1000 từ, chứa ký tự lạ, cố tình bypass system prompt. | Không cần duyệt (Auto Filter). |
| **TB2: Scope Router** | Ý định không rõ / ngoài phạm vi → Trả về thông báo lịch sự "Ngoài phạm vi" + tạo Ticket. | Log `intent_detected`, `scope_status` (IN/OUT), `confidence_router`. | Câu hỏi mập mờ vừa hỏi sản phẩm vừa đòi hoàn tiền. | CSKH tiếp nhận nếu `intent == ngoai_pham_vi`. |
| **TB3: FAQ Cache** | Vector Search timeout hoặc score < 0.86 → Chuyển sang LLM Fallback (TB4). | Log `cache_status` (HIT/MISS), `matched_faq_id`, `similarity_score`. | Không tìm thấy FAQ tương thích (similarity < 0.5). | Không cần duyệt (Fast Path). |
| **TB4: LLM Fallback** | LLM API timeout / 5xx → Fallback sang câu trả lời định sẵn "CSKH đang kiểm tra, sẽ nhắn bạn ngay". | Log `llm_prompt_tokens`, `llm_completion_tokens`, `source_docs_used`. | FAQ kho tri thức rỗng hoặc câu hỏi thiếu dữ liệu bám nguồn. | Đẩy qua LLM-as-Judge kiểm tra trước khi phát hành. |
| **TB5: LLM-as-Judge** | LLM Judge lỗi → Mặc định gán `confidence = 0` → Đẩy vào luồng HITL Ticket. | Log `judge_confidence`, `judge_reason`, `decision` (AUTO_REPLY / TICKET). | LLM tự trả lời nhưng Judge nghi ngờ có hallucination (`confidence < 0.7`). | **CSKH duyệt Ticket** trong Google Sheets trong vòng 15 phút. |

---

## 2. Tự Đánh Giá 6 Thuộc Tính Quy Trình Tin Cậy (Reliability Assessment)

| Thuộc tính | Đánh giá | Chi tiết giải trình |
|---|---|---|
| **1. Fault-tolerant** (Kháng lỗi) | **Đạt** | Có fallback 3 nấc: FAQ Cache hit → LLM Answer → Static Fallback Message nếu API chết. |
| **2. Observable** (Giám sát được) | **Đạt** | Log đầy đủ `run-log.jsonl` với `source_q_id`, `route`, `cache_hit`, `judge_confidence`, `execution_time`. |
| **3. Scalable** (Mở rộng tốt) | **Đạt** | Kiến trúc Fast Path xử lý 80% truy vấn qua Vector Cache (kết quả trong <100ms), tiết kiệm API cost LLM. |
| **4. Workable** (Dễ vận hành) | **Đạt** | Nhân sự CSKH chỉ làm việc trên giao diện quen thuộc (Google Sheets Ticket / Landing Page Chatbot). |
| **5. Idempotent** (Tính trùng lặp) | **Đạt** | Mỗi truy vấn gán UUID `source_q_id`, gửi lại 2 lần cùng câu hỏi sinh ra cùng kết quả cache không nhân đôi ticket. |
| **6. Auditable** (Kiểm toán được) | **Đạt** | Hash dữ liệu PII, lưu vết nguyên nhân chuyển ticket (`judge_reason`) giúp quản lý audit lại quyết định AI. |

---

## 3. Compliance Note (Bảo mật & Tuân thủ)

- **Quy định PII:** Mọi tin nhắn đầu vào được hash MD5 trước khi ghi vào execution log công khai.
- **Tiền bạc & Pháp lý:** Mọi yêu cầu liên quan đến `hoan_tien`, `boi_thuong`, `khiou_nai` KHÔNG ĐƯỢC tự động hóa 100%, bắt buộc ghi Ticket cho nhân viên CSKH có thẩm quyền xử lý.
