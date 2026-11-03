"""Offline structural and data-format checks for simulated cloud support labs.

No real cloud commands, accounts, or service restoration are exercised.
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
    "README.md", "RECRUITER_QUICK_START.md", "SECURITY_AND_EVIDENCE.md",
    "VALIDATION_RESULTS.json", "FINAL_VALIDATION.json",
]


def validate_csv(path: Path) -> int:
    """Reject blank/duplicate headers, missing or surplus cells, and empty files."""
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.reader(stream, strict=True)
        header = next(reader, [])
        if not header or any(not cell.strip() for cell in header):
            raise ValueError("missing/blank CSV column header")
        if len(set(header)) != len(header):
            raise ValueError("duplicate CSV column header")
        row_count = 0
        for line, row in enumerate(reader, 2):
            if len(row) != len(header):
                raise ValueError(f"row {line}: expected {len(header)} fields, got {len(row)}")
            if any(not cell.strip() for cell in row):
                raise ValueError(f"row {line}: blank field")
            row_count += 1
    if not row_count:
        raise ValueError("CSV has no records")
    return row_count


def validate(root: Path = ROOT) -> list[str]:
    issues = []
    for rel in REQUIRED + [f"{project}/README.md" for project in PROJECTS]:
        if not (root / rel).is_file():
            issues.append(f"Missing file: {rel}")

    json_files = sorted(root.rglob("*.json"))
    csv_files = sorted(root.rglob("*.csv"))
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeError, OSError, json.JSONDecodeError) as exc:
            issues.append(f"JSON error at {path.relative_to(root)}: {exc}")
    rows = 0
    for path in csv_files:
        try:
            rows += validate_csv(path)
        except (OSError, UnicodeError, csv.Error, ValueError) as exc:
            issues.append(f"CSV error at {path.relative_to(root)}: {exc}")
    print(f"Offline inventory: {len(PROJECTS)} projects, {len(json_files)} JSON, "
          f"{len(csv_files)} CSV, {rows} validated CSV rows")
    return issues


def main() -> int:
    errors = validate()
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    if errors:
        return 1
    print("PASS: offline file structure, JSON syntax, and strict CSV rows")
    print("LIMIT: no cloud access, deployment, incident remediation, or external security audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
