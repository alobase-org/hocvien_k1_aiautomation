#!/usr/bin/env python3
"""
vibe-ai-auto-score html_dashboard.py

Tạo dashboard HTML tương tác từ summary-report.json (+ thư mục *.grading.json
nếu muốn drill-down từng tiêu chí). Tự chứa 100% — CSS + JS inline, không CDN,
mở trực tiếp bằng trình duyệt.

Tính năng:
  - Bảng xếp hạng có thể sort theo từng cột
  - Bar chart điểm tổng (pure HTML/CSS)
  - Drill-down: click candidate → xem điểm từng tiêu chí con + evidence
  - Phân bố band + thống kê mean/median/min/max
  - Review queue highlight (need_review)

Usage:
    python3 html_dashboard.py --summary output/summary-report.json \
        --gradings output/ --out output/dashboard.html

Zero external dependencies.
"""

import argparse
import html
import json
from pathlib import Path


def _esc(s) -> str:
    return html.escape(str(s if s is not None else ""))


def build_dashboard(summary_path: str, gradings_dir: str | None, out_path: str) -> dict:
    summary = json.loads(Path(summary_path).read_text(encoding="utf-8"))
    gradings: dict[str, dict] = {}
    if gradings_dir:
        for f in Path(gradings_dir).glob("*.grading.json"):
            g = json.loads(f.read_text(encoding="utf-8"))
            gradings[g.get("candidate_id", f.stem)] = g

    stats = summary.get("statistics", {})
    dist = summary.get("distribution", {})
    ranking = summary.get("ranking", [])

    # build per-criterion detail JSON for drill-down
    detail = {}
    for cid, g in gradings.items():
        items = []
        for s in g.get("scores", []):
            items.append({
                "criterion": s.get("criterion_name", ""),
                "subcriterion": s.get("name", ""),
                "level": s.get("level"),
                "label": s.get("level_label", ""),
                "score": s.get("normalized_score", 0),
                "weight": s.get("weight", 0),
                "confidence": s.get("confidence_score", 1),
                "rationale": s.get("rationale", ""),
                "evidence": [e.get("verbatim_quote", "") for e in s.get("evidence", [])],
                "used_research": s.get("used_research", False),
            })
        detail[cid] = {
            "name": g.get("candidate_name", cid),
            "aggregate": g.get("aggregate", {}),
            "strengths": g.get("strengths", []),
            "weaknesses": g.get("weaknesses", []),
            "items": items,
            "need_review": g.get("need_review", False),
        }

    detail_json = json.dumps(detail, ensure_ascii=False)
    ranking_json = json.dumps(ranking, ensure_ascii=False)
    summary_json = json.dumps(summary, ensure_ascii=False)

    rows_html = []
    for r in ranking:
        flag = ' ⚠️<span class="rev">cần review</span>' if r.get("need_review") else ""
        bar = f'<div class="bar" style="width:{r["total_score"]}%"></div>'
        rows_html.append(
            f'<tr data-cid="{_esc(r["candidate_id"])}" class="row">'
            f'<td>{r["rank"]}</td>'
            f'<td class="name">{_esc(r["candidate_name"])}{flag}</td>'
            f'<td class="score">{r["total_score"]:.1f}</td>'
            f'<td><span class="band {_esc(r["band"])}">{_esc(r["band"])}</span></td>'
            f'<td class="barcell">{bar}</td></tr>'
        )

    dist_html = "".join(
        f'<div class="distrow"><span class="distlabel {_esc(k)}">{_esc(k)}</span>'
        f'<span class="distval">{v}</span></div>'
        for k, v in dist.items() if v
    )

    doc = f"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8">
<title>{_esc(summary.get("title", "Dashboard chấm điểm"))}</title>
<style>
:root{{--bg:#0f1419;--card:#1a2029;--ink:#e6e6e6;--muted:#8a93a3;--accent:#4f9cf9;--good:#2ecc71;--warn:#f1c40f;--bad:#e74c3c}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--ink);padding:24px}}
h1{{font-size:22px;margin:0 0 4px}} .sub{{color:var(--muted);font-size:13px;margin-bottom:20px}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px}}
.card{{background:var(--card);border-radius:12px;padding:16px}}
.card .k{{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.05em}}
.card .v{{font-size:26px;font-weight:600;margin-top:6px}}
table{{width:100%;border-collapse:collapse;background:var(--card);border-radius:12px;overflow:hidden}}
th,td{{padding:11px 14px;text-align:left;border-bottom:1px solid #252d39;font-size:14px}}
th{{color:var(--muted);font-size:11px;text-transform:uppercase;cursor:pointer;user-select:none}}
th:hover{{color:var(--accent)}} .row{{cursor:pointer}} .row:hover{{background:#222a36}}
.name{{font-weight:500}} .score{{font-weight:600;color:var(--accent)}}
.band{{padding:2px 10px;border-radius:999px;font-size:12px;font-weight:500}}
.Xuất{{background:#1e3a2c;color:#2ecc71}} .Tốt{{background:#23324a;color:#4f9cf9}}
.Đạt{{background:#3a3220;color:#f1c40f}} .Yếu{{background:#3a2420;color:#e67e22}} .Kém{{background:#3a2020;color:#e74c3c}}
.barcell{{width:30%}} .bar{{height:8px;border-radius:4px;background:linear-gradient(90deg,var(--accent),#7ab8ff)}}
.rev{{color:var(--warn);font-size:11px}}
.two{{display:grid;grid-template-columns:1.4fr 1fr;gap:16px}}
.distrow{{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #252d39;font-size:13px}}
.distlabel{{font-weight:500}} .distval{{color:var(--accent)}}
#detail{{background:var(--card);border-radius:12px;padding:18px;margin-top:16px;display:none}}
#detail h2{{margin:0 0 4px;font-size:17px}} #detail .agg{{color:var(--accent);font-weight:600}}
.sw{{font-size:13px;margin:6px 0}} .sw b{{color:var(--muted)}}
.item{{border-top:1px solid #252d39;padding:10px 0;font-size:13px}}
.item .lvl{{display:inline-block;width:38px;text-align:center;border-radius:4px;padding:1px 0;font-weight:600}}
.evidence{{color:var(--muted);font-style:italic;border-left:2px solid #2a3543;padding-left:8px;margin:4px 0;font-size:12px}}
.research{{color:#b388ff;font-size:11px}}
</style></head><body>
<h1>{_esc(summary.get("title","Dashboard chấm điểm"))}</h1>
<div class="sub">{summary.get("candidate_count",0)} candidate · {_esc(summary.get("rubric_id",""))} · mean {stats.get("mean",0):.1f}/100</div>
<div class="grid">
 <div class="card"><div class="k">Mean</div><div class="v">{stats.get("mean",0):.1f}</div></div>
 <div class="card"><div class="k">Median</div><div class="v">{stats.get("median",0):.1f}</div></div>
 <div class="card"><div class="k">Min / Max</div><div class="v">{stats.get("min",0):.0f} / {stats.get("max",0):.0f}</div></div>
 <div class="card"><div class="k">Stddev</div><div class="v">{stats.get("stddev",0):.1f}</div></div>
</div>
<div class="two">
 <div>
  <table id="tbl"><thead><tr>
   <th data-k="rank">#</th><th data-k="name" class="name">Candidate</th>
   <th data-k="score">Điểm</th><th data-k="band">Band</th><th>Phân bố</th>
  </tr></thead><tbody>{''.join(rows_html)}</tbody></table>
  <div id="detail"></div>
 </div>
 <div class="card"><div class="k" style="margin-bottom:8px">Phân bố band</div>{dist_html}
  <div style="margin-top:14px"><div class="k">Điểm mạnh chung</div>
   {''.join(f'<div class="sw">• {_esc(s)}</div>' for s in summary.get("top_strengths",[]))}</div>
  <div><div class="k">Điểm yếu chung</div>
   {''.join(f'<div class="sw">• {_esc(s)}</div>' for s in summary.get("common_weaknesses",[]))}</div>
  <div><div class="k">Đề xuất</div>
   {''.join(f'<div class="sw">• {_esc(s)}</div>' for s in summary.get("recommendations",[]))}</div>
 </div>
</div>
<script>
const DETAIL={detail_json};
const RANKING={ranking_json};
const bandColor={{'5':'#1e3a2c','4':'#23324a','3':'#3a3220','2':'#3a2420','1':'#3a2020'}};
document.querySelectorAll('.row').forEach(r=>r.onclick=()=>{{
 const d=DETAIL[r.dataset.cid]; if(!d)return; const box=document.getElementById('detail');
 box.style.display='block';
 let items=(d.items||[]).map(i=>`<div class="item"><span class="lvl" style="background:${{bandColor[i.level]||'#333'}}">${{i.level}}</span> <b>${{i.criterion}}</b> · ${{i.subcriterion}} (${{i.score.toFixed(1)}}/100, trọng số ${{i.weight}})${{i.used_research?' <span class="research">🔬 đã dùng research</span>':''}}<div>${{i.rationale}}</div>${{(i.evidence||[]).map(e=>`<div class="evidence">“${{e}}”</div>`).join('')}}</div>`).join('');
 box.innerHTML=`<h2>${{d.name}}</h2><div class="agg">Tổng: ${{d.aggregate.total_score}}/100 · ${{d.aggregate.band}}</div>`+
  `<div class="sw"><b>Điểm mạnh:</b> ${{(d.strengths||[]).join('; ')||'—'}}</div>`+
  `<div class="sw"><b>Điểm yếu:</b> ${{(d.weaknesses||[]).join('; ')||'—'}}</div>`+items;
}});
// sort
document.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{{
 const k=th.dataset.k; const tbody=document.querySelector('#tbl tbody');
 let rows=[...tbody.querySelectorAll('tr')];
 rows.sort((a,b)=>{{
   const ka=a.children[k==='rank'?0:k==='name'?1:k==='score'?2:3].textContent;
   const kb=b.children[k==='rank'?0:k==='name'?1:k==='score'?2:3].textContent;
   if(k==='name')return ka.localeCompare(kb);
   return parseFloat(kb)-parseFloat(ka);
 }});
 rows.forEach(r=>tbody.appendChild(r));
}});
</script></body></html>"""
    Path(out_path).write_text(doc, encoding="utf-8")
    return {"out": out_path, "candidates": len(ranking), "with_detail": len(gradings)}


def main():
    p = argparse.ArgumentParser(description="vibe-ai-auto-score HTML dashboard")
    p.add_argument("--summary", required=True)
    p.add_argument("--gradings", help="folder of *.grading.json for drill-down")
    p.add_argument("--out", default="output/dashboard.html")
    args = p.parse_args()
    print(json.dumps(build_dashboard(args.summary, args.gradings, args.out), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
