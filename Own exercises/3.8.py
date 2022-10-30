from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/sum')
def sum():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    sum = number1+number2

    response = {
        "number1" : number1,
        "number2" : number2,
        "sum" : sum
    }

    json_data = json.dumps(response, default=lambda o: o.__dict__, indent=4)

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)