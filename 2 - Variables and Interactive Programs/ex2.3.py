# Write a program that asks for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.

length_str = input("Please insert length of the rectangle: ")
width_str = input("Please insert the width of the rectangle: ")
length = float(length_str)
width = float(width_str)
perimeter = (length+width)*2
area = (length*width)
print("The perimeter of the rectangle is: " + str(perimeter))
print("The area of the rectangle is: " + str(area))
