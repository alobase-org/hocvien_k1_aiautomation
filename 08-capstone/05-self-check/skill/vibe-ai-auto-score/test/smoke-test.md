# Smoke Test — vibe-ai-auto-score (~5 phút)

Chạy sau mỗi lần update skill. Kiểm scripts + schema chạy được end-to-end trên synthetic data.
(Synthetic data ở đây là mẫu generic; khi chạy thật, rubric được sinh từ folder buổi dạy và chấm nương tay.)

## Setup
```bash
cd ~/.claude/skills/vibe-ai-auto-score
cp synthetic-data/sample-rubric.json output/rubric.json
cp synthetic-data/sample-candidate-unified.json output/candidates/team-alpha.unified.json
cp synthetic-data/sample-grading.json output/candidates/team-alpha.grading.json
```

## 1. Validator
```bash
python3 script/validator.py --run-all --artifact output/rubric.json --schema schema/rubric.schema.json --source synthetic-data/source-alpha.txt
# → ok: true
python3 script/validator.py --run-all --artifact output/candidates/team-alpha.unified.json \
  --schema schema/candidate-unified.schema.json --source synthetic-data/source-alpha.txt
# → evidence.missing_count: 0
```

## 2. Aggregator
```bash
python3 script/score_aggregator.py --verify output/candidates/team-alpha.grading.json
# → aggregate.total_score, score_drift_detected: false
python3 script/score_aggregator.py --summarize output/candidates/ --out output/summary-report.json
# → candidates: 1
```

## 2b. Adjustments + confidence gate (v2 — học từ cham_bai_capstone_v2)
```bash
cp synthetic-data/sample-grading-with-adjustments.json output/candidates/team-beta.grading.json
python3 script/score_aggregator.py --verify output/candidates/team-beta.grading.json
# Kỳ vọng:
#   base_score: 60.0          (weighted-average của 3 tiêu chí)
#   bonus_total: 8.0          (E1)
#   penalty_total: 6.0        (chỉ S1, trigger_met=true; S2 bị BỎ QUA vì trigger_met=false)
#   total_score: 62.0         (60 + 8 − 6)
#   confidence_gate.verdict: PASS (overall 0.9 ≥ 0.85)
#   adjustment_drift_detected: false
python3 script/validator.py --run-all --artifact output/candidates/team-beta.grading.json \
  --schema schema/grading-result.schema.json --source synthetic-data/source-alpha.txt
# → evidence.missing_count: 0
```

## 2c. REJECT gate (negative test — candidate bị loại khỏi ranking)
```bash
# Ép confidence thấp → gate REJECT → summarize phải tách ra rejected[]
python3 -c "import json; d=json.load(open('output/candidates/team-beta.grading.json')); [s.update({'confidence_score':0.45}) for s in d['scores']]; json.dump(d,open('output/candidates/team-beta.grading.json','w'),ensure_ascii=False,indent=2)"
python3 script/score_aggregator.py --verify output/candidates/team-beta.grading.json
# → confidence_gate.verdict: REJECT, need_review: true
python3 script/score_aggregator.py --summarize output/candidates/ --out output/summary-report.json
# → ranked (team-alpha) + rejected: 1 (team-beta)  ← REJECT KHÔNG vào xếp hạng (BR-08)
```

## 2d. Pre-flight gates + human-override gate-only (v2.1)
```bash
# Pre-flight: báo cáo read-only verdict của toàn bộ candidate, fail-fast khi có REJECT
python3 script/score_aggregator.py --gates output/candidates/
# → gate_counts {PASS, NEED_REVIEW, REJECT}; has_reject:true → exit code 1
echo "exit=$?"  # 1 nếu có REJECT, 0 nếu tất cả ≥ NEED_REVIEW threshold

# Human-override: human đã review xong team-beta, bump confidence rồi refresh CHỈ gate
python3 -c "import json; d=json.load(open('output/candidates/team-beta.grading.json')); [s.update({'confidence_score':0.9}) for s in d['scores']]; json.dump(d,open('output/candidates/team-beta.grading.json','w'),ensure_ascii=False,indent=2)"
python3 script/score_aggregator.py --gate-only output/candidates/team-beta.grading.json
# Kỳ vọng:
#   confidence_gate.verdict: REJECT → PASS
#   aggregate.total_score KHÔNG đổi (gate-only không recompute aggregate)
python3 -c "import json; a=json.load(open('output/candidates/team-beta.grading.json'))['aggregate']; print('total',a['total_score'],'gate',a['confidence_gate']['verdict'])"
# → total 62.0 gate PASS
```

## 3. HTML dashboard
```bash
python3 script/html_dashboard.py --summary output/summary-report.json \
  --gradings output/candidates/ --out output/dashboard.html
# → mở output/dashboard.html bằng trình duyệt, thấy 1 hàng + drill-down
```

## 4. Anti-hallucination check (negative test)
```bash
# Tạo candidate có evidence bịa → phải báo missing
python3 -c "import json,sys; d=json.load(open('output/candidates/team-alpha.unified.json')); d['fields'][0]['evidence'][0]['verbatim_quote']='CÂU BỊA KHÔNG CÓ TRONG FILE'; json.dump(d,open('output/bad.unified.json','w'),ensure_ascii=False,indent=2)"
python3 script/validator.py --run-all --artifact output/bad.unified.json \
  --schema schema/candidate-unified.schema.json --source synthetic-data/source-alpha.txt
# → evidence.missing_count ≥ 1, confidence giảm, need_review có thể true
```

**Pass criteria:** tất cả trả `ok`/0 missing ở bước positive; bước 4 báo missing.
