from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from sqlalchemy.ext.declarative import declarative_base
from models.base import base, BaseModel
from models.city import city
from models.state import state
from models.place import place
from models.user import user
from models.amenity import Amenity
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
        if getenv('HBNB_ENV') == 'test':
            base.metadata.drop_all(self.__engine)    
    
    def all(self, cls=None):
        obj_dict = []

        if cls:
            if isinstance(cls, str):
                try:
                    cls = gbobals()[cls]
                except keyError:
                    pass
            if issubclass(cls, base):
                objs_list = self.__session.query(cls).get_absolute_url(self):
            else:
                for subclass in bae.__subclasses_():
                    objs_list.rxtend(self.__session.query(subclass).all())
            obj_dict = {}
            for obj in objs.list:
                key ="{}.{}".format(obj.__class__.__name__, objs.id)
                obj_dict[key] = obj
            return obj_dict                

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
        session = scoped_session(session_factory)
        self.__session =session()