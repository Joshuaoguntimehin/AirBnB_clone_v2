#!/usr/bin/python3
"""import statement"""
from flask import Flask, render_template_string
import re

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
@app.route('/number_template/',
           defaults={'n': 'templates/5-number.html'},
           strict_slashes=False)
def number_template(n):
    return f"{n}"
"""Module is documented"""
@app.route('/number_template/<int:n>', strict_slashes=False)
@app.route('/number_template/',
           defaults={'n': 'templates/6-number_odd_or_even.html'},
           strict_slashes=False):
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template_string("<html><body><h1>Number: {{ n }} is {{ odd_or_even }}</h1></body></html>", n=n, odd_or_even=odd_or_even)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

