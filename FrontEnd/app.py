# Mark Meade
# app.py
import os
from logicHandling import gear
from flask import *
template_dir = os.path.abspath('/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def index():
    return render_template('index.html')


def dropdownHead():
    g = gear.Gear()
    headItems = g.headSlotItems()
    return render_template(base.html, headItems=headItems)
