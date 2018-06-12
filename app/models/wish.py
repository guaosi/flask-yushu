from flask import current_app
from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, func, desc
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    user=relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched=Column(Boolean,default=False)

    @property
    def book(self):
        yushubook=YuShuBook()
        yushubook.isbnSearch(self.isbn)
        return yushubook.first
    @classmethod
    def get_user_wishes(cls,uid):
        wishes=Wish.query.filter_by(uid=uid,launched=False).order_by(desc(Wish.create_time)).all()
        return wishes
    @classmethod
    def get_gift_counts(cls,isbn_list):
        from app.models.gift import Gift
        # 计算出对应isbn图书所赠送的人数
        count_list=db.session.query(func.count(Gift.id),Gift.isbn).filter(Gift.launched==False,Gift.isbn.in_(isbn_list),Gift.status==1).group_by(Gift.isbn).all()
        wish_count=[{'count':res[0],'isbn':res[1]} for res in count_list]
        return wish_count