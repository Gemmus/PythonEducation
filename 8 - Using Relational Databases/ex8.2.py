# Write a program that asks the user to enter the area code (for example FI) and prints out
# the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.

import mysql.connector


def type_name(code):
    cursor = connection.cursor()
    cursor.execute("SELECT type, name, iso_country FROM flying_around "
                   "WHERE iso_country='" + code + "' ORDER BY type DESC")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The type of airport is: {row[0]} and the name of the airport is: {row[1]}.")
    return


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='for_python_exercise',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

area_code = input("Please enter the area code of the airport: ").upper()
type_name(area_code)
