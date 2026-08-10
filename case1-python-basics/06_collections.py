"""
Collections: list, tuple, dict, set
Run: python 06_collections.py
"""

# list [] - ordered, changeable, duplicates allowed
volume_ids = ["vol-111", "vol-222", "vol-333"]
volume_ids.append("vol-444")
print("list:", volume_ids)

# tuple () - ordered, unchangeable - good for fixed data
region_az = ("us-east-1", "us-east-1a")
print("tuple:", region_az)

# dict {} - key/value pairs - good for tags
volume_info = {"id": "vol-111", "state": "available"}
volume_info["environment"] = "prod"   # add a new key
print("dict:", volume_info)
print("lookup:", volume_info.get("environment"))
print("missing key with default:", volume_info.get("owner", "unknown"))

# set {} (via set()) - unique values only, good for de-duplicating
envs_seen = {"prod", "dev", "prod", "dev", "staging"}
print("set (duplicates removed):", envs_seen)
