# Write a program that asks for a year and notifies whether the input year is a leap year.

year = int(input("Please enter the year of your choice: "))

if year % 4 == 0:
    if year % 100 != 0:
        print("The year of your choice is a leap year.")
    else:
        if year % 400 == 0:
            print("The year of your choice is a leap year.")
        else:
            print("The year of your choice is not a leap year.")
else:
    print("The year of your choice is not a leap year.")
