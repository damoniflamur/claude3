# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Agents & Skills

This project uses sub-agents and skills for automated Terraform review:

| Path | Purpose |
|------|---------|
| [.claude/agents/terraform-reviewer.md](.claude/agents/terraform-reviewer.md) | Orchestrates full review of any plan or PR |
| [.claude/skills/security.md](.claude/skills/security.md) | Security checks |
| [.claude/skills/cost.md](.claude/skills/cost.md) | Cost estimation and optimization |
| [.claude/skills/best-practices.md](.claude/skills/best-practices.md) | Terraform conventions and structure |

Invoke the reviewer with:
```
/terraform-reviewer
```

## Commands

```bash
terraform init
terraform validate
terraform fmt -recursive

# Save and review plan before applying
terraform plan -out=tfplan
terraform show tfplan
terraform apply tfplan

# Target a single resource
terraform plan -target=<resource_type>.<name>
terraform destroy -target=<resource_type>.<name>

# Override a variable at runtime
terraform plan -var="key=value"

# Run native tests (requires .tftest.hcl files)
terraform test
```

## Architecture

Flat single-module layout. All resources live in the root module. As the project grows, extract related resources into `modules/<name>/` subdirectories, each with its own `main.tf`, `variables.tf`, and `outputs.tf`.

**File responsibilities:**
- `main.tf` — resource definitions, grouped by service
- `variables.tf` — typed inputs; required variables (no `default`) at the top
- `outputs.tf` — IDs, ARNs, endpoints for external consumers
- `terraform.tfvars` — environment-specific values; the only file changed per deployment

## Conventions

- Use `for_each` over `count` when items have meaningful keys; use `count` only for simple on/off toggles
- Use `optional()` in object variable types for nullable fields (requires Terraform >= 1.3)
- Apply a `tags` variable (`map(string)`) to every taggable resource
- Export at minimum: resource ID, ARN, and any endpoint/DNS name
- Resource logical name is `main` for a single instance of a type; use a descriptive name when multiples exist
- Never hardcode account IDs, region strings, ARNs, or credentials in `.tf` files — always use variables or data sources

## Security Defaults

- Default to most restrictive access; explicitly opt in to public access where required
- Encryption at rest enabled on all storage resources
- IAM policies: least-privilege, no wildcard `*` actions or resources
- No secrets or credentials in `.tf` or `.tfvars` files

## AWS Authentication

```bash
# Environment variables
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_DEFAULT_REGION=us-east-1

# Or AWS CLI profile
export AWS_PROFILE=my-profile
```

## Adding New Resources

1. Add resource blocks to `main.tf` grouped with related resources
2. Add inputs to `variables.tf` with `type`, `description`, and a sensible `default`
3. Add outputs to `outputs.tf` for values needed externally
4. Set values in `terraform.tfvars`
5. Run `terraform fmt -recursive && terraform validate` before applying
