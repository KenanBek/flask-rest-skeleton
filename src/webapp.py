'''
Web application.
'''
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    '''Index page'''
    return 'Hello, World!'
