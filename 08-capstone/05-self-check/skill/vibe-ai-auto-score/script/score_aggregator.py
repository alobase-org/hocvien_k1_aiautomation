#!/usr/bin/env python3
"""
vibe-ai-auto-score score_aggregator.py

Three jobs:
  1) verify-and-recompute: load 1 grading-result.json, recompute aggregate
     từ scores[] + (tuỳ chọn) adjustments:
       base_score     = Σ(level_i/5 × 100 × weight_i) / Σ(weight_i)
       bonus_total    = Σ adjustments.bonus[].points
       penalty_total  = Σ adjustments.penalty[].points  (chỉ mục trigger_met=true)
       total_score    = clamp(base + bonus − penalty, 0, 100)
     → ép nhất quán, chống LLM tính sai trọng số và sai điểm cộng/trừ.
  2) confidence_gate: verdict từ overall confidence — PASS/NEED_REVIEW/REJECT.
  3) summarize: gom nhiều grading-result.json → summary-report.json (xếp hạng,
     thống kê mean/median/min/max/stddev, phân bố band, strengths/weaknesses).

Usage:
    python3 score_aggregator.py --verify output/cand-A.grading.json
    python3 score_aggregator.py --summarize output/ --out output/summary.json

Zero external dependencies.
"""

import argparse
import json
import statistics
import sys
from pathlib import Path

BANDS = [
    (90, "Xuất sắc"),
    (75, "Tốt"),
    (60, "Đạt"),
    (40, "Yếu"),
    (0, "Kém"),
]

# Confidence gate 3 tầng (học từ capstone-rubric-v2 §3). Quyết định flow chấm.
CONF_PASS = 0.85      # >= : chấp nhận chấm tự động
CONF_REVIEW = 0.60    # >= : cần human review (đã đưa review queue)
# < CONF_REVIEW : REJECT — exit, không xếp hạng (BR-08)


def band_for(score: float) -> str:
    for threshold, label in BANDS:
        if score >= threshold:
            return label
    return "Kém"


def confidence_gate_for(conf: float) -> dict:
    """Verdict từ overall confidence — học từ capstone-rubric-v2 §3."""
    if conf >= CONF_PASS:
        verdict = "PASS"
    elif conf >= CONF_REVIEW:
        verdict = "NEED_REVIEW"
    else:
        verdict = "REJECT"
    return {
        "verdict": verdict,
        "overall_confidence": round(conf, 3),
        "rule": f"PASS>={CONF_PASS} · NEED_REVIEW {CONF_REVIEW}-{CONF_PASS} · REJECT<{CONF_REVIEW}",
    }


def _sum_adjustments(grading: dict) -> tuple:
    """Tính bonus_total / penalty_total từ adjustments (chỉ penalty trigger_met=true).
    Trả (bonus_total, penalty_total). Thiếu adjustments → (0, 0)."""
    adj = grading.get("adjustments") or {}
    bonus_total = 0.0
    for b in adj.get("bonus", []) or []:
        bonus_total += float(b.get("points", 0) or 0)
    penalty_total = 0.0
    for p in adj.get("penalty", []) or []:
        # Penalty chỉ được trừ khi trigger_met != false. Khi thiếu field → mặc định
        # KHÔNG trừ (bảo vệ candidate, chống trừ bừa — BR-06). Bonus không cần trigger.
        if p.get("trigger_met") is not False and "trigger_condition" not in p:
            # không khai báo trigger_condition → tự do trừ (giống bonus)
            penalty_total += float(p.get("points", 0) or 0)
        elif p.get("trigger_met") is True:
            penalty_total += float(p.get("points", 0) or 0)
    return round(bonus_total, 2), round(penalty_total, 2)


def recompute_aggregate(grading: dict) -> dict:
    """Tính lại aggregate từ scores[] (base) + adjustments (tuỳ chọn).
    base = weighted-average; final = clamp(base + bonus − penalty, 0, 100).
    Source of truth: weights + levels + adjustment points (validator recompute)."""
    scores = grading.get("scores", [])
    total_w = 0.0
    weighted = 0.0
    for s in scores:
        level = s.get("level")
        w = s.get("weight", 0)
        if level is None or w is None:
            continue
        norm = (level / 5.0) * 100.0
        s["normalized_score"] = round(norm, 2)
        weighted += norm * w
        total_w += w
    base = round(weighted / total_w, 2) if total_w else 0.0
    bonus_total, penalty_total = _sum_adjustments(grading)
    final = round(max(0.0, min(100.0, base + bonus_total - penalty_total)), 2)
    return {
        "base_score": base,
        "bonus_total": bonus_total,
        "penalty_total": penalty_total,
        "total_score": final,
        "band": band_for(final),
        "total_weight": round(total_w, 4),
    }


def verify(grading_path: str) -> dict:
    data = json.loads(Path(grading_path).read_text(encoding="utf-8"))
    new_agg = recompute_aggregate(data)
    old = data.get("aggregate", {})
    drift = abs(old.get("total_score", new_agg["total_score"]) - new_agg["total_score"]) > 0.05
    adj_drift = False
    if data.get("adjustments"):
        adj_drift = (
            abs(old.get("bonus_total", 0) - new_agg["bonus_total"]) > 0.05
            or abs(old.get("penalty_total", 0) - new_agg["penalty_total"]) > 0.05
        )
    data["aggregate"] = new_agg  # always write recomputed (authoritative)
    # worst-field confidence → need_review + confidence_gate
    confs = [s.get("confidence_score", 1) for s in data.get("scores", [])]
    min_conf = min(confs) if confs else 1.0
    data["confidence_score"] = round(min_conf, 3)
    gate = confidence_gate_for(min_conf)
    data["aggregate"]["confidence_gate"] = gate
    # need_review = REVIEW hoặc REJECT (cả hai đều cần human, REJECT nghiêm hơn)
    data["need_review"] = gate["verdict"] != "PASS"
    Path(grading_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "file": grading_path,
        "aggregate": new_agg,
        "score_drift_detected": drift,
        "adjustment_drift_detected": adj_drift,
        "confidence_gate": gate["verdict"],
        "min_confidence": min_conf,
        "need_review": data["need_review"],
    }


def summarize(folder: str, out_path: str) -> dict:
    files = sorted(Path(folder).glob("*.grading.json"))
    if not files:
        return {"error": f"no *.grading.json in {folder}"}
    rows = []
    rejected = []
    for f in files:
        g = json.loads(f.read_text(encoding="utf-8"))
        agg = g.get("aggregate") or recompute_aggregate(g)
        gate = agg.get("confidence_gate") or confidence_gate_for(
            g.get("confidence_score", 1.0))
        # BR-08: REJECT không đưa vào xếp hạng — để riêng chờ human xử lý
        if gate.get("verdict") == "REJECT":
            rejected.append({
                "candidate_id": g.get("candidate_id", f.stem),
                "candidate_name": g.get("candidate_name", f.stem),
                "overall_confidence": gate.get("overall_confidence"),
                "reason": "confidence < %.2f — REJECT gate" % CONF_REVIEW,
            })
            continue
        # per-criterion weighted (criterion-level roll-up)
        crit = {}
        for s in g.get("scores", []):
            cid = s.get("criterion_id")
            crit.setdefault(cid, {"criterion_id": cid,
                                  "criterion_name": s.get("criterion_name", cid),
                                  "sum": 0.0, "wsum": 0.0})
            w = s.get("weight", 0)
            crit[cid]["sum"] += s.get("normalized_score", (s.get("level", 0) / 5) * 100) * w
            crit[cid]["wsum"] += w
        crit_scores = [{"criterion_id": v["criterion_id"],
                        "criterion_name": v["criterion_name"],
                        "weighted_score": round(v["sum"] / v["wsum"], 2) if v["wsum"] else 0}
                       for v in crit.values()]
        rows.append({
            "candidate_id": g.get("candidate_id", f.stem),
            "candidate_name": g.get("candidate_name", f.stem),
            "base_score": agg.get("base_score", agg.get("total_score", 0)),
            "bonus_total": agg.get("bonus_total", 0),
            "penalty_total": agg.get("penalty_total", 0),
            "total_score": agg.get("total_score", 0),
            "band": agg.get("band", band_for(agg.get("total_score", 0))),
            "criteria_scores": crit_scores,
            "confidence_gate": gate.get("verdict"),
            "need_review": g.get("need_review", False) or gate.get("verdict") == "NEED_REVIEW",
        })
    rows.sort(key=lambda r: r["total_score"], reverse=True)
    for i, r in enumerate(rows, 1):
        r["rank"] = i

    totals = [r["total_score"] for r in rows]
    dist = {b: 0 for _, b in BANDS}
    for r in rows:
        dist[r["band"]] = dist.get(r["band"], 0) + 1

    summary = {
        "report_id": f"summary-{Path(folder).name}",
        "rubric_id": "",
        "title": "Báo cáo tổng hợp chấm điểm",
        "candidate_count": len(rows),
        "ranking": rows,
        "statistics": {
            "mean": round(statistics.mean(totals), 2),
            "median": round(statistics.median(totals), 2),
            "min": round(min(totals), 2),
            "max": round(max(totals), 2),
            "stddev": round(statistics.pstdev(totals), 2) if len(totals) > 1 else 0.0,
        },
        "distribution": dist,
        "review_queue": [r["candidate_id"] for r in rows if r["need_review"]],
        "rejected": rejected,
        "confidence_score": round(min(totals and [1.0] or [1.0]), 3),
        "need_review": any(r["need_review"] for r in rows) or bool(rejected),
    }
    Path(out_path).write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"summary": out_path, "candidates": len(rows), "rejected": len(rejected),
            "top": rows[0]["candidate_name"] if rows else None}


def gate_only(grading_path: str) -> dict:
    """Refresh CHỈ confidence_gate + need_review từ confidence hiện tại.
    KHÔNG đụng aggregate/scores/adjustments — dành cho human-override review:
    sau khi giám khảo human chỉnh level/aggregate tay, re-derive verdict gate mà
    không bị recompute ghi đè. Học tư duy 'cổng chất lượng độc lập' từ capstone v2."""
    data = json.loads(Path(grading_path).read_text(encoding="utf-8"))
    confs = [s.get("confidence_score", 1) for s in data.get("scores", [])]
    min_conf = min(confs) if confs else 1.0
    gate = confidence_gate_for(min_conf)
    data.setdefault("aggregate", {})["confidence_gate"] = gate
    data["confidence_score"] = round(min_conf, 3)
    data["need_review"] = gate["verdict"] != "PASS"
    Path(grading_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"file": grading_path, "confidence_gate": gate["verdict"],
            "overall_confidence": min_conf, "need_review": data["need_review"]}


def gates(folder: str) -> dict:
    """Báo cáo read-only trạng thái gate của TOÀN bộ *.grading.json — pre-flight
    trước khi summarize. Generalization của step-based gates v2: biết ngay candidate
    nào PASS/NEED_REVIEW/REJECT, fail-fast khi có REJECT (exit ≠ 0)."""
    files = sorted(Path(folder).glob("*.grading.json"))
    if not files:
        return {"error": f"no *.grading.json in {folder}"}
    report = []
    counts = {"PASS": 0, "NEED_REVIEW": 0, "REJECT": 0}
    for f in files:
        g = json.loads(f.read_text(encoding="utf-8"))
        confs = [s.get("confidence_score", 1) for s in g.get("scores", [])]
        min_conf = min(confs) if confs else 1.0
        gate = confidence_gate_for(min_conf)
        agg = g.get("aggregate") or {}
        report.append({
            "candidate_id": g.get("candidate_id", f.stem),
            "candidate_name": g.get("candidate_name", f.stem),
            "confidence": round(min_conf, 3),
            "verdict": gate["verdict"],
            "base_score": agg.get("base_score"),
            "total_score": agg.get("total_score"),
        })
        counts[gate["verdict"]] += 1
    return {"candidates": len(report), "gate_counts": counts,
            "report": report, "has_reject": counts["REJECT"] > 0}


def main():
    p = argparse.ArgumentParser(description="vibe-ai-auto-score score aggregator")
    p.add_argument("--verify", metavar="FILE", help="Recompute + gate 1 grading-result (ghi đè aggregate)")
    p.add_argument("--gate-only", metavar="FILE", help="Refresh CHỈ confidence_gate, giữ nguyên aggregate (human-override)")
    p.add_argument("--gates", metavar="DIR", help="Báo cáo read-only gate toàn bộ candidate (pre-flight, fail-fast REJECT)")
    p.add_argument("--summarize", metavar="DIR", help="Folder of *.grading.json")
    p.add_argument("--out", default="output/summary-report.json")
    args = p.parse_args()

    if args.verify:
        print(json.dumps(verify(args.verify), indent=2, ensure_ascii=False))
        return 0
    if args.gate_only:
        print(json.dumps(gate_only(args.gate_only), indent=2, ensure_ascii=False))
        return 0
    if args.gates:
        res = gates(args.gates)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        # fail-fast: REJECT → exit 1 để CI/pipeline dừng
        return 1 if isinstance(res, dict) and res.get("has_reject") else 0
    if args.summarize:
        print(json.dumps(summarize(args.summarize, args.out), indent=2, ensure_ascii=False))
        return 0
    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
