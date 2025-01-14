from flask import Flask
from manova import manova


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/manova")
def get_manova():
    manova_result = manova()
    return manova_result
