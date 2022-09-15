# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town)
# from the airport database used on this course.

import mysql.connector


def getNameAndLocation(icao):
    sql = "SELECT id, name, municipality, gps_code FROM aiport"
    sql += " WHERE gps_code='" + icao + "'"
#    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The name of the airport is: {row[1]} and it is located in: {row[2]}.")
    return


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

code = input("Please enter the ICAO code of the airport: ")
getNameAndLocation(code)
