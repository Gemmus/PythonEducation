# Asks the user to enter the cabin class of a cruise ship and then prints out a written description.
# If the user enters an invalid cabin class, the program outputs an error message "Invalid cabin class".

cabin = input("Please enter your cabin class: ").upper()

if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
