import boto3
from functions import getSecret

client = boto3.client('sns')

response = client.publish(
    TopicArn=getSecret('aws-arn'),
    Message='This is a test'
    )

print(response)
