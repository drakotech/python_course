# How to Find the Median of a Python List with an Odd Number of Numbers

import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
# [1, 3, 10, 40, 83, 100, 100, 220, 400]

print(num_of_sales)
# 9

print(first_sales_items)
# [1, 3, 10, 40]

print(last_sales_items)
# [100, 100, 220, 400]

print(median)
# [83]


"""
Notes: This method works with an odd number of elements in a list.
Median is the center element, not average!

"""
