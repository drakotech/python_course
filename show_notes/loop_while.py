# Overview of While Loops in Python

nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())
  #Returns numbers counting from 99 to 1

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()

"""
What is your guess?
10
No, 10 isn't the answer, please try again

What is your guess?
42
You correctly guessed it!

"""
