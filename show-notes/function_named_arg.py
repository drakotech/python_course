# How to Utilize Named Function Arguments in Python


def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')
#Kristine Hudgens
full_name(first = 'Kristine', last = 'Hudgens')
#Kristine Hudgens
full_name(last = 'Hudgens', first = 'Kristine')
#Kristine Hudgens
# Note: this call is using the named aguments in a different 
# order, but same result.


"""
JH likes to use named argumemts when theres more than 2 arguments
to avoid confusion when calling the function. 

When using named functions the order of args doesn't matter.

"""