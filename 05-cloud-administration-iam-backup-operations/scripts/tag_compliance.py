#!/usr/bin/env python3
resources = [
    {"id":"i-0a1b2c3d4e5f60718","type":"ec2","tags":{"environment":"support-lab","owner":"cloud-operations","cost-center":"learning"}},
    {"id":"northstar-admin-backup-2026","type":"s3","tags":{"environment":"support-lab","owner":"cloud-operations","cost-center":"learning"}},
    {"id":"vol-0123456789abcdef0","type":"ebs","tags":{"environment":"support-lab","owner":"cloud-operations"}},
]
required = {"environment","owner","cost-center"}
failed = 0
for r in resources:
    missing = required - set(r["tags"])
    status = "PASS" if not missing else f"FAIL missing={','.join(sorted(missing))}"
    failed += bool(missing)
    print(f"{r['type']:4} {r['id']}: {status}")
print(f"Compliance: {len(resources)-failed}/{len(resources)} resources fully tagged")
