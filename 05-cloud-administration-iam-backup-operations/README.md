# Project 5 — Cloud Administration, IAM & Backup Operations Lab

## Executive Summary

This project simulates the day-to-day work of a Junior Cloud Administrator or Cloud Administrator I. It combines identity lifecycle administration, least-privilege role design, storage protection, backup verification, restore testing, resource tagging, and routine operational checks.

## Organization

Company: **Northstar Services**  
Environment: `support-lab`  
Primary cloud pattern: AWS terminology with equivalent Azure/GCP notes in documentation.

## Administrative Personas

| Persona | Access Need | Design |
|---|---|---|
| `cloud-ops-admin` | Administer support lab | Scoped administrative role, MFA required |
| `ops-analyst` | Read metrics/logs and reports | Read-only monitoring + report object read |
| `app-support` | Restart app service and inspect logs | Compute/session access without IAM administration |
| `backup-operator` | Run/verify backups and restores | Backup/storage actions only |

## Operational Workflows

1. New-user access request and role assignment.
2. Access denied investigation and least-privilege correction.
3. Quarterly access review.
4. S3 versioning and lifecycle protection.
5. Backup inventory verification.
6. Restore test to a separate recovery prefix.
7. Tag compliance review.
8. Daily health checklist.

## Job Skills Demonstrated

IAM/RBAC, least privilege, MFA policy, access reviews, S3 versioning/lifecycle concepts, backup and recovery, AWS CLI, PowerShell-style administrative thinking, audit documentation, change control, tagging, and operational checklists.
