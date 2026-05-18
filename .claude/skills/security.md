# Skill: Security Checks

Apply these checks to every Terraform plan or changed `.tf` file.

## S3

| Check | Severity |
|-------|---------|
| `block_public_acls`, `block_public_policy`, `ignore_public_acls`, `restrict_public_buckets` are all `true` | BLOCK if any is `false` |
| `aws_s3_bucket_server_side_encryption_configuration` present | BLOCK if missing |
| Bucket name not hardcoded with account ID or environment string | WARN |

## IAM

| Check | Severity |
|-------|---------|
| No `"Action": "*"` in any policy | BLOCK |
| No `"Resource": "*"` paired with write/delete actions | BLOCK |
| No inline policies on users — use roles | WARN |
| No IAM access keys created via Terraform | WARN |

## Networking

| Check | Severity |
|-------|---------|
| No security group with `0.0.0.0/0` on ingress ports other than 80/443 | BLOCK |
| No RDS / ElastiCache instance with `publicly_accessible = true` | BLOCK |
| VPC flow logs enabled if a VPC is created | WARN |

## General

| Check | Severity |
|-------|---------|
| No credentials, tokens, or secrets in any variable `default` | BLOCK |
| No hardcoded AWS account IDs | WARN |
| KMS key used for sensitive resources (RDS, Secrets Manager, SSM) | WARN |
| `deletion_protection = true` on RDS and DynamoDB in production | WARN |
