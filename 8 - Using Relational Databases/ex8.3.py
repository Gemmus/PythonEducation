# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database using geopy.
# examples: EFHK (Helsinki-Vantaa), EGLL (Heathrow), EGKK (Gatwick), EGGW (Luton), EGSS (London Stansted)

import mysql.connector
from geopy.distance import geodesic


def how_far(icao):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, latitude_deg, longitude_deg FROM flying_around WHERE ident='" + icao + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location = (row[1], row[2])
            return location


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='for_python_exercise',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

code1 = input("Please enter the ICAO code of the airport: ").upper()
location1 = how_far(code1)
code2 = input("Please enter the ICAO code of the airport: ").upper()
location2 = how_far(code2)

distance = geodesic(location1, location2).km
print(f"The distance between the two entered airports is: {distance:.2f}km.")
