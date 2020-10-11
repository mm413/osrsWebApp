# Mark Meade
# app.py

from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, world!'