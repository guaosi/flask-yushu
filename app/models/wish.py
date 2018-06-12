from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship
from app.models.base import Base
class Wish(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    user=relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched=Column(Boolean,default=False)