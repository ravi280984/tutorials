# cloud

Purpose

Provider-agnostic cloud tutorials that demonstrate common patterns for deploying AI workloads, storing datasets, and integrating managed services across AWS and Azure.

Prerequisites

- Python 3.10+
- AWS CLI and/or Azure CLI depending on tutorial

Run instructions

- See provider-specific READMEs in `cloud/aws/` and `cloud/azure/`.
- Each example includes steps for provisioning and teardown to avoid unnecessary costs.

Notes

- Use infrastructure-as-code templates included in provider subfolders where available.
- Use service principals, roles, and managed identities for automation.
