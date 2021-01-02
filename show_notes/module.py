# How to Create a Custom Module and Import It In the Python Repl

import math

math.sqrt(4)


# Place in file helper.py
def greeting(first, last):
  return f'Hi {first} {last}!'

# Call from repl
import helper

helper.greeting('Kristine', 'Hudgens')