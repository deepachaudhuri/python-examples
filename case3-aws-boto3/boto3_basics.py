"""
Case 3 - AWS automation with boto3 (read-only examples, safe to run).
Requires: pip install boto3, and valid AWS credentials (aws configure).
Run: python boto3_basics.py
"""

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

REGION = "us-east-1"


def tags_to_dict(tag_list):
    """AWS returns tags as [{'Key': 'Environment', 'Value': 'prod'}, ...] -> convert to a dict."""
    return {t["Key"]: t["Value"] for t in (tag_list or [])}


def list_available_volumes(ec2_client):
    """Find unattached ('available') EBS volumes tagged Environment=prod/dev, with pagination."""
    filters = [
        {"Name": "status", "Values": ["available"]},
        {"Name": "tag:Environment", "Values": ["prod", "dev"]},
    ]

    paginator = ec2_client.get_paginator("describe_volumes")
    volumes = []
    for page in paginator.paginate(Filters=filters):
        for vol in page["Volumes"]:
            volumes.append({
                "VolumeId": vol["VolumeId"],
                "Size": vol["Size"],
                "Tags": tags_to_dict(vol.get("Tags")),
            })
    return volumes


def main():
    # client = low-level, 1:1 mapping to the AWS API - most common choice for Lambdas
    ec2 = boto3.client("ec2", region_name=REGION)

    try:
        volumes = list_available_volumes(ec2)
    except NoCredentialsError:
        print("No AWS credentials found - run `aws configure` first.")
        return
    except ClientError as e:
        print(f"AWS rejected the request: {e.response['Error']['Code']}")
        return

    if not volumes:
        print("No unattached prod/dev volumes found (or none exist in this account).")
        return

    for vol in volumes:
        print(f"{vol['VolumeId']} | {vol['Size']}GB | tags={vol['Tags']}")


if __name__ == "__main__":
    main()
