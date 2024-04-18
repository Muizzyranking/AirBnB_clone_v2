#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

user = getenv('HBNB_MYSQL_USER')
pwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new instance of DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        temp = {}
        table = [User, Place, State, City, Amenity, Review]
        if cls is not None:
            for key, val in self.__session.query(classes[cls]).all():
                temp[key] = val
        else:
            for clss in table:
                for key, val in self.__session.query(clss).all():
                    temp[key] = val
        return temp

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scope = scoped_session(Session)
        self.__session = Scope()
