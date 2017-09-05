provider "aws" {
  region = "${var.region}"
  profile = "${var.profile}"

}

resource "aws_spot_instance_request" "mtg_worker01" {
  ami           = "ami-e1679399"
  spot_price    = "0.02"
  instance_type = "m3.medium"
  vpc_security_group_ids = [ "${aws_security_group.ssh_access.id}", "${aws_security_group.tcp_internal_access.id}","${aws_security_group.splunk_access.id}","${aws_security_group.internet_access.id}" ]
  subnet_id     = "subnet-401d891b"
  associate_public_ip_address = "true"
  wait_for_fulfillment = "true"

  connection {
    host = "${self.public_ip}"
    type = "ssh"
    user = "ec2-user"
    private_key = "${file("${var.private_key_path}")}"
    agent = "false"
  }

  provisioner "file" {
      source = "~/.ssh/my_github"
      destination = "~/.ssh/my_github"
  }
  provisioner "file" {
      source = "provisioners/config"
      destination = "~/.ssh/config"
  }
  provisioner "file" {
      source = "provisioners/clone_mtg_work.sh"
      destination = "~/clone_mtg_work.sh"
  }
  provisioner "remote-exec" {

    inline = [
      "chmod 600 ~/.ssh/config",
      "chmod 400 ~/.ssh/my_github",
      "chmod +x ~/clone_mtg_work.sh",
      "./clone_mtg_work.sh",
#      "git clone work",
    ]
  }
}

