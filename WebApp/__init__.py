from functools import wraps
from flask import Flask, request, jsonify, current_app
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


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


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'This page is protected and only accessible with a valid token'}), 200
