from flask import Flask, jsonify, request, session, redirect, url_for
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


# Define a function to check the token before each request
@app.before_request
def check_token():
    # Skip token validation for the login and logout routes
    if request.path in ['/login', '/logout']:
        return

    token = session.get('token')

    if not token:
        return redirect(url_for('login'))

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = data['user_id']
        # TODO: use the user ID to fetch data from the database or perform other actions
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.InvalidTokenError:
        return redirect(url_for('login'))


# Define the login and protected routes
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
    return jsonify({'message': 'You are logged in!'}), 200


@app.route('/logout')
def logout():
    session.pop('token', None)
    return jsonify({'message': 'Logout successful'}), 200


if __name__ == '__main__':
    app.run(debug=True)
