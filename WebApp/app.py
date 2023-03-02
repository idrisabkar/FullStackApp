from functools import wraps
from flask import Flask, render_template, redirect, request, jsonify, url_for, flash
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
        email = request.form.get("email")
        password = request.form.get("password")

        response = requests.get("http://127.0.0.1:8000/user", json={"email": email})
        if response.status_code == 200:
            data = response.json()
            if "password" in data and data["password"] and utils.verified(c_password=password,
                                                                          h_password=data.get("password")):
                return "ok"
            else:
                flash("Invalid email or password", "error")
                return redirect("/login")
        else:
            flash("Invalid email or password", "error")
            return redirect("/login")
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = {
            "user_name": request.form['name'],
            "email": request.form['email'],
            "password": utils.hash_password(request.form['password'])
        }
        response = requests.post("http://127.0.0.1:8000/user", json=data)
        if response.status_code == 200:
            return redirect("/login")
        else:
            flash("Invalid email or password", "error")
            return redirect("/login")

    return render_template("register.html")


@app.route("/wellcome")
@token_required
def wellcome():
    return render_template("wellcome.html")


if __name__ == "__main__":
    app.run(debug=True)
