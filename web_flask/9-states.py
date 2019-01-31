#!/usr/bin/python3
""" starts a Flask web app """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_cities(st=None):
    """ lists all of the cities by states """
    storage.reload()
    dic = storage.all("State")
    ret = []
    ent = None
    for k, v in dic.items():
        ret += [v]
        if st == v.id:
            ent = v
    return render_template('8-cities_by_states.html', states=ret, ent=ent,
                           st=st)


@app.teardown_appcontext
def kill_session(exc):
    """ kills the sqlalchemy session """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
