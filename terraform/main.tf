resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
}
resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = var.public_subnet_cidr
}
resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.main.id
  cidr_block = var.private_subnet_cidr
}
resource "aws_security_group" "public" {
  vpc_id = aws_vpc.main.id
}
resource "aws_vpc_security_group_ingress_rule" "public" {
  security_group_id = aws_security_group.public.id
  ip_protocol       = "tcp"
  from_port         = 443
  to_port           = 443
  cidr_ipv4         = "0.0.0.0/0"
}
resource "aws_vpc_security_group_ingress_rule" "admin" {
  security_group_id = aws_security_group.public.id
  ip_protocol       = "tcp"
  from_port         = 22
  to_port           = 22
  cidr_ipv4         = "203.0.113.10/32"
}
resource "aws_vpc_security_group_egress_rule" "outbound" {
  security_group_id = aws_security_group.public.id
  ip_protocol       = "-1"
  cidr_ipv4         = "0.0.0.0/0"
}