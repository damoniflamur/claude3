# CLAUDE.md

You are helping maintain a Terraform AWS project.

Goals:
- keep code simple
- explain changes clearly
- generate production-safe Terraform
- prefer reusable modules
- avoid hardcoded values

Always:
- create missing Terraform files if needed
- add variables automatically
- add outputs automatically
- add provider config if missing
- add versions.tf if missing
- use terraform fmt style
- ensure terraform validate passes
- explain folder structure

Testing workflow:
- terraform fmt
- terraform validate
- terraform plan

AWS:
- region eu-central-1
- use secure defaults
- enable encryption where possible