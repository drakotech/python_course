# How to Get and Set Data in a Python Class

class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)

print(google.client)
#Google

google.client = 'Yahoo'

print(google.client)
#Yahoo

"""
With this method in line 18we were able to set a value 
in a class.

"""