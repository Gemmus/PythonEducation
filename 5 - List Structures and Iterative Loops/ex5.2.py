# Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.

try:
    num_list = []
    num = input("Please enter a number or press enter to quit: ")

    while num != "":
        num_list.append(float(num))
        num = input("Please enter a number or press enter to quit: ")

    num_list.sort(reverse=True)
    # print(num_list)
    print(num_list[0:5])

except ValueError:
    print("Invalid input.")
