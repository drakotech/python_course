# Build a Weighted Lottery Function in Python

import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

#  weights = {
#      'winning': 1,
#      'losing': 1000
#  }
#
#  print(weighted_lottery(weights))

other_weights = {
    'green': 1,
    'yellow': 2,
    'red': 3
}

print(weighted_lottery(other_weights))

""" 
This function will return a random value from a 'bag' of values in a list. 
Using the numpy "Num Pi" library you can call the random choice method to 
acomplish this.

"""
