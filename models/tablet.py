import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import Session
from typing import List, Optional
import sys

sys.path.append("..")

from db_session import SqlAlchemyBase, create_session


class Tablet(SqlAlchemyBase):
    __tablename__ = "Menu"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    classes_1 = sqlalchemy.Column(sqlalchemy.String)
    rows_num_1 = sqlalchemy.Column(sqlalchemy.Integer)
    classes_2 = sqlalchemy.Column(sqlalchemy.String)
    rows_num_2 = sqlalchemy.Column(sqlalchemy.Integer)

    # Надо сделать функцию для записи и удаления классов
