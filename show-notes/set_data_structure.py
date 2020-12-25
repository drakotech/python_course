# Introduction to the Python Set Data Structure

# Uniqueness
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags)
#{'tutorials', 'python', 'coding'}

# Nope
#print(tags[0])

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
#True
print(query_two)
#False

"""
A Set is a merging of a dictionary and list, a dict without keys.
A set requires that all the elements in it are unique.
If a duplicate element is found it is omitted from the output.

Great for when you need a collection of data with unique elements
without the full functionality of a list. Also if you have a 
collection of elements where you need to find if an element 
exists then this gives you a straightforeward syntax of doing that.

"""