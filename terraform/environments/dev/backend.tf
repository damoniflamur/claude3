terraform {
  backend "s3" {
    bucket = "terraform-state-890381434210"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}
