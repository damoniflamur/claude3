name: tf-plan
description: Safely plan Terraform changes with validation and risk summary
allowed-tools: [Bash, Read, Grep]
Steps (run in order, stop if any step fails)

Run terraform fmt -check

If formatting errors: run terraform fmt to fix, then continue


Run terraform init -upgrade
Run terraform validate

If errors: show them clearly and stop


Run terraform plan -out=tfplan
Summarise the plan:

Resources to ADD (green)
Resources to CHANGE (yellow)
Resources to DESTROY (red) ← flag these as HIGH RISK


Ask the user: "Shall I apply this plan? (yes/no)"

Do NOT apply unless user explicitly says yes