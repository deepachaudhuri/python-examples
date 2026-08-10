"""
Pagination - never miss results on accounts with lots of resources
Run: python 03_pagination.py  (needs AWS credentials)
"""

import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")

# describe_volumes caps how many results come back per call - a paginator
# automatically loops through every page so you never silently miss results
paginator = ec2.get_paginator("describe_volumes")

total = 0
for page in paginator.paginate(Filters=[{"Name": "status", "Values": ["available"]}]):
    total += len(page["Volumes"])

print("total unattached volumes found across all pages:", total)
