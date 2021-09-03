from flask import Flask, request, redirect, render_template
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "workout"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)
