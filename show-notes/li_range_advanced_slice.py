# Advanced Techniques for Implementing Ranges and Slices in Python Lists

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
  ]

tag_range = tags[::-1]
  #['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

tags.sort(reverse=True)
  #['tutorials', 'python', 'programming', 'development', 'computer science', 'code']

tag_range = tags[1:-1:2]
  #['development', 'code']

tag_range = tags[::-1]
  #['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

tags.sort(reverse=True)

print(tags)
  #['tutorials', 'python', 'programming', 'development', 'computer science', 'code'

"""
Notes: The third parameter is called a delimiter and if you enter a positive value of 2 it will skip every
other element. A -1 value will return a reversed order of the list.

The main difference between sort and using the slice method (delimiter) is that sort works alphabetically.
the -1 slice method sorts the list by reversed index value.

The sort method will reorganize things but will not return anything due to immutability of lists in python.
Trying to assign a sorth method into a variable will return none.
"""
