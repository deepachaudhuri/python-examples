"""
Operators: arithmetic, comparison, logical
Run: python 02_operators.py
"""

# Arithmetic
a, b = 10, 3
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)    # true division  -> float
print("a // b =", a // b)   # floor division -> int
print("a % b  =", a % b)    # remainder
print("a ** b =", a ** b)   # exponent

# Comparison - always returns a bool
retention_days = 30
days_since_deleted = 34
print("days_since_deleted > retention_days:", days_since_deleted > retention_days)
print("days_since_deleted == retention_days:", days_since_deleted == retention_days)

# Logical - combine multiple conditions
environment = "prod"
is_stale = days_since_deleted > retention_days
should_delete = environment == "prod" and is_stale
print("should_delete:", should_delete)
