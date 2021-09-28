from db_session import create_session
from models.user import User

from sqlalchemy.orm import Session
from typing import Optional

from config import PATH_TO_ROOT
from exceptions import *


def get_user_by_email(email: str, session: Optional[Session] = None) -> User:
    if session is None:
        session = create_session()
    user = session.query(User).filter(User.email == email).first()
    return user


def add_user(email, password, session: Optional[Session] = None) -> int:
    if session is None:
        session = create_session()
    user = User()
    user.email = email
    user.password = password
    session.add(user)
    session.commit()
    return user.id
