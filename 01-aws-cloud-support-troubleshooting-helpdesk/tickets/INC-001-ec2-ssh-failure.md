# INC-001 — EC2 SSH Connection Failure

**Priority:** P2  
**Status:** Resolved  
**Service:** EC2 / Network Security  
**Reporter:** Application Support  
**Impact:** Support engineer could not access `ns-web-01` for maintenance.

## Customer Report

`ssh: connect to host 203.0.113.25 port 22: Operation timed out`

## Triage

The instance showed `running` with both system and instance status checks passing. HTTP service remained available, indicating the instance itself was reachable and the failure was specific to SSH connectivity.

## Investigation

```bash
aws ec2 describe-instances \
  --instance-ids i-0a1b2c3d4e5f60718 \
  --query 'Reservations[0].Instances[0].[State.Name,PublicIpAddress,SecurityGroups[0].GroupId]' \
  --output table
```

Observed result:

```text
---------------------------------
|       DescribeInstances       |
+-------------------------------+
| running                       |
| 203.0.113.25                  |
| sg-0a11bb22cc33dd44e          |
+-------------------------------+
```

Security-group review showed inbound TCP/80 and TCP/443 only. TCP/22 was not permitted from the support jump IP `198.51.100.24/32`.

## Root Cause

A prior hardening change removed the SSH ingress rule and did not preserve access from the approved support IP.

## Resolution

Added a restricted ingress rule for TCP/22 from `198.51.100.24/32` only.

```bash
aws ec2 authorize-security-group-ingress \
  --group-id sg-0a11bb22cc33dd44e \
  --protocol tcp --port 22 --cidr 198.51.100.24/32
```

## Validation

```text
$ ssh ec2-user@203.0.113.25
Last login: Wed Aug 19 18:14:31 2026 from 198.51.100.24
[ec2-user@ns-web-01 ~]$
```

## Customer-Facing Resolution

SSH access to `ns-web-01` has been restored. The instance was healthy; the issue was an inbound security-group rule that no longer allowed SSH from the approved support IP. Access was restored using a restricted `/32` rule, and the web service was not interrupted.

## Prevention

Add a security-group change checklist requiring validation of approved administrative access paths before closing network hardening changes.
