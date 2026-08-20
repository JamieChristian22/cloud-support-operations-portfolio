# Cross-Cloud Troubleshooting Matrix

| Symptom | AWS Check | Azure Check | GCP Check |
|---|---|---|---|
| VM unavailable | EC2 state/status checks | VM power state / boot diagnostics | Instance status / serial console output |
| Port blocked | Security Group / NACL | NSG | VPC firewall rule |
| Storage denied | IAM + bucket policy | RBAC + container access | IAM + bucket policy |
| CPU high | CloudWatch CPUUtilization | Azure Monitor Percentage CPU | Cloud Monitoring CPU utilization |
| Identity denied | IAM policy simulator / CloudTrail | Activity Log + role assignment | Policy Troubleshooter / Audit Logs |
| DNS wrong | Route 53 / resolver checks | Azure DNS / private DNS | Cloud DNS |

## Escalation Rule

Escalate when the fault is provider-side, requires permissions beyond the support role, risks destructive data loss, or remains unresolved after the documented isolation steps. Include timestamps, request/error IDs, affected resources, commands already run, and all configuration changes in the escalation note.
