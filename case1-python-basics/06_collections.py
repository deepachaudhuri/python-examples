"""
Collections: list, tuple, dict, set
(dict is what other languages call a "map"/"hashmap")
Run: python 06_collections.py
"""

# ---------- list [] - ordered, changeable, duplicates allowed ----------
# Use it for a growing/shrinking group of similar items, e.g. instance IDs from
# describe_instances() - AWS always hands these back as a list.
volume_ids = ["vol-111", "vol-222", "vol-333"]
volume_ids.append("vol-444")
print("list:", volume_ids)
print("first item:", volume_ids[0], "| item count:", len(volume_ids))

# ---------- tuple () - ordered, unchangeable ----------
# Use it for a fixed small group of values that belong together and shouldn't
# change, e.g. a function returning more than one related value at once.
region_az = ("us-east-1", "us-east-1a")
print("tuple:", region_az)


def check_volume(volume_id, days_old):
    """Returning a tuple is a common way to hand back 2+ related values."""
    is_expired = days_old > 30
    return volume_id, is_expired   # packs into a tuple automatically


vol_id, expired = check_volume("vol-111", 34)   # unpacked back into two variables
print(f"tuple return -> {vol_id} expired={expired}")

# ---------- dict {} - key/value pairs, a.k.a. "map"/"hashmap" ----------
# Use it whenever you look something up BY NAME instead of by position.
# Every AWS tag and almost every boto3 API response is a dict (or list of dicts).
volume_info = {"id": "vol-111", "state": "available"}
volume_info["environment"] = "prod"   # add a new key
print("dict:", volume_info)
print("lookup:", volume_info.get("environment"))
print("missing key with default:", volume_info.get("owner", "unknown"))

# AWS tags arrive as a list of {"Key":..., "Value":...} dicts - convert to a plain
# dict so lookups are simple, e.g. tags["Environment"] instead of scanning a list.
raw_aws_tags = [{"Key": "Environment", "Value": "prod"}, {"Key": "Team", "Value": "devops"}]
tags = {t["Key"]: t["Value"] for t in raw_aws_tags}
print("converted AWS tags to a dict:", tags)

# ---------- set {} (via set()) - unique values only ----------
# Use it to de-duplicate - e.g. finding how many DISTINCT AZs/regions a batch of
# volumes is spread across, ignoring repeats.
volume_azs = ["us-east-1a", "us-east-1b", "us-east-1a", "us-east-1c", "us-east-1a"]
unique_azs = set(volume_azs)
print("all AZs seen:", volume_azs)
print("unique AZs:", unique_azs, "| count:", len(unique_azs))

