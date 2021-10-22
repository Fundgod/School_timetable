from db_session import create_session
from models.user import User
from models.tablet import Tablet

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


def create_new_menu():  # Создание нового пустого меню
    session = create_session()
    tablet_to_view = Tablet()
    session.add(tablet_to_view)
    session.commit()
    return tablet_to_view.id


def delete_menu_util(menu_id):  # Удаление выбранного меню
    session = create_session()
    session.query(Tablet).filter_by(id=menu_id).delete()
    session.commit()
    return True


def get_classes(menu, session):  # Достаём Классы из расписания
    return []  # {'%ClassName': [lesson1, lesson2, , , , lesson6, lesson7]}


def get_days_from_class(class_name, session):  # Достаём расписание каждого класса для
    return True


def get_all_info_to_main():
    session = create_session()
    tablets = session.query(Tablet).all()
    json_data = {'menus_amount': len(tablets)}
    for menu in tablets:
        json_data[menu.id] = []  # Массив классов в меню
        classes = get_classes(menu, session)  # Классы в меню
        for i in classes:
            json_data[menu.id].append(get_days_from_class(i, session))  # Массив словарей в меню
        pass
    return json_data
