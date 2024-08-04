# ChatGPT-like-application-using-AWS-Bedrock-API-Lambda

Built a ChatGPT like application using AWS Bedrock, API and Lambda

In the AWS management console, navigate to AWS bedrock. Choose a base model. For this project, Cohere 6 was chosen. Request model access but uncheck Anthropic 6.

Create a Lambda IAM role: Cloudwatch full access and bedrock full access.

create a Lambda function. Change configuration setting to 500mb and 2 mins execution time.

Create an API Gateway(Rest API)
     create resources (ask) enable CORS
     create method (post) check lambda proxy integraton.
Deploy API. Copy the URL endpoint

Use postman to test the API using the URL endpoint slash ask and post method.

Code used for the lambda function is included in this repository. Refer to the AWS documentation.
     
