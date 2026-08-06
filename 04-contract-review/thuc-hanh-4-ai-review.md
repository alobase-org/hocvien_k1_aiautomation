# Hướng dẫn Thực hành 4 — AI Policy Review & Evidence/Omission Check (Harness: KB Policy + Verbatim Quote) (15')

> **Thuộc bài lab**: [Buổi 04: Thẩm định hợp đồng tự động](./lab.md)  
> **Tư duy trọng tâm**: **Knowledge Base Policy Check & Anti-Hallucination** — Đối chiếu điều khoản bóc tách với Kho tri thức Red Flags dạng Markdown (`checklist-rui-ro.md`) và dùng Code Node xác minh trích dẫn nguyên văn (`verbatim_quote`) để bắt triệt để AI bịa thông tin (*hallucination*) và điều khoản bị bỏ sót (*omission*).

---

## 🎯 Mục tiêu bài thực hành
- Vận hành Node `TH3 - Evidence + Omission (semantics)` thực hiện:
  - **Verbatim Quote Evidence Check**: Đối chiếu trích dẫn của AI với văn bản hợp đồng gốc (`contract_original` / `contract_text`), nếu trích dẫn không có thật ➡️ tạo cờ `hallucination`.
  - **Omission Check**: Quét 11 nhóm điều khoản bắt buộc TC01 - TC12 (đối tượng, thanh toán, nghĩa vụ, thời hạn, chấm dứt, bảo mật, IP, bồi thường, bất khả kháng, phạt vi phạm, tranh chấp) ➡️ phát hiện điều khoản bị thiếu trong hợp đồng.
- Vận hành Node `TH4 - Policy Review vs KB Red Flags` đối chiếu với Kho tri thức Red Flags (`templates/checklist-rui-ro.md`):
  - Áp dụng 12 quy tắc rủi ro KB_RULES (phát sinh chi phí, mốc thanh toán cảm tính, nghĩa vụ độc quyền, tiến độ đóng đinh, đơn phương chấm dứt/gia hạn, bảo mật vô thời hạn, cướp IP trước thanh toán, bồi thường không giới hạn, tự động gia hạn, bất khả kháng hẹp, phạt vượt 8%, tòa án bất lợi).
  - Tự động gán mức Severity (🔴 HIGH / 🟡 MED / 💡 LOW) và sinh gợi ý chỉnh sửa đối ứng (Redline).

---

## 📥 Input → ⚙️ Action → 📤 Output

- **Input**: Mảng `clauses` từ Thực hành 3 + văn bản hợp đồng gốc + Kho tri thức Red Flags ([templates/checklist-rui-ro.md](./templates/checklist-rui-ro.md)).
- **Action**: 
  1. **Evidence & Omission Check (Node TH3)**:
     - Kiểm tra chuỗi `verbatim_quote` có xuất hiện trong `contract_original` hay không. Nếu không ➡️ push vào `hallucinations`.
     - Strip dấu tiếng Việt và test 11 regex group bắt buộc ➡️ tạo mảng `omissions` chứa các nhóm điều khoản bị thiếu.
  2. **Policy Review vs KB Red Flags (Node TH4)**:
     - Duyệt từng điều khoản qua 12 bộ quy tắc `KB_RULES`.
     - Nếu khớp từ khóa bẫy ➡️ gán `red_flags`, nâng severity lên HIGH/MED và điền nội dung `redline` đề xuất khắc phục.
- **Output**: Mảng `clauses_reviewed`, `red_flags` và đối tượng `evidence_checked` chứa danh sách hallucinations và omissions.

---

## 🛠️ Công cụ & Tài nguyên
- **Tool chính**: n8n Nodes: `TH3 - Evidence + Omission (semantics)` & `TH4 - Policy Review vs KB Red Flags`.
- **Kho tri thức Red Flags**: [templates/checklist-rui-ro.md](./templates/checklist-rui-ro.md).
- **Jupyter Demo Notebook**: Step 5 trong [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb).

---

## 📊 Tiêu chuẩn Nghiệm thu (SLI/SLO)
- [ ] 100% điều khoản được rà soát rủi ro và gán mức Severity (🔴 HIGH / 🟡 MED / 💡 LOW) kèm đề xuất Redline.
- [ ] Phát hiện chính xác các bẫy Red Flag trong hợp đồng mẫu:
  - Bẫy đơn phương gia hạn một chiều (HD05 ➡️ TC05 - HIGH)
  - Bẫy bồi thường thiệt hại vô hạn/gián tiếp (HD06 ➡️ TC08 - HIGH)
  - Bẫy mốc thanh toán cảm tính "hài lòng" (HD03 ➡️ TC02 - HIGH)
- [ ] Bắt được điều khoản bị bỏ sót: **TC05 - Chấm dứt & Hậu quả chấm dứt** (mẫu hợp đồng dịch vụ cố ý không có điều khoản chấm dứt).

---

## ⏱️ Các bước thực hiện (Time-box 15')

1. **Bước 1 (3') — Khám phá Node Evidence & Omission Check (TH3)**:
   - Mở n8n Canvas UI, xem mã nguồn node **"TH3 - Evidence + Omission (semantics)"**.
   - Quan sát logic `REQUIRED_GROUPS` gồm 11 tiêu chuẩn bắt buộc và hàm check `contract.includes(quote)`.

2. **Bước 2 (4') — Khám phá Node Policy Review vs KB Red Flags (TH4)**:
   - Mở node **"TH4 - Policy Review vs KB Red Flags"**.
   - Quan sát 12 quy tắc `KB_RULES` được chuyển đổi trực tiếp từ file Kho tri thức [checklist-rui-ro.md](./templates/checklist-rui-ro.md).

3. **Bước 3 (5') — Trải nghiệm qua Jupyter Notebook Step 5**:
   - Mở notebook [`test/04_contract_review_lab_demo.ipynb`](file:///Users/shimazu/Documents/9.%20active/alobase/course_ai_automation/giao_trinh/giang-day/05-thuc-hanh/04-contract-review/test/04_contract_review_lab_demo.ipynb).
   - Chạy **Step 5: Policy Review vs Kho Tri Thức Red Flag & Evidence/Omission Check trên n8n**.
   - Xác nhận log inspect node đọc thành công từ n8n API.

4. **Bước 4 (3') — Đánh giá Kết quả Cảnh báo**:
   - Kiểm tra mảng `red_flags` phát hiện các điều khoản rủi ro HIGH (HD03, HD05, HD06) và mảng `omissions` phát hiện thiếu nhóm Chấm dứt.
   - Sẵn sàng chuyển dữ liệu sang bài **Thực hành 5**.

---

## 🔒 Nguyên tắc Safety & Control
> **Rule: Không Evidence ➡️ Không Tin**: AI trong ngành pháp lý chỉ có giá trị khi trích dẫn chính xác nguyên văn từng từ. Mọi trích dẫn sai khác văn bản gốc đều bị cảnh báo cờ Hallucination ngay lập tức.

---

## 🆘 Hướng dẫn khi bị kẹt (Stuck > 8')
- Xem cấu hình chi tiết các node TH3 & TH4 trong file workflow giải pháp: [checkpoints/n8n-contract-review-solution.json](./checkpoints/n8n-contract-review-solution.json).
