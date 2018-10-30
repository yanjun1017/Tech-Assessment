variable "iam_username" {} 

resource "aws_iam_policy" "yanjun-ec2-policy" {
  name = "yanjun-ec2-policy"
  path = "/"
  policy = <<EOF
{
     "Version": "2012-10-17", 
     "Statement": [
  {
        "Effect": "Allow",
        "Action": [
            "ec2:*"
        ],
        "Resource": "*"
  }
  ]
}
EOF
}

resource "aws_iam_user_policy_attachment" "yanjun-ec2" {

    user = "${var.iam_username}"
    policy_arn = "${aws_iam_policy.yanjun-ec2-policy.arn}"
}


