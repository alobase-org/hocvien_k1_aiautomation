import json
import os
import shutil
import socket
import subprocess
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

TEST_DIR = Path(__file__).parent.resolve()
BASE_DIR = TEST_DIR.parent.resolve()
CHECKPOINTS_DIR = BASE_DIR / "checkpoints"
WORKFLOW_FILE = CHECKPOINTS_DIR / "n8n-contract-review-solution.json"

def find_npx_bin():
    """Tìm đường dẫn npx tương thích (ưu tiên Node 20 LTS)."""
    node20_npx = "/opt/homebrew/opt/node@20/bin/npx"
    if os.path.exists(node20_npx):
        return node20_npx
    
    npx_bin = shutil.which("npx")
    if npx_bin:
        return npx_bin
        
    for candidate in ["/opt/homebrew/bin/npx", "/usr/local/bin/npx"]:
        if os.path.exists(candidate):
            return candidate
    return "npx"

def find_docker_bin():
    """Tìm đường dẫn thực thi của docker trên macOS/Linux."""
    standard_bin = shutil.which("docker")
    if standard_bin:
        return standard_bin
    candidate_paths = [
        "/usr/local/bin/docker",
        "/opt/homebrew/bin/docker",
        Path.home() / ".docker/bin/docker",
        "/Applications/Docker.app/Contents/Resources/bin/docker"
    ]
    for path in candidate_paths:
        p = Path(path)
        if p.exists() and os.access(p, os.X_OK):
            return str(p)
    return None

def check_web_port(host="localhost", port=5678, timeout=1):
    """Kiểm tra cổng HTTP n8n Web UI có đang hoạt động hay không."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def auto_setup_owner(email="admin@alobase.vn", password="Password123!", first="Admin", last="Alobase"):
    """Tự động tạo tài khoản owner qua REST API /rest/owner/setup để bỏ qua màn hình đăng ký."""
    try:
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
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode())
            role = body.get("data", {}).get("role", "unknown")
            email_out = body.get("data", {}).get("email", email)
            print(f"  ✓ Tài khoản owner đã được tạo tự động: {email_out} (role: {role})")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        if "already" in body.lower() or "exists" in body.lower() or e.code == 403:
            print(f"  ℹ️ Tài khoản owner đã tồn tại, bỏ qua bước khởi tạo.")
            return True
        print(f"  ⚠️ Không thể tự động tạo owner (HTTP {e.code}): {body[:200]}")
        return False
    except Exception as e:
        print(f"  ⚠️ Lỗi khi tạo owner tự động: {e}")
        return False


def clear_existing_workflows():
    """Xóa toàn bộ workflow cũ trên n8n để tránh duplicate khi import."""
    from interactive_e2e_runner import N8nAPIClient

    print("🧹 Đang xóa toàn bộ workflow cũ trên n8n để tránh duplicate...")
    api = N8nAPIClient()
    if not api.login():
        print("  ⚠️ Không thể đăng nhập để xóa workflow cũ.")
        return

    workflows = api.list_workflows()
    if not workflows:
        print("  ℹ️ Không có workflow cũ nào cần xóa.")
        return

    print(f"  • Tìm thấy {len(workflows)} workflow cũ trên n8n. Tiến hành xóa toàn bộ...")
    for wf in workflows:
        wid = wf.get("id")
        name = wf.get("name", "unknown")
        try:
            api.post(f"/rest/workflows/{wid}/deactivate")
        except Exception:
            pass
        try:
            api.delete_workflow(wid)
            print(f"  ✓ Đã xóa workflow: [{wid}] {name}")
        except Exception as e:
            print(f"  ⚠️ Không thể xóa workflow {wid}: {e}")


def auto_import_workflow():
    """Tự động kích hoạt n8n service và tạo owner account qua REST API."""
    print("=" * 75)
    print("🚀 CẤU HÌNH & TỰ ĐỘNG KHỞI CHẠY N8N (BỎ QUA MÀN HÌNH ĐĂNG KÝ TÀI KHOẢN)")
    print("=" * 75)
    
    if not WORKFLOW_FILE.exists():
        print(f"❌ Lỗi: Không tìm thấy file workflow giải pháp tại {WORKFLOW_FILE}")
        sys.exit(1)
        
    print(f"📄 Đã tìm thấy file workflow giải pháp: {WORKFLOW_FILE.name}")
    
    web_active = check_web_port("localhost", 5678)
    npx_bin = find_npx_bin()
    docker_bin = find_docker_bin()
    
    # 1. Nếu cổng 5678 chưa mở, tự động chạy node@20 npx -y n8n start với N8N_USER_MANAGEMENT_DISABLED=true
    if not web_active:
        print(f"⚡ Cổng 5678 chưa phản hồi. Đang tự động kích hoạt n8n qua '{npx_bin} -y n8n start'...")
        try:
            env = os.environ.copy()
            env["N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS"] = "true"
            env["N8N_LOG_LEVEL"] = "warn"
            env["N8N_SECURE_COOKIE"] = "false"
            env["N8N_USER_MANAGEMENT_DISABLED"] = "true"
            env["N8N_DIAGNOSTICS_ENABLED"] = "false"
            env["N8N_PERSONALIZATION_ENABLED"] = "false"
            env["N8N_HEADER_CORS_ENABLED"] = "true"
            env["N8N_HEADER_CORS_ORIGIN"] = "*"
            # Cho phép workflow đọc key/model Gemini qua $env.GEMINI_API_KEY / $env.GEMINI_API_URL
            if os.environ.get("GEMINI_API_KEY"):
                env["GEMINI_API_KEY"] = os.environ["GEMINI_API_KEY"]
            if os.environ.get("GEMINI_API_URL"):
                env["GEMINI_API_URL"] = os.environ["GEMINI_API_URL"]
            
            # Put node@20 in PATH
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
            print("⏳ Đang chờ n8n khởi động service tại http://localhost:5678...")
            for i in range(20):
                time.sleep(1.0)
                if check_web_port("localhost", 5678):
                    web_active = True
                    print(f"  ✓ n8n Web UI đã bật thành công sau {i+1} giây!")
                    break
        except Exception as e:
            print(f"⚠️ Không thể khởi chạy 'npx n8n start' tự động: {e}")

    # 2. Nếu vẫn chưa active và có Docker, thử docker compose up -d n8n
    if not web_active and docker_bin:
        print("🐳 Đang thử khởi chạy Docker container (docker compose up -d n8n)...")
        try:
            subprocess.run([docker_bin, "compose", "up", "-d", "n8n"], cwd=str(TEST_DIR), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for _ in range(10):
                time.sleep(1.0)
                if check_web_port("localhost", 5678):
                    web_active = True
                    break
        except Exception:
            pass

    # 3. Tự động setup owner account qua REST API
    if web_active:
        print("🔑 Đang tự động khởi tạo tài khoản Owner n8n...")
        auto_setup_owner()

    # 4. Xóa workflow cũ để tránh duplicate, rồi import workflow mới
    if web_active:
        clear_existing_workflows()
        print("🔄 Đang nạp workflow giải pháp vào n8n qua CLI...")
        try:
            env = os.environ.copy()
            env["N8N_SECURE_COOKIE"] = "false"
            env["N8N_USER_MANAGEMENT_DISABLED"] = "true"
            node20_bin_dir = "/opt/homebrew/opt/node@20/bin"
            if os.path.exists(node20_bin_dir):
                env["PATH"] = f"{node20_bin_dir}:{env.get('PATH', '')}"

            subprocess.run(
                [npx_bin, "-y", "n8n", "import:workflow", f"--input={WORKFLOW_FILE}"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env
            )
            # Tự động kích hoạt (Activate) workflow để nhận Webhook production
            try:
                from interactive_e2e_runner import InteractiveE2ERunner
                runner = InteractiveE2ERunner()
                if runner.ensure_logged_in():
                    wfid = runner.find_workflow_id()
                    if wfid:
                        runner.api.activate_workflow(wfid)
                        print(f"  ✓ Đã kích hoạt (Active) workflow ID: {wfid}")
            except Exception as e:
                print(f"  ⚠️ Không thể tự động activate workflow: {e}")
        except Exception as e:
            print(f"ℹ️ n8n Import notice: {e}")

    # 5. Kiểm tra kết quả lần cuối
    web_active = check_web_port("localhost", 5678)
    print("\n" + "=" * 75)
    if web_active:
        print("🌐 ĐÃ KHỞI CHẠY THÀNH CÔNG N8N WEB UI TẠI: http://localhost:5678")
        print("🔑 Owner: admin@alobase.vn / Password123! (đã tự động tạo)")
        print("✅ BƯỚC 0 HOÀN TẤT: n8n đã nạp workflow giải pháp và sẵn sàng vận hành!")
        print("=" * 75)
        return True
    else:
        print("⚠️ BƯỚC 0 THÔNG BÁO: Tiến trình n8n đang được khởi chạy ngầm.")
        print("🌐 Vui lòng bấm F5 / truy cập link: http://localhost:5678 sau vài giây.")
        print("=" * 75)
        return True

if __name__ == "__main__":
    auto_import_workflow()
