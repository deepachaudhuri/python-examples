"""
Final Project - EBS Volume Cleanup Lambda

Deletes unattached ('available') EBS volumes once they've passed their
environment's retention window, based on the `Environment` and `DeletedDate` tags.

See README.md in this folder for the full design/explanation.
"""

import logging
import os
from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client("ec2")

RETENTION_DAYS = {
    "prod": int(os.environ.get("PROD_RETENTION_DAYS", 30)),
    "dev": int(os.environ.get("DEV_RETENTION_DAYS", 7)),
}
DRY_RUN = os.environ.get("DRY_RUN", "true").lower() == "true"

TAG_ENV_KEY = "Environment"
TAG_DELETED_KEY = "DeletedDate"  # ISO date (YYYY-MM-DD), stamped when the parent instance was terminated


def tags_to_dict(tag_list):
    """AWS returns tags as [{'Key': ..., 'Value': ...}, ...] -> convert to a dict."""
    return {t["Key"]: t["Value"] for t in (tag_list or [])}


def get_stale_volumes():
    """Yield all unattached EBS volumes, page by page."""
    paginator = ec2.get_paginator("describe_volumes")
    filters = [{"Name": "status", "Values": ["available"]}]
    for page in paginator.paginate(Filters=filters):
        for volume in page["Volumes"]:
            yield volume


def days_since(date_str):
    deleted_on = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    return (now - deleted_on).days


def is_eligible_for_cleanup(tags):
    """Check the Environment + DeletedDate tags against the retention policy."""
    environment = tags.get(TAG_ENV_KEY)
    deleted_date = tags.get(TAG_DELETED_KEY)

    if environment not in RETENTION_DAYS or not deleted_date:
        return False, None

    try:
        age_days = days_since(deleted_date)
    except ValueError:
        logger.warning("Bad %s tag value: %s", TAG_DELETED_KEY, deleted_date)
        return False, None

    return age_days > RETENTION_DAYS[environment], age_days


def delete_volume(volume_id):
    try:
        ec2.delete_volume(VolumeId=volume_id)
        logger.info("Deleted volume %s", volume_id)
        return True
    except ClientError as e:
        logger.error("Failed to delete %s: %s", volume_id, e.response["Error"]["Message"])
        return False


def lambda_handler(event, context):
    summary = {"scanned": 0, "eligible": 0, "deleted": 0, "skipped": 0, "errors": 0}

    for volume in get_stale_volumes():
        summary["scanned"] += 1
        volume_id = volume["VolumeId"]
        tags = tags_to_dict(volume.get("Tags"))

        eligible, age_days = is_eligible_for_cleanup(tags)
        if not eligible:
            summary["skipped"] += 1
            continue

        summary["eligible"] += 1
        environment = tags[TAG_ENV_KEY]
        logger.info(
            "%s (%s) is %s days old, past the %s-day retention for '%s'",
            volume_id,
            tags.get("Name", "unnamed"),
            age_days,
            RETENTION_DAYS[environment],
            environment,
        )

        if DRY_RUN:
            logger.info("[DRY RUN] would delete %s", volume_id)
            continue

        if delete_volume(volume_id):
            summary["deleted"] += 1
        else:
            summary["errors"] += 1

    logger.info("Cleanup summary: %s", summary)
    return summary


if __name__ == "__main__":
    print(lambda_handler({}, None))
