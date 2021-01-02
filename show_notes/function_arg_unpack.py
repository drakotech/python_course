# Guide to Function Argument Unpacking in Python


def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
#Hi Kristine M Hudgens
greeting('Tiffany', 'Hudgens')
#Hi Tiffany Hudgens


def greeting(*names): #note: args can be anything (not common conv)
  print('Hi ' + ' '.join(names))
  


greeting('Kristine', 'M', 'Hudgens')
#Hi Kristine M Hudgens
greeting('Tiffany', 'Hudgens')
#Hi Tiffany Hudgens


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
#Hi Kristine M Hudgens, I hope that you're having a good Afternoon
greeting('Morning', 'Tiffany', 'Hudgens')
#Hi Tiffany Hudgens, I hope that you're having a good Morning

"""
Common convention is to call *args the list of arguments when 
unpacking.

The * is only used when declaring the function, inside the function
you can just use args.

Using multiple named args with an unpacking one will assign whatever
you named first then in order until the *args.

"""