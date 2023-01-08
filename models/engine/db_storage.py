#!/usr/bin/python3
""" Class DBstorage """
import models
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class DBStorage:
    """ Class DBStorage """
    __engine = None
    __session = None

    def all(self, cls=None):
        if cls and cls in self.mapped_tables().keys():
            return {'{}.{}'.format(type(st).__name__, st.id): st
                    for st in self.__session.query(cls)
                    if
                    type(st) == cls}
        objects = {}
        for clss in self.mapped_tables().values():
            for st in self.__session.query(clss):
                objects['{}.{}'.format(type(st).__name__, st.id)] = st
        return objects

    def mapped_tables(self):
        """
                returns all classes and their references
                :return:
                """
        from models.user import User
        from models.city import City
        from models.review import Review
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        return {
                "User": User,
                "State": State,
                "City": City,
                "Place": Place,
                "Review": Review,
                "Amenity": Amenity

                }

    def classes(self):
        """
        returns all classes and their references
        :return:
        """
        from models.base_model import BaseModel
        from models.base_model import Base
        from models.user import User
        from models.city import City
        from models.review import Review
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        return {"BaseModel": BaseModel, "User": User,
                "State": State, "City": City,
                "Place": Place, "Review": Review,
                "Amenity": Amenity,
                'Base': Base
                }

    def __init__(self):
        """ init """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user,
                                              password,
                                              host,
                                              database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            self.allClass()['Base'].metadata.drop_all(self.__engine)

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload """
        from models.base_model import BaseModel
        from models.base_model import Base
        from models.user import User
        from models.city import City
        from models.review import Review
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
        self.__engine.execute("set foreign_key_checks = 0")

    def close(self):
        """remove on the private session attribute
        """
        self.__session.close()
