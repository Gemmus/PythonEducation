largest = 0
smallest = 0

while True:
    num = input("Please enter a number or press enter to quit: " )
    if num == "":
        break
    num = float(num)
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Your smallest number is: " + str(smallest) + " and your largest is: " + str(largest))
