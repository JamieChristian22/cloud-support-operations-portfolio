# Network Troubleshooting Runbook

1. **Resolve the name.** Compare DNS output with the expected current IP.
2. **Test the IP directly.** If direct IP works but hostname fails, stay in DNS.
3. **Inspect route selection.** Confirm both forward and return paths.
4. **Check cloud controls.** Validate source CIDR, protocol, destination port, and rule direction.
5. **Check host controls.** Confirm OS firewall and listening socket.
6. **Check application.** Use `curl -v` or protocol-specific client to validate end-to-end response.
7. **Retest from original source.** Do not close based only on localhost success.

## Escalation Evidence

Include source IP, destination IP/name, destination port, timestamp, DNS answer, route output, security-control IDs, host firewall status, and the exact client error.
