import os

from flask import Flask, render_template
dfrom flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return template ("homepage.vue")


    return app
