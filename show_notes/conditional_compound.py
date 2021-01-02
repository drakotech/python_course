# How to Build Compound Conditionals in Python

username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')
#Access permitted


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')
#Access permitted


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')
#Access permitted


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')
#You can access the admin dashboard


"""
The or operation checks the left side expression for true if it
finds it, it skips everything on the right.

And is higher level security because it strings on multiple 
expressions that require all of them to be true before executing.

'and not' expressions are used when the first expression needs to 
be true and the next expression needs to be false.

"""