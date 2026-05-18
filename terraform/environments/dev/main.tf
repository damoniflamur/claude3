module "s3" {
  source = "../../modules/s3"

  bucket_name        = "my-company-dev-data-890381434210"
  env                = "dev"
  project            = "my-company"
  owner              = "platform-team"
  versioning_enabled = true
}
