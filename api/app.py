from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")  # 关键点：直接在路由中写 .json
def index():
    return "Hello world!"
@app.route("/data.json")  # 关键点：直接在路由中写 .json
def get_data():
    return jsonify({
        "message": "This is a .json endpoint",
        "data": [1, 2, 3]
    })

if __name__ == "__main__":
    app.run(debug=True)