#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)
"""
    creating an instance of Flask app
"""

@app.route('/')
def index():
    """
        a function that render a html template
    """
    return render_template('./0-index.html')


if __name__ == 'main':
    app.run(debug=True)