# Implement a backend service that gets the ICAO code of an airport and then returns the name
# and location of the airport in JSON format.
# The information is fetched from the airport database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport?code=EFHK
# The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

import mysql.connector
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/airport')
def airport():
    argument = request.args
    code = (argument.get("code"))
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM flying_around WHERE ident='" + code + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            response = {
                "ICAO": code,
                "Name": row[1],
                "Location": row[2]
            }

            json.dumps(response, default=lambda o: o.__dict__, indent=4)
            return response


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='for_python_exercise',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
