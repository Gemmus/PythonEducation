# Write a program that asks for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.

import sys

x = 0
while x < 5:
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    if username == "python" and password == "rules":
        print("Welcome.")
        sys.exit(0)
    x = x + 1

if x == 5:
    print("Access denied.")

    sys.exit(0)
