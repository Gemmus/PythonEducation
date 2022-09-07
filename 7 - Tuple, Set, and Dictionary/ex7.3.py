# Write a program for fetching and storing airport data.
# The program asks if they want to (1) enter a new airport, (2) fetch the information of an existing airport or (3) quit. done
# (1) If the user chooses to enter a new airport, the program asks to (a) enter the ICAO code and (b) name of the airport.
# (2) If the user chooses to fetch airport information instead,
# the program (a) asks for the ICAO code of the airport and (b) prints out the corresponding name.
# (3) If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.

data = {"HELSINKI-VANTAA": "EFHK", "HEATHROW": "EGLL", "GATWICK": "EGKK", "LUTON": "EGGW", "LONDON STANSTED": "EGSS"}

action = input("""
Please enter A, if you wish to enter a new airport
          or B, if you wish to fetch information of an existing airport
          or C, iy you wish to quit: 
""")

while action.upper() != "C":
    if action.upper() == "A":
        code = input("Please enter the ICAO code of the airport: ")
        name = input("Please enter the name of the airport: ")
        data.update({name: code})
    elif action.upper() == "B":
        code = input("Please enter the ICAO code of the airport: ")
#        if code.upper() in data:
#        print(f"For the ICAO code of {code} the corresponding airport is {data[code.upper()]}.")
        print(f"For the ICAO code of {code} the corresponding airport is {data["EGLL"]}.")
    action = input("""
    Please enter A, if you wish to enter a new airport
              or B, if you wish to fetch information of an existing airport
              or C, iy you wish to quit:
    """)
else:
    print("You chose to quit. Have a safe flight!")

print(data)
