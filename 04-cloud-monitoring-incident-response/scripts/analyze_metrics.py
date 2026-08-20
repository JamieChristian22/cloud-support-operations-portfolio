#!/usr/bin/env python3
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "evidence" / "metrics.csv"
rows = list(csv.DictReader(path.open()))
critical_cpu = [r for r in rows if float(r["cpu_percent"]) > 90]
critical_5xx = [r for r in rows if float(r["http_5xx_percent"]) > 5]
print(f"Samples: {len(rows)}")
print(f"CPU > 90% samples: {len(critical_cpu)}")
print(f"HTTP 5xx > 5% samples: {len(critical_5xx)}")
print(f"Peak CPU: {max(float(r['cpu_percent']) for r in rows):.1f}%")
print(f"Peak 5xx: {max(float(r['http_5xx_percent']) for r in rows):.1f}%")
print(f"Final CPU: {float(rows[-1]['cpu_percent']):.1f}%")
print(f"Final 5xx: {float(rows[-1]['http_5xx_percent']):.1f}%")
