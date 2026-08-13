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
    env = os.environ.copy()
    env["N8N_SECURE_COOKIE"] = "false"
    env["N8N_USER_MANAGEMENT_DISABLED"] = "true"
    env["N8N_DIAGNOSTICS_ENABLED"] = "false"
    env["N8N_PERSONALIZATION_ENABLED"] = "false"
    node20_bin_dir = "/opt/homebrew/opt/node@20/bin"
    if os.path.exists(node20_bin_dir):
        env["PATH"] = f"{node20_bin_dir}:{env.get('PATH', '')}"

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
        target = matches[0] if matches else None
        if not target:
            print("  ⚠️ Chưa tìm thấy workflow B5 để activate.")
            return False
        workflow = api.get_workflow(target["id"])
        if workflow.get("active"):
            print("  ✓ Workflow B5 đã active.")
            return True
        body = {"versionId": workflow.get("versionId")} if workflow.get("versionId") else None
        api.request("POST", f"/rest/workflows/{target['id']}/activate", body=body)
        print("  ✓ Đã activate workflow B5.")
        return True
    except Exception as exc:
        print(f"  ⚠️ Không thể activate workflow tự động: {exc}")
        return False


def auto_import_workflow():
    print("=" * 75)
    print("🚀 B5 — AUTO-LAUNCH & AUTO-IMPORT N8N CSKH BOT WORKFLOW")
    print("=" * 75)
    if not WORKFLOW_FILE.exists():
        print(f"❌ Không tìm thấy workflow solution: {WORKFLOW_FILE}")
        sys.exit(1)

    npx_bin = find_npx_bin()
    web_active = check_web_port()
    if not web_active:
        print("📦 n8n chưa chạy; import workflow bằng CLI trước khi start để webhook được register lúc boot...")
        import_workflow()
        print(f"⚡ Cổng 5678 chưa mở. Đang chạy: {npx_bin} -y n8n start")
        env = os.environ.copy()
        env["N8N_SECURE_COOKIE"] = "false"
        env["N8N_USER_MANAGEMENT_DISABLED"] = "true"
        env["N8N_DIAGNOSTICS_ENABLED"] = "false"
        env["N8N_PERSONALIZATION_ENABLED"] = "false"
        node20_bin_dir = "/opt/homebrew/opt/node@20/bin"
        if os.path.exists(node20_bin_dir):
            env["PATH"] = f"{node20_bin_dir}:{env.get('PATH', '')}"
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
        activate_imported_workflow()
        print("🌐 n8n Web UI: http://localhost:5678")
        print("🔑 Owner: dùng biến N8N_EMAIL/N8N_PASSWORD hoặc credential demo local đã cấu hình.")
        print("✅ Step 0 hoàn tất: workflow B5 đã sẵn sàng.")
        return True

    print("⚠️ n8n đang khởi động ngầm. Mở http://localhost:5678 sau vài giây rồi chạy lại cell.")
    return False


if __name__ == "__main__":
    auto_import_workflow()
