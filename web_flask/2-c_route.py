#!/usr/bin/python3
""" starts a Flask web app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ says hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ says hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ displays "C" followed by text variable """
    return ("C " + str(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
