#!usr/bin/python3

from flask import Flask
from controllers import usersController

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
