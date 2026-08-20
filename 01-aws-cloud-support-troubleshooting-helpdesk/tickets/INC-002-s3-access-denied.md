# INC-002 — S3 AccessDenied

**Priority:** P2  
**Status:** Resolved  
**Service:** Amazon S3 / IAM  
**Reporter:** Operations Analyst  
**Impact:** Analyst could list the bucket but could not download a daily CSV report.

## Symptom

```text
An error occurred (AccessDenied) when calling the GetObject operation: Access Denied
```

## Investigation

The user `ops-analyst` successfully ran `aws s3 ls s3://northstar-support-lab-2026/`, proving bucket listing permission. Policy review showed `s3:ListBucket` but no object-level `s3:GetObject` permission.

## Root Cause

The IAM policy contained bucket-level permission only. S3 object actions require the object ARN pattern `arn:aws:s3:::northstar-support-lab-2026/*`.

## Resolution

Applied the least-privilege read policy stored in `config/s3-read-policy.json`.

## Validation

```text
$ aws s3 cp s3://northstar-support-lab-2026/reports/daily-2026-08-19.csv .
download: s3://northstar-support-lab-2026/reports/daily-2026-08-19.csv to ./daily-2026-08-19.csv
```

## Customer-Facing Resolution

Report downloads are working again. Your role could list the bucket but did not include permission to read objects. Read-only access was added only for objects in the reporting bucket.

## Prevention

Review bucket-level versus object-level ARNs during IAM policy peer review.
