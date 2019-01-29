#!/usr/bin/python3
""" starts a Flask web app """
from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """ displays Python followed by text variable default=is cool """
    return ("Python " + str(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ displays a given int """
    return (str(n) + " is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays an HTML page if n is an int """
    if type(n) == int:
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
