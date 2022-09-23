# Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

import random

try:
    a = random.randint(1, 10)
#    print(a)
    guess = int(input("Please guess my chosen number: "))

    while guess != a:
        if guess < a:
            guess = int(input("Too low. Guess again:"))
        if guess > a:
            guess = int(input("Too high. Guess again:"))
    else:
        print("Correct.")

except ValueError:
    print("That's not a number. I quit.")
