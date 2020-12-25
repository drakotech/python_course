# Guide to Nested Collections in Python Dictionaries

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

astros = teams['astros']
print(astros)
#['Altuve', 'Correa', 'Bregman']
print(teams['angels'])
#['Trout', 'Pujols'] 
print(teams['yankees'])
#['Judge', 'Stanton']

"""
Notes: Slicing methods are possible through this method.
For example: print(teams['astros'][:2]) 
Will return: ['Altuve', 'Correa']

Dictionaries aren't immutable like lists.

"""