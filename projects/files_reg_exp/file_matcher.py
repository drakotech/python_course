# Using Regular Expressions to List File Types in Python

import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('Text files:', file)

        if fnmatch.fnmatch(file, '*.rb'):
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, '*.yml'):
            print('Yaml files:', file)

        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()
#Python files: file_matcher.py
#Ruby files: scripts.rb
#Text files: something.txt

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print(second_base_players)
#['Jose Altuve 2B', 'Scooter Gennett 2B']


"""
fnMatch = (File Name)Match

By importing the fnmatch library you can use regular expressions 
when you are working with files.

You can also use fnmatch for any other part of python that you
need! 

The second_base_players variable is using fnmatch to find a
regular expression in the list of players.

"""