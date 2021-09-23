from flask import Flask, request, redirect, render_template
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from datetime import timedelta

from db_session import db_session_init
from config import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "workout"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)


# db_session_init(PATH_TO_DB)

# login_manager = LoginManager()
# login_manager.init_app(app)
# unique_codes_manager = UniqueCodesManager()
# unique_codes_manager.generate_unique_codes(10)

@app.errorhandler(404)
def error_404(error):
    return render_template("404.html")


@app.route("/")
def start_menu():
    return render_template("base.html")


def main():
    app.run(host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
