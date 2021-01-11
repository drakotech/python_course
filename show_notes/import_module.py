# How to Import a Custom Python Module into Another File

# libs/helper.py file
def greeting(first, last):
    return f'Hi {first} {last}!'

# main.py file
import sys
sys.path.insert(0, './libs')
import helper

def render():
    print(helper.greeting('Kristine', 'Hudgens'))


render()

"""
Importing a module from another directory, you will need to 
import the builit in library "sys" and specify the location
of the module to be imported with sys.path.insert

"""