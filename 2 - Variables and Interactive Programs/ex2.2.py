import sys
import math

radius_str = input("Please insert radius of the circle: ")
radius = float(radius_str)
area = (radius**2)*math.pi
print("The area of the circle is: " + str(area))

sys.exit(0)
