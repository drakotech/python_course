# Guide to the sorted Function in Python

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

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list)

"""
Notes: Sort vs Sorted. Sort doesn't return anything and is a safe way to work with lists.
Sorted returns the list sorted that can then be stored in a new variable.

"""
