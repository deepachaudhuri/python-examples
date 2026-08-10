# Python for DevOps — Learning Path

**Home** | [1. Basics](case1-python-basics/README.md) | [2. Intermediate](case2-intermediate/README.md) | [3. AWS boto3](case3-aws-boto3/README.md) | [Final Project](final-project-ebs-cleanup/README.md)

This folder is a self-contained crash course to get you ready in Python,
with a DevOps/AWS angle. It goes from **basic syntax → intermediate concepts → AWS
automation with boto3 → a final real-world Lambda project**.

Work through the folders in order:

```
python-examples/
├── case1-python-basics/        → Easy: syntax, variables, data types, control flow
├── case2-intermediate/         → Medium: functions, error handling, files, datetime
├── case3-aws-boto3/            → Advanced: talking to AWS with boto3
└── final-project-ebs-cleanup/  → Final Project: Lambda that cleans up stale EBS volumes
```

Each folder has its own `README.md` explaining the concepts, with **one small runnable
`.py` file per concept** (e.g. loops, conditionals, error handling) so you can run and
tweak each one individually. Run any file locally with:

```bash
python case1-python-basics/01_variables_and_datatypes.py
```

---

## 1. Why Python for DevOps?

Python is the most common scripting language in DevOps because:
- AWS, Azure, GCP all provide first-class Python SDKs (`boto3`, `azure-sdk`, etc.)
- AWS Lambda, Ansible, and most CI/CD tooling support/are written in Python
- It's readable, quick to write, and has a huge standard library (no need to reinvent
  things like JSON parsing, file I/O, datetime math, etc.)

You don't need to be a "software engineer" level Python expert. You need to be
comfortable with variables, loops, functions, dictionaries, error handling, reading/
writing files, and calling AWS APIs. That's exactly what this guide covers.

---

## 2. Variables & Data Types (the absolute basics)

A **variable** is just a name that points to a value in memory. Python is
**dynamically typed** — you don't declare a type, Python figures it out at runtime.

```python
name = "Deepa"          # str   (text)
age = 28                 # int   (whole number)
cpu_usage = 72.5         # float (decimal number)
is_prod = True           # bool  (True/False)
tags = ["prod", "web"]   # list  (ordered, changeable collection)
volume_ids = ("vol-1", "vol-2")   # tuple (ordered, unchangeable)
unique_zones = {"us-east-1a", "us-east-1b"}  # set (unique values only)
metadata = {"env": "prod", "days_old": 32}   # dict (key-value pairs)
```

Key things an interviewer expects you to know:
- **Mutable vs immutable**: lists/dicts/sets can change in place; strings/tuples/ints cannot.
- **Type checking**: `type(age)` → `<class 'int'>`, or `isinstance(age, int)` → `True`.
- **Type casting**: `str(age)`, `int("28")`, `float("72.5")`.
- **None**: Python's "no value" (like `null`). Used a lot for optional tags/fields:
  `deleted_date = tags.get("DeletedDate")  # None if the tag doesn't exist`

That's enough theory — the rest is learned by writing code. Go to
[case1-python-basics/README.md](case1-python-basics/README.md).

---

## 3. Roadmap

| Case | Level | Topics | Folder |
|------|-------|--------|--------|
| Case 1 | Easy | Variables, data types, operators, if/else, loops, functions, lists & dicts | [case1-python-basics](case1-python-basics/README.md) |
| Case 2 | Medium | Functions (`*args`/`**kwargs`), list comprehensions, try/except, file I/O, JSON, `datetime`/`timedelta` | [case2-intermediate](case2-intermediate/README.md) |
| Case 3 | Advanced | `boto3` basics: client vs resource, describing AWS resources, filtering by tags, pagination, error handling | [case3-aws-boto3](case3-aws-boto3/README.md) |
| Final Project | Real-world | Lambda function: EBS volume cleanup based on `Environment` tag + age (30 days prod / 7 days dev) | [final-project-ebs-cleanup](final-project-ebs-cleanup/README.md) |

---

## 4. What interviewers usually ask (quick cheat sheet)

- Difference between **list, tuple, set, dict** and when to use each.
- **Mutable default arguments** gotcha (`def f(x=[])` is a classic trap).
- `is` vs `==` (identity vs equality).
- List comprehensions vs loops (`[x for x in items if condition]`).
- `try/except/else/finally` and raising custom exceptions.
- Reading/writing files, `with open(...) as f:` (context managers close the file automatically).
- `*args` / `**kwargs` for flexible function signatures.
- How `boto3` clients authenticate (env vars, IAM role, `~/.aws/credentials`, credential chain).
- Pagination in AWS APIs (`describe_volumes` returns max 1000 items per call — use paginators).
- Idempotency and dry-run patterns before doing anything destructive (like deleting a volume).
- How you'd test a Lambda locally before deploying it.

Once you're comfortable with cases 1–3, move to the
[final project](final-project-ebs-cleanup/README.md) — that's the one to be ready to
explain end-to-end in your interview.
