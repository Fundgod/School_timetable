import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import Session
from typing import List, Optional
import sys

sys.path.append("..")

from db_session import SqlAlchemyBase, create_session


class Tablet(SqlAlchemyBase):
    __tablename__ = "menus"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    classes = sqlalchemy.Column(sqlalchemy.String)
