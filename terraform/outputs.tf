output "vpc_id" {
  description = "ID of the bank vpc"
  value       = aws_vpc.main.id
}