# Azure and GCP Administrative Equivalents

| Admin Task | AWS | Azure | GCP |
|---|---|---|---|
| User/role access | IAM roles/policies | Entra ID + Azure RBAC | Cloud IAM roles |
| MFA / strong auth | IAM Identity Center / account controls | Entra Conditional Access/MFA | Google identity/MFA controls |
| Object protection | S3 Versioning | Blob versioning | Object Versioning |
| Lifecycle | S3 Lifecycle | Blob lifecycle management | Cloud Storage lifecycle |
| Audit | CloudTrail | Activity Log | Cloud Audit Logs |
| Resource tags | Tags | Tags | Labels |

The operational principle is the same across providers: grant the minimum access needed, make changes auditable, protect recoverable data, and verify restoration rather than assuming backups are valid.
