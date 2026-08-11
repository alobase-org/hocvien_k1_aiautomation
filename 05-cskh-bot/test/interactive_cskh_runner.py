#!/usr/bin/env python3
import json
import os
import urllib.error
import urllib.request
from urllib.parse import quote
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
CHECKPOINTS_DIR = BASE_DIR / "checkpoints"
TEMPLATES_DIR = BASE_DIR / "templates"

N8N_BASE_URL = "http://localhost:5678"
N8N_EMAIL = os.environ.get("N8N_EMAIL", "admin@alobase.vn")
N8N_PASSWORD = os.environ.get("N8N_PASSWORD", "local-demo-password")
WORKFLOW_NAME = "B5 K1 - Retail CSKH Bot"


class N8nAPIClient:
    def __init__(self, base_url=N8N_BASE_URL, email=N8N_EMAIL, password=N8N_PASSWORD):
        self.base_url = base_url.rstrip("/")
        self.email = email
        self.password = password
        self._cookie = None

    def login(self):
        passwords_to_try = [self.password, "Password123!", "local-demo-password"]
        for pwd in passwords_to_try:
            payload = json.dumps({"emailOrLdapLoginId": self.email, "password": pwd}).encode()
            req = urllib.request.Request(
                f"{self.base_url}/rest/login",
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    raw_cookie = resp.headers.get("Set-Cookie", "")
                    if raw_cookie:
                        self._cookie = raw_cookie.split(";")[0].strip()
                    print("  ✓ Đăng nhập n8n REST API thành công.")
                    return True
            except Exception:
                continue
        print(f"  ⚠️ Login lỗi: Không thể đăng nhập với email {self.email}")
        return False

    def _headers(self):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if self._cookie:
            headers["Cookie"] = self._cookie
        return headers

    def request(self, method, path, body=None, timeout=30):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            f"{self.base_url}{path}",
            data=data,
            headers=self._headers(),
            method=method
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw.strip() else {}

    def list_workflows(self):
        resp = self.request("GET", "/rest/workflows")
        return resp.get("data", [])

    def get_workflow(self, workflow_id):
        resp = self.request("GET", f"/rest/workflows/{workflow_id}")
        return resp.get("data", resp)

    def activate_workflow(self, workflow_id):
        try:
            workflow = self.get_workflow(workflow_id)
            body = {"versionId": workflow.get("versionId")} if workflow.get("versionId") else None
            self.request("POST", f"/rest/workflows/{workflow_id}/activate", body=body)
            print("  ✓ Workflow đã active.")
        except Exception as exc:
            print(f"  ℹ️ Activate notice: {exc}")

    def delete_workflow(self, workflow_id):
        try:
            try:
                self.request("POST", f"/rest/workflows/{workflow_id}/deactivate")
            except Exception:
                pass
            try:
                self.request("POST", f"/rest/workflows/{workflow_id}/archive")
            except Exception:
                pass
            return self.request("DELETE", f"/rest/workflows/{workflow_id}")
        except Exception as exc:
            print(f"  ⚠️ Delete workflow notice: {exc}")

    def post_webhook(self, path, payload):
        req = urllib.request.Request(
            f"{self.base_url}/webhook/{path}",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw.strip() else {}


class CSKHBotDemoRunner:
    def __init__(self):
        self.api = N8nAPIClient()
        self.workflow_id = None
        self.workflow = None
        self.webhook_path = "cskh"

    def ensure_logged_in(self):
        return self.api.login()

    def find_workflow(self):
        workflows = self.api.list_workflows()
        matches = [wf for wf in workflows if WORKFLOW_NAME in wf.get("name", "")]
        matches.sort(key=lambda wf: (bool(wf.get("active")), wf.get("updatedAt", "")), reverse=True)
        for wf in matches:
            self.workflow_id = wf["id"]
            self.workflow = self.api.get_workflow(self.workflow_id)
            self.webhook_path = self.resolve_webhook_path()
            return self.workflow
        raise RuntimeError(f"Không tìm thấy workflow chứa tên: {WORKFLOW_NAME}")

    def resolve_webhook_path(self):
        if not self.workflow:
            return "cskh"
        for node in self.workflow.get("nodes", []):
            if node.get("type") != "n8n-nodes-base.webhook":
                continue
            path = node.get("parameters", {}).get("path", "cskh")
            webhook_id = node.get("webhookId")
            if webhook_id:
                return path or webhook_id
            node_name = quote(node.get("name", "").lower(), safe="")
            return f"{self.workflow_id}/{node_name}/{path}"
        return "cskh"

    def activate(self):
        if not self.workflow_id:
            self.find_workflow()
        self.api.activate_workflow(self.workflow_id)

    def inspect_nodes(self):
        if not self.workflow:
            self.find_workflow()
        nodes = self.workflow.get("nodes", [])
        rows = []
        for node in nodes:
            rows.append({
                "name": node.get("name"),
                "type": node.get("type"),
                "position": node.get("position")
            })
        return rows

    def trigger_chat(self, question, source_q_id="NB-DEMO"):
        if not self.workflow_id:
            self.find_workflow()
        return self.api.post_webhook(self.webhook_path, {
            "question": question,
            "source_q_id": source_q_id,
            "channel": "jupyter_notebook"
        })

    def load_test_cases(self):
        with open(CHECKPOINTS_DIR / "test-cases.json", "r", encoding="utf-8") as f:
            return json.load(f)["cases"]

    def run_test_cases(self):
        cases = self.load_test_cases()
        results = []
        for case in cases:
            out = self.trigger_chat(case["khach_hoi"], case["id"])
            results.append({
                "id": case["id"],
                "question": case["khach_hoi"],
                "expected_route": case.get("ky_vong_route"),
                "actual_route": out.get("route"),
                "cache_hit": out.get("cache_hit"),
                "intent": out.get("intent"),
                "need_human": out.get("need_human"),
                "source": out.get("nguon"),
                "answer": out.get("answer")
            })
        return results
