# Skill: Best Practices Checks

## Variables
- Every variable must have `type` and `description` → **WARN** if missing
- No `type = any` → **WARN**
- Variables holding secrets must have `sensitive = true` → **BLOCK** if missing

## Outputs
- Every output must have a `description` → **WARN** if missing
- Export at minimum: ID, ARN, and endpoint per resource → **WARN** if missing

## Naming
- Logical names: lowercase with underscores, no hyphens → **WARN**
- No hardcoded names in `main.tf` — use variables → **WARN**

## State
- Remote backend required in production (not local state) → **WARN**
- `prevent_destroy = true` on stateful resources (RDS, S3 with data) → **WARN**

## Formatting
- Must pass `terraform fmt` → **WARN**
- Must pass `terraform validate` → **BLOCK**
- Provider version pinned with `~>` → **WARN**
