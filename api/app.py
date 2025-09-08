from flask import Flask, Response
import csv
from io import StringIO


app = Flask(__name__)


@app.route("/")  # 关键点：直接在路由中写 .json
def index():
    return "Hello world!"

@app.route("/test")  # 关键点：直接在路由中写 .json
def test():
    return "Hello world! This is a test!"
@app.route("/data.json")  # 关键点：直接在路由中写 .json
def get_data():
    data = [
  {"question": "Who are you?", "answer": "I'm a AI Assistant."},
  {"question": "What can you do?", "answer": "Answer questions."}
]
    # 创建 CSV 文件内容
    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=["question", "answer"])
    writer.writeheader()
    writer.writerows(data)

    # 返回 CSV 响应
    return Response(
        csv_buffer.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=data.csv"}
    )

if __name__ == "__main__":
    app.run(debug=True)