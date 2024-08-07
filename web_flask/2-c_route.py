#!/usr/bin/python3
"""import statament"""
from flask import Flask

"""app definition """
app = Flask(__name__)


"""This defines a route for the root URL (/)"""


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"


""" This defines a route for the root URL (/). """


@app.route('/', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
