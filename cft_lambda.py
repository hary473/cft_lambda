import boto3

def lambda_handler(event, context):
   # Create a CloudFormation client
   cloudformation = boto3.client('cloudformation')

   # Create an S3 client
   s3 = boto3.client('s3')

   # Define the S3 bucket and key for the CloudFormation template
   s3_bucket = 'my-bucket'
   s3_key = 'cloudformation-template.yaml'

   # Download the template file from S3
   response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
   template_body = response['Body'].read().decode('utf-8')

   # Create the CloudFormation stack
   stack_name = 'my-stack'
   response = cloudformation.create_stack(
       StackName=stack_name,
       TemplateBody=template_body
   )

   return {
       'statusCode': 200,
       'body': 'CloudFormation stack created successfully'
   }