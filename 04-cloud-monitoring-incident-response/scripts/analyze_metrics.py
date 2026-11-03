#!/usr/bin/env python3
"""Offline alert and recovery-window analysis for synthetic cloud-monitoring data.

Only reads local CSV evidence. Does not query or remediate any cloud account.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import json
import math
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT / "evidence" / "metrics.csv"


def analyze_metrics(rows, cpu_threshold=90.0, error_threshold=5.0, sustained=2):
    """Detect consecutive threshold breaches and when sample values recover.

    The reporting cadence and thresholds are assumptions. An interval between
    two observations is not evidence of uninterrupted service impact.
    """
    if sustained < 1 or not isinstance(sustained, int):
        raise ValueError("sustained must be a positive integer")
    if not rows:
        raise ValueError("Monitoring evidence has no samples")
    parsed = []
    for i, row in enumerate(rows, 1):
        try:
            stamp = datetime.fromisoformat(row["timestamp"])
            if stamp.tzinfo is None:
                raise ValueError("Timestamp must have an explicit UTC offset")
            measures = {k: float(row[k]) for k in ("cpu_percent", "http_5xx_percent", "disk_used_percent")}
            if not all(math.isfinite(x) and 0 <= x <= 100 for x in measures.values()):
                raise ValueError("Percentages must be finite and within 0–100")
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"Invalid monitoring sample {i}: {exc}") from exc
        moment = stamp.astimezone(timezone.utc)
        if parsed and moment <= parsed[-1]["moment"]:
            raise ValueError(f"Monitoring sample {i} is not chronologically increasing")
        parsed.append({"moment": moment, "timestamp": row["timestamp"],
                       **measures,
                       "cpu_breach": measures["cpu_percent"] > cpu_threshold,
                       "http_breach": measures["http_5xx_percent"] > error_threshold})
    windows, active = [], None
    for sample in parsed:
        alert = sample["cpu_breach"] or sample["http_breach"]
        if alert:
            if active is None:
                active = {"start": sample["timestamp"], "end": sample["timestamp"],
                          "samples": 0, "correlated_samples": 0,
                          "max_cpu_percent": 0.0, "max_http_5xx_percent": 0.0}
            active["end"] = sample["timestamp"]
            active["samples"] += 1
            active["correlated_samples"] += int(sample["cpu_breach"] and sample["http_breach"])
            active["max_cpu_percent"] = max(active["max_cpu_percent"], sample["cpu_percent"])
            active["max_http_5xx_percent"] = max(active["max_http_5xx_percent"], sample["http_5xx_percent"])
        elif active is not None:
            active["next_normal_sample"] = sample["timestamp"]
            active["sustained_alert"] = active["samples"] >= sustained
            windows.append(active)
            active = None
    if active is not None:
        active["next_normal_sample"] = None
        active["sustained_alert"] = active["samples"] >= sustained
        windows.append(active)
    return {
        "samples": len(parsed),
        "cpu_breaches": sum(x["cpu_breach"] for x in parsed),
        "http_5xx_breaches": sum(x["http_breach"] for x in parsed),
        "correlated_breaches": sum(x["cpu_breach"] and x["http_breach"] for x in parsed),
        "peak_cpu_percent": max(x["cpu_percent"] for x in parsed),
        "peak_http_5xx_percent": max(x["http_5xx_percent"] for x in parsed),
        "final_cpu_percent": parsed[-1]["cpu_percent"],
        "final_http_5xx_percent": parsed[-1]["http_5xx_percent"],
        "alert_windows": windows,
        "sustained_windows": sum(x["sustained_alert"] for x in windows),
        "thresholds": {"cpu_percent_above": cpu_threshold,
                       "http_5xx_percent_above": error_threshold,
                       "consecutive_samples": sustained},
        "scope": "Synthetic sampled evidence only; no live incident response or SLA claims.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=PROJECT / "outputs/incident_diagnostics.json")
    args = parser.parse_args()
    with args.input.open(encoding="utf-8-sig", newline="") as stream:
        analysis = analyze_metrics(list(csv.DictReader(stream)))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(analysis, indent=2) + "\n", encoding="utf-8")
    print(f"Analyzed {analysis['samples']} monitoring samples; "
          f"{analysis['sustained_windows']} sustained alert window(s).")
    print("LIMIT: No cloud resources were accessed or repaired.")


if __name__ == "__main__":
    main()
