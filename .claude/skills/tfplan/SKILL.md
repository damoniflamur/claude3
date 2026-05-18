---
name: tfplan
description: Safely plan Terraform changes with validation and risk summary. Creates a GitHub PR for team review before apply.
user-invocable: true
allowed-tools:
  - Bash
  - Read
  - mcp__github__create_pull_request
  - mcp__github__list_pull_requests
---

# /tfplan — Terraform Plan with GitHub PR Review

Steps (run in order):

1. Run `terraform fmt -check` inside `terraform/environments/dev`.
   - If formatting errors: run `terraform fmt` to fix.
   - If errors persist after fix, stop and show the error.

2. Run `terraform init -upgrade`.
   - If it fails, stop and display the error to the user.

3. Run `terraform validate`.
   - If errors: show them clearly and stop.

4. Run `terraform plan -out=tfplan`. Summarise the plan:
   - Resources to ADD (green)
   - Resources to CHANGE (yellow)
   - Resources to DESTROY (red) ← flag these as HIGH RISK

5. Create a GitHub PR for plan review:
   a. Run `terraform show -no-color tfplan` to capture the full human-readable plan.
   b. Create a plan-review branch:
      ```
      git checkout -b plan-review/$(date +%Y%m%d-%H%M%S)
      ```
   c. Write the plan output to `plan-output.md` at the repo root and commit it:
      ```
      git add plan-output.md && git commit -m "chore: terraform plan output for review"
      ```
   d. Push the branch: `git push -u origin <branch-name>`
   e. Use `mcp__github__create_pull_request` with:
      - `owner`: `damoniflamur`
      - `repo`: `claude3`
      - `title`: `Terraform Plan Review — <YYYY-MM-DD HH:MM>`
      - `body`: plan summary (ADD/CHANGE/DESTROY counts) followed by full plan output in a code block
      - `head`: the plan-review branch name
      - `base`: `main`
   f. Return to main: `git checkout main`
   g. Tell the user: "Plan PR created: <PR URL>. Review and approve it, then run `/tfapply`."

6. Do NOT apply. The PR approval is the gate — stop here.
