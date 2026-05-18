---
name: tfapply
description: Apply a saved Terraform plan. PR review is informational only — no approval gate.
user-invocable: true
allowed-tools:
  - Bash
  - Read
  - mcp__github__list_pull_requests
  - mcp__github__merge_pull_request
---

# /tfapply — Apply a Terraform Plan

Steps:

**Step A — Verify plan file:**

1. Check that `tfplan` exists in `terraform/environments/dev/`.
   - If missing, tell the user to run `/tfplan` first and stop.

**Step B — Check PR status (informational only):**

2. Use `mcp__github__list_pull_requests` (owner: `damoniflamur`, repo: `claude3`, state: `open`) to find a PR whose title starts with `Terraform Plan Review`.
   - If a plan PR is found: note it for merging after apply.
   - If no plan PR is found: inform the user and continue. This is non-blocking.

**Step C — Confirm and apply:**

3. Show a one-line summary: run `terraform show -no-color tfplan` in `terraform/environments/dev/` and extract the `Plan: X to add, Y to change, Z to destroy` line.

4. Ask: "Are you sure you want to apply? Type YES to confirm." Accept only `YES` (case-sensitive). Any other input: stop.

5. Run `terraform apply tfplan` in `terraform/environments/dev/` and show the output summary.
   - If `terraform apply` fails, display the error message and stop.

6. If apply succeeds and a plan PR was found, use `mcp__github__merge_pull_request` to merge it as a record of the applied change.
