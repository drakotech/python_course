# How to Use the Ternary Operator in Python Conditionals

role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'
#cannot access

if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)
#cannot access

"""
Ternary operators allow you to reorganize a typical if
statement into a single line and removes duplicate
assignments.

Used when you want to assign a variable under a condition.

"""