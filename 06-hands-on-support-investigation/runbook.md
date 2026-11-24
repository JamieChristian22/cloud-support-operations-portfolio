# Diagnostic runbook (macOS)

Run one step at a time; collect evidence before changes.

| Command | Purpose |
|---|---|
| `ping -c 4 8.8.8.8` | Basic ICMP reachability; failure can reflect filtering |
| `dig google.com` | Detailed DNS query, records, resolver and timing |
| `nslookup google.com` | Quick DNS verification |
| `traceroute -n -m 15 -w 2 google.com` | Responding network hops; asterisks alone do not prove outage |
| `curl -I https://www.google.com` | HTTP HEAD response and headers |
| `docker ps -a` | List running and stopped containers |
| `docker logs --tail 20 youthful_einstein` | Read recent captured logs |
| `docker inspect --format '{{json .State}}' youthful_einstein` | Read runtime state |
| `netstat -an -p tcp \| grep '\.3000 .*LISTEN'` | Check matching host TCP listener; not container-internal networking |

## API testing
In Postman select GET, enter https://postman-echo.com/get and Send. Add Params role=cloud-support and status=active; resend and inspect args. Query syntax: ? begins parameters, = assigns value, & separates parameters. GET retrieves; POST submits; PUT replaces; PATCH partially updates; DELETE removes. For incorrect filters inspect query parameters and response before changing DNS.

## Interpretation
200 success; 301 redirect; 304 not modified; 400 bad request; 401 authentication required; 403 forbidden; 404 missing resource; 429 rate limit; 500 server error; 502 bad gateway; 503 unavailable; 504 gateway timeout. Successful DNS does not guarantee HTTP health. Nonzero container exit requires investigation, not automatic deletion.

Do not publish cookies, credentials or raw headers. No cloud deployment required.
