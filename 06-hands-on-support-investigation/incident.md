# INC-2026-001 — Guestbook container unavailable

Date investigated: 2026-11-24. Environment: macOS, Docker Desktop. Simulated priority: P3. Status: investigated, root cause pending.

## Symptoms and scope
Local container youthful_einstein (guestbook:v1) was stopped with exit code 2. Historical logs show it listened on port 3000. No actual customer impact established.

## Investigation
External DNS resolution returned IPv4 addresses; traceroute reached the selected Google destination at hop 9; curl returned HTTP/2 200. Postman Cloud Agent returned HTTP 200 for both Echo requests and echoed both query parameters. These tests do not prove Guestbook health or direct Mac-to-Echo connectivity.

Docker listed four stopped containers, three with exit code 0 and Guestbook with code 2. Logs show six HTTP 200, four HTTP 304 and one HTTP 404 for /favicon.ico. Inspection showed Running=false, OOMKilled=false, PID=0, Error empty and ExitCode=2.

## Root cause
Undetermined. Missing favicon is not established as causal. No recorded OOM kill or Docker state error. Historical successful requests establish prior operation only.

## Next actions
Review application source and exit behavior, configuration and dependencies; verify host listener and port mappings; reproduce in an isolated local environment with approval; validate recovery before closing.

## Resolution
No restart, deletion or configuration change performed during investigation. Recovery not verified. Netstat output not supplied. Escalate with sanitized evidence and outstanding questions.
