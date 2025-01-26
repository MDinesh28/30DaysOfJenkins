# Jenkins Freestyle Job: Clone GitHub Repo and Run Shell Script

This repository contains a guide and example setup for creating a **Jenkins freestyle job** that clones a GitHub repository and runs a shell script automatically.

---

## 🚀 Features

- **Automate repository cloning**: Clone a GitHub repository with Jenkins.
- **Run shell scripts**: Execute a shell script from the cloned repository.
- **Debugging support**: Print the working directory and file structure for troubleshooting.

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

1. **Jenkins** installed and running.
2. **Git** installed on the Jenkins server.
3. A **GitHub repository** with a shell script you want to run.

---

## 🛠️ Steps to Set Up the Jenkins Job

### 1. Create a Freestyle Job
- Log in to your Jenkins dashboard.
- Click **New Item** and create a **Freestyle project**.

### 2. Configure Source Code Management
- Under **Source Code Management**, select **Git**.
- Enter your repository URL (https://github.com/MDinesh28/30DaysOfJenkins.git).
- Add GitHub credentials if your repository is private.

### 3. Add a Build Step to Run the Shell Script
- Under **Build**, click **Add build step** and select **Execute shell**.
- Add the following commands:

  ```bash
  # Print the current working directory
  echo "Current working directory: $(pwd)"

  # List all files in the current directory
  echo "Files in the current directory:"
  ls -la

# 📖 Medium Post
For a detailed step-by-step guide with screenshots and best practices, check out my Medium post:

👉 [Automate Your Workflow: Clone a GitHub Repo and Run a Shell Script with Jenkins](https://medium.com/@mekadinesh4/clone-a-github-repo-and-run-a-shell-script-with-jenkins-23f5999fb569)
