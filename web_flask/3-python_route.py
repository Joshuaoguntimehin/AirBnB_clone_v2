#!/usr/bin/python3
"""import statement"""
from flask import Flask

app = Flask(__name__)
"""/hbnb returns "HBNB" """


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"
"""/hbnb returns "HBNB"""


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"
"""/c/<text> replaces underscores with spaces in the text and returns "C """


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f"Python {text}"

