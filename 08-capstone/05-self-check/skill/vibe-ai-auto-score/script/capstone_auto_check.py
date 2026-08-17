#!/usr/bin/env python3
"""
Capstone Auto-Check — kiểm tra tự động package đồ án B8 (AI Automation K1)

Kiểm deterministic (không LLM):
  [1] Cấu trúc package (đủ file theo package-structure)
  [2] Brief 7 mục + tiêu chí đo được (heuristic)
  [3] Workflow n8n JSON: đồ thị node/connection nguyên vẹn (không key/target mồ côi)
  [4] run-log: ≥2 vòng, ≥1 vòng FAIL, có evidence
  [5] pitch.html: mở được, đủ 6 slide, không còn placeholder
  [6] RUNTIME (chỉ khi n8n local đang chạy): import workflow + chạy 1 input
      qua webhook + đọc kết quả execution — đúng bước GV phải làm tay.

Cách dùng:
  python3 capstone_auto_check.py <thư-mục-package-học-viên> [--input "tin nhắn test"]
                                 [--n8n-url http://localhost:5678]
                                 [--email admin@alobase.vn] [--password Password123!]

Nếu n8n chưa chạy: các check [1]-[5] vẫn chạy; [6] báo SKIP kèm hướng dẫn khởi động.
Pattern n8n REST API mượn từ B4: 04-contract-review/test/interactive_e2e_runner.py
"""
import argparse
import http.cookiejar
import json
import re
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path

REQUIRED_FILES = [
    "usecase-brief.md", "resource-map.md", "risk-log.md", "acceptance-checklist.md", "README.md",
    "d1-agent-skill/SKILL.md",
    "d1-agent-skill/test/test-case.md",
    "d2-n8n-e2e/e2e-test.md",
    "d2-n8n-e2e/run-log.md",
    "d3-mvp/spec-kit.md",
    "d3-mvp/improve-log.md",
    "d3-mvp/RUN.md",
    "d4-package/pitch.html",
]
BRIEF_SECTIONS = ["Bài toán", "Người dùng", "Input hàng ngày", "Output mong muốn",
                  "Quy trình xử lý", "Tiêu chí thành công", "Ràng buộc"]


def ok(check, detail):
    print(f"  [PASS] {check} — {detail}")
    return True


def bad(check, detail):
    print(f"  [FAIL] {check} — {detail}")
    return False


def skip(check, detail):
    print(f"  [SKIP] {check} — {detail}")
    return None


def read_or_none(p: Path):
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return None


def check_structure(pkg: Path):
    print("\n[1] Cấu trúc package")
    missing = [f for f in REQUIRED_FILES if not (pkg / f).exists()]
    if missing:
        return bad("đủ file", f"thiếu {len(missing)}: {', '.join(missing[:5])}")
    return ok("đủ file", f"{len(REQUIRED_FILES)}/{len(REQUIRED_FILES)} file chuẩn đều có")


def check_brief(pkg: Path):
    print("\n[2] Usecase brief")
    t = read_or_none(pkg / "usecase-brief.md")
    if t is None:
        return bad("file brief", "không đọc được usecase-brief.md")
    miss = [s for s in BRIEF_SECTIONS if s not in t]
    if miss:
        return bad("7 mục", f"thiếu mục: {', '.join(miss)}")
    measurable = re.findall(r"\b\d+[0-9/%]*\s*(?:mẫu test|giờ|phút|%|lần)", t)
    if len(measurable) < 2:
        return bad("tiêu chí đo được", f"chỉ tìm {len(measurable)} con số đo được, cần ≥2")
    return ok("7 mục + đo được", f"đủ 7 mục, {len(measurable)} con số đo được")


def check_workflow_graph(pkg: Path):
    print("\n[3] Workflow n8n — đồ thị node/connection")
    wf_files = sorted((pkg / "d2-n8n-e2e").glob("workflow*.json"))
    if not wf_files:
        return bad("file workflow", "không thấy d2-n8n-e2e/workflow*.json")
    try:
        w = json.loads(wf_files[0].read_text(encoding="utf-8"))
    except Exception as e:
        return bad("JSON hợp lệ", f"lỗi parse: {e}")
    nodes = w.get("nodes", [])
    conns = w.get("connections", {})
    names = {n.get("name") for n in nodes}
    errs = [k for k in conns if k not in names]
    errs += [e.get("node") for v in conns.values() for b in v.get("main", []) for e in b
             if e.get("node") not in names]
    has_webhook = any(n.get("type") == "n8n-nodes-base.webhook" for n in nodes)
    if errs:
        return bad("đồ thị nguyên vẹn", f"connection trỏ node không tồn tại: {errs[:3]}")
    if not has_webhook:
        return bad("có webhook", "không tìm thấy node webhook — không chạy được bằng input")
    path = next((n["parameters"].get("path") for n in nodes
                 if n.get("type") == "n8n-nodes-base.webhook" and "path" in n.get("parameters", {})), None)
    return ok("đồ thị nguyên vẹn", f"{len(nodes)} node, {len(conns)} connection đều khớp, webhook path: /{path}")


def check_runlog(pkg: Path):
    print("\n[4] Run-log")
    t = read_or_none(pkg / "d2-n8n-e2e" / "run-log.md")
    if t is None:
        return bad("file run-log", "không đọc được d2-n8n-e2e/run-log.md")
    vong = len(re.findall(r"^##\s*Vòng", t, re.M))
    has_fail = bool(re.search(r"Kết luận:?\s*\*?\*?FAIL", t, re.I))
    has_evidence = bool(re.search(r"execution\s*#?\d+|anh-demo/|executions/\d+", t, re.I))
    if vong < 2:
        return bad("≥2 vòng", f"chỉ có {vong} vòng")
    if not has_fail:
        return bad("≥1 vòng FAIL", "không có vòng nào ghi FAIL — nghi vấn copy nguyên (xem rubric D2c)")
    if not has_evidence:
        return bad("evidence", "không thấy execution ID hoặc ảnh — check lại template run-log")
    return ok("≥2 vòng + FAIL + evidence", f"{vong} vòng, có FAIL, có evidence (lưu ý: evidence vẫn cần GV verify bằng mắt ở bước [6])")


def check_pitch(pkg: Path):
    print("\n[5] Pitch HTML")
    pitch_path = next((p for p in [pkg / "d4-package" / "pitch.html", pkg / "pitch.html"] if p.exists()), None)
    if pitch_path is None:
        return bad("file pitch", "không thấy d4-package/pitch.html")
    t = read_or_none(pitch_path)
    slides = len(re.findall(r'<section[^>]*class="[^"]*slide', t))
    leftover = re.findall(r"\[ĐIỀN[^\]]*\]|\[TÊN[^\]]*\]|\[Họ tên[^\]]*\]", t)
    if slides < 6:
        return bad("6 slide", f"chỉ đếm {slides} slide")
    if leftover:
        return bad("placeholder", f"còn {len(leftover)} chỗ chưa điền")
    return ok("6 slide, sạch placeholder", "mở bằng trình duyệt để kiểm tra hiển thị + số liệu")


# ---------- [6] Runtime qua n8n REST API (mượn pattern B4) ----------

class N8nClient:
    def __init__(self, base, email, password):
        self.base = base.rstrip("/")
        self.email, self.password = email, password
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar))

    def _req(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method,
                                     headers={"Content-Type": "application/json"})
        with self.opener.open(req, timeout=20) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw else {}

    def login(self):
        return self._req("POST", "/rest/login",
                         {"emailOrLdapLoginId": self.email, "password": self.password})


def port_open(host, port, timeout=1):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def check_runtime(pkg: Path, n8n_url, email, password, test_input):
    print("\n[6] RUNTIME — import workflow + chạy 1 input (bước GV phải làm)")
    from urllib.parse import urlparse
    u = urlparse(n8n_url)
    if not port_open(u.hostname or "localhost", u.port or 5678):
        return skip("n8n local", f"{n8n_url} không phản hồi. Khởi động: `npx n8n start` (xem 04-contract-review/thuc-hanh-1-n8n-setup.md) rồi chạy lại. Các check [1]-[5] vẫn hợp lệ.")
    try:
        cli = N8nClient(n8n_url, email, password)
        cli.login()
    except Exception as e:
        return bad("login n8n", f"{e} — kiểm tra email/password (mặc định lớp B4)")
    wf_files = sorted((pkg / "d2-n8n-e2e").glob("workflow*.json"))
    wf = json.loads(wf_files[0].read_text(encoding="utf-8"))
    wf.pop("id", None)
    try:
        created = cli._req("POST", "/api/v1/workflows", wf)
        wid = created.get("id")
    except Exception as e:
        return bad("import workflow", f"{e}")
    print(f"        imported: workflow id {wid} — '{created.get('name')}'")
    # activate + gọi webhook
    try:
        cli._req("POST", f"/api/v1/workflows/{wid}/activate")
    except Exception:
        pass  # một số bản n8n yêu cầu activate qua PUT settings
    hook = next((n["parameters"]["path"] for n in wf["nodes"]
                 if n.get("type") == "n8n-nodes-base.webhook" and "path" in n.get("parameters", {})), None)
    results = []
    try:
        data = json.dumps({"data": test_input}).encode()
        req = urllib.request.Request(f"{n8n_url}/webhook/{hook}", data=data,
                                     headers={"Content-Type": "application/json"})
        with urllib.opener.open(req, timeout=60) as r:
            body = r.read().decode(errors="replace")[:800]
        results.append(ok("chạy input qua webhook", f"/webhook/{hook} trả 200 — xem response trong output"))
        print(f"        response (800 ký tự đầu): {body[:200]}...")
    except urllib.error.HTTPError as e:
        results.append(bad("chạy input qua webhook", f"HTTP {e.code}: {e.read().decode(errors='replace')[:200]}"))
    except Exception as e:
        results.append(bad("chạy input qua webhook", f"{e}"))
    # dọn: xoá workflow vừa import
    try:
        cli._req("DELETE", f"/api/v1/workflows/{wid}")
        print("        (đã dọn workflow test)")
    except Exception:
        print(f"        ⚠ không xoá được workflow {wid} — GV xoá tay trên UI")
    verdict = all(r for r in results if r is not None)
    return verdict


def main():
    ap = argparse.ArgumentParser(description="Capstone Auto-Check B8")
    ap.add_argument("package", help="thư mục package học viên (vd ho-ha-capstone)")
    ap.add_argument("--input", default="Yêu cầu test tự động từ capstone_auto_check — vui lòng xử lý.",
                    help="tin nhắn test đưa vào workflow")
    ap.add_argument("--n8n-url", default="http://localhost:5678")
    ap.add_argument("--email", default="admin@alobase.vn")
    ap.add_argument("--password", default="Password123!")
    args = ap.parse_args()

    pkg = Path(args.package).resolve()
    if not pkg.is_dir():
        sys.exit(f"Không tìm thấy thư mục: {pkg}")
    print(f"Capstone Auto-Check — {pkg.name}")
    results = [check_structure(pkg), check_brief(pkg), check_workflow_graph(pkg),
               check_runlog(pkg), check_pitch(pkg),
               check_runtime(pkg, args.n8n_url, args.email, args.password, args.input)]
    hard = [r for r in results if r is False]
    skipped = [r for r in results if r is None]
    print("\n──────────────────────────────")
    print(f"Kết quả: {len(results)-len(hard)-len(skipped)} PASS · {len(hard)} FAIL · {len(skipped)} SKIP")
    if hard:
        print("→ Có FAIL: fix theo gợi ý ở trên rồi chạy lại.")
        sys.exit(1)
    if skipped:
        print("→ Có SKIP (n8n chưa chạy): chạy `npx n8n start` rồi chạy lại để check runtime.")
    else:
        print("→ PASS toàn bộ (kể cả runtime). Lưu ý: phần phân loại lỗi nghiệp vụ vẫn cần GV/đồng nghiệp đọc output.")


if __name__ == "__main__":
    main()
