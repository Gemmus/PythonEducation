import sys

list1 = []
num = input("Please enter a number or press enter to quit: ")

if num == "":
    print("You chose to quit without entering a single number.")
    sys.exit(0)

list1.append(num)
while num != "":
    num = input("Please enter a number or press enter to quit: ")
    if num == "":
        break
    list1.append(num)

print("Your smallest number is: " + str(min(list1)) + " and your largest is: " + str(max(list1)))

sys.exit(0)
