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
