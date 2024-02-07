#!/usr/bin/env python3
"""
    basics flask set up
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
        class configuration for babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTF'

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
        a function that get the best matched language
        from the locale
    """
    request.accept_languages.best_match(app.config['LANGUAGES'])


app.route('/')
def index():
    """
        a function that renders a html template
    """
    return render_template('./2-index.html')


if __name__ == 'main':
    app.run(debug=True)