# Introduction to Python Tuples

# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable 
# List: mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
#Python Basics
print(sub_heading)
#Intro guide to python   
print(content)
#Some cool python content

"""
Notes: Main difference would be that a list can cause bugs because
it is mutable and can be changed at run time. Whereas a tuple will
not change its structure and throw an error.

"""