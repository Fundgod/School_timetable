from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo

from validators import *


class LoginForm(FlaskForm):
	email = EmailField("Почта", validators=[DataRequired(message="Заполните это поле!")])
	password = PasswordField("Пароль", validators=[DataRequired(message="Заполните это поле!")])
	remember_me = BooleanField("Запомнить меня")
	submit = SubmitField("Войти")


class RegisterForm(FlaskForm):
	email = EmailField("Почта", validators=[DataRequired(message="Заполните это поле!")])
	password = PasswordField("Пароль", validators=[DataRequired(message="Заполните это поле!"), PasswordValidator()])
	password_repeat = PasswordField("Повторите пароль", validators=[DataRequired(message="Заполните это поле!"), EqualTo("password", message="Пароли не совпадают")])
	submit = SubmitField("Зарегистрироваться")
