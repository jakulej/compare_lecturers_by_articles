from flask import Flask
from manova import manova
from author_mapping import get_author_name_mapping
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/manova/<first>/<second>", methods=['GET'])
def get_manova(first, second):
    manova_result = manova(first,second)
    return manova_result

@app.route("/people", methods=['GET'])
def get_people():
    people = get_author_name_mapping()
    return people