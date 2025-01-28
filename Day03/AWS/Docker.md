# **Private Docker Registry in Amazon ECR**

This repository contains a step-by-step guide to set up a private Docker registry in **Amazon Elastic Container Registry (ECR)**. It includes instructions to:
- Launch an EC2 instance with Docker.
- Create a simple Docker application.
- Push the Docker image to an ECR repository.

---

## **Prerequisites**
Before you begin, ensure you have the following:
1. An **AWS account**.
2. **AWS CLI** installed and configured on your local machine or EC2 instance.
3. **Docker** installed on your EC2 instance.

---

## **Steps to Set Up a Private Docker Registry in ECR**

### **1. Launch an EC2 Instance with Docker**
1. Go to the AWS Management Console and launch an EC2 instance (e.g., Amazon Linux 2 AMI).
2. SSH into the instance:
  
3. Install Docker:
   ```bash
   sudo yum update -y
   sudo yum install docker -y
   sudo service docker start
   ```


---

### **2. Create a Simple Docker Application**
1. Create a project directory:
   ```bash
   mkdir my-docker-app
   cd my-docker-app
   ```
2. Create an `index.html` file:
   
3. Create a `Dockerfile`

---

### **3. Create an ECR Repository**
1. Go to the **Amazon ECR** console.
2. Click **Create repository** and name it (e.g., `my-docker-repo`).
3. Note the **Repository URI** for pushing and pulling images.

---

### **4. Push the Docker Image to ECR**


### **5. Verify the Push**
1. Go to the ECR console and verify that the image has been pushed successfully.
## **Repository Structure**
```
my-docker-app/
├── index.html          # Simple HTML file
├── Dockerfile          # Dockerfile to build the image
```

---

# 📖 Medium Post
For a detailed step-by-step guide with screenshots and best practices, check out my Medium post:

👉 [How to Set Up a Private Docker Registry in Amazon ECR](https://medium.com/@mekadinesh4/how-to-set-up-a-private-docker-registry-in-amazon-ecr-998bc688f2eb)
