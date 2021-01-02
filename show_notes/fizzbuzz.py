# FizzBuzz.py

"""
Aim: Print numbers from 1 to max and print 'Fizz' for multiples
of 3, 'Buzz' for multiples of 5, and 'FizzBuzz' for multiples 
of both.

"""

def fizzbuzz(max):
    for num in range(1, (max + 1)):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz') 
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


fizzbuzz(100)
