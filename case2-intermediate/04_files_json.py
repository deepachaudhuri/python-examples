"""
Reading/writing files and JSON
Run: python 04_files_json.py
"""

import json
import os

volumes = [
    {"VolumeId": "vol-111", "Environment": "prod", "DaysOld": 34},
    {"VolumeId": "vol-222", "Environment": "dev", "DaysOld": 3},
]

output_path = os.path.join(os.path.dirname(__file__), "volumes_report.json")

# "with" auto-closes the file even if an error happens partway through
with open(output_path, "w") as f:
    json.dump(volumes, f, indent=2)
print("wrote:", output_path)

with open(output_path) as f:
    loaded = json.load(f)
print("loaded back from disk:", loaded[0])

os.remove(output_path)  # cleanup after the demo
