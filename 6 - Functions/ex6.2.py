# Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.


def roll(side):
    import random
    dice = random.randint(1, side)
    return dice


side = int(input("How many sides does the dice have? "))
number = roll(side)
print(number)
while number != side:
    number = roll(side)
    print(number)
