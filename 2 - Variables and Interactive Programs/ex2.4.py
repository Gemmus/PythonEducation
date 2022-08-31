# Write a program that asks for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

num1_str = input("Please insert the first integer number of your choice: ")
num2_str = input("Please insert the second integer number of the your choice: ")
num3_str = input("Please insert the third integer number of the your choice: ")
num1 = int(float(num1_str))
num2 = int(float(num2_str))
num3 = int(float(num3_str))
summary = (num1+num2+num3)
product = (num1*num2*num3)
ave = (num1+num2+num3)/3
print("The sum of your three chosen numbers is: " + str(summary))
print("The product of your three chosen numbers is: " + str(product))
print("The average of your three chosen numbers is: " + str(ave))
