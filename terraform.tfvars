aws_region         = "us-east-1"
bucket_name        = "my-app-bucket-unique-456"
versioning_enabled = true

tags = {
  Environment = "dev"
  Project     = "my-app"
  ManagedBy   = "terraform"
  Owner       = "platform-team"
  CostCenter  = "engineering"
}

lifecycle_rules = [
  {
    id      = "transition-to-ia"
    enabled = true
    prefix  = ""
    transitions = [
      {
        days          = 30
        storage_class = "STANDARD_IA"
      },
      {
        days          = 90
        storage_class = "GLACIER"
      }
    ]
    expiration_days = null
  }
]
