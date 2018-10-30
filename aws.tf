# aws.tf
variable "AWS_ACCESS_KEY" {}
variable "AWS_SECRET_KEY" {}

provider "aws" {
  region     = "us-east-2"
  access_key = "${var.AWS_ACCESS_KEY}"
  secret_key = "${var.AWS_SECRET_KEY}"
}

resource "aws_key_pair" "yanjun-key" {
  key_name   = "yanjun-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDqessrDx4xzKKtzLPDlGFGshUi4ze6O1k1sVhsCxVJP18GWJ3rjJmee6YYP16xxHc1bE7nO7tFImnw5LwC6CeS3cpUEV45p5EbJ5D2wZteCXYdGYj32BQNDakrhxIDj2rIgeZ3bhdc3Kj5YUWJWORn13RWlBQpOU8Ob1mPwAQ3b03N+hfpuplYDN1cdD6P06I8xVxh/h4FgZ1cRLXlRtufSCcQlZh+CbIQnWxg2dhV0w7BR6FfCno8slyz09WXG1nndRCnIc3SFvwVdaet9bYF5LBd9ikeLR2RU8vaHms5HGeenY4W2DHoJCe/8q4/OFatRKMFSX5GLMB9poBgpuyx yanjunli@Yanjuns-MacBook.home"
}

resource "aws_instance" "yanjun-ec2" {
  ami                  = "ami-04c305e118636bc7d"
  instance_type        = "t3.small"
  key_name             = "${aws_key_pair.yanjun-key.key_name}"
  iam_instance_profile = "${aws_iam_instance_profile.yanjun-ec2-profile.name}"
  security_groups = ["${aws_security_group.web-node.name}"]

   user_data = <<-EOF
              sudo apt-get update
              EOF
  tags {
    Name = "yanjun-ec2"
  }
}


resource "aws_iam_instance_profile" "yanjun-ec2-profile" {
    
  name = "yanjun-ec2-profile"
}



