from functools import wraps
from flask import Flask, render_template, redirect, request, jsonify, url_for
import requests
import jwt

from WebApp import utils
from settings import variables

app = Flask(__name__)

app.config['SECRET_KEY'] = variables.SECRET_KEY


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return func(*args, **kwargs)

    return decorated


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return redirect(url_for("wellcome"))
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = {
            "user_name": request.form['name'],
            "email": request.form['email'],
            "password": utils.encrypt(request.form['password'])
        }
        response = requests.post("http://127.0.0.1:8000/user", json=data)
        if response.status_code == 200:
            return render_template("login.html")
        else:
            return jsonify(status=response.status_code)
    return render_template("register.html")


@app.route("/wellcome")
@token_required
def wellcome():
    return render_template("wellcome.html")


if __name__ == "__main__":
    app.run(debug=True)
