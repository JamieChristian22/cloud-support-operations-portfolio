#!/usr/bin/env bash
set -euo pipefail
REGION="us-east-1"
BUCKET="northstar-admin-backup-2026"

echo "== Unresolved EC2 Status Issues =="
aws ec2 describe-instance-status --region "$REGION" --include-all-instances \
  --query 'InstanceStatuses[?InstanceStatus.Status!=`ok` || SystemStatus.Status!=`ok`].[InstanceId,InstanceStatus.Status,SystemStatus.Status]' \
  --output table

echo "== Bucket Versioning =="
aws s3api get-bucket-versioning --bucket "$BUCKET"

echo "== Critical CloudWatch Alarms =="
aws cloudwatch describe-alarms --region "$REGION" --state-value ALARM --output table
