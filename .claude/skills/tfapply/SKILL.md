---
name: tfapply
description: Apply a saved Terraform plan after GitHub PR approval.
user-invocable: true
allowed-tools:
  - Bash
  - Read
  - mcp__github__list_pull_requests
  - mcp__github__get_pull_request_reviews
  - mcp__github__merge_pull_request
---

# /tfapply — Apply a Reviewed Terraform Plan

Steps:

**Step A — Verify plan file:**

1. Check that `tfplan` exists in `terraform/environments/dev/`.
   - If missing, tell the user to run `/tfplan` first and stop.

**Step B — Check PR approval:**

2. Use `mcp__github__list_pull_requests` (owner: `damoniflamur`, repo: `claude3`, state: `open`) to find a PR whose title starts with `Terraform Plan Review`.
   - If no plan PR is found: warn the user that no review PR exists. This is non-blocking — continue to step 3.
   - If a plan PR is found, use `mcp__github__get_pull_request_reviews` to check approval status.
     - If the PR has no approving review: tell the user to approve the PR first and stop.
     - If the PR is approved: continue.

**Step C — Confirm and apply:**

3. Show a one-line summary: run `terraform show -no-color tfplan` in `terraform/environments/dev/` and extract the `Plan: X to add, Y to change, Z to destroy` line.

4. Ask: "Are you sure you want to apply? Type YES to confirm." Accept only `YES` (case-sensitive). Any other input: stop.

5. Run `terraform apply tfplan` in `terraform/environments/dev/` and show the output summary.
   - If `terraform apply` fails, display the error message and stop.

6. If apply succeeds and a plan PR was found, use `mcp__github__merge_pull_request` to merge it as a record of the applied change.
