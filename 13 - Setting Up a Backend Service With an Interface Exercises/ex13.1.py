# Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
# Use the prior prime number exercise as a starting point.
# For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number?number=31
# The response must be in the format of {"Number":31, "isPrime":true}.

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/prime_number')
def prime_number():
    argument = request.args
    number = int(argument.get("number"))
    answer = ["true"]
    if number > 1:
        if number != 2:
            for i in range(2, number - 1):
                if number % i == 0:
                    answer.insert(0, "false")
                    break
    else:
        answer.insert(0, "false")

    response = {
        "Number": number,
        "isPrime": answer[0]
    }

    json.dumps(response, default=lambda o: o.__dict__, indent=4)
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
