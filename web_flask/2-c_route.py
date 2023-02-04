#!/usr/bin/python3
"""
Cretes a flask app and listens on 0.0.0.0:500
"""
from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
