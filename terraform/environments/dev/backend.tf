terraform {
  backend "s3" {
    bucket = "my-company-tfstate"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}
