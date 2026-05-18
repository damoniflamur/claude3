---
name: tfapply
description: Apply a saved Terraform plan that was already reviewed. Use when the user asks to apply, run tfapply, or execute a saved plan.
user-invocable: true
allowed-tools:
  - Bash
  - Read
---

# /tfapply — Apply a Reviewed Terraform Plan

Steps:

1. Check that the `tfplan` file exists.
   - If it does not exist, tell the user to run `/tfplan` first and stop.
   - If it exists, run `terraform show tfplan` to verify it is a valid plan. If invalid or corrupt, tell the user to regenerate it with `/tfplan` and stop.

2. Show a one-line summary of what will change by parsing the plan output for resource names and actions (e.g., "Plan: 2 to add, 1 to change, 0 to destroy.").

3. Ask: "Are you sure you want to apply? Type YES to confirm." Accept only `YES` (case-sensitive). If the user provides any other input, ask again or stop.

4. Run `terraform apply tfplan` and show the output summary.
