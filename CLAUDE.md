# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does
Manages AWS infrastructure (VPC, EC2, S3) with reusable Terraform modules across dev and prod environments.

## Rules
- Never run `terraform apply` without explicit user approval
- Always run `terraform fmt` and `terraform validate` before planning
- Never touch prod without explicit confirmation
- Tag every resource: `env`, `project`, `owner`
- Never edit modules directly per environment — modules in `terraform/modules/` are shared

## Commands
Always `cd` into the target environment before running Terraform:

```bash
cd terraform/environments/dev   # or prod

terraform fmt                   # format; run before any plan
terraform validate              # validate; run before any plan
terraform init -upgrade         # init or upgrade providers
terraform plan -out=tfplan      # plan and save output
terraform apply tfplan          # apply saved plan only
```

## Custom skills
- `/tfplan` — runs fmt, init, validate, plan, summarises adds/changes/destroys (flags destroys as HIGH RISK), then asks for confirmation before applying
- `/tfapply` — applies a saved `tfplan` file; requires typing `YES` (exact) to confirm

Use these skills instead of running Terraform commands manually.

## Architecture
```
terraform/
├── modules/          ← reusable building blocks (shared across envs)
│   ├── vpc/          ← VPC, subnets, internet gateway
│   ├── ec2/          ← EC2 instance + security group
│   └── s3/           ← S3 bucket (encrypted, public access blocked)
└── environments/
    ├── dev/          ← small instances, no S3 versioning
    └── prod/         ← larger instances, S3 versioning enabled
```

Remote state is stored in S3 bucket `my-company-tfstate`, one key per environment. Region: `us-east-1`. Requires Terraform >= 1.6.

Sensitive files (`.tfvars.json`, override files) and local state/plan files are gitignored.
