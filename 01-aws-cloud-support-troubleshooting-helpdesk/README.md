# Project 1 — AWS Cloud Support Troubleshooting & Help Desk Lab

## Executive Summary

This project simulates a Tier 1/Tier 2 AWS cloud support queue for a small SaaS company named **Northstar Services**. Eight customer-impacting incidents are triaged, investigated, resolved, validated, and documented. The lab emphasizes the workflow expected of a Cloud Support Associate or Cloud Support Engineer I: understand the symptom, collect evidence, isolate the fault domain, apply the least-risk fix, confirm service restoration, communicate clearly, and record prevention steps.

## Environment

- AWS Region: `us-east-1`
- VPC: `northstar-prod-vpc` — `10.20.0.0/16`
- Public subnet: `10.20.10.0/24`
- Application instance: `ns-web-01`
- Linux: Amazon Linux 2023
- Web service: Nginx on TCP/80
- Storage: S3 bucket `northstar-support-lab-2026`
- DNS zone: `northstar-lab.internal`
- Monitoring: Amazon CloudWatch
- Identity: AWS IAM

## Incident Queue

| ID | Severity | Issue | Root Cause | Final Status |
|---|---|---|---|---|
| INC-001 | P2 | SSH connection failure | TCP/22 absent from security group | Resolved |
| INC-002 | P2 | S3 AccessDenied | Missing `s3:GetObject` permission | Resolved |
| INC-003 | P1 | Website unavailable | Nginx service stopped | Resolved |
| INC-004 | P2 | DNS resolution failure | Incorrect private DNS record | Resolved |
| INC-005 | P2 | High CPU alert | Runaway Python process | Resolved |
| INC-006 | P3 | Analyst cannot view CloudWatch logs | IAM policy missing logs read permissions | Resolved |
| INC-007 | P2 | Disk usage > 90% | Unrotated application logs | Resolved |
| INC-008 | P2 | App health check fails after change | Security group opened wrong port | Resolved |

## Support Workflow Used

1. Acknowledge and assign the ticket.
2. Confirm impact and severity.
3. Reproduce or verify the symptom.
4. Check recent changes.
5. Isolate identity, compute, network, storage, DNS, or application layer.
6. Collect command/configuration evidence.
7. Implement the smallest safe correction.
8. Validate from the customer's perspective.
9. Send a customer-facing resolution note.
10. Record root cause and prevention action.

## Key Skills Demonstrated

AWS EC2, S3, IAM, VPC security groups, Route 53 concepts, CloudWatch, Linux systemd, process investigation, filesystem analysis, AWS CLI, customer communication, incident prioritization, root-cause analysis, and knowledge-base writing.
