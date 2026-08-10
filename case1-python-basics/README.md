# Case 1 — Python Basics (Easy)

[Home](../README.md) | **1. Basics** | [2. Intermediate](../case2-intermediate/README.md) | [3. AWS boto3](../case3-aws-boto3/README.md) | [Final Project](../final-project-ebs-cleanup/README.md)

Goal: be comfortable reading/writing simple Python — variables, data types,
conditionals, loops, functions, and the core collections (`list`, `dict`, `tuple`, `set`).

Each concept below has its own small, runnable file so you can experiment with one
thing at a time instead of one giant script.

**Jump to a topic:** [Variables & data types](#variables) · [Operators](#operators) · [Conditionals](#conditionals) · [Loops](#loops) · [Functions](#functions) · [Collections](#collections)

<a id="variables"></a>
## 1. Variables & data types → [01_variables_and_datatypes.py](01_variables_and_datatypes.py)
```bash
python 01_variables_and_datatypes.py
```
A **variable** is just a name pointing to a value. Python figures out the type for
you (dynamically typed) — no need to declare `int x = 5` like in Java/C#.
- `str`, `int`, `float`, `bool` → single values
- `type(x)` tells you the type; `str(x)` / `int(x)` / `float(x)` convert between types
- `None` means "no value" — common for a tag that might not exist:
  `deleted_date = tags.get("DeletedDate")  # None if the tag isn't set`

<a id="operators"></a>
## 2. Operators → [02_operators.py](02_operators.py)
```bash
python 02_operators.py
```
- **Arithmetic**: `+ - * / // % **` (`/` always gives a float, `//` gives a whole number, `%` gives the remainder)
- **Comparison**: `== != > < >= <=` → always produce a `bool` (`True`/`False`)
- **Logical**: `and or not` → combine multiple `bool` conditions, e.g.
  `environment == "prod" and days_old > 30`

<a id="conditionals"></a>
## 3. Conditionals (`if` / `elif` / `else`) → [03_conditionals.py](03_conditionals.py)
```bash
python 03_conditionals.py
```
```python
if cpu_usage > 80:
    print("scale up")
elif cpu_usage < 20:
    print("scale down")
else:
    print("steady state")
```
- Python uses **indentation** (not `{}`) to define a block — this trips up a lot of
  beginners coming from other languages.
- `elif` = "else if", checked only if the one above was `False`.
- Conditions can be nested (an `if` inside another `if`) for multi-step logic, like
  "if prod, then check if it's past retention".

<a id="loops"></a>
## 4. Loops (`for` / `while`) → [04_loops.py](04_loops.py)
```bash
python 04_loops.py
```
```python
for server in servers:          # loop over a list
    print(server)

for name, env in tags.items():  # loop over a dict (key, value pairs)
    print(name, env)

count = 0
while count < 3:                # loop while a condition stays True
    count += 1
```
- `for` is used when you know what you're iterating over (a list, dict, range).
- `while` is used when you loop until some condition changes (e.g. retrying).
- `break` exits the loop immediately; `continue` skips to the next iteration.
- `enumerate(list)` gives you both the index and the value when you need both.

<a id="functions"></a>
## 5. Functions → [05_functions.py](05_functions.py)
```bash
python 05_functions.py
```
```python
def greet(name):
    return f"Hello, {name}"
```
- Functions let you avoid repeating code — write the logic once, call it many times.
- **Default arguments** (`def is_stale(days_old, threshold=30)`) let the caller
  optionally override a value.
- Functions can return more than a plain value — e.g. a `dict` summarizing a result.

<a id="collections"></a>
## 6. Collections (`list`, `tuple`, `dict`, `set`) → [06_collections.py](06_collections.py)
```bash
python 06_collections.py
```
These four are how Python groups multiple values together. Picking the right one is a
very common interview question, so know **what each is** and **when to use it**:

| Type | Syntax | Ordered? | Changeable? | Duplicates? | Real-world analogy |
|------|--------|----------|-------------|-------------|---------------------|
| **list** | `[1, 2, 3]` | Yes | Yes | Yes | A to-do list — add/remove/reorder items freely |
| **tuple** | `(1, 2, 3)` | Yes | **No** | Yes | A fixed record, like a date `(year, month, day)` — shouldn't change |
| **dict** | `{"key": "value"}` | Yes (insertion order) | Yes | Keys must be unique | A phone book — look up a value by name, not by position. **This is what other languages (Java/JS) call a "map"/"hashmap" — Python just calls it `dict`.** |
| **set** | `{1, 2, 3}` | No | Yes | **No** — auto-removes dupes | A guest list where nobody can be added twice |

### `list` — an ordered, changeable collection
Use it when you have **many items of the same kind** and the order/count can change.
```python
instance_ids = ["i-0123", "i-0456", "i-0789"]
instance_ids.append("i-0999")
```
**AWS scenario:** `describe_instances()` / `describe_volumes()` almost always return a
**list** of resources — e.g. `response["Volumes"]` is a list of every volume that
matched your filter. You loop over that list to process each one.

### `tuple` — an ordered, unchangeable collection
Use it for a **fixed, small group of values that belong together and shouldn't change**.
```python
region_az = ("us-east-1", "us-east-1a")   # region + AZ always travel together
```
**AWS scenario:** returning more than one related value from a function, e.g.
`return volume_id, is_expired` returns a tuple `(volume_id, is_expired)` — cheap and
common, and since it's unchangeable it's safe to pass around without someone
accidentally mutating it later.

### `dict` (a.k.a. "map"/"hashmap" in other languages) — key/value lookups
Use it whenever you need to **look something up by name** instead of by position.
```python
tags = {"Environment": "prod", "Team": "devops"}
print(tags["Environment"])          # "prod"
print(tags.get("Owner", "unknown")) # safe lookup with a default if missing
```
**AWS scenario:** this is huge in AWS automation — **every tag, every API response
from boto3, is a dict** (or a list of dicts). AWS tags literally come back as
`[{"Key": "Environment", "Value": "prod"}]`, which you convert into a normal dict
`{"Environment": "prod"}` to make lookups easy (see [case3](../case3-aws-boto3/README.md)).

### `set` — unique values only
Use it when you only care about **distinct values**, not order or duplicates.
```python
regions_seen = {"us-east-1", "us-west-2", "us-east-1"}  # -> {"us-east-1", "us-west-2"}
```
**AWS scenario:** you scan 500 EBS volumes and want to know how many **unique**
Availability Zones they're spread across — put the AZ of each volume into a `set` and
the duplicates disappear automatically.

### Quick decision guide
- Need to **loop through many similar items**? → `list`
- Need a **small fixed group of values, shouldn't change**? → `tuple`
- Need to **look up a value by name/key** (like tags)? → `dict`
- Need to **remove duplicates / check uniqueness**? → `set`

Once all six feel comfortable, move on to
[case2-intermediate](../case2-intermediate/README.md).
