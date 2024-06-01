# 0x03. User authentication service

##  1. Declaring API Routes in Flask App
### 1.1. Define Routes

In your Flask application, define routes for user authentication endpoints. These routes typically include:

    /signup: For user registration
    /login: For user login
    /logout: For user logout
    /profile: For accessing user profile information
    /reset_password: For resetting user password

### 1.2. Route Handlers

Each route should have a corresponding function (route handler) that executes the required authentication logic and returns an appropriate response.

### 1.3. Example
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    # Signup logic
    return jsonify({'message': 'User signed up successfully'}), 201

# Define other routes similarly

if __name__ == '__main__':
    app.run(debug=True)


##  2. Getting and Setting Cookies
### 2.1. Setting Cookies

You can set cookies in Flask using the set_cookie method of the Response object.

### 2.2. Getting Cookies

To retrieve cookies in Flask, you can use the request.cookies dictionary.

### 2.3. Example
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response('Setting Cookie')
    resp.set_cookie('username', 'john')
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('username')
    return 'Welcome ' + name

if __name__ == '__main__':
    app.run(debug=True)

##  3. Retrieving Request Form Data
### 3.1. Accessing Form Data

In Flask, you can access form data submitted via POST requests using the request.form dictionary.

### 3.2. Example

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Authenticate user with provided credentials
    return 'Login successful'

if __name__ == '__main__':
    app.run(debug=True)

User Authentication Service README

Welcome to the User Authentication Service README. This document serves as a guide for developers to understand the implementation of user authentication features in a Flask web application. Below are the instructions covering various aspects of API routes declaration, cookie management, request form data retrieval, and HTTP status code handling.
1. Declaring API Routes in Flask App
1.1. Define Routes

In your Flask application, define routes for user authentication endpoints. These routes typically include:

    /signup: For user registration
    /login: For user login
    /logout: For user logout
    /profile: For accessing user profile information
    /reset_password: For resetting user password

1.2. Route Handlers

Each route should have a corresponding function (route handler) that executes the required authentication logic and returns an appropriate response.
1.3. Example

python

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    # Signup logic
    return jsonify({'message': 'User signed up successfully'}), 201

# Define other routes similarly

if __name__ == '__main__':
    app.run(debug=True)

2. Getting and Setting Cookies
2.1. Setting Cookies

You can set cookies in Flask using the set_cookie method of the Response object.
2.2. Getting Cookies

To retrieve cookies in Flask, you can use the request.cookies dictionary.
2.3. Example

python

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response('Setting Cookie')
    resp.set_cookie('username', 'john')
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('username')
    return 'Welcome ' + name

if __name__ == '__main__':
    app.run(debug=True)

3. Retrieving Request Form Data
3.1. Accessing Form Data

In Flask, you can access form data submitted via POST requests using the request.form dictionary.
3.2. Example

python

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Authenticate user with provided credentials
    return 'Login successful'

if __name__ == '__main__':
    app.run(debug=True)

##  4. Returning Various HTTP Status Codes
### 4.1. HTTP Status Codes

Flask provides various methods to return different HTTP status codes along with the response.

### 4.2. Example
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/profile')
def profile():
    user_data = {'username': 'user123', 'email': 'user@example.com'}
    if user_data:
        return jsonify(user_data), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

