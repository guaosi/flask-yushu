from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
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
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status']=1
        return super(Query, self).filter_by(**kwargs)
db=SQLAlchemy(query_class=Query)
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
    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
    def delete(self):
        self.status=0