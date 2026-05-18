My Terraform Project
What this project does
Manages AWS infrastructure with Terraform.
Rules Claude must follow

Never run terraform apply without my approval
Always run terraform fmt and terraform validate before planning
Use remote state (S3 backend), never local state in production
Tag every resource with: env, owner, project

Project details

Cloud: AWS
Region: us-east-1
Terraform version: >= 1.6
State bucket: my-company-tfstate

Module structure
Every module must have:
modules/<name>/main.tf
modules/<name>/variables.tf
modules/<name>/outputs.tf