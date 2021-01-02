# How to Add to a List in Python with Both In Place and Copy Processes

tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming'
#['python', 'development', 'tutorials', 'Programming']
# This will replace the last value with 'Programming'


# In Place
tags.extend('Programming')
#['python', 'development', 'tutorials', 'code', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
# This method returns each letter as a new element in the list


tags.extend(['Programming'])
#['python', 'development', 'tutorials', 'code', 'Programming']
# Encased in list syntax the element added will be the entire word as a single entry.
# The extend method follows list immutability and will not allow itself to be assigned into a variable.

# New List
new_tags = tags + ['Programming']
# Make sure to encase in list syntax otherise an error of data type  merging will happen.

print(new_tags)
#['python', 'development', 'tutorials', 'code', 'Programming']

print(tags)
#['python', 'development', 'tutorials', 'code', 'Programming']
