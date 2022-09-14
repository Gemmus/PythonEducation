# Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends.

try:
    inch = float(input("Please enter the length in inch: "))

    while inch >= 0:
        cm = inch * 0.3937007874
        print(f"Length in centimeter: {cm:.2f}")
        inch = float(input("Please enter the length in inch: "))

    print("Program ends.")

except ValueError:
    print("Invalid input.")
