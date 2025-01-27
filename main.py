from flask import Flask,request
from manova import manova


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/manova/<first>/<second>", methods=['GET'])
def get_manova(first, second):
    manova_result = manova(first,second)
    return manova_result
