#!/usr/bin/python3
""" starts flask we app that listens to 0.0.0.0 on port 5000 """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ says hello """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
