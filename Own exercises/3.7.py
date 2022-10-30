from flask import Flask, request

app = Flask(__name__)


@app.route('/summary')
def summary():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    addition = number1+number2
    return str(addition)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

# http://127.0.0.1:5000/summary?number1=13&number2=29
