# INC-007 — Disk Usage Above 90%

**Priority:** P2  
**Status:** Resolved  
**Service:** EC2 / Linux Storage  
**Impact:** Risk of application failure due to low root-volume free space.

## Investigation

```text
$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1       20G   19G  1.0G  95% /

$ sudo du -xhd1 /var | sort -h
180M /var/cache
16G  /var/log
```

`/var/log/northstar/app.log` had grown to 14 GB because log rotation was disabled.

## Root Cause

Application logging had no active rotation policy.

## Resolution

Compressed and retained the most recent seven daily logs, removed obsolete test logs, and installed `config/northstar-logrotate.conf`.

## Validation

```text
/dev/xvda1       20G  6.2G   14G  32% /
```

## Prevention

Monitor filesystem utilization at 75% warning and 90% critical thresholds and enforce log rotation.
