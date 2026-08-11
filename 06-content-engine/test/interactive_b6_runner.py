#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Live E2E runner cho buổi 6 Content Engine — gọi webhook n8n THẬT (không mock).

    B6_WEBHOOK_ANGLES=https://<n8n-cua-ban>/webhook/b6/angles \\
    B6_WEBHOOK_GENERATE=https://<n8n-cua-ban>/webhook/b6/generate \\
    B6_WEBHOOK_APPROVE=https://<n8n-cua-ban>/webhook/b6/approve \\
    python interactive_b6_runner.py [--full]


TC05 (generate_full) chạy trọn Lớp 2→3→4 — TỐN PHÍ ảnh thật + mất ~2 phút. Mặc định SKIP,
chỉ chạy khi truyền --full.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

LAB = Path(__file__).resolve().parents[1]
CASES_PATH = LAB / "checkpoints" / "test-cases.json"

loi = []
canh_bao = []


def kiem(dat: bool, mo_ta: str, chi_tiet: str = "", nghiem_trong: bool = True):
    print(f"    {'✓' if dat else '✗'} {mo_ta}{(' — ' + chi_tiet) if chi_tiet else ''}")
    if not dat:
        (loi if nghiem_trong else canh_bao).append(mo_ta)


def post(url: str, payload: dict, timeout: int = 150) -> dict:
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw.strip() else {}
    except urllib.error.HTTPError as e:
        return {"_http_error": e.code, "_body": e.read().decode("utf-8", "replace")}
    except urllib.error.URLError as e:
        return {"_network_error": str(e.reason)}


class B6Runner:
    def __init__(self):
        self.urls = {
            "angles": os.environ.get("B6_WEBHOOK_ANGLES", ""),
            "generate": os.environ.get("B6_WEBHOOK_GENERATE", ""),
            "approve": os.environ.get("B6_WEBHOOK_APPROVE", ""),
        }
        thieu = [k for k, v in self.urls.items() if not v]
        if thieu:
            raise RuntimeError(
                f"Thiếu biến môi trường B6_WEBHOOK_{thieu[0].upper()} (và có thể các biến khác). "
                f"Lấy 3 URL production từ n8n giống hệt app-duyet-solution.html.")
        self.context = {}  # id case -> response, để case sau tái dùng (vd TC05 dùng angle của TC01)

    def chay_angles(self, case: dict) -> dict:
        return post(self.urls["angles"], case["payload"])

    def chay_generate(self, case: dict) -> dict:
        return post(self.urls["generate"], case["payload"], timeout=180)

    def chay_approve(self, case: dict) -> dict:
        return post(self.urls["approve"], case["payload"])

    def kiem_angles(self, case: dict, out: dict):
        kv = case["ky_vong"]
        angles = out.get("angles") or []
        kiem(len(angles) == kv.get("so_angle", 5), "số ý tưởng đúng kỳ vọng",
             f"nhận {len(angles)}, kỳ vọng {kv.get('so_angle', 5)}")
        if "brief_id_echo" in kv:
            kiem(out.get("brief_id") == kv["brief_id_echo"], "brief_id echo đúng đầu vào",
                 f"nhận '{out.get('brief_id')}'")
        covered = set(out.get("personas_covered") or [])
        if "min_personas_covered" in kv:
            kiem(len(covered) >= kv["min_personas_covered"], "đủ số chân dung tối thiểu được phủ",
                 f"phủ {sorted(covered)}")
        if "chi_duoc_persona" in kv:
            allowed = set(kv["chi_duoc_persona"])
            bia = covered - allowed
            kiem(not bia, "không tự bịa chân dung ngoài input", f"bịa thêm: {sorted(bia)}" if bia else "")

    def kiem_generate_thieu_angle(self, case: dict, out: dict):
        kv = case["ky_vong"]
        source_angle_id = ((out.get("assets") or {}).get("source_angle_id")
                            if isinstance(out.get("assets"), dict) else None)
        loi_ro_rang = bool(out.get("_http_error") or out.get("_network_error")
                            or not source_angle_id or "error" in out)
        if kv.get("khong_duoc_co_source_angle_id_hop_le"):
            kiem(loi_ro_rang, "thiếu angle → lỗi/rỗng rõ ràng, KHÔNG âm thầm tự bịa source_angle_id",
                 f"phản hồi: {json.dumps(out, ensure_ascii=False)[:200]}")

    def kiem_generate_full(self, case: dict, out: dict, angle_da_chon: dict):
        kv = case["ky_vong"]
        assets = out.get("assets") or {}
        if kv.get("source_angle_id_khop_angle_da_chon"):
            kiem(assets.get("source_angle_id") == angle_da_chon.get("angle_id"),
                 "source_angle_id khớp đúng angle đã chọn (không lệch ý tưởng)",
                 f"nhận '{assets.get('source_angle_id')}', đã chọn '{angle_da_chon.get('angle_id')}'")
        for field in kv.get("co_du_field", []):
            kiem(field in out, f"response có field '{field}'")
        jvp = out.get("judge_van_phong") or {}
        for field in kv.get("judge_van_phong_dung_field", []):
            kiem(field in jvp, f"judge_van_phong có field '{field}'")
        ja = out.get("judge_anh") or {}
        for field in kv.get("judge_anh_dung_field", []):
            kiem(field in ja, f"judge_anh có field '{field}'")
        if ja.get("vi_pham_chinh_sach") is True:
            kiem(not out.get("image_url"), "Judge ảnh chặn → image_url thật sự rỗng (không lọt ảnh vi phạm)")
            canh_bao.append(f"{case['id']}: Judge ảnh chặn ảnh lần chạy này — {ja.get('reason', '')[:150]}")

    def kiem_approve(self, case: dict, out: dict):
        kv = case["ky_vong"]
        if "status_echo" in kv:
            kiem(out.get("status") == kv["status_echo"], "status trả về đúng kỳ vọng (đã áp enum guard)",
                 f"nhận '{out.get('status')}'")
        if kv.get("co_log_id"):
            kiem(bool(out.get("log_id")), "có log_id — đã ghi Publish_Log thật")


def load_cases():
    if not CASES_PATH.exists():
        sys.exit(f"Không thấy {CASES_PATH}")
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true",
                     help="Chạy cả TC05 (generate_full) — tốn phí ảnh thật + mất ~2 phút")
    args = ap.parse_args()

    try:
        runner = B6Runner()
    except RuntimeError as e:
        sys.exit(str(e))
    cases = load_cases()
    print(f"Gọi webhook thật tại: angles={runner.urls['angles']}")
    print(f"                       generate={runner.urls['generate']}")
    print(f"                       approve={runner.urls['approve']}\n")

    for case in cases:
        loai = case["loai"]
        if loai == "generate_full" and not args.full:
            print(f"⏭  {case['id']} ({case['mo_ta']}) — SKIP (chạy tốn phí ảnh thật, cần --full)")
            continue

        print(f"▶ {case['id']} — {case['mo_ta']}")
        if loai == "angles":
            out = runner.chay_angles(case)
            runner.context[case["id"]] = out
            runner.kiem_angles(case, out)
        elif loai == "generate":
            out = runner.chay_generate(case)
            runner.kiem_generate_thieu_angle(case, out)
        elif loai == "generate_full":
            nguon = case["dung_angle_tu"]
            angles_out = runner.context.get(nguon)
            if not angles_out or not angles_out.get("angles"):
                kiem(False, f"cần chạy {nguon} (angles) thành công trước để lấy 1 angle thật")
                continue
            angle_da_chon = angles_out["angles"][0]
            payload = dict(case["payload_template"])
            payload["angle"] = angle_da_chon
            out = post(runner.urls["generate"], payload, timeout=180)
            runner.kiem_generate_full(case, out, angle_da_chon)
        elif loai == "approve":
            out = runner.chay_approve(case)
            runner.kiem_approve(case, out)
        else:
            kiem(False, f"loại case không rõ: {loai}")
        print()

    print()
    if canh_bao:
        print(f"CẢNH BÁO ({len(canh_bao)}): " + "; ".join(canh_bao))
    if loi:
        print(f"CHƯA ĐẠT ({len(loi)}): " + "; ".join(loi))
        return 1
    print("ĐẠT — mọi case đã chạy (kể cả case cố tình gửi sai) đều đúng kỳ vọng, qua webhook n8n thật.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
