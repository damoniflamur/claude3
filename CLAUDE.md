# My Terraform Project

## What this project does
Manages AWS infrastructure (VPC, EC2, S3) with reusable Terraform modules.

## Rules Claude must follow
- Never run `terraform apply` without my approval
- Always run `terraform fmt` and `terraform validate` before planning
- Never touch prod without explicit confirmation
- Tag every resource: env, project, owner

## Project structure
```
terraform/
├── modules/          ← reusable building blocks
│   ├── vpc/          ← VPC, subnets, internet gateway
│   ├── ec2/          ← EC2 instance + security group
│   └── s3/           ← S3 bucket (encrypted, public blocked)
└── environments/
    ├── dev/          ← small instances, no versioning
    └── prod/         ← larger instances, versioning on
```

## How to work in this project
- Always cd into the environment folder before running terraform
  cd terraform/environments/dev
- State is stored in S3, one key per environment
- Modules live in terraform/modules/ — never edit them per environment

## Project details
- Cloud: AWS
- Region: us-east-1
- Terraform version: >= 1.6
- State bucket: my-company-tfstate