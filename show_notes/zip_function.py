# Guide to Python's Zip Function

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)

print(list(scoreboard))
#[('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]

"""
The Zip function works as a quick way to merge multiple 
lists together into a set of tuples.

Handy for APIs and machine learning where you would need 
to combine data into a new collection with organized data
where the first item will be assigned to each other etc.

WIthout turning it into a list on line 8 a zip object will
be returned.

"""