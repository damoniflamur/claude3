---
name: tfplan
description: Safely plan Terraform changes with validation and risk summary. Use when the user asks to plan, run tfplan, or check what Terraform will change.
user-invocable: true
allowed-tools:
  - Bash
  - Read
---

# /tfplan — Terraform Plan with Risk Summary

Steps (run in order, stop if any step fails):

1. Run `terraform fmt -check`. If formatting errors: run `terraform fmt` to fix, then continue.

2. Run `terraform init -upgrade`.

3. Run `terraform validate`. If errors: show them clearly and stop.

4. Run `terraform plan -out=tfplan`. Summarise the plan:
   - Resources to ADD (green)
   - Resources to CHANGE (yellow)
   - Resources to DESTROY (red) ← flag these as HIGH RISK

5. Ask the user: "Shall I apply this plan? (yes/no)". Do NOT apply unless user explicitly says yes.
