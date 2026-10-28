#!/usr/bin/env python3
"""Validate advanced-grill-me state; read-only, Python standard library only."""
import json
import sys
from pathlib import Path

STATUSES = {"interviewing", "draft", "approved", "not_ready"}
DECISION_STATUSES = {"unresolved", "proposed", "approved", "deferred"}
REQUIRED = {"schema_version", "session_id", "topic", "mode", "status", "decisions", "open_questions", "risks", "evidence", "next_action", "user_approved"}

def validate(data):
    errors = []
    if not isinstance(data, dict): return ["Top-level value must be an object"]
    errors += [f"Missing key: {x}" for x in sorted(REQUIRED - set(data))]
    if data.get("schema_version") != 1: errors.append("schema_version must be 1")
    if data.get("status") not in STATUSES: errors.append("Invalid status")
    if not isinstance(data.get("session_id"), str) or not data["session_id"].strip(): errors.append("session_id required")
    if not isinstance(data.get("user_approved"), bool): errors.append("user_approved must be boolean")
    for key in ("decisions", "open_questions", "risks", "evidence"):
        if not isinstance(data.get(key), list): errors.append(f"{key} must be a list")
    decisions = data.get("decisions", [])
    if isinstance(decisions, list):
        ids = []
        for i, d in enumerate(decisions):
            if not isinstance(d, dict): errors.append(f"decisions[{i}] must be object"); continue
            for key in ("id", "question", "status", "prerequisites"):
                if key not in d: errors.append(f"decisions[{i}] missing {key}")
            if d.get("status") not in DECISION_STATUSES: errors.append(f"decisions[{i}] invalid status")
            if not isinstance(d.get("prerequisites"), list): errors.append(f"decisions[{i}] prerequisites must be array")
            if isinstance(d.get("id"), str): ids.append(d["id"])
        if len(ids) != len(set(ids)): errors.append("Duplicate decision IDs")
        known = set(ids)
        for i, d in enumerate(decisions):
            if isinstance(d, dict) and isinstance(d.get("prerequisites"), list):
                for p in d["prerequisites"]:
                    if p not in known: errors.append(f"decisions[{i}] unknown prerequisite {p}")
    if data.get("status") == "approved" and data.get("user_approved") is not True:
        errors.append("Approved status requires explicit user_approved=true")
    return errors

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_state.py <state.json>", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        for error in errors: print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OK: state schema and basic invariants validated")
    return 0
if __name__ == "__main__": sys.exit(main())
