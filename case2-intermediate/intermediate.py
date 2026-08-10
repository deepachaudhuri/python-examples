"""
Case 2 - Intermediate Python
Run: python intermediate.py
"""

import json
from datetime import datetime, timedelta, timezone

# ---------- 1. *args / **kwargs ----------
def delete_volumes(*volume_ids, dry_run=True, **extra_options):
    for vol_id in volume_ids:
        if dry_run:
            print(f"[DRY RUN] would delete {vol_id}")
        else:
            print(f"deleting {vol_id}")
    print("extra options:", extra_options)

delete_volumes("vol-111", "vol-222", dry_run=True, reason="stale")

# ---------- 2. List / dict comprehensions ----------
volumes = [
    {"VolumeId": "vol-111", "Environment": "prod", "DaysOld": 34},
    {"VolumeId": "vol-222", "Environment": "dev", "DaysOld": 3},
    {"VolumeId": "vol-333", "Environment": "prod", "DaysOld": 12},
]

prod_volumes = [v for v in volumes if v["Environment"] == "prod"]
volume_by_id = {v["VolumeId"]: v for v in volumes}

print("prod volumes:", prod_volumes)
print("lookup by id:", volume_by_id["vol-222"])

# ---------- 3. Error handling ----------
class MissingTagError(Exception):
    """Raised when a required tag is missing from a resource."""


def get_environment_tag(volume):
    try:
        return volume["Environment"]
    except KeyError:
        raise MissingTagError(f"volume {volume.get('VolumeId')} has no Environment tag")


try:
    get_environment_tag({"VolumeId": "vol-999"})
except MissingTagError as e:
    print("caught expected error:", e)
finally:
    print("finished tag lookup attempt")

# ---------- 4. Files & JSON ----------
with open("volumes_report.json", "w") as f:
    json.dump(volumes, f, indent=2)

with open("volumes_report.json") as f:
    loaded = json.load(f)
print("loaded back from disk:", loaded[0])

# ---------- 5. datetime / timedelta ----------
RETENTION_DAYS = {"prod": 30, "dev": 7}

deleted_on = datetime.now(timezone.utc) - timedelta(days=34)
now = datetime.now(timezone.utc)
days_since_deletion = (now - deleted_on).days
print("days since deletion:", days_since_deletion)

environment = "prod"
if days_since_deletion > RETENTION_DAYS[environment]:
    print(f"volume is past the {environment} retention window -> eligible for cleanup")

# ---------- 6. Tiny bit of OOP ----------
class Volume:
    def __init__(self, volume_id, environment, days_old):
        self.volume_id = volume_id
        self.environment = environment
        self.days_old = days_old

    def is_expired(self, retention_days):
        return self.days_old > retention_days


v = Volume("vol-111", "prod", 34)
print("is_expired:", v.is_expired(RETENTION_DAYS[v.environment]))
