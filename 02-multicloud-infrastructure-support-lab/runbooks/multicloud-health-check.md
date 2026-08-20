# Multi-Cloud Health Check Runbook

## AWS

```bash
aws ec2 describe-instances --region us-east-1 --filters Name=tag:environment,Values=support-lab
aws s3api head-bucket --bucket northstar-multicloud-aws-2026
aws cloudwatch describe-alarms --region us-east-1 --state-value ALARM
```

Expected state: compute `running`, storage reachable, no unresolved alarms.

## Azure

```bash
az vm list -g rg-support-lab-eastus -d -o table
az storage account show -g rg-support-lab-eastus -n nssupportlab2026
az monitor metrics alert list -g rg-support-lab-eastus -o table
```

Expected state: VM `PowerState/running`, storage account `Succeeded`, no active critical metric alerts.

## GCP

```bash
gcloud compute instances list --filter='labels.environment=support-lab'
gcloud storage buckets describe gs://northstar-multicloud-gcp-2026
gcloud monitoring policies list
```

Expected state: instance `RUNNING`, bucket accessible, no unresolved critical alert policies firing.
