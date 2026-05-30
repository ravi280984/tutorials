# cloud/aws

Purpose

AWS-focused tutorials: deploying models to EC2/ECS, using S3 for storage, and examples of using AWS managed services with AI workloads.

Prerequisites

- AWS account and CLI configured
- Python 3.10+
- AWS IAM permissions for resources used in each tutorial

Run instructions

- Follow individual guides in this folder. Typical steps include:
  1. Configure AWS CLI: `aws configure`
  2. Deploy CloudFormation/Terraform/AWS CDK templates (see each tutorial).

Notes

- Do not commit AWS credentials. Use environment variables or IAM roles.
- Clean up resources after experiments to avoid costs.
