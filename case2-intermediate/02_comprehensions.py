"""
List & dict comprehensions
Run: python 02_comprehensions.py
"""

volumes = [
    {"VolumeId": "vol-111", "Environment": "prod", "DaysOld": 34},
    {"VolumeId": "vol-222", "Environment": "dev", "DaysOld": 3},
    {"VolumeId": "vol-333", "Environment": "prod", "DaysOld": 12},
]

# list comprehension - build a new list by filtering an existing one
prod_volumes = [v for v in volumes if v["Environment"] == "prod"]
print("prod volumes:", prod_volumes)

# list comprehension - transform each item into something else
volume_ids = [v["VolumeId"] for v in volumes]
print("just the ids:", volume_ids)

# dict comprehension - build a lookup table keyed by VolumeId
volume_by_id = {v["VolumeId"]: v for v in volumes}
print("lookup by id:", volume_by_id["vol-222"])
