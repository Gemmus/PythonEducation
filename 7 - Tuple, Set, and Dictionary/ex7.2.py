# Write a program that asks the user to enter names.
# After each name is read the program either prints out New name or Existing name
# depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.

names = set([])
name = input("Please enter a name or press enter to quit: ")

while name != "":
    if name in names:
        print("Existing name")
    else:
        names.add(name)
        print("New name")
    name = input("Please enter a name: ")

else:
    for n in names:
        print(n)
