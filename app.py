import os

from flask import Flask, render_template
from . import db
from . import submission, user

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('settings.cfg', silent=True)
    
    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    app.register_blueprint(submission.bp)    
    app.register_blueprint(user.bp)

    @app.route('/home')
    @app.route('/')
    def index():
        return render_template('HomePage.vue')


    return app