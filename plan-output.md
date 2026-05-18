
Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # module.s3.aws_s3_bucket.this will be updated in-place
  ~ resource "aws_s3_bucket" "this" {
        id                          = "my-company-dev-data-890381434210"
      ~ tags                        = {
            "env"     = "dev"
          ~ "owner"   = "platform-team" -> "platform-team-core"
            "project" = "my-company-app"
        }
      ~ tags_all                    = {
          ~ "owner"   = "platform-team" -> "platform-team-core"
            # (2 unchanged elements hidden)
        }
        # (12 unchanged attributes hidden)

        # (3 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.
