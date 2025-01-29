# Automate Docker Image Builds and Pushes to Amazon ECR Using Jenkins

## Overview
This project automates the process of building Docker images and pushing them to Amazon Elastic Container Registry (ECR) using Jenkins. It streamlines continuous integration (CI) for Docker-based applications.

## Prerequisites
Before setting up the pipeline, ensure you have the following:

- **Jenkins Server**: Installed and running.
- **Docker**: Installed on the Jenkins server or agent.
- **AWS CLI**: Installed and configured with appropriate permissions.
- **AWS IAM Credentials**: IAM user with necessary permissions for ECR.
- **Git Repository**: Your project source code hosted on GitHub.

## Step 1: Install Required Plugins
To enable Docker and AWS integration in Jenkins:

1. Go to **Manage Jenkins > Manage Plugins**.
2. Install the following plugins:
   - **Docker Pipeline**
   - **Stage View**
   - **AWS Credentials Plugin**

## Step 2: Add AWS Credentials in Jenkins
1. Navigate to **Manage Jenkins > Manage Credentials**.
2. Select the correct scope (e.g., Global).
3. Click **Add Credentials** and choose **AWS Credentials**.
4. Enter the following details:
   - **Access Key ID**: Your AWS access key.
   - **Secret Access Key**: Your AWS secret key.
   - **ID**: Give it a unique name (e.g., `aws-creds`).
5. Click **Save**.

## Step 3: Create an ECR Repository in AWS
1. Open the **AWS Management Console**.
2. Go to **ECR > Create Repository**.
3. Provide a repository name (e.g., `my-docker-repo`).
4. Note down the **Repository URI** (used in the pipeline).

## Step 4: Create a Jenkins Pipeline
1. In the **Jenkins Dashboard**, click **New Item**.
2. Enter a name (e.g., `docker-ecr-pipeline`).
3. Select **Pipeline** and click **OK**.


## Step 5: Run the Jenkins Pipeline
1. Save the pipeline script in Jenkins.
2. Click **Build Now** to start the process.
3. Monitor the logs to ensure the image is successfully built and pushed.

## Step 6: Verify the Image in Amazon ECR
1. Open the **AWS ECR Console**.
2. Navigate to your repository.
3. Confirm that the Docker image has been uploaded.

## Conclusion
This project automates Docker image builds and deployments to AWS ECR, ensuring efficient CI/CD workflows. By using Jenkins, you can streamline your DevOps pipeline for continuous integration and deployment.

# 📖 Medium Post
For a detailed step-by-step guide with screenshots and best practices, check out my Medium post:

👉 [Automate Docker Image Builds and Pushes to Amazon ECR Using Jenkins](https://medium.com/@mekadinesh4/automate-docker-image-builds-and-pushes-to-amazon-ecr-using-jenkins-042db8e8e7c3)

