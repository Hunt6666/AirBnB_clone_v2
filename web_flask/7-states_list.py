#!/usr/bin/python3
""" starts a Flask web app """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ lists all of the states """
    storage.reload()
    dic = storage.all("State")
    ret = {}
    for 

if __name__ == "__main__":
    app.run(host="0.0.0.0")
