variable "aws_region" {
  description = "AWS region to deploy the bank infrastructure"
  type        = string
  default     = "us-east-1"
}
variable "vpc_cidr" {
  description = "cidr block for bank vpc"
  type        = string
  default     = "10.0.0.0/16"
}
variable "public_subnet_cidr" {
  description = "cidr block for our bank public subnet"
  type        = string
  default     = "10.0.1.0/24"
}
variable "private_subnet_cidr" {
  description = "cidr block for our bank private subnet"
  type        = string
  default     = "10.0.2.0/24"
}