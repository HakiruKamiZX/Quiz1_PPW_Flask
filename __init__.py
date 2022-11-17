import os

from flask import Flask, render_template

app = Flask(__name__)

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('settings.cfg', silent=True)
    

    return app
