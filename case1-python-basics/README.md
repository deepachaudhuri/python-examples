# Case 1 — Python Basics (Easy)

Goal: be comfortable reading/writing simple Python — variables, data types,
conditionals, loops, functions, and the core collections (`list`, `dict`, `tuple`, `set`).

Run it:
```bash
python basics.py
```

## Concepts covered

### 1. Variables & data types
See the main [README](../README.md#2-variables--data-types-the-absolute-basics) for the
basics. Rule of thumb: `str`, `int`, `float`, `bool` for single values; `list`, `dict`,
`tuple`, `set` for collections.

### 2. Operators
- Arithmetic: `+ - * / // % **`
- Comparison: `== != > < >= <=`
- Logical: `and or not`

### 3. Conditionals
```python
if cpu_usage > 80:
    print("scale up")
elif cpu_usage < 20:
    print("scale down")
else:
    print("steady state")
```

### 4. Loops
```python
for server in servers:          # loop over a list
    print(server)

for name, env in tags.items():  # loop over a dict
    print(name, env)

count = 0
while count < 3:                # loop with a condition
    count += 1
```

### 5. Functions
```python
def greet(name):
    return f"Hello, {name}"
```
Functions let you avoid repeating code — write once, call many times.

### 6. Collections
- **list** `[]` — ordered, changeable, allows duplicates → good for a list of instance IDs.
- **tuple** `()` — ordered, unchangeable → good for fixed data like `(region, az)`.
- **dict** `{}` — key/value pairs → good for tags: `{"Environment": "prod"}`.
- **set** `{}` (via `set()`) — unique values only → good for de-duplicating AZs/regions.

Open [basics.py](basics.py) for runnable examples of every concept above.
