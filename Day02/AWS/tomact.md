# Tomcat Server Setup on Amazon Linux EC2 Instance

This guide provides step-by-step instructions to deploy an Apache Tomcat server on an Amazon Linux EC2 instance.

## Prerequisites

Before starting, ensure you have the following:

- An AWS account.
- Basic knowledge of AWS EC2 and Linux commands.
- An SSH client (e.g., Terminal, PuTTY).
- A key pair for EC2 access.

---

## Step 1: Launch an EC2 Instance

1. Log in to the [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to **EC2** and click **Launch Instance**.
3. Choose the **Amazon Linux 2 AMI**.
4. Select the **t2.micro** instance type (eligible for the Free Tier).
5. Configure the security group to allow the following:
   - **SSH (Port 22)**: Allow access from your IP address.
   - **HTTP (Port 80)**: Allow access from `0.0.0.0/0`.
   - **Custom TCP (Port 8080)**: Allow access from `0.0.0.0/0`.
6. Launch the instance and download the `.pem` key pair for SSH access.

---

## Step 2: Connect to the EC2 Instance
Open your SSH client (e.g., Terminal or PuTTY).

## Step 3: Install and Configure Tomcat
Download and install Tomcat

## Step 4: Access Tomcat
Open a web browser and navigate to:

    http://<public-ip>:8080
      
Replace <public-ip> with your EC2 instance's public IP address.

Verify that the Tomcat welcome page is displayed.
# 📖 Medium Post
For a detailed step-by-step guide with screenshots and best practices, check out my Medium post:

👉 [How to Set Up a Tomcat Server on an Amazon Linux EC2 Instance](https://medium.com/@mekadinesh4/how-to-set-up-a-tomcat-server-on-an-amazon-linux-ec2-instance-42222cf3cbd9)
