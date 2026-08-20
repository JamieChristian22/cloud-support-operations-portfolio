# Project 2 — Multi-Cloud Infrastructure Support Lab

## Executive Summary

This project demonstrates operational support across AWS, Microsoft Azure, and Google Cloud Platform using a standardized application pattern: one small Linux compute instance, one private object-storage location, identity-controlled administrative access, and monitoring. The emphasis is not on advanced architecture; it is on recognizing equivalent services, validating configuration consistently, and supporting common compute/storage/IAM issues across providers.

## Standardized Lab Design

| Capability | AWS | Azure | GCP |
|---|---|---|---|
| Compute | EC2 | Azure VM | Compute Engine |
| Object storage | S3 | Blob Storage | Cloud Storage |
| Identity | IAM | Entra ID + Azure RBAC | Cloud IAM |
| Network | VPC | VNet | VPC |
| Monitoring | CloudWatch | Azure Monitor | Cloud Monitoring |
| CLI | AWS CLI | Azure CLI | gcloud |

## Naming Standard

- Environment: `support-lab`
- Region: AWS `us-east-1`, Azure `eastus`, GCP `us-east1`
- Application port: TCP/80
- Admin access: restricted, no open SSH from the internet in the documented design
- Tags/labels: `environment=support-lab`, `owner=cloud-operations`, `cost-center=learning`

## Operational Tasks Demonstrated

1. Inventory compute resources.
2. Verify power/state and IP assignment.
3. Verify storage existence and access policy.
4. Verify least-privilege identity configuration.
5. Check monitoring/health signals.
6. Compare equivalent services across clouds.
7. Use Terraform to encode a reproducible baseline for provider-neutral support practice.

## Job Relevance

This project supports interviews for Cloud Support Associate, Cloud Operations Associate, Cloud Support Specialist, Junior Cloud Administrator, and Cloud Operations Analyst by proving multi-cloud vocabulary plus hands-on operational thinking.
