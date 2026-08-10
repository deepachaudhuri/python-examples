"""
Variables & Data Types
Run: python 01_variables_and_datatypes.py
"""

name = "web-server-01"      # str   - text
age_days = 34                # int   - whole number
cpu_usage = 91.2              # float - decimal number
is_prod = True                  # bool  - True/False

print(name, age_days, cpu_usage, is_prod)
print(type(name), type(age_days), type(cpu_usage), type(is_prod))

# type casting - converting between types
age_as_text = str(age_days)
text_as_number = int("42")
print(age_as_text, type(age_as_text))
print(text_as_number, type(text_as_number))

# None = "no value yet" - common when an optional tag doesn't exist
deleted_date = None
print("deleted_date is:", deleted_date)
