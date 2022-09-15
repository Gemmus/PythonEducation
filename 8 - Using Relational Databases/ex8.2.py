# Write a program that asks the user to enter the area code (for example FI) and prints out
# the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.

import mysql.connector


def getTypeAndName(code):
    sql = "SELECT id, type, name, iso_country FROM airport"
    sql += " WHERE iso_country='" + code + "' ORDER BY type ASC"
#    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The type of airport is: {row[1]} and the name of the airport is: {row[2]}.")
    return


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='people',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

area_code = input("Please enter the area code of the airport: ")
getTypeAndName(area_code)
