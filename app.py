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
    checked_categories = list()
    num_checked_boxes = 0

    length = form['length']
    length = length.strip() # remove leading & trailing whitespace

    # user did not enter a valid length
    if not length.isnumeric():
        return render_template('error.html', message="invalid length")

    # check if user checked any checkboxes
    for checkbox in ['upper', 'lower', 'numeric', 'special']:
        if form.getlist(checkbox) == ['on']:
            checked_categories.append('num_' + checkbox)
            num_checked_boxes += 1

    # user did not check any boxes
    if num_checked_boxes == 0:
        return render_template('error.html', message="did not check off any checkboxes")

    # user's number of requirements is greater than length given
    if num_checked_boxes > int(length):
        return render_template('error.html', message="checked off more checkboxes than given length")

    data = {
        "length": int(length),
        "checked_categories": checked_categories,
        "num_checked_boxes": num_checked_boxes
    }

    password = functions.generator(data)
    return render_template('result.html', password = password)