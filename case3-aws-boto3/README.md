# Case 3 — AWS Automation with `boto3` (Advanced)

Goal: know how to talk to AWS from Python. This is the bridge between "I know Python
syntax" and "I can write the Lambda project".

Install boto3 locally to experiment (Lambda already has it built in):
```bash
pip install boto3
```

Run it (needs valid AWS credentials configured, e.g. `aws configure`):
```bash
python boto3_basics.py
```

## Concepts covered

### 1. Client vs Resource
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

### 2. Authentication
boto3 looks for credentials in this order (the "credential chain"):
1. Explicit params in code (avoid hardcoding secrets!)
2. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
3. `~/.aws/credentials` file (`aws configure`)
4. **IAM role** attached to the compute (EC2 instance profile, or in our case, the
   **Lambda execution role**) — this is the standard/secure way in production; never
   hardcode credentials in a Lambda.

### 3. Describing resources & filtering by tags
```python
response = ec2.describe_volumes(
    Filters=[
        {"Name": "status", "Values": ["available"]},          # unattached volumes
        {"Name": "tag:Environment", "Values": ["prod", "dev"]},
    ]
)
volumes = response["Volumes"]
```
Filters are applied server-side by AWS — much more efficient than pulling everything
and filtering in Python.

### 4. Reading tags
Tags come back as a list of `{"Key": ..., "Value": ...}` dicts, not a plain dict —
you usually convert them:
```python
def tags_to_dict(tag_list):
    return {t["Key"]: t["Value"] for t in tag_list or []}
```

### 5. Pagination
Some AWS list/describe calls cap results (e.g. 1000 items) and return a
`NextToken`. Use a **paginator** so you never miss results:
```python
paginator = ec2.get_paginator("describe_volumes")
for page in paginator.paginate(Filters=filters):
    for volume in page["Volumes"]:
        ...
```

### 6. Error handling with boto3
```python
from botocore.exceptions import ClientError

try:
    ec2.delete_volume(VolumeId=volume_id)
except ClientError as e:
    error_code = e.response["Error"]["Code"]
    print(f"AWS rejected the request: {error_code}")
```

Open [boto3_basics.py](boto3_basics.py) for runnable examples (safe — read-only, no
deletions).
