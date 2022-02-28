from functools import reduce

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet_array = [letter for letter in alphabet]

word = "cab"

reduce(lambda a, b : a + b, word)
sum = lambda a, b : a + b

sum2 = sum(10, 10)

print(sum2)