#!/bin/python3
"""
Loads the content of a database and post on the site
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def name_list():
    print(storage.all())
    return render_template("7-states_list.html", how=storage.all())


@app.teardown_appcontext
def remove():
    """Close the session"""
    storage.close()


if __name__ == "main":
    app.run(host="0.0.0.0")
