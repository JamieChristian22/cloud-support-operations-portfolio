# Project 4 — Cloud Monitoring & Incident Response Lab

## Executive Summary

This project simulates a cloud operations on-call workflow for **Northstar Services**. Monitoring detects abnormal CPU, disk utilization, and application error-rate conditions. The project shows how an operations analyst acknowledges an alert, correlates metrics and logs, determines customer impact, mitigates safely, validates recovery, communicates status, and completes a post-incident review.

## Monitoring Policy

| Signal | Warning | Critical | Action |
|---|---:|---:|---|
| CPU utilization | > 75% for 10 min | > 90% for 5 min | Inspect top processes and recent workload changes |
| Root disk used | > 75% | > 90% | Inspect logs/cache, preserve required data, reclaim safely |
| HTTP 5xx rate | > 2% for 5 min | > 5% for 5 min | Correlate deploys, app logs, dependency health |
| Instance health | n/a | Failed check | Check provider status, host state, reboot/escalate only with approval |

## Major Incident

`IR-001` combines CPU saturation and elevated HTTP 5xx responses after a synthetic load script is mistakenly left running. The incident includes an alert timeline, triage notes, log evidence, mitigation, validation, and postmortem.

## Job Skills Demonstrated

CloudWatch/Azure Monitor/GCP Monitoring concepts, alert thresholds, logs/metrics correlation, incident severity, on-call communication, root-cause analysis, recovery validation, postmortem writing, and operational follow-up.
