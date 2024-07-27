#!/usr/bin/python3
"""import statement"""

from flask import Flask

"""blocked or used by other applications"""
app = Flask(__name__)

""" persists, consider providing additional details"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == "__main__":
    """ Configure the app to listen on all interfaces (0.0.0.0) on port 5000"""
    app.run(host='0.0.0.0', port=5000, debug=True)
