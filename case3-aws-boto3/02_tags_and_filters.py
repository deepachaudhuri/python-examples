"""
Describing resources & filtering by tags
Run: python 02_tags_and_filters.py  (needs AWS credentials)
"""

import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")


def tags_to_dict(tag_list):
    """AWS returns tags as [{'Key': 'Environment', 'Value': 'prod'}, ...] -> convert to a dict."""
    return {t["Key"]: t["Value"] for t in (tag_list or [])}


response = ec2.describe_volumes(
    Filters=[
        {"Name": "status", "Values": ["available"]},          # unattached volumes only
        {"Name": "tag:Environment", "Values": ["prod", "dev"]},
    ]
)

for vol in response["Volumes"]:
    print(vol["VolumeId"], tags_to_dict(vol.get("Tags")))
