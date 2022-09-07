# Write a program that asks the user for a number of a month
# and then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

import calendar

seasons = ("spring", "summer", "autumn", "winter")
month = int(input("Please enter the number of a month (1-12): "))
print(calendar.month_name[month])

if month in (12, 1, 2):
    print(f"It is {seasons[3]} during that month.")
elif month in (3, 4, 5):
    print(f"It is {seasons[0]} during that month.")
elif month in (6, 7, 8):
    print(f"It is {seasons[1]} during that month.")
else:
    print(f"It is {seasons[2]} during that month.")
