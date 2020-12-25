# Guide to Continue and Break in Python Loops

usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')
    """
    jon is allowed
    tyrion is allowed
    theon is allowed
    Sorry, cersei, you are not allowed
    sansa is allowed

    """

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)

  """
  jon
  tyrion
  theon
  cersei was found at index 3
  
  """

"""
The main difference between continue and break is that break stops
going thorugh the rest of the collection all the way to the top of
the code block. In the example above break was used and stopped the
for in loop as well as the if statement and because of this, 
Sansa was omitted.

"""