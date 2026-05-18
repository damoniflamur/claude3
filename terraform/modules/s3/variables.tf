variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "env" {
  description = "Environment name (dev, prod)"
  type        = string
}

variable "project" {
  description = "Project name for tagging"
  type        = string
}

variable "owner" {
  description = "Owner for tagging"
  type        = string
}

variable "versioning_enabled" {
  description = "Enable S3 versioning"
  type        = bool
  default     = false
}
