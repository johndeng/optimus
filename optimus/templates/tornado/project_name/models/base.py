# coding: utf-8

import logging

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from {{ project_name }} import settings

models_logger = logging.getLogger("{{ project_name }}.models")

database_uri = URL(
    drivername='mysql',
    username=settings.DATABASE_USER,
    password=settings.DATABASE_PW,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    database=settings.DATABASE_NAME,
    query={"charset": 'utf8'}
)

engine = create_engine(database_uri)

Base = declarative_base()
Session = sessionmaker(autocommit=True, autoflush=True, bind=engine)


class Sessionized(object):
    """
    Interface class for wrapping up the "session" in the SQLAlchemy required
    for all database communication. This allows subclasses to have a "query"
    and "commit" method that doesn't require managing of the session by hand.
    """

    session = Session()

    @classmethod
    def _new(cls, *args, **kwargs):
        """ Just like __init__, except the new object is committed to the
            db before being returned.
        """
        obj = cls(*args, **kwargs)
        obj._commit()
        return obj

    def _commit(self):
        """ Commits current object to the database.
        """
        with self.session.begin():
            self.session.add(self)

    def _delete(self):
        """ Deletes current object from the database.
        """
        with self.session.begin():
            self.session.delete(self)

    @classmethod
    def query(cls, **kwargs):
        """ For example, you want to query a user by email:

            ```
                user = User.query(email=email).first()
            ```
        """

        q = cls.session.query(cls)

        if kwargs:
            q = q.filter_by(**kwargs)

        return q

    @classmethod
    def delete(cls, **kwargs):

        try:
            cls.query(**kwargs).first()._delete()
        except:
            pass

    def save(self):

        self._commit()
