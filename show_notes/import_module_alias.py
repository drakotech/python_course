# How to Import a Module and Assign an Alias in Python

import sys
sys.path.insert(0, './libs')
import helper as h

def render():
    print(h.greeting('Tiffany', 'Hudgens'))


render()


import math as m

m.sqrt(4)

"""
Used when needing to call functions from another file and use
an alias for cleaner code. Can work with any code library.

Styntax is:
import <module> as <alias>

"""