# sqs.tf

# NOTE: The AWS provider is already configured in versions.tf, so it is not
# redeclared here to avoid a duplicate provider configuration error. It uses
# your existing account via env/credentials/profile.

resource "aws_sqs_queue" "orders" {
  name                       = "orders-queue"
  visibility_timeout_seconds = 30
  message_retention_seconds  = 345600 # 4 days
  # fifo_queue = true                  # for orders.fifo
}
