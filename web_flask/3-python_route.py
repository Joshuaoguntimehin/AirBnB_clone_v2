#!/usr/bin/python3
"""Import statement"""
from flask import Flask, escape

"""App definition"""
app = Flask(__name__)

"""Displays 'Hello HBNB!' when accessed."""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

"""Displays 'HBNB' when accessed."""


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

"""Displays 'C ' followed by the text variable with underscores replaced by spaces."""


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f"C {escape(text)}"

"""Displays 'Python ' followed by the text variable with underscores replaced by spaces.
Defaults to 'is cool' if no text is provided."""


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

