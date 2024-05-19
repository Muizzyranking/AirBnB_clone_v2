#!/usr/bin/python3
"""Module to start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown():
    """Closes the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
