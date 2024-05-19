#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a message when routing /"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a message when routing /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns a message when routing /c/<text>"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is_cool"):
    """Returns a message when routing /python/<text>"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns a message when routing /number/<n> only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns a message when routing
    /number_template/<n> only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even_odd(n):
    """Returns a message when routing
    /number_odd_or_even/<n> only if n is an integer"""
    if n % 2 == 0:
        return render_template(
            "6-number_odd_or_even.html", n=n, odd_even="even")
    else:
        return render_template(
            "6-number_odd_or_even.html", n=n, odd_even="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
