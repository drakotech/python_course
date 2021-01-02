# Working with the slice Class in Python to Store Slices

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])
# ['development', 'code']

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
# 1

print(slice_obj.stop)
# 4

print(slice_obj.step)
# 2

print(tags[slice_obj])
# ['development', 'code']

"""
Notes: The slice class is a way of finding out what the slice object is made up of. Useful wen working with machine learning algorithms.

Slice obj are also helpful when working with a set range repeatedly.

"""
