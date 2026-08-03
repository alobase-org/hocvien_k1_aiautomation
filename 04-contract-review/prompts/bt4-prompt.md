# Prompt Thực hành 4 — Evidence check + omission (Harness: Evidence verbatim)

> Tư duy mới: **Evidence verbatim** — code check evidence có thật trong hợp đồng → bắt clause AI bịa (hallucination) + omission. Thực hành 4/5.
> Input: `clauses.json` (Thực hành 3) + text `contract-redacted.md` + `checklist-rui-ro.md`. Output: `evidence-checked.json`.

## Code Python cho n8n Code node

```python
# Code node Thực hành 4 — Evidence verbatim check + omission detection
# Input: clauses.json (item.json['clauses']), contract_text, checklist 8 điều khoản bắt buộc

REQUIRED_CLAUSES = [
    "đối tượng", "giá trị", "thanh toán", "nghĩa vụ",
    "chấm dứt", "bảo mật", "tranh chấp", "pháp luật áp dụng"
]

for item in _input.all():
    clauses = item.json.get("clauses", [])
    contract = item.json.get("contract_redacted", "")
    hallucinations = []
    
    for c in clauses:
        quote = c.get("evidence", {}).get("verbatim_quote", "")
        # Flag hallucination nếu verbatim quote không có thật trong hợp đồng
        if quote and quote not in contract:
            hallucinations.append({
                "id": c.get("id"),
                "flag": "hallucination",
                "reason": "verbatim quote KHÔNG xuất hiện nguyên văn trong hợp đồng"
            })
            
    contract_lower = contract.lower()
    omissions = [kw for kw in REQUIRED_CLAUSES if kw not in contract_lower]
    
    item.json["evidence_checked"] = {
        "hallucinations": hallucinations,
        "omissions": omissions,
        "n_clauses": len(clauses)
    }

return _input.all()
```

**HV làm trong n8n:** thêm Code node sau Thực hành 3 → input clauses + contract_text → Execute → mở `evidence_checked`: có hallucination không? có omission không?

**SLI/SLO:** ≥1 hallucination HOẶC ≥1 omission (contract mẫu cài sẵn).

**Chaining**: `evidence-checked.json` → input Thực hành 5.
**Harness cốt lõi**: Evidence="có thật" — chống AI bịa điều khoản (kẻ thù chết người ở pháp lý).
