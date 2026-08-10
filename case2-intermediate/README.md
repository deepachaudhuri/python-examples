# Case 2 — Intermediate Python (Medium)

Goal: the concepts you'll actually use in a real automation script — flexible
functions, comprehensions, error handling, files/JSON, and date math (critical for the
final project's "delete if older than N days" logic).

Run it:
```bash
python intermediate.py
```

## Concepts covered

### 1. `*args` and `**kwargs`
Lets a function accept a variable number of arguments.
```python
def delete_volumes(*volume_ids, dry_run=True, **extra_options):
    ...
```
- `*args` collects extra positional args into a tuple.
- `**kwargs` collects extra keyword args into a dict.

### 2. List / dict comprehensions
A compact way to build a list or dict from another iterable.
```python
prod_volumes = [v for v in volumes if v["Environment"] == "prod"]
volume_by_id = {v["VolumeId"]: v for v in volumes}
```
Readable and idiomatic — interviewers like seeing this instead of manual for-loops
with `.append()`.

### 3. Error handling (`try/except/else/finally`)
```python
try:
    delete_volume(volume_id)
except ClientError as e:
    log.error(f"Failed to delete {volume_id}: {e}")
else:
    log.info(f"Deleted {volume_id}")
finally:
    log.info("Done processing volume")
```
- `except` catches specific errors (never use a bare `except:`).
- `finally` always runs — good for cleanup/logging regardless of success or failure.
- You can also raise your own errors: `raise ValueError("missing tag")`.

### 4. Files & JSON
```python
with open("volumes.json") as f:      # "with" auto-closes the file
    data = json.load(f)

with open("report.json", "w") as f:
    json.dump(data, f, indent=2)
```

### 5. `datetime` and `timedelta` — the core of the final project
```python
from datetime import datetime, timezone

deleted_on = datetime(2026, 7, 1, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
days_since_deletion = (now - deleted_on).days
```
This is exactly how we'll decide if an EBS volume has been "orphaned" long enough to
be deleted.

### 6. A tiny bit of OOP
You don't need deep OOP for this interview, just enough to read code:
```python
class Volume:
    def __init__(self, volume_id, environment, days_old):
        self.volume_id = volume_id
        self.environment = environment
        self.days_old = days_old

    def is_expired(self, retention_days):
        return self.days_old > retention_days
```

Open [intermediate.py](intermediate.py) for runnable examples.
