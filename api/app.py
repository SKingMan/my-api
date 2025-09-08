from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")  # 关键点：直接在路由中写 .json
def index():
    return "Hello world!"

@app.route("/test")  # 关键点：直接在路由中写 .json
def test():
    return "Hello world! This is a test!"
@app.route("/data.json")  # 关键点：直接在路由中写 .json
def get_data():
    return jsonify({
        "question": "Who are you?",
        "answer": "I'm a AI Assistant."
    })

if __name__ == "__main__":
    app.run(debug=True)