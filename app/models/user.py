from flask_login import UserMixin, current_user
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.lib.helper import isIsbnOrKey
from app.models.base import Base
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(Base,UserMixin):
    #__tablename__='user1'
    id=Column(Integer,primary_key=True,autoincrement=True)
    nickname=Column(String(24),nullable=False)
    phone_number=Column(String(18),unique=True)
    _password=Column('password',String(256))
    email=Column(String(50),unique=True,nullable=False)
    confirmed=Column(Boolean,default=False)
    beans=Column(Float,default=0) #鱼豆
    send_counter=Column(Integer,default=0)
    receive_counter=Column(Integer,default=0)
    wx_open_id=Column(String(50))
    wx_name=Column(String(32))
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)
    def check_password(self,raw):
        return check_password_hash(self._password,raw)
    #判断是否可以赠书
    def can_save_to_list(self,isbn):
        # 1.判断isbn格式
        # 2.判断isbn是否存在
        # 3.一个人不能同时赠送多本书(根据launched)
        # 4.用户既不能又在赠送这本书状态下又索要这本书
        if isIsbnOrKey(isbn)!= 'isbn':
            return False

        yushubook=YuShuBook()
        yushubook.isbnSearch(isbn)
        if not yushubook.first:
            return False

        gift=Gift.query.filter_by(uid=current_user.id,isbn=isbn,launched=False).first() #证明这个用户这个书正在赠送
        wish=Wish.query.filter_by(uid=current_user.id,isbn=isbn,launched=False).first() #证明这个用户这个书正在索要
        if not gift and not wish:
            return True
        return False

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))