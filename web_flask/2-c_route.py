#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application
"""

from flask import Flask
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
