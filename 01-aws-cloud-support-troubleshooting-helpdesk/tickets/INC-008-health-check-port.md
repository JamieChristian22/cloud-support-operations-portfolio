# INC-008 — Health Check Fails After Change

**Priority:** P2  
**Status:** Resolved  
**Service:** EC2 / Security Group  
**Impact:** Application health check failed immediately after a network change.

## Investigation

Nginx listened on TCP/80 and responded locally. The security-group change ticket intended to allow health checks on TCP/80 but added TCP/8080 instead.

```text
$ sudo ss -lntp | grep nginx
LISTEN 0 511 0.0.0.0:80 0.0.0.0:* users:(("nginx",pid=1044,fd=6))
```

## Root Cause

Incorrect destination port in the security-group rule.

## Resolution

Removed TCP/8080 rule and added TCP/80 from the health-check source CIDR `10.20.20.0/24`.

## Validation

Three consecutive health checks returned `200 OK` and the target state returned to healthy.

## Prevention

Require source/destination/port validation in network-change peer review.
