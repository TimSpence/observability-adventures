import pymysql
from flask import Flask, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db = SQLAlchemy()
username = "lol"
password = "lol"
userpass = "mysql+pymysql://" + username + ":" + password + "@"
server = "db"
dbname = "/lol"

app.config["SQLALCHEMY_DATABASE_URI"] = userpass + server + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db.init_app(app)


@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/health")
def health_check():
    return jsonify(health="OK")


@app.route("/slow-endpoint")
def slow_endpoint():
    db.session.query(text("1")).from_statement(text("SELECT sleep(10)")).all()
    return jsonify(slept=10)


@app.route("/buggy-endpoint")
def buggy_endpoint():
    var = 1 / 0
    return jsonify(buggy="definitely")


@app.route("/redirect")
def redirectme():
    return redirect("/")
