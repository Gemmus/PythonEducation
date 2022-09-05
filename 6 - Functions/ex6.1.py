# Write a function (without parameters) that returns a random dice roll between 1 and 6.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.


def roll():
    import random
    dice = random.randint(1, 6)
    return dice


number = roll()
print(number)
while number != 6:
    number = roll()
    print(number)
