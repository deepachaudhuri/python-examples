# Case 1 — Python Basics (Easy)

Goal: be comfortable reading/writing simple Python — variables, data types,
conditionals, loops, functions, and the core collections (`list`, `dict`, `tuple`, `set`).

Each concept below has its own small, runnable file so you can experiment with one
thing at a time instead of one giant script.

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

## 2. Operators → [02_operators.py](02_operators.py)
```bash
python 02_operators.py
```
- **Arithmetic**: `+ - * / // % **` (`/` always gives a float, `//` gives a whole number, `%` gives the remainder)
- **Comparison**: `== != > < >= <=` → always produce a `bool` (`True`/`False`)
- **Logical**: `and or not` → combine multiple `bool` conditions, e.g.
  `environment == "prod" and days_old > 30`

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

## 6. Collections (`list`, `tuple`, `dict`, `set`) → [06_collections.py](06_collections.py)
```bash
python 06_collections.py
```
- **list** `[]` — ordered, changeable, allows duplicates → good for a list of instance IDs.
- **tuple** `()` — ordered, unchangeable → good for fixed data like `(region, az)`.
- **dict** `{}` — key/value pairs → good for tags: `{"Environment": "prod"}`.
  `.get(key, default)` is the safe way to read a key that might not exist.
- **set** `{...}` (or `set()`) — unique values only → good for de-duplicating AZs/regions.

Once all six feel comfortable, move on to
[case2-intermediate](../case2-intermediate/README.md).
