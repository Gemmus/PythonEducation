# Write a program that asks a mass in medieval units: talents, pounds, and lots.
# The program converts the input to full kilograms and grams and outputs the result to the user.

try:
    talent = float(input("Please enter talents: "))
    pound = float(input("Please enter pounds: "))
    lot = float(input("Please enter lots: "))
    if talent > 0 and pound > 0 and lot > 0:
        grams = (talent*20*32*13.3)+(pound*32*13.3)+(13.3*lot)
        kilograms = grams/1000
        grams_left = grams % 1000
        print(f"The weight in modern unit is: {kilograms:2f} kg and {grams_left:2f} grams.")
    else:
        print("Value cannot be negative.")

except ValueError:
    print("Invalid input.")
