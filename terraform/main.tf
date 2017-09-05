provider "aws" {
  region = "${var.region}"
  profile = "${var.profile}"

}

resource "aws_spot_instance_request" "worker01" {
  ami           = "ami-0cb95574"
  spot_price    = "0.01"
  instance_type = "t1.micro"
  vpc_security_group_ids = [ "${aws_security_group.ssh_access.id}", "${aws_security_group.tcp_internal_access.id}","${aws_security_group.splunk_access.id}","${aws_security_group.internet_access.id}" ]
  subnet_id     = "subnet-401d891b"
  associate_public_ip_address = "true"
  wait_for_fulfillment = "true"

   provisioner "remote-exec" {
      connection {
        host = "${self.public_ip}"
        type = "ssh"
        user = "ec2-user"
        private_key = "${file("${var.private_key_path}")}"
        agent = "false"
      }
     inline = [
       "touch foo",
     ]
   }
}

