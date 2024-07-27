#!/usr/bin/python3
"""import statement"""
from flask import Flask

"""defination of app"""
app = Flask(__name__)

""" : This defines a route for the root URL (/),"""
@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"

""": This defines a route for the root URL (/)"""
@app.route('/', strict_slashes=False)
def HBMB():
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
