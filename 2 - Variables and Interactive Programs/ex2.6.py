# Write a program that draws two random combinations of numbers for a combination lock:
#       a 3-digit code where each number is between 0 and 9.
#       a 4-digit code where each number is between 1 and 6.

import random
a = random.randrange(0, 10)
b = random.randrange(0, 10)
c = random.randrange(0, 10)
print("Your random 3-digit code is: ", a, b, c)

c = random.randrange(1, 7)
d = random.randrange(1, 7)
e = random.randrange(1, 7)
f = random.randrange(1, 7)
print("You random 4-digit code is: ", c, d, e, f)
