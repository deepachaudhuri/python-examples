"""
Conditionals: if / elif / else
Run: python 03_conditionals.py
"""

cpu_usage = 91.2

if cpu_usage > 80:
    print("ALERT: scale up")
elif cpu_usage < 20:
    print("scale down")
else:
    print("steady state")

# Nested conditions + combined logic - close to real DevOps decision-making
environment = "prod"
days_old = 34
retention_days = 30

if environment == "prod":
    if days_old > retention_days:
        print("prod volume is past retention -> eligible for cleanup")
    else:
        print("prod volume still within retention window")
else:
    print("not a prod resource, skipping this rule")
