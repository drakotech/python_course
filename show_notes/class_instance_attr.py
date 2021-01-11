# Class vs Instance Attributes in Python

class Website:
  def __init__(self, title):
    self.title = title


ws = Website('My Website Title')
print(ws.__dict__)
#{'title': 'My Website Title'}

ws_two = Website('My Second Title')
print(ws_two.__dict__)
#{'title': 'My Second Title'}


class DifferentWebsite:
  title = 'My Class Title'

dw = DifferentWebsite()
print(dw.title)
#My Class Title

dw_two = DifferentWebsite()
print(dw_two.title)
#My Class Title

"""
The main difference between a class attribute and an instance
attribute is the name.
Class attribute is an attribute that belongs to the class definition.
It is hard coded directly into the class and you can call it
whenever you need it.

An instance attribute belongs to the instance as above where we
needed to pass that value in directly into the instance whenever
we created it. And for every other instance of the class we needed to
pass a different value in order to have access to it.

One of the easiest ways is when working with another persons code we 
can use the __dict__ function to look at everything we have access to.

"""