from flask import Flask, request, jsonify
from manova import manova
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/manova")
def get_manova():
    manova_result = manova()
    return manova_result

# -------------------------------------------------------------------------------
@app.route('/compare', methods=['POST'])
def compare_lecturers():
    data = request.json
    lecturer1 = data.get('lecturer1')
    lecturer2 = data.get('lecturer2')

    # Replace with your comparison logic
    result = {
        "lecturer1": lecturer1,
        "lecturer2": lecturer2,
        "comparison": "Sample comparison result"
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)