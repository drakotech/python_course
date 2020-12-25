def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
#Hi Guest!
greeting('Kristine')
#Hi Kristine! 


# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
#1911817852992
#[1]
print(some_function())
#1911817852992
#[1, 1]       

"""
It is bad practice to ever set a default variable as a list
because lists are immutable. You can see it creates a list with
multiple references to the same list.

"""