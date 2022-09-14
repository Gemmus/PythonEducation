# Write a program that asks for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

try:
    num1 = int(input("Please insert the first integer number of your choice: "))
    num2 = int(input("Please insert the second integer number of the your choice: "))
    num3 = int(input("Please insert the third integer number of the your choice: "))
    summary = (num1+num2+num3)
    product = (num1*num2*num3)
    ave = (num1+num2+num3)/3
    print(f"The sum of your three chosen numbers is: {summary}")
    print(f"The product of your three chosen numbers is: {product}")
    print(f"The average of your three chosen numbers is: {ave}")
except ValueError:
    print("Invalid input.")
