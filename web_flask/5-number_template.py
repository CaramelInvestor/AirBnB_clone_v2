#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application
"""

from flask import Flask, render_template
from flask import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Replace underscores with spaces and display 'C '
    followed by the value of the text variable"""
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Replace underscores with spaces and display 'Python '
    followed by the value of the text variable"""
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display "n is a number" only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """Display an HTML page with H1 tag: "Number: n"
    if n is an integer"""
    return render_template('5-number_template.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
