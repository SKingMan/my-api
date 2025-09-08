from flask import Flask, jsonify
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
    return jsonify({
        "data": [
            {"product_id": "P001", "name": "无线耳机", "price": 299, "stock": 156, "category": "电子设备"},
            {"product_id": "P002", "name": "机械键盘", "price": 399, "stock": 89, "category": "电脑外设"},
            {"product_id": "P003", "name": "智能手表", "price": 899, "stock": 42, "category": "可穿戴设备"}
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)