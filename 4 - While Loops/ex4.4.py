import random

a = random.randint(1, 10)
guess = int(input("Please guess my chosen number: "))

while guess != a:
    if guess < a:
        guess = int(input("Too low. Guess again:"))
    if guess > a:
        guess = int(input("Too high. Guess again:"))
else:
    print("Correct.")
