cabin_str = input("Please enter your cabin class: ")
cabin = cabin_str

if "LUX" in cabin:
    print("Upper-deck cabin with a balcony.")
elif "A" in cabin:
    print("Above the car deck, equipped with a window.")
elif "B" in cabin:
    print("Windowless cabin above the car deck.")
elif "C" in cabin:
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
