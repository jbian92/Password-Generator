# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

import functions

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/result', methods = ['POST'])
def result():
    form = request.form
    upper = False
    lower = False

    length = form['length']
    length = length.strip() # remove leading & trailing whitespace

    # user did not enter a valid length
    if not length.isnumeric():
        return "Error: You did not enter a valid length."

    # check if user checked any checkboxes
    if form.getlist('upper') == ['on']:
        upper = True
    if form.getlist('lower') == ['on']:
        lower = True

    data = {
        "length": int(length),
        "upper": upper,
        "lower": lower
    }

    password = functions.generator(data)
    return render_template('result.html', password = password)