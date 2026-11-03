"""Offline incident-triage regression cases. No cloud resources are contacted."""
import csv
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "04-cloud-monitoring-incident-response/scripts/analyze_metrics.py"
spec = importlib.util.spec_from_file_location("monitoring_analysis", MODULE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def row(stamp, cpu, errors, disk=40):
    return {"timestamp": stamp, "cpu_percent": str(cpu),
            "http_5xx_percent": str(errors), "disk_used_percent": str(disk)}


class MonitoringDiagnosticsTests(unittest.TestCase):
    def test_real_synthetic_evidence_has_correlated_incident_and_recovery(self):
        with module.SOURCE.open(encoding="utf-8-sig", newline="") as file:
            result = module.analyze_metrics(list(csv.DictReader(file)))
        self.assertEqual(result["samples"], 7)
        self.assertEqual(result["cpu_breaches"], 3)
        self.assertEqual(result["http_5xx_breaches"], 3)
        self.assertEqual(result["correlated_breaches"], 3)
        self.assertEqual(result["sustained_windows"], 1)
        window = result["alert_windows"][0]
        self.assertEqual(window["samples"], 3)
        self.assertEqual(window["next_normal_sample"], "2026-08-19T18:22:00-04:00")

    def test_short_spike_is_not_sustained(self):
        samples = [row("2026-01-01T00:00:00+00:00", 91, 2),
                   row("2026-01-01T00:05:00+00:00", 40, 0)]
        result = module.analyze_metrics(samples)
        self.assertEqual(result["sustained_windows"], 0)
        self.assertFalse(result["alert_windows"][0]["sustained_alert"])

    def test_open_incident_has_no_claimed_recovery(self):
        samples = [row("2026-01-01T00:00:00+00:00", 91, 1),
                   row("2026-01-01T00:05:00+00:00", 95, 8)]
        result = module.analyze_metrics(samples)
        self.assertIsNone(result["alert_windows"][0]["next_normal_sample"])

    def test_missing_bad_and_non_monotonic_samples_fail_closed(self):
        bads = [
            [],
            [row("bad-timestamp", 50, 2)],
            [row("2026-01-01T00:00:00", 50, 2)],
            [row("2026-01-01T00:00:00+00:00", float("nan"), 2)],
            [row("2026-01-01T00:00:00+00:00", 101, 2)],
            [row("2026-01-01T00:05:00+00:00", 10, 1),
             row("2026-01-01T00:03:00+00:00", 12, 1)],
        ]
        for records in bads:
            with self.subTest(records=records), self.assertRaises(ValueError):
                module.analyze_metrics(records)


if __name__ == "__main__":
    unittest.main()
