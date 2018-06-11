from sqlalchemy import Column, Integer, String
from app.models.base import Base
class Book(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String(60),nullable=False)
    author=Column(String(30),default='佚名')
    binding=Column(String(20))
    publisher=Column(String(50))
    print=Column(String(20))
    page=Column(Integer)
    pubdate=Column(String(20))
    isbn=Column(String(15),unique=True,nullable=False)
    summary=Column(String(1000))
    image=Column(String(100))
    def sapple(self):
        pass