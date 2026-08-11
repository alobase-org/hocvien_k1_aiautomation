# Pha 2: Thiết Kế Quy Trình Hiện Trạng (As-is) & Quy Trình Tối Ưu (ESIA To-be)

> **Mục tiêu:** Phân tích 5 bước quy trình CSKH thủ công hiện tại (As-is) và áp dụng phương pháp ESIA (Eliminate - Simplify - Integrate - Automate) để thiết kế quy trình To-be chuẩn production.

---

## 1. Bảng Quy trình Hiện trạng (As-is - 5 bước)

| Bước | Người thực hiện | Input | Output | Điểm nghẽn / Lỗi lặp |
|---|---|---|---|---|
| **B1** | Khách hàng | Câu hỏi qua Website / Zalo / Fanpage | Tin nhắn thô | Khách gửi rải rác, không đúng định dạng, chứa câu hỏi chung chung hoặc khiếu nại đè nặn. |
| **B2** | Nhân viên CSKH | Tin nhắn thô từ khách | Phân loại chủ đề thủ công | Mất 3-5 phút/tin nhắn để đọc và xác định khách đang hỏi phí ship, đổi trả hay khiếu nại. |
| **B3** | Nhân viên CSKH | File Word/Excel chính sách bán hàng | Tra cứu câu trả lời thủ công | Tra cứu thủ công dễ sót/nhầm lẫn quy định bảo hành; trả lời không nhất quán giữa các nhân viên. |
| **B4** | Nhân viên CSKH | Thông tin tra cứu được | Tin nhắn phản hồi gửi khách | Trả lời lặp đi lặp lại 50 câu hỏi giống nhau mỗi ngày; tốn thời gian soạn tin. |
| **B5** | Nhân viên CSKH | Thông tin khiếu nại / hoàn tiền | Note thủ công vào Google Sheets | Bỏ sót các ca phức tạp/hoàn tiền cần quản lý duyệt; không có điểm cảnh báo rủi ro tự động. |

---

## 2. Phân tích ESIA & Đề xuất Quy trình Mới (To-be)

| Bước (To-be) | Hành động (E/S/I/A) | Chi tiết tối ưu & Điểm HITL | Ai làm (AI/Người) | Nhánh Automation |
|---|---|---|---|---|
| **TB1: Tiếp nhận & Guardrail** | **S (Simplify)** | Lọc Prompt Injection, normalize văn bản, coi tin nhắn khách = DATA. Từ chối ngay câu độc hại. | AI (n8n Code) | n8n workflow |
| **TB2: Scope & Intent Router** | **I (Integrate)** | Phân loại câu hỏi thuộc phạm vi bán lẻ hay ngoài scope (`thong_tin`, `gia`, `ky_thuat`, `khieu_nai`, `ngoai_pham_vi`). | AI (n8n Code/LLM) | n8n workflow |
| **TB3: FAQ Cache Fast Path** | **A (Automate)** | So khớp Exact & Cosine Similarity vector DB 15 FAQ. Nếu score ≥ 0.86 → **Reply ngay không gọi LLM**. | AI (Vector DB + n8n) | n8n workflow |
| **TB4: LLM Fallback (Gắn nguồn)** | **A (Automate)** | Khi Cache Miss → LLM tổng hợp câu trả lời **bắt buộc trích dẫn nguồn** từ `chinh-sach-ho-tro.md`. | AI (LLM Answer) | AI Agent / n8n |
| **TB5: LLM-as-Judge & Gate** | **I (Integrate)** | LLM thứ 2 chấm điểm `{confidence, reason}`. Nếu confidence < 0.7 HOẶC intent nhạy cảm → Chuyển HITL Ticket. | AI (LLM Judge) | n8n workflow |
| **TB6: Xử lý HITL Ticket & Reply** | **A + Người (HITL)** | Tin nhắn an toàn → Auto reply qua Chatbot UI. Tin nhắn nhạy cảm → Ghi Google Sheets Ticket cho CSKH xử lý. | AI + Người (CSKH) | App vibe coding + Sheets |

**Ký hiệu:** E — Eliminate · S — Simplify · I — Integrate · A — Automate

---

## 3. Quy tắc Vàng HITL (Human-in-the-loop)

- **BẮT BUỘC HITL** cho các trường hợp:
  1. Ý định thuộc nhóm `khieu_nai` (Khiếu nại chất lượng sản phẩm/dịch vụ).
  2. Ý định thuộc nhóm `hoan_tien` / Đổi trả phức tạp.
  3. Ý định ngoài phạm vi bán lẻ (`ngoai_pham_vi`).
  4. Điểm tin cậy từ LLM-as-Judge có `confidence < 0.7`.
- **Lý do:** Tuyệt đối không để AI tự động hứa hẹn bồi thường tài chính hoặc cam kết chính sách vượt thẩm quyền.
