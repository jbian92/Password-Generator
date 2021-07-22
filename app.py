# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

import functions

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/', methods = ['GET'])
def main():
    return render_template('main.html')

@app.route('/result', methods = ['POST'])
def result():
    form = request.form
    upper = False
    lower = False
    numeric = False
    checked_boxes = 0

    length = form['length']
    length = length.strip() # remove leading & trailing whitespace

    # user did not enter a valid length
    if not length.isnumeric():
        return render_template('main.html')

    # check if user checked any checkboxes
    if form.getlist('upper') == ['on']:
        upper = True
        checked_boxes += 1
    if form.getlist('lower') == ['on']:
        lower = True
        checked_boxes += 1
    if form.getlist('numeric') == ['on']:
        numeric = True
        checked_boxes += 1

    # user did not check any boxes
    if checked_boxes == 0:
        return render_template('main.html')

    data = {
        "length": int(length),
        "upper": upper,
        "lower": lower,
        "numeric": numeric
    }

    password = functions.generator(data)
    return render_template('result.html', password = password)