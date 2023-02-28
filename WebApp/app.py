from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("wellcome.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print(request.form['email'])
        print(request.form['password'])
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        print(request.form['email'])
        print(request.form['password'])
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
