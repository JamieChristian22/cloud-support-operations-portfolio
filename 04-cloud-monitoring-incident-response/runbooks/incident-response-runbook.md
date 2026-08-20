# Incident Response Runbook

## Detect and Acknowledge

Record alert name, resource, threshold, first-breach time, and current customer impact. Assign severity before troubleshooting.

## Stabilize

Confirm provider/service health and instance health. Avoid rebooting or scaling blindly until the fault domain is understood unless the service is in immediate danger and the approved emergency procedure requires it.

## Investigate

Correlate metrics, logs, recent changes, process/resource usage, and dependency health. Capture timestamps so evidence can be aligned.

## Mitigate

Choose the least-disruptive action likely to restore service. Record who approved the action when required.

## Validate

Use a defined clean window. For this lab: CPU below 50%, 5xx below 1%, successful external health checks, and no new error burst for 10 minutes.

## Communicate and Close

Send a concise impact/status update, then complete a root-cause statement and corrective actions with owners.
