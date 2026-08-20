# NET-001 — Wrong DNS Record

**Symptom:** `curl https://web01.corp.northstar.internal` timed out.

`dig +short` returned `10.60.20.52`, but inventory showed the active server at `10.60.20.25`. Direct connection to `10.60.20.25:443` succeeded.

**Root cause:** stale A record from a retired instance.

**Fix:** update A record to `10.60.20.25` and flush client resolver cache.

**Validation:** DNS returns `10.60.20.25`; HTTPS returns `200 OK`.
