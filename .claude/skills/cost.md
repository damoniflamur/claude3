# Skill: Cost Checks

Apply these checks to every Terraform plan or changed `.tf` file.

## S3

| Check | Severity |
|-------|---------|
| `aws_s3_bucket_lifecycle_configuration` present to transition or expire objects | WARN if missing |
| `bucket_key_enabled = true` in encryption config (reduces KMS API costs) | INFO if missing |
| Intelligent-Tiering considered for buckets with unpredictable access patterns | INFO |

## EC2 / Compute

| Check | Severity |
|-------|---------|
| No `t2.*` instance types — prefer `t3.*` or `t4g.*` (better price/perf) | WARN |
| Spot instances or savings plans considered for non-critical workloads | INFO |
| `ebs_optimized = true` on instances that support it | WARN if missing |
| No unattached EBS volumes (`aws_ebs_volume` without an attachment resource) | WARN |

## RDS

| Check | Severity |
|-------|---------|
| `multi_az = false` in non-production (avoids 2x cost) | INFO |
| Automated backups retention ≤ 7 days in dev/staging | INFO |
| Aurora Serverless v2 considered for variable-load databases | INFO |

## General

| Check | Severity |
|-------|---------|
| Resources that will be destroyed and recreated (`-/+`) flagged for cost impact | WARN |
| NAT Gateway present — flag as high cost (~$32/month + data transfer) | INFO |
| No CloudWatch log groups without `retention_in_days` set (unbounded storage) | WARN |
