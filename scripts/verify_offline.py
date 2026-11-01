"""Offline structural checks for the simulated cloud support portfolio.

Does not connect to AWS, Azure, GCP, or verify real-world infrastructure.
Run: python scripts/verify_offline.py
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
    "01-aws-cloud-support-troubleshooting-helpdesk",
    "02-multicloud-infrastructure-support-lab",
    "03-cloud-networking-connectivity-troubleshooting",
    "04-cloud-monitoring-incident-response",
    "05-cloud-administration-iam-backup-operations",
]
REQUIRED = [
    "README.md",
    "RECRUITER_QUICK_START.md",
    "SECURITY_AND_EVIDENCE.md",
    "VALIDATION_RESULTS.json",
    "FINAL_VALIDATION.json",
]
errors: list[str] = []
for relative in REQUIRED + [f"{p}/README.md" for p in PROJECTS]:
    if not (ROOT / relative).is_file():
        errors.append(f"Missing file: {relative}")

json_files = list(ROOT.rglob("*.json"))
csv_files = list(ROOT.rglob("*.csv"))
for path in json_files:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeError, OSError, json.JSONDecodeError) as exc:
        errors.append(f"JSON error at {path.relative_to(ROOT)}: {exc}")
for path in csv_files:
    try:
        with path.open(encoding="utf-8-sig", newline="") as fh:
            reader = csv.reader(fh)
            header = next(reader, None)
            if not header or not any(c.strip() for c in header):
                errors.append(f"Missing CSV header: {path.relative_to(ROOT)}")
            for _ in reader:
                pass
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"CSV error at {path.relative_to(ROOT)}: {exc}")

print(f"Offline inventory: {len(PROJECTS)} projects, {len(json_files)} JSON files, {len(csv_files)} CSV files")
if errors:
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    sys.exit(1)
print("PASS: required project files, JSON syntax, and CSV readability")
print("LIMIT: does not confirm deployments, cloud access, incident remediation, or security of external accounts")
