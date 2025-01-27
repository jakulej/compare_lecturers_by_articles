from flask import Flask, request, jsonify
from manova import manova
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/compare/manova", methods=['POST'])
def get_manova():
    # data = request.json
    # lecturer1 = data.get('lecturer1')
    # lecturer2 = data.get('lecturer2')

    manova_result = manova()
    return manova_result