phone = input("Please enter phone number: ")
digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

output = ""
for i in phone:
    output += digits.get(i, "!") + " "
print(output)
