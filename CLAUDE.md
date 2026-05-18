# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does
Manages AWS infrastructure (S3) with reusable Terraform modules across environments. Currently only the `dev` environment and `s3` module are implemented.

## Rules
- Never run `terraform apply` without explicit user approval
- Always run `terraform fmt` and `terraform validate` before planning
- Never touch prod without explicit confirmation
- Tag every resource with `env`, `project`, and `owner`
- Never edit `terraform/modules/` directly for a single environment — modules are shared

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
├── modules/
│   └── s3/           ← S3 bucket (AES256 encryption, public access blocked, optional versioning)
└── environments/
    └── dev/          ← calls modules; versioning_enabled = false
```

Remote state: S3 bucket `my-company-tfstate`, key `<env>/terraform.tfstate`, region `us-east-1`. Provider: AWS `~> 5.0`. Requires Terraform >= 1.6.

The `tfplan` binary is gitignored (see `.gitignore`) — never commit it.

## s3 module interface

| Variable | Type | Required | Notes |
|---|---|---|---|
| `bucket_name` | string | yes | |
| `env` | string | yes | used for tagging |
| `project` | string | yes | used for tagging |
| `owner` | string | yes | used for tagging |
| `versioning_enabled` | bool | no | default `false` |

Outputs: `bucket_id`, `bucket_arn`.
