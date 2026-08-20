#!/usr/bin/env python3
import json
from datetime import datetime, timezone

inventory = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "environment": "support-lab",
    "aws": {
        "region": "us-east-1",
        "compute": "EC2",
        "instance": "aws-support-web-01",
        "storage": "northstar-multicloud-aws-2026",
        "monitoring": "CloudWatch"
    },
    "azure": {
        "region": "eastus",
        "compute": "Azure VM",
        "instance": "az-support-web-01",
        "storage": "nssupportlab2026",
        "monitoring": "Azure Monitor"
    },
    "gcp": {
        "region": "us-east1",
        "compute": "Compute Engine",
        "instance": "gcp-support-web-01",
        "storage": "northstar-multicloud-gcp-2026",
        "monitoring": "Cloud Monitoring"
    }
}
print(json.dumps(inventory, indent=2))
