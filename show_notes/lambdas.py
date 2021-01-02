# Guide to Python Lambdas


full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))
#Hi there Kristine Hudgens

"""
Functions are known as first class citiens where they are treated
as objects.

Lambdas are more like variables that can perform an operation.
They allow yout oquickly and easily wrap functionality, store
it in a variable, and then pass that value, pass that entire
process to other functions.

"""