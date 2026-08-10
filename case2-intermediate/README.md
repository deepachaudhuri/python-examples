# Case 2 — Intermediate Python (Medium)

[Home](../README.md) | [1. Basics](../case1-python-basics/README.md) | **2. Intermediate** | [3. AWS boto3](../case3-aws-boto3/README.md) | [Final Project](../final-project-ebs-cleanup/README.md)

Goal: the concepts you'll actually use in a real automation script — flexible
functions, comprehensions, error handling, files/JSON, and date math (critical for the
final project's "delete if older than N days" logic).

Each concept has its own runnable file, same as case 1.

## 1. `*args` and `**kwargs` → [01_args_kwargs.py](01_args_kwargs.py)
```bash
python 01_args_kwargs.py
```
Lets a function accept a variable number of arguments.
```python
def delete_volumes(*volume_ids, dry_run=True, **extra_options):
    ...
```
- `*args` collects any extra **positional** args into a tuple.
- `**kwargs` collects any extra **keyword** args into a dict.
- Useful when a function needs to stay flexible as callers pass more options over time.

## 2. List / dict comprehensions → [02_comprehensions.py](02_comprehensions.py)
```bash
python 02_comprehensions.py
```
A compact way to build a list or dict from another iterable.
```python
prod_volumes = [v for v in volumes if v["Environment"] == "prod"]
volume_by_id = {v["VolumeId"]: v for v in volumes}
```
Readable and idiomatic — interviewers like seeing this instead of manual for-loops
with `.append()`.

## 3. Error handling (`try/except/else/finally`) → [03_error_handling.py](03_error_handling.py)
```bash
python 03_error_handling.py
```
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
- `else` runs only if no exception was raised.
- `finally` always runs — good for cleanup/logging regardless of success or failure.
- You can also define and raise your own errors, e.g. `class MissingTagError(Exception)`.

## 4. Files & JSON → [04_files_json.py](04_files_json.py)
```bash
python 04_files_json.py
```
```python
with open("volumes.json") as f:      # "with" auto-closes the file
    data = json.load(f)

with open("report.json", "w") as f:
    json.dump(data, f, indent=2)
```
`json.load`/`json.dump` convert between JSON text and Python dicts/lists — this is how
you'd read a config file or write a cleanup report to disk.

## 5. `datetime` and `timedelta` → [05_datetime.py](05_datetime.py)
```bash
python 05_datetime.py
```
```python
from datetime import datetime, timezone

deleted_on = datetime(2026, 7, 1, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
days_since_deletion = (now - deleted_on).days
```
This is exactly how the final project decides if an EBS volume has been "orphaned"
long enough to be deleted. Also covers `datetime.strptime()` for parsing a date stored
as plain text in a tag (e.g. `"2026-07-01"`).

## 6. A tiny bit of OOP → [06_oop_basics.py](06_oop_basics.py)
```bash
python 06_oop_basics.py
```
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
`__init__` runs when you create an object (`Volume(...)`); `self` refers to that
specific instance's data.

Once comfortable, move on to [case3-aws-boto3](../case3-aws-boto3/README.md).
