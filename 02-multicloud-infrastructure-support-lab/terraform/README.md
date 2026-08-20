# Terraform Notes

This directory encodes a small multi-cloud support baseline. It intentionally contains **no credentials or secrets**. Authentication is expected through each provider's normal CLI/session mechanism. Resource names, regions, CIDRs, and tags are fully specified; cloud account/subscription/project authentication remains external by design.

Before use, review provider costs and replace the GCP `project` value only if applying in your own account. The checked-in configuration is portfolio code, not evidence that resources were deployed in a live account.
