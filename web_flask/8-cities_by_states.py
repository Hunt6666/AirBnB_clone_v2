#!/usr/bin/python3
""" starts a Flask web app """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_states():
    """ lists all of the cities by states """
    storage.reload()
    dic = storage.all("State")
    ret = []
    for k, v in dic.items():
        ret += [v]
    return render_template('8-cities_by_states.html', states=ret)


@app.teardown_appcontext
def kill_session(exc):
    """ kills the sqlalchemy session """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
