"""
Case 1 - Python Basics
Run: python basics.py
"""

# ---------- 1. Variables & data types ----------
name = "web-server-01"      # str
age_days = 34                 # int
cpu_usage = 91.2               # float
is_prod = True                  # bool

print(name, age_days, cpu_usage, is_prod)
print(type(name), type(age_days), type(cpu_usage), type(is_prod))

# ---------- 2. Operators ----------
retention_days = 30
days_since_deleted = 34
is_older_than_retention = days_since_deleted > retention_days
print("Older than retention?", is_older_than_retention)

# ---------- 3. Conditionals ----------
if cpu_usage > 80:
    print("ALERT: scale up")
elif cpu_usage < 20:
    print("scale down")
else:
    print("steady state")

# ---------- 4. Loops ----------
servers = ["web-1", "web-2", "worker-1"]
for server in servers:
    print("checking server:", server)

tags = {"Environment": "prod", "Team": "devops"}
for key, value in tags.items():
    print(f"{key} = {value}")

count = 0
while count < 3:
    print("retry attempt", count)
    count += 1

# ---------- 5. Functions ----------
def greet(user_name):
    return f"Hello, {user_name}!"

print(greet("Deepa"))

def is_stale(days_old, threshold):
    """Returns True if a resource is older than the given threshold."""
    return days_old > threshold

print("Is stale?", is_stale(days_since_deleted, retention_days))

# ---------- 6. Collections ----------
volume_ids = ["vol-111", "vol-222", "vol-333"]        # list
region_az = ("us-east-1", "us-east-1a")                # tuple
unique_envs = {"prod", "dev", "prod", "dev"}            # set -> duplicates removed
volume_info = {"id": "vol-111", "state": "available"}   # dict

print(volume_ids)
print(region_az)
print(unique_envs)   # {'prod', 'dev'}
print(volume_info)
