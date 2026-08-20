# INC-006 — Analyst Cannot Read CloudWatch Logs

**Priority:** P3  
**Status:** Resolved  
**Service:** IAM / CloudWatch Logs  
**Impact:** Operations analyst could view metrics but could not open application log streams.

## Investigation

IAM simulator testing showed `logs:DescribeLogGroups` allowed but `logs:GetLogEvents` denied.

## Root Cause

The read-only operations policy had incomplete CloudWatch Logs permissions.

## Resolution

Added `logs:DescribeLogStreams`, `logs:GetLogEvents`, and `logs:FilterLogEvents` for `/northstar/support/*` log groups only.

## Validation

Analyst successfully opened `/northstar/support/nginx` and filtered events without write permission.

## Prevention

Use a tested role-permission matrix for each support persona.
