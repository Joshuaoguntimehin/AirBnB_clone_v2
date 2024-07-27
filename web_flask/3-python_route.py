#!/usr/bin/python3
"""import statement"""
from flask import Flask

"""app definition"""
app = Flask(__name__)

"""/: Displays "Hello HBNB!" when accessed."""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


"""/: Displays "HBNB" when accessed."""


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


"""which sets the text variable to its default value """


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f"C {text}"


""" which sets the text variable to its default value "is cool"""


@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    text = text.replace('_' ' ')
    return f"python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
