# How to Use a Tuple as a Dictionary Key in Python

priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys()))
#[(1, 'premier'), (1, 'mvp'), (2, 'standard')]

"""
On line 10 we converted the result into a list because otherwise
it would return a view object.

"""