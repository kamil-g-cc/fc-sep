import data
import bcrypt
from flask import Flask, session, redirect, render_template, url_for, request

# put your code here

app = Flask(__name__)
app.secret_key = b'$2b$12$Irdd6Ahm4DEcnmKlkvpnceJLIHZ6IxXxW6KUyquUvyvS3IVTiaRae'

LOGIN_EMAIL = 'gggaaa12345@wp.pl'
HASH_PW = b'$2b$12$hcQZVUIYaImyxGF8oiUXEO3oqGxh8//XSSkKncOm17IoFO8fu0pbe'


@app.route('/')
def index():
    session['first_time'] = 'yes'
    user_name = ''
    if 'user_name' in session:
        user_name = session['user_name']
    return render_template("index.html", user_name=user_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_data = dict(request.form)

        if login_data["email"] == LOGIN_EMAIL:
            if bcrypt.checkpw(login_data["password"].encode('utf-8'), HASH_PW):
                session['user_name'] = LOGIN_EMAIL
                return redirect(url_for("index"))
        return render_template('login.html', bad_login=True)

    elif request.method == 'GET':
        return render_template("login.html")


if __name__ == '__main__':
    app.run()
