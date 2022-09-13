The Purple Cow Project

TJ Groover - Site Reliability Engineer II
For my proof of concept, I decided to build and implement an SSL expiration checker. The tool is called Fearless for “Project Purple Cow” https://github.com/tgroove01/Fearless. This tool will potentially monitor the customer’s domains for SSL certificates ensuring that they are always valid. I decided to create a serverless function using AWS Lambda, AWS api and Terraform. AWS lambda allows AWS is a service that lets you run code for any type of application without managing servers. The AWS API we used supports integration with AWS Lambda functions, allowing to us implement an HTTP API using Lambda functions to handle and respond to HTTP requests.The Infrastructure as a code tool that I decided to utilitize was Terraform. I believe Terraform was the best way to approach this particular problem. Terraform and AWS integrated with each other seamlessly. I was able to leverage many Terraforms built in AWS modules. Some of the modules I implemented to complete the task were, aws_iam_role for security, aws api integration and most importantly the aws lambda function to run my python code to check the ssl certificates.

In order to run this particular solution you can run it using a bash in your terminal of choice. Here’s a quick example on how to run this program using bash.
Open terminal 
Copy code below
Past code in terminal
Edit the details to your liking. For example, I am currently using google.com but we can use whatever domain you would like.


curl --location --request POST 'https://bidhxl6svh.execute-api.us-east-1.amazonaws.com/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "hostname": “google.com",
    "port": "443"
}'


Some of the future features that I would like to use, is being able to continuously monitor multiple domains at one time. I would be able to do this by hardcoding the domains directly into the python code or we could feed a text file into python to parse and retrieve the domain information.
