# Deep-Research cho tiêu chí khó — Hướng dẫn lưu trữ

Tham chiếu cho Phase 4 (optional). Mục tiêu: chấm tiêu chí khó bằng FACT đã verify, không bằng cảm tính.

## 1. Khi nào chạy research

Chỉ khi rubric có tiêu chí con `needs_research=true`. Đó là các tiêu chí mà giám khảo thông thường
không chắc kiến thức chuyên môn cần thiết:
- "Đúng chuẩn luật/quy định" (luật VN, NĐ, ISO...)
- "Đúng best-practice kiến trúc/ngành"
- "So với benchmark ngành"
- "Có bị lỗi bảo mật phổ biến X không"

## 2. Quy trình

```
Cho mỗi tiêu chí con needs_research=true:
  ↓
1. Lấy research_query từ rubric (hoặc tinh chỉnh cho cụ thể)
  ↓
2. Invoke skill deep-research với câu hỏi đó
  ↓
3. LƯU kết quả: output/research/<subcriterion-id>.md
     - Phải có citation nguồn (URL, tên tài liệu)
     - Phải có phần "Tiêu chuẩn/điều kiện để đạt mỗi mức 1-5" (áp vào rubric)
  ↓
4. Khi chấm (Phase 5): đối chiếu candidate với research
     - used_research = true
     - research_source = output/research/<id>.md
     - evidence có thể trỏ sang research (xem kb/evidence-rules.md mục 5)
```

## 3. Format file research lưu trữ

```markdown
# Research: <tên tiêu chí con>

**Subcriterion ID:** SEC-01
**Research query:** Định nghĩa "tuân thủ bảo mật cơ bản" cho ứng dụng web năm 2026?

## Fact / Tiêu chuẩn tham chiếu
- Fact 1: ... [source: OWASP Top 10 2025, URL]
- Fact 2: ... [source: ...]

## Áp vào rubric (điều kiện đạt mỗi mức)
- 5: ...
- 4: ...
- 3: ...
- 2: ...
- 1: ...

## Nguồn
1. ...
2. ...
```

## 4. Tại sao phải lưu trữ

- **Audit:** nếu ai hỏi "sao chấm mức 3?", có research file để truy vết.
- **Tái dùng:** cùng rubric chấm nhiều đợt → không cần research lại.
- **Chống drift:** fact cố định, không phụ thuộc "nhớ" của LLM ở lần chấm sau.

## 5. Anti-patterns

- ❌ Chạy research nhưng không lưu file → mất tham chiếu, không audit được
- ❌ Dùng research không có citation → fact không verify được → thành hallucination khác
- ❌ Áp research mơ hồ (không dịch ra điều kiện từng mức) → vẫn chấm cảm tính
