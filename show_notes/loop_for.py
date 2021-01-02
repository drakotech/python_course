# How to Implement Python Loops for Lists, Tuples, and Dictionaries

players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
  print(player)

  #Altuve
  #Bregman      
  #Correa       
  #Gattis

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
  print('Position', position)
  print('Player', player)

  #Position 2b  
  #Player Altuve
  #Position 3b
  #Player Bregman
  #Position ss
  #Player Correa
  #Position dh
  #Player Gattis


"""
Anything after a : has to be indented.

looping through dictionaries requires a variable for 
the key aswell as the value.

"""