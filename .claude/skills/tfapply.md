name: tf-apply
description: Apply a Terraform plan that was already reviewed
allowed-tools: [Bash, Read]
Steps

Check that tfplan file exists

If not: tell user to run /tf-plan first


Show a one-line summary of what will change
Ask: "Are you sure you want to apply? Type YES to confirm."

Wait for explicit YES (not yes, not y)


Run terraform apply tfplan
Show the output summary