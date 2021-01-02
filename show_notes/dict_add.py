# How to Add New Key/Value Pairs to Python Dictionaries

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

teams['red sox'] = ['Price', 'Betts']

print(teams)
"""
{ 'astros': ['Altuve', 'Correa', 'Bregman'],
  'angels': ['Trout', 'Pujols'], 
  'yankees': ['Judge', 'Stanton'], 
  'red sox': ['Price', 'Betts']
}

Notes: Declaring a new key and value pair works by
using the variable, declaring a new key with it, then assigning
a new vaule to it (line 9).

"""