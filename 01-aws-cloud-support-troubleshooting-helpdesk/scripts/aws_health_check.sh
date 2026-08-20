#!/usr/bin/env bash
set -euo pipefail
REGION="us-east-1"
INSTANCE_ID="i-0a1b2c3d4e5f60718"
BUCKET="northstar-support-lab-2026"

echo "== EC2 State =="
aws ec2 describe-instances --region "$REGION" --instance-ids "$INSTANCE_ID" \
  --query 'Reservations[0].Instances[0].[State.Name,PrivateIpAddress,PublicIpAddress]' --output table

echo "== Instance Status Checks =="
aws ec2 describe-instance-status --region "$REGION" --instance-ids "$INSTANCE_ID" \
  --query 'InstanceStatuses[0].[InstanceStatus.Status,SystemStatus.Status]' --output table

echo "== S3 Reachability =="
aws s3api head-bucket --bucket "$BUCKET" && echo "Bucket reachable"
