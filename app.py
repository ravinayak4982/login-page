from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__)

# Simulated database of user information (username, hashed password)
users = {
    "user1": "5f4dcc3b5aa765d61d8327deb882cf99",  # 'password' hashed with MD5
    # Add more users here
}

def hash_password(password):
    # Hash the password using a secure hash function like SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == hash_password(password):
        return "Login successful!"
    else:
        return "Login failed. Please check your username and password."

if __name__ == '__main__':
    app.run(debug=True)
