# Overview of Keyword Arguments in Python Functions


def greeting(**kwargs):
  print(kwargs)


greeting()
#{}
# When no keword args were given
greeting(first = 'Kristine', last = 'Hudgens')
#{'first': 'Kristine', 'last': 'Hudgens'}

def conditional_greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')
# In this function we use the if conditional


conditional_greeting()
#Hi Guest!
conditional_greeting(first = 'Kristine', last = 'Hudgens')
#Hi Kristine Hudgens, have a great day!  


"""
This is all about how to inclued named arguments while unpacking.

Comm conv is using **kw + args for 'keyword argumets'.

Main difference between * and ** is that * returns a list and **
returns a dictionary to allow for key value calls.

"""