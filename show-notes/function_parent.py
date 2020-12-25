# How to Nest Functions in Parent Functions in Python

def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')


"""
Correct indentation is important. If you use 2 spces,
then 4 would be needed inside of the child function.

Benefit is that child functions are able to access its
parent's variables.

Use nested functions when the nested function does not need
to be called by a different part of the application. 

If a nested function is needed by aother function outside 
of its parent then it should be its own function.

"However, if some other part of the program needs access
to the full_name function, you may want to keep it separate,
and call them independent of each other." 

"That's my personal rule of thumb when it comes to choosing
when and when not to nest functions in python."
~ Jorden Hudgens

"""