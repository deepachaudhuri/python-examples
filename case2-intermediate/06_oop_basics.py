"""
Just enough OOP to read real-world automation code
Run: python 06_oop_basics.py
"""

class Volume:
    def __init__(self, volume_id, environment, days_old):
        self.volume_id = volume_id
        self.environment = environment
        self.days_old = days_old

    def is_expired(self, retention_days):
        return self.days_old > retention_days

    def __repr__(self):
        return f"Volume({self.volume_id}, {self.environment}, {self.days_old}d)"


volumes = [
    Volume("vol-111", "prod", 34),
    Volume("vol-222", "dev", 3),
]

RETENTION_DAYS = {"prod": 30, "dev": 7}

for v in volumes:
    expired = v.is_expired(RETENTION_DAYS[v.environment])
    print(v, "-> expired:", expired)
