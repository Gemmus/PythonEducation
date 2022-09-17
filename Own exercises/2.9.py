
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
