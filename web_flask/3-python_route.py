#!/usr/bin/python3
""" A script that starts a flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints  a Message when the index function is called """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """ Prints a message when the hbnb route is requested """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is_text(text):
    """ Prints a message when the c_is_text route is requested """
    return ("C " + text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_text(text="is_cool"):
    """ Prints a message when the python_is_text route is requested """
    return ("Python " + text.replace('_', ' '))


if __name__ == "__main__":
    """ Main function to start app """
    app.run(host="0.0.0.0", port=5000)
