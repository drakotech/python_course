# Overview of Python Dictionaries

players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer",
}

second_base = players['2b']
#{'ss': 'Correa', '2b': 'Altuve', '3b': 'Bregman', 'DH': 'Gattis', 'OF': 'Springer'}
designated_hitter = players['DH']
#Gattis

print(designated_hitter)

"""
Notes: The Key Lookup method is case sensitive. 
So looking up 'dh' will return KeyError: 'dh'

"""