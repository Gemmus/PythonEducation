# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

number = 3
while number <= 1000:
    print(number)
    number += 3

# or:
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

# or with for loop:
# for number in range(3, 1001, 3):
#    print(number)
