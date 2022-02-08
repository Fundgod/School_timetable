from flask import Flask, render_template
from flask_login import LoginManager, login_required
from datetime import timedelta

from utils import create_new_menu, delete_menu_util, get_all_info_to_main

from config import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "workout"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)


@app.errorhandler(404)
def error_404(error):
    return render_template("404.html")


@app.route("/")
def main_menu():

    return render_template("main.html")


@app.route("/js/add_menu", methods=['GET'])
@login_required
def add_menu():
    temp_id = create_new_menu()
    return str(temp_id)


@app.route("/js/delete_menu/<menu_id>", methods=['GET'])
@login_required
def delete_menu(menu_id):
    if delete_menu_util(menu_id):
        return 'Yes'
    return 'No'


def main():
    app.run(host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
