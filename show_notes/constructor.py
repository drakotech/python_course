# Guide to Python's __init__ Constructor Function

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def formatter(self):
    return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)

print(google.formatter())
#Google owes: $100
print(snapchat.formatter())
#SnapChat owes: $200

"""
Double underscore == "Dunder"

The __init__ constructor assigned client and total arguments
to the variables.

Requires self argument to access the variables.

"""