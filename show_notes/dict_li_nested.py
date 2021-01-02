# Guide to Working with Lists of Nested Dictionaries


teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

#print(teams[0])
#{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}

angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1])
#Pujols

"""
Notes: Created a variable called teams, with a list of 2 dict
inside those dict is a key value pair with more nested
collections. This goes through how to access nested values 
with different data types. 

Advice: go one at a time to make sure each is accessing the 
value correctly.

"""