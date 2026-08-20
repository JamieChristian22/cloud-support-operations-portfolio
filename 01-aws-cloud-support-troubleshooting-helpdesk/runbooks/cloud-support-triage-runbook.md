# Cloud Support Triage Runbook

## 1. Establish Impact

Confirm affected user/service, start time, business impact, and whether the issue is reproducible. Assign P1 when a critical service is unavailable for all users, P2 for material degradation or blocked workflows, and P3 for limited-impact access or informational issues.

## 2. Check Service Health

For EC2: instance state and both status checks. For S3/IAM: reproduce with AWS CLI and capture the exact error. For web applications: test DNS, TCP reachability, HTTP status, then service status on the host.

## 3. Check Recent Changes

Review security-group, IAM, DNS, package, deployment, and maintenance changes made immediately before the issue.

## 4. Isolate the Layer

Work from outside inward: DNS → route/network → security control → host → process/application → data/permissions.

## 5. Correct Safely

Prefer the least-permissive and smallest change that restores service. Avoid broad `0.0.0.0/0` administrative access and avoid wildcard IAM permissions unless strictly required.

## 6. Validate

Repeat the original failing action and verify metrics/logs return to normal. Validation must be from the user or service perspective, not only from the console.

## 7. Close

Document root cause, exact resolution, validation evidence, user communication, and prevention action.
