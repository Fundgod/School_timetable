import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
import logging


SqlAlchemyBase = dec.declarative_base()

__factory = None


def db_session_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f"sqlite:///{db_file.strip()}?check_same_thread=False"
    logging.info(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str)
    __factory = orm.sessionmaker(bind=engine)

    # from models import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()