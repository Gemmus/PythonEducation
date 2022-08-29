import sys

length = float(input("Please enter the length of the zander in cm: "))

if length < 42:
    minus = (42-length)
    print("Zander must be released back to the lake as it is " + str(minus) + " cm below the limit size.")

if length >= 42:
    print("Zander fulfills the limit size.")

sys.exit(0)
