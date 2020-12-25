# How to Check if a Value is Included in a Python String or List

sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word.lower() in sentence.lower():
  print('The word is in the sentence')
  #The word is in the sentence
else:
  print('The word is not in the sentence')


nums = [1, 2, 3, 4]

if 3 in nums:
  print('The number was found')
  #The number was found
else:
  print('The number was not found')

"""
The 'in operator' is used to look for values inside a collection
of data.

If you are working with conflicting case sentences "D vs. d"
You can use the .lower() method to put it all in lowercase.

"""