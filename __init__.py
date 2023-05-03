from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route("/health")
def health_check():
    return jsonify(health="OK")
