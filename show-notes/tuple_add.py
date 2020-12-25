# How to Add Elements to a Tuple by Leveraging Re-Assignment

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
#2708907858304
print(id(post))
#2708907858304

post += ('published',)

print(id(post))
#2708913037776

title, sub_heading, content, status = post

print(title)
#Python Basics
print(sub_heading)
#Intro guide to python   
print(content)
#Some cool python content
print(status)
#published

"""
Notes: Simply adding ('published') would be treated like a str 
and would throw an error. Instead you should use ('published',)
to let python know you mean to add to a tuple.

Following laws of immutability you can see how when we applied 
the reassignment to add the 'published' value, the id of the 
tuple changed. You are no longer working with the original tuple
instead a new one.

"""