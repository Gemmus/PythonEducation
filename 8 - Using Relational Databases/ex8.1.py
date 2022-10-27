# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town)
# from the airport database used on this course.
# examples: EFHK (Helsinki-Vantaa), EGLL (Heathrow), EGKK (Gatwick), EGGW (Luton), EGSS (London Stansted)

import mysql.connector


def name_location(icao):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM flying_around WHERE ident='" + icao + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[1]} is located in: {row[2]}.")
    return


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='for_python_exercise',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

code = input("Please enter the ICAO code of the airport: ").upper()
name_location(code)
