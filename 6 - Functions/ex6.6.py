# Write a function that receives two parameters:
#   the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas
#   and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.

import math


def func(first, second):
    unit = (second*4)/(math.pi*(first/100)**2)
    print(f"{unit:.2f} euro/m^2")
    return unit


diameter1 = float(input("Please enter the diameter (in cm) of the first pizza: "))
price1 = float(input("Please enter the price (in euro) of the first pizza: "))

diameter2 = float(input("Please enter the diameter (in cm) of the second pizza: "))
price2 = float(input("Please enter the price (in euro) of the second pizza: "))

ratio1 = func(diameter1, price1)
ratio2 = func(diameter2, price2)

if ratio1 < ratio2:
    print("The first pizza provides a better value for money.")

elif ratio1 > ratio2:
    print("The second pizza provides a better value for money.")

else:
    print("They provide the same value for money.")
