import boto3
import random

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("State:", instance['State']['Name'])
        print("-"*20)
import random

s3 = boto3.client('s3')

bucket_name = f"sunil-auto-{random.randint(1000,9999)}"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket created:", bucket_name)
