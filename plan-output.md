# Terraform Plan Output — 2026-05-18 23:28

## Summary
- **ADD:** 0
- **CHANGE:** 1
- **DESTROY:** 0

## Changes

```
Terraform will perform the following actions:

  # module.s3.aws_s3_bucket.this will be updated in-place
  ~ resource "aws_s3_bucket" "this" {
        id                          = "my-company-dev-data-890381434210"
      ~ tags                        = {
            "env"     = "dev"
          ~ "owner"   = "platform-team" -> "platform-team-2"
            "project" = "my-company"
        }
      ~ tags_all                    = {
          ~ "owner"   = "platform-team" -> "platform-team-2"
            # (2 unchanged elements hidden)
        }
        # (12 unchanged attributes hidden)
        # (3 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.
```
