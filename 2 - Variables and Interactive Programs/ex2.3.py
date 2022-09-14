# Write a program that asks for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.

try:
    length = float(input("Please insert length of the rectangle: "))
    width = float(input("Please insert the width of the rectangle: "))
    if length > 0 and width > 0:
        perimeter = (length+width)*2
        area = (length*width)
        print(f"The perimeter of the rectangle is: {perimeter}")
        print(f"The area of the rectangle is: {area}")
    else:
        print("Value cannot be negative.")
except ValueError:
    print("Invalid input.")
