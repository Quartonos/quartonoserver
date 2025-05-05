from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def hello():
    return jsonify(message="Pong")
