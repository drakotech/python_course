# Overview of Python List Query Processes: len(), Negative Indexes, and index()

itags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)

"""
Returns:

4
code
3

Notes: You can grab last item of a list by using negative index. -1 starts from the end, -2 is second from the end etc.
"""
