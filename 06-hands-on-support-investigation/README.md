# Hands-on network, API and container support investigation

**November 24, 2026 | Guided local lab | No cloud resources deployed**

This lab documents actual local diagnostics and public endpoint tests, distinct from the repository's synthetic scenarios. The Guestbook incident is an investigation of a historical local container exit, not a production customer outage.

- [Incident report](incident.md)
- [Command runbook](runbook.md)
- [Sanitized observations](evidence.md)
- [Postman collection](postman-collection.json) (reconstructed from verified requests; not an original export)

Skills: DNS, TCP/IP, HTTP, REST APIs, query parameters, Docker logs, runtime inspection, evidence-based escalation.

Outcome: external connectivity and API requests succeeded; Guestbook exit cause and recovery remain unconfirmed. Ping and dig were covered/reported, but their outputs were not inspected; netstat execution and local report saving were not verified.
