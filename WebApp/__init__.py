from flask import Flask, jsonify, request, session
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # TODO: verify the user's credentials and generate a JWT
    user_id = 123
    token = jwt.encode({'user_id': user_id}, app.config['SECRET_KEY'], algorithm='HS256')

    session['token'] = token
    return jsonify({'message': 'Login successful'}), 200

@app.route('/protected')
def protected():
    token = session.get('token')

    if not token:
        return jsonify({'message': 'Unauthorized'}), 401

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = data['user_id']
        # TODO: use the user ID to fetch data from the database or perform other actions
        return jsonify({'message': f'Welcome, user {user_id}!'}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

@app.route('/logout')
def logout():
    session.pop('token', None)
    return jsonify({'message': 'Logout successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
