import sqlalchemy
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from typing import Dict
import sys

sys.path.append("..")

from db_session import SqlAlchemyBase
from exceptions import NotFoundError


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)

    # def set_password(self, password):
    #    self.password = generate_password_hash(password)

    # def check_password(self, password):
    #     return
