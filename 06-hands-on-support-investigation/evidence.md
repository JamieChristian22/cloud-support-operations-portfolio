# Sanitized observations

Manually transcribed from screenshots reviewed during guided training, not raw machine exports.

| Test | Observation | Evidence status |
|---|---|---|
| Ping | Lesson covered | Output unverified |
| Dig | User reported execution | Output unverified |
| Nslookup | Multiple IPv4 answers | Screenshot |
| Traceroute | Destination reached at hop 9; one unanswered probe at hop 8 | Screenshot |
| Curl | HTTP/2 200 | Screenshot |
| Postman GET | 200 OK, 254 ms, 1.2 KB | Screenshot |
| Postman GET with params | 200 OK, 167 ms, 1.39 KB | Screenshot |
| Docker ps -a | 4 stopped, 0 running, 1 nonzero exit | Screenshot |
| Docker logs | Listening on :3000; 6 HTTP 200, 4 HTTP 304, 1 HTTP 404 | Screenshot |
| Docker inspect | Exited, exit code 2, OOMKilled false, Error empty | Screenshot |
| Netstat | Host listener concept covered | Output unverified |

## Echo response excerpt
```json
{"args":{"role":"cloud-support","status":"active"}}
```

## Container inventory
| Image | Exit code |
|---|---|
| hello-world | 0 |
| guestbook:v1 | 2 |
| cloud-insurance-app:1.0 | 0 |
| cloud-insurance-app:1.0 | 0 |

Historical Guestbook logs (June 9, 2026) show requests to /, /style.css, /script.js, /jquery.min.js, /lrange/guestbook and /favicon.ico. The favicon returned 404; no causal crash evidence visible. State inspection on November 24 confirms stopped state. Two API latency samples do not establish performance improvement.

Raw screenshots excluded because they contain cookies and identifiers. No production data or remediation claims.
