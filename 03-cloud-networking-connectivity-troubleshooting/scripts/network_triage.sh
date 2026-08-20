#!/usr/bin/env bash
set -euo pipefail
HOST="web01.corp.northstar.internal"
IP="10.60.20.25"
PORT="443"

echo "== DNS =="
getent hosts "$HOST" || true

echo "== Route =="
ip route get "$IP" || true

echo "== TCP Test =="
timeout 3 bash -c "</dev/tcp/$IP/$PORT" && echo "TCP $PORT reachable" || echo "TCP $PORT blocked/unreachable"

echo "== HTTPS =="
curl -k -sS -o /dev/null -w 'HTTP %{http_code}\n' --connect-timeout 3 "https://$HOST" || true
