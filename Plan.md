## **30-Day AWS + Jenkins-Centric DevOps Plan**  

### **Day 1**  
- **AWS Project**: Deploy a static website to **S3 + CloudFront**.  
- **Jenkins DevOps Project**: Create a **Jenkins freestyle job** to clone a GitHub repo and run a shell script.  
- **Jenkins Focus Area**: Basic Jenkins setup, Git integration.  
- **Tools Integrated**: GitHub, Shell Scripting.  

---

### **Day 2**  
- **AWS Project**: Launch an **EC2 instance** with a Tomcat server.  
- **Jenkins DevOps Project**: Write a **Jenkins pipeline** to deploy a WAR file to Tomcat on EC2.  
- **Jenkins Focus Area**: Declarative Pipelines, EC2 agents.  
- **Tools Integrated**: Tomcat, SSH.  

---

### **Day 3**  
- **AWS Project**: Set up a **private Docker registry** in **ECR**.  
- **Jenkins DevOps Project**: Build a Docker image and push to ECR using Jenkins.  
- **Jenkins Focus Area**: Docker integration, AWS Credentials.  
- **Tools Integrated**: Docker, ECR.  

---

### **Day 4**  
- **AWS Project**: Deploy a **Lambda function** via AWS CLI.  
- **Jenkins DevOps Project**: Add a **Jenkins stage** to scan Lambda code with **SonarQube**.  
- **Jenkins Focus Area**: Quality Gates, SonarQube Plugin.  
- **Tools Integrated**: SonarQube, Lambda.  

---

### **Day 5**  
- **AWS Project**: Create a **VPC** using **Terraform**.  
- **Jenkins DevOps Project**: Use Jenkins to run `terraform apply` and provision AWS infra.  
- **Jenkins Focus Area**: Terraform-Jenkins integration.  
- **Tools Integrated**: Terraform, VPC.  

---

### **Day 6**  
- **AWS Project**: Set up **Nexus Repository** on EC2.  
- **Jenkins DevOps Project**: Configure Jenkins to pull artifacts from Nexus for deployment.  
- **Jenkins Focus Area**: Nexus Artifact Manager plugin.  
- **Tools Integrated**: Nexus, Maven.  

---

### **Day 7**  
- **AWS Project**: Deploy an **EKS cluster** using `eksctl`.  
- **Jenkins DevOps Project**: Use Jenkins to deploy a **Helm chart** to EKS.  
- **Jenkins Focus Area**: Kubernetes Plugin, Helm integration.  
- **Tools Integrated**: EKS, Helm.  

---

### **Day 8**  
- **AWS Project**: Configure **Auto Scaling** for EC2 instances.  
- **Jenkins DevOps Project**: Write a Jenkins pipeline to trigger scaling via AWS CLI.  
- **Jenkins Focus Area**: Parameterized Pipelines.  
- **Tools Integrated**: AWS CLI, Auto Scaling.  

---

### **Day 9**  
- **AWS Project**: Create an **RDS MySQL instance**.  
- **Jenkins DevOps Project**: Use Jenkins to run **Ansible playbooks** for DB schema updates.  
- **Jenkins Focus Area**: Ansible Plugin, Credentials Binding.  
- **Tools Integrated**: Ansible, RDS.  

---

### **Day 10**  
- **AWS Project**: Set up **CloudWatch Alarms** for EC2.  
- **Jenkins DevOps Project**: Deploy **Prometheus + Grafana** via Jenkins and monitor metrics.  
- **Jenkins Focus Area**: Post-build actions, Dashboards.  
- **Tools Integrated**: Prometheus, Grafana.  

---

### **Day 11**  
- **AWS Project**: Build a **serverless API** with **API Gateway + Lambda**.  
- **Jenkins DevOps Project**: Create a Jenkins pipeline with **GitHub webhooks** for CI/CD.  
- **Jenkins Focus Area**: Webhooks, GitHub Integration.  
- **Tools Integrated**: GitHub, Lambda.  

---

### **Day 12**  
- **AWS Project**: Use **AWS Secrets Manager** for DB passwords.  
- **Jenkins DevOps Project**: Retrieve secrets in Jenkins using the Secrets Manager plugin.  
- **Jenkins Focus Area**: Credential Security, Plugins.  
- **Tools Integrated**: Secrets Manager.  

---

### **Day 13**  
- **AWS Project**: Deploy a **Java app** on **ECS Fargate**.  
- **Jenkins DevOps Project**: Use Jenkins to build Docker images and deploy to ECS.  
- **Jenkins Focus Area**: ECS Deployment Plugin.  
- **Tools Integrated**: Docker, ECS.  

---

### **Day 14**  
- **AWS Project**: Configure **IAM Roles** for EC2 instances.  
- **Jenkins DevOps Project**: Use Jenkins to validate IAM policies with AWS CLI.  
- **Jenkins Focus Area**: Security Best Practices.  
- **Tools Integrated**: IAM, AWS CLI.  

---

### **Day 15**  
- **AWS Project**: Create a **CloudFormation stack** for a web app.  
- **Jenkins DevOps Project**: Migrate the stack to Jenkins using `aws cloudformation` commands.  
- **Jenkins Focus Area**: AWS SDK Integration.  
- **Tools Integrated**: CloudFormation.  

---

### **Day 16**  
- **AWS Project**: Set up **Route 53 DNS** for an S3 static site.  
- **Jenkins DevOps Project**: Automate DNS updates via Jenkins and **GitOps (FluxCD)**.  
- **Jenkins Focus Area**: GitOps Workflows.  
- **Tools Integrated**: FluxCD, Git.  

---

### **Day 17**  
- **AWS Project**: Use **AWS Systems Manager (SSM)** for EC2 patching.  
- **Jenkins DevOps Project**: Trigger SSM documents from Jenkins using Ansible.  
- **Jenkins Focus Area**: Hybrid Pipelines (Ansible + Jenkins).  
- **Tools Integrated**: SSM, Ansible.  

---

### **Day 18**  
- **AWS Project**: Deploy **Kubernetes CronJobs** on EKS.  
- **Jenkins DevOps Project**: Use Jenkins to schedule CronJobs and analyze logs with **K8sGPT**.  
- **Jenkins Focus Area**: Log Parsing, Plugins.  
- **Tools Integrated**: K8sGPT, Kubernetes.  

---

### **Day 19**  
- **AWS Project**: Deploy **Kubecost** on EKS for cost monitoring.  
- **Jenkins DevOps Project**: Integrate Kubecost alerts into Jenkins build notifications.  
- **Jenkins Focus Area**: Notifications (Email/Slack).  
- **Tools Integrated**: Kubecost, Slack Plugin.  

---

### **Day 20**  
- **AWS Project**: Use **AWS CodeBuild** to compile a Java app.  
- **Jenkins DevOps Project**: Replace CodeBuild with a Jenkins pipeline using **Maven**.  
- **Jenkins Focus Area**: Maven Builds, Parallel Stages.  
- **Tools Integrated**: Maven, Nexus.  

---

### **Day 21**  
- **AWS Project**: Configure **AWS WAF** for an **Application Load Balancer (ALB)**.  
- **Jenkins DevOps Project**: Automate WAF rule deployment via Jenkins + Terraform.  
- **Jenkins Focus Area**: Infrastructure-as-Code Pipelines.  
- **Tools Integrated**: Terraform, WAF.  

---

### **Day 22**  
- **AWS Project**: Set up **VPC Flow Logs** for network auditing.  
- **Jenkins DevOps Project**: Use Jenkins to analyze logs with **Athena** and **Grafana**.  
- **Jenkins Focus Area**: Analytics Pipelines.  
- **Tools Integrated**: Athena, Grafana.  

---

### **Day 23**  
- **AWS Project**: Deploy a **Redis cluster** using **ElastiCache**.  
- **Jenkins DevOps Project**: Write a Jenkins pipeline to test Redis connectivity.  
- **Jenkins Focus Area**: Integration Testing.  
- **Tools Integrated**: Ansible, Redis.  

---

### **Day 24**  
- **AWS Project**: Orchestrate **Lambda workflows** with **Step Functions**.  
- **Jenkins DevOps Project**: Trigger Step Functions from Jenkins using AWS SDK.  
- **Jenkins Focus Area**: AWS SDK Pipelines.  
- **Tools Integrated**: Step Functions, SDK.  

---

### **Day 25**  
- **AWS Project**: Set up **Cross-Account IAM Roles**.  
- **Jenkins DevOps Project**: Use Jenkins to assume roles across AWS accounts.  
- **Jenkins Focus Area**: Multi-Account Security.  
- **Tools Integrated**: IAM, STS.  

---

### **Day 26**  
- **AWS Project**: Deploy **Prometheus Operator** on EKS.  
- **Jenkins DevOps Project**: Configure Jenkins to auto-remediate alerts (e.g., pod crashes).  
- **Jenkins Focus Area**: Alert-Driven Pipelines.  
- **Tools Integrated**: Prometheus, K8sGPT.  

---

### **Day 27**  
- **AWS Project**: Use **AWS App Runner** for a containerized app.  
- **Jenkins DevOps Project**: Compare Jenkins vs. App Runner’s built-in CI/CD.  
- **Jenkins Focus Area**: CI/CD Tool Evaluation.  
- **Tools Integrated**: Docker, App Runner.  

---

### **Day 28**  
- **AWS Project**: Enable **AWS Config** for compliance audits.  
- **Jenkins DevOps Project**: Run compliance checks via Jenkins and fail builds on violations.  
- **Jenkins Focus Area**: Compliance-as-Code.  
- **Tools Integrated**: AWS Config, Lambda.  

---

### **Day 29**  
- **AWS Project**: Build a **multi-region failover system** with **Route 53**.  
- **Jenkins DevOps Project**: Simulate failure and trigger Jenkins rollback pipelines.  
- **Jenkins Focus Area**: Disaster Recovery Pipelines.  
- **Tools Integrated**: Route 53, Terraform.  

---

### **Day 30**  
- **AWS Project**: Deploy a **GitOps pipeline** with **FluxCD** on EKS.  
- **Jenkins DevOps Project**: Use Jenkins to sync FluxCD and audit changes with **K8sGPT**.  
- **Jenkins Focus Area**: GitOps + Jenkins Synergy.  
- **Tools Integrated**: FluxCD, K8sGPT.  

---
