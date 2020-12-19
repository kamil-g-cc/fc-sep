import data
import bcrypt
from flask import Flask, session, redirect, render_template, url_for, request, make_response

# put your code here

app = Flask(__name__)
app.secret_key = b'$2b$12$Irdd6Ahm4DEcnmKlkvpnceJLIHZ6IxXxW6KUyquUvyvS3IVTiaRae'

LOGIN_EMAIL = 'kaszczak.jaroslaw@outlook.com'
HASH_PW = b'$2b$12$s8Qmmgn4m6eDXuq1KTdgI.Y2yF6kfoXKBl9xk0C6Bj7Z7FxSTkEsG'


@app.route('/')
def index():
    user_name = ''
    is_pierwszy_raz = request.cookies.get('pierwszy_raz')
    is_drugi_raz = request.cookies.get('drugi_raz')
    if is_pierwszy_raz == "moje pierwsze ciasteczko ever!":
        print("bylem tutaj, tonny halik")
    if is_drugi_raz:
        print("drugi", is_drugi_raz)

    resp = make_response(render_template("index.html", user_name=user_name))
    resp.set_cookie(key='drugi_raz', value='moje pierwsze ciasteczko ever!', max_age=5)
    if 'user_name' in session:
        user_name = session['user_name']
    return resp


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == LOGIN_EMAIL:
            if bcrypt.checkpw(password.encode('UTF-8'), HASH_PW):
                session['user_name'] = LOGIN_EMAIL
                return redirect(url_for('index'))
            else:
                return render_template('login_form.html', bad_login=True)

    elif request.method == 'GET':
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('user_name')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()
