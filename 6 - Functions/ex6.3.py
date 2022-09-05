# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def litre(first):
    result = first * 3.7854
    return result


gallon = float(input("Please enter the volume in gallons: "))
result = litre(gallon)
print(f"The entered volume in gallon is {result:.2f} in litre.")
