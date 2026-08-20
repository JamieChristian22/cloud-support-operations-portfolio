# NET-002 — Missing Return Route

**Symptom:** operations client `10.60.30.15` could send traffic toward `10.60.20.25`, but sessions timed out.

Route inspection on the application side showed no path for `10.60.30.0/24`. The route table contained local routes only.

**Root cause:** return route to the operations subnet was omitted during network segmentation.

**Fix:** add `10.60.30.0/24` through the internal transit/peering path used by the lab design.

**Validation:** bidirectional path confirmed with TCP/443 test and application request.
