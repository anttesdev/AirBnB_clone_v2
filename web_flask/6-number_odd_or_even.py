#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    A function that returns Hello HNBB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    A function that returns HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    A function that replaces any text followed by c with an underscore
    by a space and returns the whole text
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    replaces a "is cool" text with the argument text
    and removes underscores
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    A function that returns a number if it
    is an Integer
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    A function that renders an HTML
    page if n is an integer
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    A function that will render an HTML
    page based on whether the number is odd or even
    """
    number_type = "even" if n % 2 == 0 else "odd"
    return render_template('number_odd_or_even.html', num=n,
                           number_type=number_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
