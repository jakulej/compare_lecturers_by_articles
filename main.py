from flask import Flask
from manova import manova
from cluster_latest import compare_all_articles


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/manova")
def get_manova():
    manova_result = manova()
    return manova_result

@app.route("/cluster")
def get_manova():
    result = compare_all_articles()
    return result