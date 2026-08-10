"""
Functions
Run: python 05_functions.py
"""

def greet(name):
    return f"Hello, {name}!"

print(greet("Deepa"))


def is_stale(days_old, threshold=30):
    """Default argument: threshold=30 is used if the caller doesn't pass one."""
    return days_old > threshold

print(is_stale(34))               # uses default threshold=30
print(is_stale(5, threshold=7))   # overrides the default


def summarize(volume_id, environment, days_old):
    """Functions can return multiple pieces of info in one call, e.g. as a dict."""
    threshold = 30 if environment == "prod" else 7
    return {"volume_id": volume_id, "stale": is_stale(days_old, threshold)}

print(summarize("vol-111", "dev", 10))
