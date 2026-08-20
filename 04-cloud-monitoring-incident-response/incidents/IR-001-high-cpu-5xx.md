# IR-001 — CPU Saturation and Elevated HTTP 5xx

**Severity:** SEV-2  
**Start:** 2026-08-19 18:02 EDT  
**Detected:** 2026-08-19 18:07 EDT  
**Mitigated:** 2026-08-19 18:24 EDT  
**Resolved:** 2026-08-19 18:31 EDT  
**Customer impact:** Intermittent slow responses and 7.8% HTTP 5xx errors for the lab web service.

## Alert

- CPU > 90% for 5 minutes
- HTTP 5xx > 5% for 5 minutes

## Timeline

- **18:07** Alert acknowledged; incident opened.
- **18:09** Instance/provider health checks normal; CPU 96%.
- **18:12** Application logs show request backlog but no dependency outage.
- **18:15** `ps` identifies `python3 /opt/northstar/tools/load-test.py` at ~91% CPU.
- **18:18** Change review finds a synthetic test started at 17:55 with no stop time.
- **18:21** Load process stopped after confirming it was non-production support tooling.
- **18:24** CPU falls below 35%; 5xx rate begins normalizing.
- **18:31** 10-minute validation window clean; incident resolved.

## Root Cause

A synthetic load test was launched against the support application environment and left active beyond its test window. The test consumed CPU, causing request queueing and elevated 5xx responses.

## Mitigation

Stopped the synthetic load process and removed the temporary cron entry. No instance reboot was required.

## Validation

- CPU: 21–28% during validation
- HTTP 5xx: 0.2%
- Three external health checks: 200 OK
- No new application error bursts in logs

## Corrective Actions

1. Run synthetic load only in isolated test environments.
2. Require automatic expiration for temporary test jobs.
3. Alert on unexpected sustained process CPU above 80%.
4. Add a change-ticket field for test end time.
