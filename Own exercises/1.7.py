weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":     # we make sure it's not capital sensitive
    converter = weight * 0.45
    print(f"You are {converter:.3f} kilos.")

elif unit.upper() == "K":
    converter = weight / 0.45
    print(f"You are {converter:.3f} pounds.")
