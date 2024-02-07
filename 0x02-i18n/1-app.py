#/usr/bin/env python3
"""
    basics flask setup
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """
        class configuration for babel languages and timezone
        english as default language
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@app.route('/')
def index():
    """
        function that render a html template
    """
    return render_template('./1-index.html')


if __name__ == 'main':
    app.run(debug=True)