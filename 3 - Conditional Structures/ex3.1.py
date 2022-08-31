# Write a program that asks a fisher the length of a zander in centimeters.
# The zander must fulfill the size limit (42 cm).
# Otherwise the program instructs to release the fish back into the lake
# and notifies the user of how many centimeters below the size limit the caught fish was.

length = float(input("Please enter the length of the zander in cm: "))

if length < 42:
    minus = (42-length)
    print("Zander must be released back to the lake as it is " + str(minus) + " cm below the limit size.")

if length >= 42:
    print("Zander fulfills the limit size.")
