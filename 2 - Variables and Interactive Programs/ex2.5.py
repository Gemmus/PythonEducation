talent_str = input("Please enter talents: ")
pound_str = input("Please enter pounds: ")
lot_str = input("Please enter lots: ")
talent = float(talent_str)
pound = float(pound_str)
lot = float(lot_str)
grams = (talent*20*32*13.3)+(pound*32*13.3)+(13.3*lot)
kilograms = grams/1000
grams_left = grams % 1000

print("The weight in modern unit is: " + str(int(kilograms)) + " kg and " + str(int(grams_left)) + " grams")
