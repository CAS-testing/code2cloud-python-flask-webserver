provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "data" {
  # bucket is public
  # bucket is not encrypted
  # bucket does not have access logs
  # bucket does not have versioning
  bucket        = "application-side-card-test"
  force_destroy = true
  tags = {
    git_commit           = "16ae402f91674d1653e9482a5ed550ebdfaedebc"
    git_file             = "s3.tf"
    git_last_modified_at = "2025-07-09 12:30:57"
    git_last_modified_by = "166496865+Aviv-Cohen-PAN@users.noreply.github.com"
    git_modifiers        = "166496865+Aviv-Cohen-PAN"
    git_org              = "Aviv-Cohen-PAN"
    git_repo             = "code2cloud-python-flask-webserver"
    yor_name             = "data"
    yor_trace            = "b2863525-8553-4f79-948a-b8a991889fca"
  }
}
