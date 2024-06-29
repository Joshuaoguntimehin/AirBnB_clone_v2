from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        # MySQL connection string
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}',
                                      pool_pre_ping=True)

    
    
    def all(self, cls=None):
        classes = [User, State, City, Amenity, Place, Review]
        obj_dict = {}

        if cls:
            objs =self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dictionary[key] = obj
        else:
            for _class in classes:
                objs = self.__session.query(_class).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dictionary[key] = obj
        return obj_dictionary

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    def reload(self):
        """Create all tables in the database and initialize the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
