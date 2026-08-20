# INC-004 — DNS Resolution Failure

**Priority:** P2  
**Status:** Resolved  
**Service:** DNS  
**Impact:** Internal users could not resolve `app.northstar-lab.internal`.

## Investigation

```text
$ dig +short app.northstar-lab.internal
10.20.10.52
```

The active application server address was `10.20.10.25`. The DNS A record still pointed to a retired host.

## Root Cause

The DNS record was not updated during the prior instance replacement.

## Resolution

Changed the A record from `10.20.10.52` to `10.20.10.25` and retained a 60-second TTL for the lab.

## Validation

```text
$ dig +short app.northstar-lab.internal
10.20.10.25
$ curl -I http://app.northstar-lab.internal
HTTP/1.1 200 OK
```

## Prevention

Include DNS validation in replacement/decommission change plans.
