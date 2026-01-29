# 1. Define Provider
provider "aws" {
  region = "us-east-1"
}

# 2. Query the Default VPC and its Subnets
data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# 3. Create ECR Repositories
resource "aws_ecr_repository" "webapp" {
  name                 = "webapp-repo"
  image_tag_mutability = "MUTABLE"
  force_delete         = true # Useful for students to cleanup easily
}

resource "aws_ecr_repository" "mysql" {
  name                 = "mysql-repo"
  image_tag_mutability = "MUTABLE"
  force_delete         = true
}

# 4. Create Security Group for EC2
resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow HTTP and SSH"
  vpc_id      = data.aws_vpc.default.id

  # SSH Access
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # App Ports (8081, 8082, 8083)
  ingress {
    from_port   = 8081
    to_port     = 8083
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 5. Create EC2 Instance in a Public Subnet
resource "aws_instance" "app_server" {
  ami                         = "ami-0440d3b780d96b29d" # Amazon Linux 2023
  instance_type               = "t2.micro"
  subnet_id                   = data.aws_subnets.default.ids[0] # Picks the first default subnet
  vpc_security_group_ids      = [aws_security_group.allow_web.id]
  associate_public_ip_address = true
  
  # Ensure you have a key pair created in AWS console first
  key_name = "vockey" 

  tags = {
    Name = "CLO835-Assignment1"
  }
}

# 6. Output the Public IP to connect later
output "ec2_public_ip" {
  value = aws_instance.app_server.public_ip
}