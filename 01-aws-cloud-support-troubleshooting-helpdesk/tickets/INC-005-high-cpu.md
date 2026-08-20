# INC-005 — High CPU Utilization

**Priority:** P2  
**Status:** Resolved  
**Service:** EC2 / CloudWatch  
**Impact:** Response times increased and CPU alarm exceeded 90% for 10 minutes.

## Investigation

CloudWatch showed CPU rising from 18% baseline to 96%. On-host process review:

```text
$ ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head
  PID COMMAND         %CPU %MEM
 7821 python3         91.4  1.8
 1044 nginx            1.2  0.8
```

`/opt/northstar/tools/load-test.py` was running outside an approved test window.

## Root Cause

A forgotten synthetic load test continued running on the production-like support instance.

## Resolution

Stopped PID 7821, removed the temporary cron entry, and verified no service dependency on the process.

## Validation

CPU returned below 25% within five minutes and application latency normalized.

## Prevention

Move load tests to an isolated test instance and require expiration on temporary cron jobs.
