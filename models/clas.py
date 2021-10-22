import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import Session
from typing import List, Optional
import sys

sys.path.append("..")

from db_session import SqlAlchemyBase, create_session


class Clas(SqlAlchemyBase):
    __tablename__ = "clas"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    day_1 = sqlalchemy.Column(sqlalchemy.String)
    day_2 = sqlalchemy.Column(sqlalchemy.String)
    day_3 = sqlalchemy.Column(sqlalchemy.String)
    day_4 = sqlalchemy.Column(sqlalchemy.String)
    day_5 = sqlalchemy.Column(sqlalchemy.String)
    day_6 = sqlalchemy.Column(sqlalchemy.String)
    # Надо сделать функцию для записи и прочтения уроков

    """def get_members(self, session: Optional[Session] = None) -> List[User]:
        if session is None:
            session = create_session()
        members = set(map(int, self.members.split(';')))
        return session.query(User).filter(User.id.in_(members)).all()"""
