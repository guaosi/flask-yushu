from flask import current_app
from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, desc, func
from sqlalchemy.orm import relationship
from app.models.base import Base, db

from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    user=relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    #book=relationship('Book')
    #bid=Column(Integer,ForeignKey('book.id'))
    launched=Column(Boolean,default=False)
    @property
    def book(self):
        yushubook=YuShuBook()
        yushubook.isbnSearch(self.isbn)
        return yushubook.first
    @classmethod
    def recent(cls):
        gifts=Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(desc(Gift.create_time)).distinct().limit(current_app.config['RECENT_BOOK_COUNT']).all()
        return gifts
    @classmethod
    def get_user_gifts(cls,uid):
        gifts=Gift.query.filter_by(uid=uid,launched=False).order_by(desc(Gift.create_time)).all()
        return gifts
    @classmethod
    def get_wish_counts(cls,isbn_list):
        from app.models.wish import Wish
        # 计算出对应isbn图书所索要的人数
        count_list=db.session.query(func.count(Wish.id),Wish.isbn).filter(Wish.launched==False,Wish.isbn.in_(isbn_list),Wish.status==1).group_by(Wish.isbn).all()
        wish_count=[{'count':res[0],'isbn':res[1]} for res in count_list]
        return wish_count
    def is_myself_gift(self,uid):
        return True if uid==self.uid else False