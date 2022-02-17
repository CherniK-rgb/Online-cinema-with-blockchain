from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from application import db
from models import Message, User


@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")


@app.route('/catalog')
@login_required
def catalog():
    return render_template("Catalog.html")


@app.route('/news')
@login_required

def news():
    return render_template("News.html")


@app.route('/pages')
@login_required

def pages():
    return render_template("Pages.html")


@app.route('/about')
def about():
    return render_template("About.html")


@app.route('/posts', methods=['POST', 'GET'])
def posts():
    users= User.query.orser_by(User.login).all()
    return render_template("posts.html", users=users)


@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        useres = Useres(title=title, intro=intro, text=text)

        try:
            db.session.add(useres)
            db.session.commit()
            return redirect('/home')
        except:
            return "Произошла ошибка при создании статьи"
    else :
        return render_template("User.html")


@app.route('/admin')
def admin():
    return render_template("Admin.html")


@app.route('/main1', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
@login_required
def main():
    return render_template('main.html', messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
@login_required
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    db.session.add(Message(text, tag))
    db.session.commit()

    return redirect(url_for('main'))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            return redirect(next_page)
        else:
            flash('Login or password is not correct')
    else:
        flash('Please fill login and password fields')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please, fill all fields!')
        elif password != password2:
            flash('Passwords are not equal!')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))

    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('hello_world'))


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response