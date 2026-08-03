# Prompt Thực hành 5 — Harness gộp + report + HITL (capstone)

> Tư duy mới: **Pipeline + Determinism** — gộp Thực hành 1-4 thành 1 n8n workflow end-to-end. Thực hành 5/5.
> Input: 4 artifact Thực hành 1-4 + contract holdout (GV phát). Output: `report.docx` / `report.xlsx` + section HITL.

## Workflow n8n gộp (HV nối)

```
Manual Trigger
   → Code node Redact (Thực hành 2) ── contract-redacted
      → AI node Extract (Thực hành 3) ── clauses.json
         → Code node Schema validate ── IF fail → loop AI (max 2)
            → Code node Evidence+omission check (Thực hành 4)
               → Code node Tổng hợp report (Thực hành 5)
                  → Write file report.docx / report.xlsx
```

## Code node Tổng hợp (sinh report + score + approved)

> Pattern tham khảo Viettel code-review-bot: **score 0-100 + approved flag** cho HITL; **severity emoji 🔴/🟡/💡/❓**.

```python
# Code node Thực hành 5 — tổng hợp report + Contract Score + approved
SEV = {"HIGH": "🔴", "MED": "🟡", "SUGGEST": "💡", "CLARIFY": "❓"}

for item in _input.all():
    ec = item.json.get("evidence_checked", {})
    clauses = item.json.get("clauses", [])
    rows = []
    n_high = n_med = 0
    
    for c in clauses:
        is_hallu = any(h["id"] == c.get("id") for h in ec.get("hallucinations", []))
        flag = "hallucination" if is_hallu else ""
        sev = c.get("severity", "MED")
        if sev == "HIGH":
            n_high += 1
        elif sev == "MED":
            n_med += 1
            
        rows.append({
            "clause_id": c.get("id"),
            "tieu_de": c.get("tieu_de"),
            "severity": SEV.get(sev, "🟡") + " " + sev,
            "blocking": sev == "HIGH",
            "evidence": c.get("evidence", {}).get("verbatim_quote", ""),
            "flag": flag,
            "suggestion": c.get("de_xuat", "Cần điều chỉnh quy định rõ ràng hơn"),
            "confidence": c.get("confidence_score", 0.95)
        })
        
    n_hallu = len(ec.get("hallucinations", []))
    n_omit = len(ec.get("omissions", []))
    
    # Công thức tính điểm Contract Score (pattern Viettel code-review)
    score = max(0, 100 - n_high * 15 - n_med * 5 - n_hallu * 20 - n_omit * 10)
    approved = (score >= 70 and n_hallu == 0)
    
    item.json["report"] = {
        "tong_hop": {
            "contract_score": score,
            "approved_recommendation": approved,
            "n_clauses": ec.get("n_clauses", len(clauses)),
            "n_high": n_high,
            "n_med": n_med,
            "n_hallucination": n_hallu,
            "omissions": ec.get("omissions", [])
        },
        "chi_tiet": rows,
        "hitl": {
            "nguoi_duyet": "",
            "ngay": "",
            "quyet_dinh": "CHỜ PHÁP CHẾ DUYỆT (HITL)"
        }
    }

return _input.all()
```

## Nghiệm thu (SLI/SLO)
- Workflow chạy end-to-end 1 click trên contract holdout.
- Báo cáo Thẩm định `report.docx` / `report.xlsx`: sheet/mục "Tóm tắt" (số hallucination/omission) + "Chi tiết" (clause, evidence, flag) + section **"Người duyệt + ngày + quyết định"**.
- HV đóng Pháp chế → điền quyết định "duyệt / yêu cầu sửa" + lý do.

**Safety/HITL (CRITICAL)**: Quyết định "duyệt hợp đồng" LUÔN thuộc human. Workflow chỉ đề xuất + flag.
