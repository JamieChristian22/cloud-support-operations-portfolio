# Configuration Artifacts

This folder contains realistic configuration artifacts used by the AWS Cloud Support Troubleshooting & Help Desk project.

## Files

### `s3-read-policy.json`
Least-privilege S3 read policy used for IAM access troubleshooting.

### `northstar-logrotate.conf`
Linux log rotation policy for the Northstar application and Nginx logs.

### `ec2-web-security-group.json`
Security-group definition demonstrating HTTP/HTTPS access and restricted SSH administration.

### `cloudwatch-high-cpu-alarm.json`
CloudWatch alarm configuration for sustained EC2 CPU utilization at or above 80 percent.

### `northstar-nginx.conf`
Nginx reverse-proxy and health-check configuration for the application workload.

### `northstar-app.service`
Systemd unit showing how the application would be managed and automatically restarted on failure.

## Support Skills Demonstrated

- IAM and least-privilege permissions
- EC2 network access control
- CloudWatch monitoring and alert thresholds
- Linux service management
- Nginx reverse-proxy troubleshooting
- Log management and retention
- Operational configuration documentation

All IDs, domains, and IP addresses are documentation-safe lab values. No production credentials or customer data are included.
