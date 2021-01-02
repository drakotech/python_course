# How to Combine All Argument Types in a Single Python Function


def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('Morning',
         'Kristine', 'Hudgens',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')
#Returns:
"""
Hi Kristine Hudgens, I hope that you're having a good Morning.
Your tasks for the day are:
first -> Empty dishwasher  
second -> Take pupper out  
third -> math homework 

"""


"""
Comm conv when using a large number of arguments is to put them all
on a different line.

"""