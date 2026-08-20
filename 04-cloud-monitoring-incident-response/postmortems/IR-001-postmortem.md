# Postmortem — IR-001

## Summary

On August 19, 2026, the Northstar support web service experienced degraded performance and intermittent HTTP 5xx errors for approximately 29 minutes. Monitoring detected sustained CPU saturation and an elevated 5xx rate. Operations identified a synthetic load process running outside its approved window and stopped it. Service recovered without reboot or data loss.

## What Went Well

- Monitoring detected the issue within five minutes of the critical threshold.
- Provider/instance health was ruled out quickly.
- Metrics and application logs were correlated before making changes.
- The mitigation was low risk and did not require infrastructure replacement.

## What Could Improve

- Test tooling did not enforce a stop time.
- The test occurred in a support environment shared with a customer-facing demonstration workload.
- The change record lacked an explicit rollback/stop condition.

## Root Cause Category

Operational process / change control.

## Follow-Up Owners

- Cloud Operations: implement expiration wrapper for load tests.
- Application Support: move performance tests to dedicated environment.
- Documentation: update change checklist and on-call runbook.
