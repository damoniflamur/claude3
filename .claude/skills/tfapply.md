---
name: tfapply
description: Apply a Terraform plan that was already reviewed
allowed-tools:
  - Bash
  - Read
---

Steps

1. Check that `tfplan` file exists. If not: tell user to run `/tfplan` first.

2. Show a one-line summary of what will change.

3. Ask: "Are you sure you want to apply? Type YES to confirm." Wait for explicit `YES` (not `yes`, not `y`).

4. Run `terraform apply tfplan` and show the output summary.
