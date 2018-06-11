from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship
from app.models.base import Base
class Gift(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    user=relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    #book=relationship('Book')
    #bid=Column(Integer,ForeignKey('book.id'))
    launched=Column(Boolean,default=False)