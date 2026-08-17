#!/usr/bin/env python3
"""
vibe-ai-auto-score validator.py

Validates assessment artifacts against JSON schemas, recursively verifies ALL
evidence items (including evidence nested inside fields[] / scores[]) exist in
the original source files, checks confidence scores, auto-flags need_review,
and logs execution. Routes low-confidence items to the review queue.

Tại sao đệ quy evidence: artifact của skill này (candidate-unified, grading-result)
có evidence nằm SÂU trong từng field / từng tiêu chí — không chỉ ở top-level.
Chỉ kiểm top-level sẽ bỏ sót hallucination ẩn trong từng điểm chấm.

Usage:
    python3 validator.py --artifact output/foo.json --schema schema/foo.schema.json
    python3 validator.py --run-all --artifact output/foo.json --schema schema/foo.schema.json --source input/bai.txt
    python3 validator.py --preflight-target /path/to/file
    python3 validator.py --log STEP ACTION TARGET STATUS

Zero external dependencies (stdlib only).
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# ============================================================================
# JSON Schema validation (minimal draft-07 subset, stdlib only)
# ============================================================================

class SchemaError(Exception):
    pass


def validate_type(value: Any, schema_type: str) -> bool:
    if schema_type == "string":
        return isinstance(value, str)
    if schema_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if schema_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if schema_type == "boolean":
        return isinstance(value, bool)
    if schema_type == "array":
        return isinstance(value, list)
    if schema_type == "object":
        return isinstance(value, dict)
    if schema_type == "null":
        return value is None
    return True


def validate_instance(instance: Any, schema: dict, path: str = "$") -> list[str]:
    errors: list[str] = []
    if not isinstance(schema, dict):
        return [f"{path}: schema must be an object"]

    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(validate_type(instance, t) for t in types):
            errors.append(f"{path}: expected type {types}, got {type(instance).__name__}")

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}, got {instance!r}")

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} not in enum {schema['enum']}")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: string too short")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(f"{path}: string too long")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: does not match pattern {schema['pattern']!r}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        for key, op in [("minimum", lambda a, b: a >= b), ("maximum", lambda a, b: a <= b),
                        ("exclusiveMinimum", lambda a, b: a > b),
                        ("exclusiveMaximum", lambda a, b: a < b)]:
            if key in schema and not op(instance, schema[key]):
                errors.append(f"{path}: {instance} violates {key} {schema[key]}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: array too short ({len(instance)} < {schema['minItems']})")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{path}: array too long")
        if "items" in schema:
            for i, item in enumerate(instance):
                errors.extend(validate_instance(item, schema["items"], f"{path}[{i}]"))

    if isinstance(instance, dict):
        if "required" in schema:
            missing = [k for k in schema["required"] if k not in instance]
            if missing:
                errors.append(f"{path}: missing required fields {missing}")
        if "properties" in schema:
            for key, subschema in schema["properties"].items():
                if key in instance:
                    errors.extend(validate_instance(instance[key], subschema, f"{path}.{key}"))

    return errors


def validate_artifact(artifact_path: str, schema_path: str) -> dict:
    try:
        with open(artifact_path) as f:
            instance = json.load(f)
    except Exception as e:
        return {"ok": False, "errors": [f"Cannot read artifact: {e}"], "warnings": []}
    try:
        with open(schema_path) as f:
            schema = json.load(f)
    except Exception as e:
        return {"ok": False, "errors": [f"Cannot read schema: {e}"], "warnings": []}
    errors = validate_instance(instance, schema)
    return {"ok": len(errors) == 0, "errors": errors, "warnings": []}


# ============================================================================
# Recursive evidence collection (key difference from generic validator)
# ============================================================================

def collect_evidence(obj: Any, found: list[dict] | None = None, path: str = "$") -> list[dict]:
    """Đệ quy tìm mọi object có key 'verbatim_quote' → coi là 1 evidence item."""
    if found is None:
        found = []
    if isinstance(obj, dict):
        if "verbatim_quote" in obj and isinstance(obj.get("verbatim_quote"), str):
            found.append({"quote": obj["verbatim_quote"], "source": obj.get("source", ""),
                          "location": obj.get("location", ""), "path": path})
        for k, v in obj.items():
            collect_evidence(v, found, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            collect_evidence(v, found, f"{path}[{i}]")
    return found


def _normalize(text: str) -> str:
    """Chuẩn hóa để so khớp evidence: lowercase + collapse whitespace + strip."""
    return re.sub(r"\s+", " ", (text or "")).strip().lower()


def verify_evidence_recursive(artifact: dict, source_files: list[str]) -> dict:
    """Kiểm MỖI evidence (kể cả nested) có tồn tại trong source.
    Tại sao normalize: trích dẫn có thể khác whitespace/newline nhẹ — normalize
    giúp bắt trúng mà không tạo false-missing, nhưng vẫn chống hallucination nội dung."""
    all_evidence = collect_evidence(artifact)
    sources: dict[str, str] = {}
    for sf in source_files:
        if Path(sf).exists():
            try:
                sources[sf] = Path(sf).read_text(encoding="utf-8", errors="ignore")
            except Exception:
                sources[sf] = ""

    verified, missing = [], []
    for ev in all_evidence:
        quote = ev["quote"]
        src = ev["source"]
        nquote = _normalize(quote)
        found = False
        if src and src in sources and nquote and nquote in _normalize(sources[src]):
            found = True
        elif src and Path(src).exists():
            try:
                if nquote and nquote in _normalize(Path(src).read_text(encoding="utf-8", errors="ignore")):
                    found = True
            except Exception:
                pass
        else:
            # search across provided sources
            for content in sources.values():
                if nquote and nquote in _normalize(content):
                    found = True
                    break
        (verified if found else missing).append(ev)

    adjustment = -0.2 * len(missing) if missing else 0.0
    return {
        "total_evidence": len(all_evidence),
        "verified": len(verified),
        "missing_count": len(missing),
        "missing": [{"quote": m["quote"][:120], "path": m["path"]} for m in missing],
        "confidence_adjustment": adjustment,
    }


# ============================================================================
# Confidence (recursive: min across nested confidence_score)
# ============================================================================

def collect_confidences(obj: Any) -> list[float]:
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "confidence_score" and isinstance(v, (int, float)) and not isinstance(v, bool):
                out.append(float(v))
            else:
                out.extend(collect_confidences(v))
    elif isinstance(obj, list):
        for v in obj:
            out.extend(collect_confidences(v))
    return out


def check_confidence(artifact: dict, threshold: float = 0.7) -> dict:
    confs = collect_confidences(artifact)
    if not confs:
        score = artifact.get("confidence_score")
    else:
        score = min(confs)  # worst-field governs overall confidence
    if score is None:
        return {"passes": False, "score": None, "reason": "no confidence_score found", "min_field": None}
    return {
        "passes": score >= threshold,
        "score": score,
        "min_field": min(confs) if confs else None,
        "reason": f"min field confidence {score} {'≥' if score >= threshold else '<'} threshold {threshold}",
    }


# ============================================================================
# Execution log (Tip 4)
# ============================================================================

LOG_PATH = os.environ.get("VIBE_EXECUTION_LOG", "output/execution_log.jsonl")


def log_execution(step: str, action: str, target: str, status: str,
                  duration_ms: int = 0, schema_validated: bool = False,
                  evidence_verified: bool = False) -> dict:
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "step": step, "action": action, "target": target,
        "actor": os.environ.get("VIBE_ACTOR", "vibe-ai-auto-score"),
        "status": status, "duration_ms": duration_ms,
        "schema_validated": schema_validated, "evidence_verified": evidence_verified,
    }
    p = Path(LOG_PATH)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


# ============================================================================
# Full pipeline
# ============================================================================

def run_all(artifact_path: str, schema_path: str | None = None,
            source_files: list[str] | None = None,
            confidence_threshold: float = 0.7) -> dict:
    start = time.time()
    schema_result = {"ok": True, "errors": [], "warnings": []}
    if schema_path:
        schema_result = validate_artifact(artifact_path, schema_path)

    try:
        with open(artifact_path) as f:
            artifact = json.load(f)
    except Exception as e:
        return {"ok": False, "errors": [f"Cannot read artifact: {e}"],
                "duration_ms": int((time.time() - start) * 1000)}

    evidence_result = verify_evidence_recursive(artifact, source_files or [])

    base_conf = artifact.get("confidence_score")
    confs = collect_confidences(artifact)
    base_conf = min(confs) if confs else (base_conf or 0.0)
    adjusted_conf = max(0.0, base_conf + evidence_result["confidence_adjustment"])
    confidence_result = check_confidence({**artifact, "confidence_score": adjusted_conf}, confidence_threshold)

    if not confidence_result["passes"]:
        artifact["need_review"] = True

    duration = int((time.time() - start) * 1000)
    ok = schema_result["ok"] and confidence_result["passes"] and evidence_result["missing_count"] == 0
    log_execution("validate", "run_all", artifact_path,
                  "success" if ok else "fail", duration,
                  schema_result["ok"], evidence_result["missing_count"] == 0)

    return {
        "ok": ok,
        "schema": schema_result,
        "evidence": evidence_result,
        "confidence": confidence_result,
        "adjusted_confidence_score": adjusted_conf,
        "duration_ms": duration,
    }


# ============================================================================
# Preflight (hook mode)
# ============================================================================

PROTECTED_PATHS = [r".*/template/.*", r".*/archive/.*", r".*/\.git/.*"]


def preflight_check(target_path: str) -> dict:
    for pattern in PROTECTED_PATHS:
        if re.match(pattern, target_path):
            return {"allowed": False, "reason": f"protected pattern {pattern}"}
    return {"allowed": True, "reason": "OK"}


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="vibe-ai-auto-score validator")
    parser.add_argument("--artifact")
    parser.add_argument("--schema")
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument("--threshold", type=float, default=0.7)
    parser.add_argument("--preflight-target")
    parser.add_argument("--run-all", action="store_true")
    parser.add_argument("--log", nargs=4, metavar=("STEP", "ACTION", "TARGET", "STATUS"))
    args = parser.parse_args()

    if args.log:
        print(json.dumps(log_execution(*args.log), indent=2, ensure_ascii=False))
        return 0
    if args.preflight_target:
        r = preflight_check(args.preflight_target)
        print(json.dumps(r, indent=2))
        return 0 if r["allowed"] else 1
    if args.run_all:
        if not args.artifact:
            print("ERROR: --artifact required for --run-all", file=sys.stderr)
            return 2
        r = run_all(args.artifact, args.schema, args.source, args.threshold)
        print(json.dumps(r, indent=2, ensure_ascii=False))
        return 0 if r["ok"] else 1
    if args.artifact and args.schema:
        r = validate_artifact(args.artifact, args.schema)
        print(json.dumps(r, indent=2, ensure_ascii=False))
        return 0 if r["ok"] else 1
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
