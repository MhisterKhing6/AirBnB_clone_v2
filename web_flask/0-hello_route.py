#!/usr/bin/python3
"""
Cretes a flask app and listens on 0.0.0.0:500
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Print Hello HBNB to th console
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
