"""
Database Utility
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import DATABASE as _database


def get_connection():
    """
    get database connection based on setting
    :return:
    """
    db_string = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        _database['username'], _database['password'],
        _database['db'], _database['db_name']
    )
    try:
        return create_engine(db_string)

    except:
        return False


def get_session():
    """
    generate db session
    :return:
    """
    engine = get_connection()
    if engine:
        return sessionmaker(bind=engine)()


def create_table():
    """
    Create database tables
    :return:
    """

    from temp_tracker.models import BASE
    BASE.metadata.create_all(get_connection())
