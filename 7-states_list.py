#!/usr/bin/python3
"""
Cretes a flask app and listens on 0.0.0.0:500
"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.place import Place
app = Flask(__name__)

how = storage.all(State)
@app.route('/states_list')
def rout_list():
    """
    render a page for html list
    """
    return render_template('7-states_list.html', how=how)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
