# Write a program that asks for the radius of a circle and prints out the area of the circle.

import math
try:
    radius = float(input("Please insert radius of the circle: "))
    if radius >= 0:
        area = (radius**2)*math.pi
        print(f"The area of the circle is: {area:.2f}")
    else:
        print("Value cannot be negative.")
except ValueError:
    print("Invalid input.")
