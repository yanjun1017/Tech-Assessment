

resource "aws_iam_policy_attachment" "ec2fullaccess" {
  name = "ec2fullaccess"
  users = ["yanjun9876@gmail.com"]
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
}
