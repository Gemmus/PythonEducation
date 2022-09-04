# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

import random

dice_numbers = []
piece = int(input("How many dices should be rolled? "))

for n in range(piece):
    a = random.randint(1, 6)
    dice_numbers.append(a)

print(f"The sum of the numbers is: {sum(dice_numbers)}")
