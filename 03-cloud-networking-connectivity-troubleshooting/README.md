# Project 3 — Cloud Networking & Connectivity Troubleshooting Lab

## Executive Summary

This project focuses on one of the most common cloud-support responsibilities: determining why a user or service cannot reach a cloud resource. Four real-world incident scenarios isolate faults across DNS, routing, security controls, and application ports.

## Lab Network

- VPC/VNet-style CIDR: `10.60.0.0/16`
- Public subnet: `10.60.10.0/24`
- Private application subnet: `10.60.20.0/24`
- Operations subnet: `10.60.30.0/24`
- Web server: `10.60.20.25`
- Internal DNS name: `web01.corp.northstar.internal`
- Expected application port: TCP/443

## Troubleshooting Method

`DNS → IP route → network ACL/firewall → security group/NSG → host firewall → listening process → application response`

## Scenarios

1. DNS points to the wrong private IP.
2. Route table lacks return path to operations subnet.
3. Security control allows TCP/80 while application listens on TCP/443.
4. Host firewall blocks TCP/443 even though cloud security controls are correct.

## Skills Demonstrated

DNS, CIDR/subnetting, route tables, security groups/NSGs/firewalls, `dig`, `nslookup`, `curl`, `ss`, `ip route`, `traceroute`, TCP port testing, structured fault isolation, and change validation.
