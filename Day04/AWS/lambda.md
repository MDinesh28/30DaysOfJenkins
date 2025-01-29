# Deploying an AWS Lambda Function via AWS CLI

## Introduction
AWS Lambda is a powerful serverless compute service that allows you to run code without provisioning or managing servers. This guide walks you through deploying a Lambda function using the AWS Command Line Interface (CLI).

---

## Prerequisites
Before deploying a Lambda function, ensure you have:

1. **AWS CLI Installed & Configured**  
   - Install AWS CLI from [AWS official website](https://aws.amazon.com/cli/).
   - Run `aws configure` and provide your AWS credentials.

2. **IAM Permissions**  
   - Ensure you have permissions to create IAM roles, Lambda functions, and attach policies.

3. **Python Installed (If Using Python Lambda)**  
   - Install Python from [Python.org](https://www.python.org/) if necessary.

---

## Step 1: Write Your Lambda Function
Create a Python file (`lambda_function.py`) with a simple handler:

---

## Step 2: Package Your Code
AWS Lambda requires the function to be uploaded as a ZIP file.


## Step 3: Create an IAM Role for Lambda
A Lambda function needs an IAM role with execution permissions.

1. **Create a Trust Policy (`trust-policy.json`)**:
  

2. **Create the IAM Role:**
   ```sh
   aws iam create-role --role-name LambdaBasicExecutionRole --assume-role-policy-document file://trust-policy.json
   ```

3. **Attach the AWS Lambda Policy:**
   ```sh
   aws iam attach-role-policy --role-name LambdaBasicExecutionRole \
       --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   ```

4. **Retrieve the IAM Role ARN:**
   ```sh
   aws iam get-role --role-name LambdaBasicExecutionRole
   ```

Copy the Role ARN from the output.

---

Step 4: Deploy the Lambda Function

Run the following command, replacing YOUR_ROLE_ARN with the IAM role ARN:

    aws lambda create-function \
    --function-name MyLambdaFunction   \
    --runtime python3.8   \
    --role YOUR_ROLE_ARN   \
    --handler lambda_function.lambda_handler   \
    --zip-file fileb://function.zip

Step 5: Invoke the Lambda Function

To test the function:

    aws lambda invoke --function-name MyLambdaFunction output.txt

To view the response:

    type output.txt

Expected output:

    {"statusCode": 200, "body": "\"Hi! Hello! This is Lambda working with you.\""}



## Step 6: Update the Lambda Function
If you make changes to your function, update it:

1. **Repackage the function:**
   ```sh
   zip function.zip lambda_function.py
   ```

2. **Update the function in AWS Lambda:**
   ```sh
   aws lambda update-function-code --function-name MyLambdaFunction --zip-file fileb://function.zip
   ```

---


## Step 8: Delete the Lambda Function (Cleanup)
If you no longer need the Lambda function:

```sh
aws lambda delete-function --function-name MyLambdaFunction
```

To delete the IAM role:
```sh
aws iam delete-role --role-name LambdaBasicExecutionRole
```

---
# 📖 Medium Post
For a detailed step-by-step guide with screenshots and best practices, check out my Medium post:

👉 [Deploying an AWS Lambda Function via AWS CLI](https://medium.com/@mekadinesh4/deploying-an-aws-lambda-function-via-aws-cli-07a473bb5287)

