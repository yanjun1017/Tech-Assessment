provider "aws" {
  region     = "us-east-2"
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] 
}

resource "aws_key_pair" "yj-key" {
  key_name   = "yj-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1d4zwPeP0h/5k0MdJ/SSbkPaBHe+5GHBznKtPQsA+Nt8jZAVYnBIMLfah1eVHqtsfu21yFckbZtNFbTDDsXRblBK7GyPa9QKjPq3nNAnP0Wm8JRs6BhvvkKEBfP9AemOctSjzu/K9/x/KgF0OuxkKrG9UBDSQLaeWS7125mWM/x11YXstB6UO3DxMgV6kAKx1ctdR8bOg+zHVChM+aMm0SDq6glfufWMKqgUMAgc4z64Ae0bHT6rmSePop1+7UTzdNciZMr8ZNW+dabHnSP8H/bMQ2V8DvV0OFXArDubE+Tz3ETqnJ4RLadF2PnII2WXRaCesU1hEKRuop2Ycg1k/ yanjunli@Yanjuns-MacBook.local"

  depends_on = ["aws_iam_policy_attachment.ec2fullaccess"]
}

resource "aws_instance" "yanjun-ec2" {
  ami                  = "${data.aws_ami.ubuntu.id}"
  instance_type        = "t3.small"
  key_name             = "yj-key"
  security_groups = ["${aws_security_group.web-node.id}"]
  associate_public_ip_address = true
  subnet_id = "subnet-0dcfe57d2d8b39f9d"

  root_block_device{
    volume_size = 20
  }

    user_data = <<-EOF
              #!/bin/bash
              apt update
              sudo apt-get install \
                apt-transport-https \
                ca-certificates \
                curl \
                software-properties-common
              sudo apt-key fingerprint 0EBFCD88
              sudo add-apt-repository \
               "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
               $(lsb_release -cs) \
               stable"
              sudo apt-get update && sudo apt-get install docker-ce
              usermod -aG docker ubuntu
              git clone https://github.com/yanjun1017/Tech-Assessment.git /home/ubuntu/Tech-Assessment
              chmod -R 777 /home/ubuntu/Tech-Assessment
              docker build -t assessment /home/ubuntu/Tech-Assessment/
              docker run -d -p 80:80 -v /home/ubuntu/Tech-Assessment:/home/joyvan/Tech-Assessment --rm --name jupyter assessment
              EOF
  tags {
    Name = "yanjun-ec2"
  }
  lifecycle {
    create_before_destroy = true
  }
  connection {
    user = "ubuntu"
  }

  depends_on = ["aws_iam_policy_attachment.ec2fullaccess", "aws_key_pair.yj-key"]
}




