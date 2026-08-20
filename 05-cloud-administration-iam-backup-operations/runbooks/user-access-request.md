# User Access Request Runbook

## Example Request

**User:** Maya Reed  
**Department:** Operations  
**Requested persona:** `ops-analyst`  
**Business need:** Read CloudWatch metrics/logs and download operational CSV reports.  
**Approval:** Operations Manager  
**MFA:** Required before role use.

## Procedure

1. Confirm manager approval and business purpose.
2. Map request to existing role before creating any new policy.
3. Verify the role does not include write/delete/admin permissions.
4. Assign access and require MFA.
5. Test the intended actions: read metrics, read logs, download report.
6. Test a prohibited action: IAM administration must remain denied.
7. Record access-review date.

## Validation

Expected allowed: monitoring read, log read, report download.  
Expected denied: create IAM user, delete S3 bucket, modify security groups.
