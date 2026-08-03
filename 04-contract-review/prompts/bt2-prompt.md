# Prompt Thực hành 2 — Redaction 4 cấp (Code node Python trong n8n)

> Tư duy mới: **Redaction** (tham khảo CCHC `vibe-cchc-orchestrator/kb/bao-mat-ktnn.md`). Che PII trước khi qua AI.
> Thực hành 2/5 — Redaction. Input: contract text. Output: `contract-redacted.md`.

## Code Python cho n8n Code node

```python
# Code node Thực hành 2 — Redact 4 cấp trước khi qua AI
import re

def redact(text):
    # Cấp 1 — PII Email
    text = re.sub(r'[\w.+-]+@[\w-]+\.\w+', '[email redact]', text)
    
    # Cấp 2 — Mã số thuế (MST)
    text = re.sub(r'(?i)(Mã số thuế:\s*)\d{10}', r'\1[MST redact]', text)
    
    # Cấp 1 — PII SĐT
    text = re.sub(r'\b0\d{9,10}\b', '0xxx', text)
    
    # Cấp 2 — Giá trị tài chính
    text = re.sub(r'\b\d{1,3}(?:[.,]\d{3})+(?:\s*(?:VNĐ|VND|đồng))?\b', '[giá trị redact]', text)
    
    # Cấp 3 — Nhạy cảm đối tác đại diện
    text = re.sub(r'Nguyễn Văn An', 'Đại diện Bên A', text)
    text = re.sub(r'Trần Thị Bình', 'Đại diện Bên B', text)

    # Cấp 4 — Gate Tối mật
    for kw in ['tối mật', 'bí mật nhà nước']:
        if kw in text.lower():
            raise Exception(f'CẤP 4 "{kw}" → STOP workflow, cần xử lý AI Local')
            
    return text

for item in _input.all():
    raw = item.json.get('contract_text', '')
    item.json['contract_redacted'] = redact(raw)

return _input.all()
```

**HV làm trong n8n:** Manual Trigger → Code node (dán code trên, input contract_text) → Execute → lấy `contract_redacted` → lưu `contract-redacted.md`.

**Chaining**: `contract-redacted.md` → input AI node Thực hành 3.
**Safety (CRITICAL)**: cổng "redact trước AI" (CCHC). Cấp 4 = gate STOP.
