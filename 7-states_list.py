import models
from models import storage
from models.state import State
from flask import Flask, render_template

l = Flask(__name__)
@l.route("/")
def name():
    print(storage.all())
    return render_template()

l.run(host="0.0.0.0")