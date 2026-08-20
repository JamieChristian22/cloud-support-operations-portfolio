# INC-003 — Website Unavailable

**Priority:** P1  
**Status:** Resolved  
**Service:** EC2 / Nginx  
**Impact:** Customer web page returned a connection error.

## Investigation

Network path and security group were valid. Instance status checks were healthy. On-host service review found Nginx inactive.

```text
$ sudo systemctl status nginx
○ nginx.service - nginx web server
   Loaded: loaded
   Active: inactive (dead) since Wed 2026-08-19 18:33:12 EDT
```

Journal review showed the service had been manually stopped during a package-maintenance test.

## Root Cause

Nginx was stopped and not restarted after maintenance.

## Resolution

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl is-active nginx
```

## Validation

```text
active
HTTP/1.1 200 OK
Server: nginx
```

## Customer-Facing Resolution

The website is available again. Infrastructure and network checks were healthy; the Nginx service on the application server had remained stopped after maintenance. The service was restarted, enabled at boot, and verified with an HTTP 200 response.

## Prevention

Add a post-maintenance service validation step to the maintenance runbook.
