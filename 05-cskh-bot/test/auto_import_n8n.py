#!/usr/bin/env python3
import json
import os
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

TEST_DIR = Path(__file__).parent.resolve()
BASE_DIR = TEST_DIR.parent.resolve()
WORKFLOW_FILE = BASE_DIR / "checkpoints" / "n8n-cskh-bot-solution.json"
VECTOR_DB_URL = os.environ.get("CSKH_VECTOR_DB_URL", "http://127.0.0.1:8095")


def find_npx_bin():
    node20_npx = "/opt/homebrew/opt/node@20/bin/npx"
    if os.path.exists(node20_npx):
        return node20_npx
    return shutil.which("npx") or "npx"


def check_web_port(host="localhost", port=5678, timeout=1):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def vector_db_health():
    try:
        with urllib.request.urlopen(f"{VECTOR_DB_URL}/health", timeout=2) as resp:
            body = json.loads(resp.read().decode())
            return body
    except Exception:
        return None


def ensure_vector_db():
    health = vector_db_health()
    if health and health.get("ok"):
        print(f"  ✓ Vector DB đã sẵn sàng ({health.get('documents')} docs): {VECTOR_DB_URL}")
        return True

    server_script = TEST_DIR / "vector_db_server.py"
    if not server_script.exists():
        print(f"❌ Không tìm thấy vector DB server: {server_script}")
        return False

    print(f"🧠 Vector DB chưa chạy. Đang start: {VECTOR_DB_URL}")
    subprocess.Popen(
        [sys.executable, str(server_script), "--reset"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    for i in range(15):
        time.sleep(1)
        health = vector_db_health()
        if health and health.get("ok"):
            print(f"  ✓ Vector DB đã seed {health.get('documents')} docs sau {i + 1} giây.")
            return True
    print("  ⚠️ Vector DB chưa sẵn sàng; chạy lại cell sau vài giây nếu n8n báo lỗi RAG.")
    return False


def get_n8n_env():
    env = os.environ.copy()
    env["N8N_SECURE_COOKIE"] = "false"
    env["N8N_USER_MANAGEMENT_DISABLED"] = "true"
    env["N8N_DIAGNOSTICS_ENABLED"] = "false"
    env["N8N_PERSONALIZATION_ENABLED"] = "false"
    env["NODE_FUNCTION_ALLOW_BUILTIN"] = "fs,path,https"
    env["GEMINI_MODEL"] = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")
    for key_name in ("GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_AI_API_KEY"):
        if os.environ.get(key_name):
            env[key_name] = os.environ[key_name]
    node20_bin_dir = "/opt/homebrew/opt/node@20/bin"
    if os.path.exists(node20_bin_dir):
        env["PATH"] = f"{node20_bin_dir}:{env.get('PATH', '')}"
    return env


def auto_setup_owner(
    email=os.environ.get("N8N_EMAIL", "admin@alobase.vn"),
    password=os.environ.get("N8N_PASSWORD", "local-demo-password"),
    first="Admin",
    last="Alobase"
):
    payload = json.dumps({
        "email": email,
        "password": password,
        "firstName": first,
        "lastName": last
    }).encode("utf-8")
    req = urllib.request.Request(
        "http://localhost:5678/rest/owner/setup",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode())
            email_out = body.get("data", {}).get("email", email)
            print(f"  ✓ Tài khoản owner đã được tạo: {email_out}")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="ignore")
        if e.code in (400, 403) or "already" in body.lower() or "exists" in body.lower():
            print("  ℹ️ Tài khoản owner đã tồn tại, bỏ qua.")
            return True
        print(f"  ⚠️ Không thể tạo owner (HTTP {e.code}): {body[:160]}")
        return False
    except Exception as exc:
        print(f"  ⚠️ Không thể tạo owner: {exc}")
        return False


def import_workflow():
    npx_bin = find_npx_bin()
    env = get_n8n_env()
    result = subprocess.run(
        [npx_bin, "-y", "n8n", "import:workflow", f"--input={WORKFLOW_FILE}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
        timeout=60
    )
    if result.returncode == 0:
        print("  ✓ Đã import workflow solution vào n8n.")
    else:
        print("  ℹ️ Import workflow notice:")
        print((result.stderr or result.stdout)[-600:])
    return True


def activate_imported_workflow():
    try:
        from interactive_cskh_runner import N8nAPIClient
        api = N8nAPIClient()
        if not api.login():
            return False
        workflows = api.list_workflows()
        matches = [wf for wf in workflows if "B5 K1 - Retail CSKH Bot" in wf.get("name", "")]
        matches.sort(key=lambda wf: (bool(wf.get("active")), wf.get("updatedAt", "")), reverse=True)
        
        with open(WORKFLOW_FILE, "r", encoding="utf-8") as f:
            wf_solution = json.load(f)

        target = matches[0] if matches else None
        if not target:
            print("  📦 Workflow chưa có trên n8n API, đang import...")
            resp = api.request("POST", "/rest/workflows", body=wf_solution)
            target = resp.get("data", resp)
            print(f"  ✓ Đã import workflow B5: {target.get('name')} (id={target.get('id')})")
        else:
            # Update existing target workflow nodes & connections with latest solution file
            try:
                api.request("POST", f"/rest/workflows/{target['id']}/deactivate")
            except Exception:
                pass

            api.request("PATCH", f"/rest/workflows/{target['id']}", body={
                "nodes": wf_solution["nodes"],
                "connections": wf_solution["connections"],
                "name": wf_solution["name"]
            })
            target = api.get_workflow(target["id"])

        # Deactivate all other B5 workflows to prevent webhook route collision
        for wf in matches:
            if wf["id"] != target["id"]:
                try:
                    api.request("POST", f"/rest/workflows/{wf['id']}/deactivate")
                except Exception:
                    pass

        # Activate target workflow with versionId payload
        version_id = target.get("versionId")
        body = {"versionId": version_id} if version_id else {}
        api.request("POST", f"/rest/workflows/{target['id']}/activate", body=body)
        print(f"  ✓ Đã activate workflow B5 ({target['id']}).")
        return True
    except Exception as exc:
        print(f"  ⚠️ Không thể activate workflow tự động: {exc}")
        return False


def clear_existing_workflows():
    """Xóa hoặc dọn dẹp workflow trùng lặp trên n8n (nếu có)."""
    try:
        from interactive_cskh_runner import N8nAPIClient
        api = N8nAPIClient()
        if not api.login():
            return
        workflows = api.list_workflows()
        cskh_wfs = [wf for wf in workflows if "B5 K1 - Retail CSKH Bot" in wf.get("name", "")]
        if len(cskh_wfs) > 1:
            print(f"🧹 Tìm thấy {len(cskh_wfs)} workflow CSKH Bot trùng lặp, tiến hành dọn dẹp...")
            for wf in cskh_wfs[1:]:
                try:
                    api.delete_workflow(wf['id'])
                    print(f"  ✓ Đã xóa workflow trùng lặp: [{wf['id']}] {wf.get('name')}")
                except Exception as exc:
                    print(f"  ⚠️ Delete workflow notice: {exc}")
    except Exception as exc:
        print(f"  ⚠️ Lỗi khi dọn dẹp workflow: {exc}")


def auto_import_workflow():
    print("=" * 75)
    print("🚀 B5 — AUTO-LAUNCH & AUTO-IMPORT N8N CSKH BOT WORKFLOW")
    print("=" * 75)
    if not WORKFLOW_FILE.exists():
        print(f"❌ Không tìm thấy workflow solution: {WORKFLOW_FILE}")
        sys.exit(1)

    ensure_vector_db()

    npx_bin = find_npx_bin()
    web_active = check_web_port()
    if not web_active:
        print("📦 n8n chưa chạy; import workflow bằng CLI trước khi start để webhook được register lúc boot...")
        import_workflow()
        print(f"⚡ Cổng 5678 chưa mở. Đang chạy: {npx_bin} -y n8n start")
        env = get_n8n_env()
        subprocess.Popen(
            [npx_bin, "-y", "n8n", "start"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            env=env,
            start_new_session=True
        )
        print("⏳ Đang chờ n8n tại http://localhost:5678 ...")
        for i in range(25):
            time.sleep(1)
            if check_web_port():
                web_active = True
                print(f"  ✓ n8n đã sẵn sàng sau {i + 1} giây.")
                break

    if web_active:
        auto_setup_owner()
        clear_existing_workflows()
        activate_imported_workflow()
        print("🌐 n8n Web UI: http://localhost:5678")
        print("🔑 Owner: dùng biến N8N_EMAIL/N8N_PASSWORD hoặc credential demo local đã cấu hình.")
        print("✅ Step 0 hoàn tất: workflow B5 đã sẵn sàng.")
        return True

    print("⚠️ n8n đang khởi động ngầm. Mở http://localhost:5678 sau vài giây rồi chạy lại cell.")
    return False


if __name__ == "__main__":
    auto_import_workflow()
