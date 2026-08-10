# Case 3 — AWS Automation with `boto3` (Advanced)

Goal: know how to talk to AWS from Python. This is the bridge between "I know Python
syntax" and "I can write the Lambda project".

Install boto3 locally to experiment (Lambda already has it built in):
```bash
pip install boto3
```

All examples below need valid AWS credentials configured (`aws configure`) and are
**read-only** except the error-handling one, which intentionally targets a volume ID
that doesn't exist so nothing real gets deleted.

## 1. Client vs Resource → [01_client_vs_resource.py](01_client_vs_resource.py)
```bash
python 01_client_vs_resource.py
```
`boto3` gives you two styles of API:
- **client** — low-level, maps 1:1 to the AWS API, returns raw dicts. Most Lambda
  automation uses `client` because it's explicit and predictable.
  ```python
  ec2 = boto3.client("ec2", region_name="us-east-1")
  ```
- **resource** — higher-level, object-oriented wrapper (not available for every
  service). Nice for quick scripts, less common in production Lambdas.
  ```python
  ec2 = boto3.resource("ec2")
  ```

**Authentication** (how boto3 finds credentials, in order): explicit params in code
(avoid!) → environment variables → `~/.aws/credentials` → an **IAM role** attached to
the compute (in Lambda, this is the execution role — the standard, secure approach;
never hardcode credentials).

## 2. Describing resources & filtering by tags → [02_tags_and_filters.py](02_tags_and_filters.py)
```bash
python 02_tags_and_filters.py
```
```python
response = ec2.describe_volumes(
    Filters=[
        {"Name": "status", "Values": ["available"]},          # unattached volumes
        {"Name": "tag:Environment", "Values": ["prod", "dev"]},
    ]
)
```
Filters are applied **server-side** by AWS — far more efficient than pulling
everything and filtering in Python. Tags come back as a list of
`{"Key": ..., "Value": ...}` dicts, not a plain dict, so we convert them:
```python
def tags_to_dict(tag_list):
    return {t["Key"]: t["Value"] for t in tag_list or []}
```

## 3. Pagination → [03_pagination.py](03_pagination.py)
```bash
python 03_pagination.py
```
Some AWS list/describe calls cap results (e.g. 1000 items) and return a `NextToken`.
Use a **paginator** so you never silently miss results on a large account:
```python
paginator = ec2.get_paginator("describe_volumes")
for page in paginator.paginate(Filters=filters):
    for volume in page["Volumes"]:
        ...
```

## 4. Error handling with boto3 → [04_error_handling.py](04_error_handling.py)
```bash
python 04_error_handling.py
```
```python
from botocore.exceptions import ClientError

try:
    ec2.delete_volume(VolumeId=volume_id)
except ClientError as e:
    error_code = e.response["Error"]["Code"]
    print(f"AWS rejected the request: {error_code}")
```
Always catch `ClientError` (and `NoCredentialsError` if credentials might be missing)
around any AWS API call — never let one bad/missing resource crash the whole script.

Once comfortable, move on to the
[final project](../final-project-ebs-cleanup/README.md), which combines everything
from cases 1–3 into one real Lambda function.
