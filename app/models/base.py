from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger
class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try: #开启事务
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
db=SQLAlchemy()
class Base(db.Model):
    __abstract__=True
    create_time=Column(Integer)
    status=Column(SmallInteger,default=1)
    def set_attr(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
                setattr(self,key,value)
    def __init__(self):
        self.create_time=int(datetime.now().timestamp())