# Backup and Restore Test Runbook

## Objective

Verify that a protected report object can be recovered without overwriting the current copy.

## Source

`s3://northstar-admin-backup-2026/backups/2026-08-19/customer-summary.csv`

## Recovery Target

`s3://northstar-admin-backup-2026/recovery-tests/2026-08-19/customer-summary.csv`

## Procedure

1. Confirm bucket versioning is enabled.
2. Record the source object's version ID and checksum.
3. Copy the selected version to the recovery-test prefix.
4. Download the recovered object.
5. Compare SHA-256 checksum with the recorded source checksum.
6. Record result and delete only the temporary recovery-test copy after sign-off.

## Success Criteria

- Correct historical object version recovered.
- SHA-256 checksum matches.
- Current production-like copy unchanged.
- Recovery result documented.
