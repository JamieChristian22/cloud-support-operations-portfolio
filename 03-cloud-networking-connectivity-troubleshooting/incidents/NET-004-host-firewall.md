# NET-004 — Host Firewall Blocks HTTPS

**Symptom:** DNS, route table, and cloud security rules were correct, but TCP/443 timed out.

On-host inspection showed `firewalld` active with port 443 absent from the permitted services.

```bash
sudo firewall-cmd --list-all
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

**Root cause:** host firewall policy was not updated after the service changed from HTTP to HTTPS.

**Validation:** TCP/443 connection and HTTPS request succeeded externally; host firewall remained enabled.
