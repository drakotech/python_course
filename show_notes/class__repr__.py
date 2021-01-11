# Overview of Dunder Methods in Python: __repr__

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self):
    return f"Invoice({self.client}, {self.total})"


inv = Invoice('Google', 500)
print(str(inv))
#Invoice from Google for 500
print(repr(inv))
#Invoice(Google, 500)

"""
__repr__ is a debugging tool to return values and variables 
to ensure the data is being passed correctly.

"""