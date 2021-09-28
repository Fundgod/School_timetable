from flask import Flask, request, redirect, render_template
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from datetime import timedelta

from utils import get_user_by_email, add_user

from forms import *
from db_session import db_session_init, create_session
from models.user import User
from config import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "workout"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)


db_session_init(PATH_TO_DB)

login_manager = LoginManager()
login_manager.init_app(app)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")


@login_manager.user_loader
def load_user(user_id):
    return create_session().query(User).get(user_id)


@app.errorhandler(404)
def error_404(error):
    return render_template("404.html")


@app.route("/")
def start_menu():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def authorization():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template("login.html", message="Неправильный логин или пароль", form=form)
    return render_template("login.html", form=form)


@app.route("/register/", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = create_session()
        if get_user_by_email(form.email.data, session=db_sess):
            return render_template(
                "register.html",
                form=form,
                message="Пользователь с таким адресом электронной почты уже зарегистрирован"
            )
        add_user(form.email.data, form.password.data, db_sess)
        return render_template("registered_successfully.html")
    return render_template("register.html", form=form)


def main():
    app.run(host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
