from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def c_to_f(celsius):
    return celsius * 9.0 / 5 + 32


@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        c = float(celsius)
    except ValueError:
        return "Please enter a valid number."

    f = c_to_f(c)
    return f"{c}°C is {f:.1f}°F"


if __name__ == '__main__':
    app.run(debug=True)
