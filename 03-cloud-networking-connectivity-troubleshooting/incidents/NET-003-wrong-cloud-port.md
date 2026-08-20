# NET-003 — Wrong Cloud Firewall Port

**Symptom:** server was reachable by ICMP-equivalent diagnostics, but HTTPS failed.

`ss -lntp` confirmed the app listened on `0.0.0.0:443`. Cloud security control allowed TCP/80 from `10.60.30.0/24` but had no TCP/443 rule.

**Root cause:** deployment checklist copied an HTTP rule into an HTTPS-only environment.

**Fix:** remove unused TCP/80 access and allow TCP/443 from `10.60.30.0/24`.

**Validation:** TLS handshake and `HTTP/1.1 200 OK` succeeded from operations subnet.
