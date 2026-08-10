"""
datetime / timedelta - the core of the final project's "how old is this" logic
Run: python 05_datetime.py
"""

from datetime import datetime, timedelta, timezone

RETENTION_DAYS = {"prod": 30, "dev": 7}

# simulate a volume that was "deleted" 34 days ago
deleted_on = datetime.now(timezone.utc) - timedelta(days=34)
now = datetime.now(timezone.utc)
days_since_deletion = (now - deleted_on).days
print("days since deletion:", days_since_deletion)

environment = "prod"
if days_since_deletion > RETENTION_DAYS[environment]:
    print(f"volume is past the {environment} retention window -> eligible for cleanup")
else:
    print(f"volume is still within the {environment} retention window")

# parsing a date tag stored as plain text, e.g. "2026-07-01"
tag_value = "2026-07-01"
parsed_date = datetime.strptime(tag_value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
print("parsed tag date:", parsed_date, "-> days old:", (now - parsed_date).days)
