"""
client vs resource
Run: python 01_client_vs_resource.py  (needs AWS credentials, e.g. `aws configure`)
"""

import boto3

# client - low-level, 1:1 mapping to the AWS API, returns raw dicts - most common in Lambdas
ec2_client = boto3.client("ec2", region_name="us-east-1")
print("client type:", type(ec2_client))

# resource - higher-level, object-oriented wrapper (not available for every AWS service)
ec2_resource = boto3.resource("ec2", region_name="us-east-1")
print("resource type:", type(ec2_resource))

# the same call, in each style:
response = ec2_client.describe_volumes(MaxResults=5)
print("client call returned", len(response["Volumes"]), "volumes (as raw dicts)")

for volume in ec2_resource.volumes.limit(5):
    print("resource call ->", volume.id, volume.state)
