# What Does it Mean to Return a Value from a Python Function?

def full_name(first, last):
  return f'{first} {last}'


kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')


greeting(kristine)
#Hi Kristine Hudgens!

"""
If we were to use print instead of return in the full_name function 
then the greeting function would print 
Hi none 
Because when you print to the console none is returned. 
So the first and last variables = none since nothing is stored in
it.

"""