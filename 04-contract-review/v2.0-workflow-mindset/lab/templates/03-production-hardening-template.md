# Template — Kiến trúc Hybrid & Hardening cho Production

> Dùng cho BT3. Phân rã kiến trúc 3 trụ cột (n8n, AI Agent, Vibe-coded App) + 4 lớp phòng thủ Hardening.

## Tên quy trình: [điền]
## Ngày: [điền]

---

## 1. Kiến trúc Hybrid — Phân rã trách nhiệm

### 1.1 n8n (Điều phối xương sống)
| Bước | Chức năng n8n | Trigger / Node |
|------|---------------|----------------|
| | | |

### 1.2 AI Agent (Bộ não nhận thức)
| Bước | Chức năng AI Agent | Công cụ AI |
|------|---------------------|------------|
| | | |

### 1.3 Vibe-coded App (Giao diện HITL)
| Bước | Chức năng App | Loại UI |
|------|---------------|---------|
| | | |

---

## 2. Bảng Hardening — 4 lớp phòng thủ

| Bước to-be | Fallback branch | Execution log | Edge case | HITL (ai/khi nào) |
|------------|-----------------|---------------|-----------|---------------------|
| | | | | |

---

## 3. Compliance Note

- [Bước liên quan PII/tiền bạc → bắt buộc HITL]
- [Quy định bảo mật dữ liệu cần tuân thủ]

---

## 4. Luồng tích hợp giữa 3 trụ cột

```
[Mô tả luồng: n8n trigger → AI Agent xử lý → App hiển thị → Người duyệt → n8n thực thi]
```
