# Pha 1: Ma trận Ưu tiên Use-case CSKH (Impact x Difficulty Matrix)

> **Mục tiêu:** Đánh giá các use-case tiềm năng trong bộ phận CSKH & Vận hành bán lẻ để chọn Quick Win có Tác động cao + Độ phức tạp thấp đến trung bình.

---

## 1. Bảng đánh giá Use-case

| STT | Tên Use-case | Tác động (Impact: 1-5) | Độ phức tạp (Complexity: 1-5) | Phân loại | Ghi chú & Rủi ro |
|---|---|---|---|---|---|
| **UC1** | **CSKH Bot đa tầng (Guardrail + FAQ Cache + Judge + HITL)** | **5** | **2** | **Quick Win (Top 1)** | Giải quyết 70-80% câu hỏi lặp lại; an toàn tuyệt đối nhờ 2-layer LLM & HITL gate. |
| UC2 | Tự động xử lý hoàn tiền & hủy đơn tự động | 4 | 5 | Dài hạn (Complex) | Rủi ro gian lận tài chính cao, cần tích hợp Core ERP/Banking API. |
| UC3 | Tự động phân loại email khiếu nại chất lượng sản phẩm | 3 | 3 | Cân nhắc (Fill-in) | Khối lượng email không quá lớn, có thể xử lý bán tự động. |
| UC4 | Bot tra cứu mã vận đơn & trạng thái đơn hàng real-time | 4 | 3 | Quick Win (Top 2) | Cần kết nối API đơn vị vận chuyển (GHTK/GHN). |
| UC5 | Tự động tổng hợp báo cáo hài lòng khách hàng (NPS/CSAT) | 3 | 2 | Phụ trợ (Fill-in) | Dễ làm nhưng giá trị trực tiếp cho CSKH hàng ngày thấp hơn UC1. |

---

## 2. Ma trận Trực quan (Tác động vs Độ phức tạp)

```
        TÁC ĐỘNG (IMPACT)
          ▲
        5 │  [UC1: CSKH Bot Đa Tầng] ⭐      [UC2: Hoàn tiền tự động]
          │  (Quick Win - Ưu tiên số 1)     (High Complexity)
        4 │  [UC4: Tra cứu Vận đơn]
        3 │  [UC5: Báo cáo CSAT]             [UC3: Phân loại Email]
        2 │
        1 │
          └─────────────────────────────────────────────────────► ĐỘ PHỨC TẠP
             1         2         3         4         5 (COMPLEXITY)
```

---

## 3. Khuyến nghị Chọn Use-case cho Dự án Automation

**Lựa chọn chính:** **UC1 — CSKH Bot đa tầng với Semantic Search, FAQ Cache Fast Path & LLM-as-Judge**.
- **Lý do chọn:**
  1. **Giá trị cao:** Giải phóng 2 nhân sự CSKH khỏi các câu hỏi trùng lặp về phí ship, chính sách đổi trả, bảo hành.
  2. **Độ tin cậy cao (Zero Hallucination):** Kiến trúc bám kho tri thức (`faq-cskh.md` + `chinh-sach-ho-tro.md`), kết hợp Fast Path Cache không qua LLM.
  3. **Kiểm soát rủi ro:** Phân định rõ câu hỏi an toàn (trả lời tự động) vs câu hỏi nhạy cảm/hoàn tiền (HITL Ticket).
