# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town)
# from the airport database used on this course.
# examples: EFHK (Helsinki-Vantaa), EGLL (Heathrow), EGKK (Gatwick), EGGW (Luton), EGSS (London Stansted)

import mysql.connector


def getNameAndLocation(icao):
    cursor = connection.cursor()
    cursor.execute("SELECT name, municipality, gps_code FROM flying_around WHERE gps_code='" + icao + "'")
    result = cursor.fetchall()
#    print(result)
    if cursor.rowcount > 0:
        for row in result:
            print(f"The name of the airport is: {row[0]} and it locates in: {row[1]}.")
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
getNameAndLocation(code)
