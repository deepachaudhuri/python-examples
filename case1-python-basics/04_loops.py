"""
Loops: for and while
Run: python 04_loops.py
"""

servers = ["web-1", "web-2", "worker-1"]

# for loop over a list
for server in servers:
    print("checking server:", server)

tags = {"Environment": "prod", "Team": "devops"}

# for loop over a dict
for key, value in tags.items():
    print(f"{key} = {value}")

# for loop with enumerate - use when you also need the index
for index, server in enumerate(servers):
    print(f"[{index}] {server}")

# while loop - repeats until the condition becomes False
count = 0
while count < 3:
    print("retry attempt", count)
    count += 1

# break / continue
for server in servers:
    if server == "worker-1":
        continue          # skip this one, keep looping
    if server == "web-2":
        break              # stop the loop entirely
    print("processing:", server)
