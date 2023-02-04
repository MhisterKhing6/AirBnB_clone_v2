#!/usr/bin/python3
"""
Cretes a flask app and listens on 0.0.0.0:500
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """
    Print Hello HBNB to th console
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def root_hbnb():
    """
    Print HBNB to html page
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def root_cisfun(text):
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def root_python(text="is cool"):
    return "Python {}".format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
