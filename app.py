import bcrypt

import data
from flask import Flask, session, url_for, render_template, request

# put your code here

app = Flask(__name__)
app.secret_key = bcrypt.gensalt()


LOGIN_EMAIL = 'kaszczak.jaroslaw@outlook.com'
PASSWORD = 'qwerty'


@app.route('/')
def index():
    session['first_time'] = 'tak'
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print(email)
        print(password)

    return render_template('login_form.html')


if __name__ == '__app__':
    app.run()
