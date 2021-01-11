# How to Import a Single Function from a Python Module

from math import sqrt

sqrt(4)

import sys
sys.path.insert(0, 'C:/Users/georg/code/bottega/python/python_import/libs')
from helper import greeting

def render():
    print(greeting('Tiffany', 'Hudgens'))


render()

"""
This is about how to import a specfic function from a module
the syntax is:
from <module> import <function>

"""