"""
boto3 error handling with botocore.exceptions
Run: python 04_error_handling.py  (needs AWS credentials)
"""

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

ec2 = boto3.client("ec2", region_name="us-east-1")

try:
    ec2.delete_volume(VolumeId="vol-doesnotexist123")
except ClientError as e:
    error_code = e.response["Error"]["Code"]
    print(f"AWS rejected the request: {error_code}")
except NoCredentialsError:
    print("No AWS credentials found - run `aws configure` first.")
