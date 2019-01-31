#!/usr/bin/python3
"""
Module for DB storage
"""
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """
    Class DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of a new DBStorage instance"""
        usr = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, db),
            pool_pre_ping=True)
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query the current db for all objects
           Args:
               cls: Class name of the object to be queried
        """
        if cls is None:
            classes = ['State', 'City', 'Place', 'Amenity', 'User', 'Review']

            results = []
            for cls in classes:
                query_rows = self.__session.query(eval("{}".format(cls))).all()
                for element in query_rows:
                    results.append(element)

        else:
            results = self.__session.query(eval("{}".format(cls))).all()

        dictionary = {}
        for element in results:
            ele_class = element.to_dict()['__class__']
            key = ele_class + '.' + str(element.id)
            dictionary[key] = element
        return dictionary

    def new(self, obj):
        """Add new object to the current db session
            Args:
                obj: object to be added
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the db session
        Args:
            obj: obj to be deleted, None by default
        """
        self.__session.delete(obj)

    def reload(self):
        """Create all tables in db and create the db session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ closes the current session """
        self.__session.remove()
