from flask_login import current_user
from sqlalchemy import Column, Integer, String, SmallInteger

from app.lib.enums import PendingStatus
from app.models.base import Base, db
from app.view_models.book import BookViewModel


class Drift(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
    # 邮寄信息
    recipient_name=Column(String(20),nullable=False)
    address=Column(String(100),nullable=False)
    message=Column(String(200))
    mobile=Column(String(20),nullable=False)

    # 书籍信息
    isbn=Column(String(13))
    book_title=Column(String(50))
    book_author=Column(String(30))
    book_img=Column(String(50))

    # 请求者信息
    requester_id=Column(Integer)
    requester_name=Column(String(20))

    # 赠送者信息
    gifter_id=Column(Integer)
    gift_id=Column(Integer)
    gifter_name=Column(String(20))

    #状态
    _pending=Column('pending',SmallInteger,default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)
    @pending.setter
    def pending(self,status):
        self._pending=status.value

    def save_to_drift(self,drift_form,current_gift,current_user_id,current_user_nickname):
        with db.auto_commit():
            #将验证中有的字段快速填充到对象实例相同的字段
            drift_form.populate_obj(self)
            self.gift_id=current_gift.id
            self.requester_id=current_user_id
            self.requester_name=current_user_nickname
            self.gifter_id=current_gift.uid
            book=BookViewModel(current_gift.book)
            self.book_title=book.title
            self.book_author=book.author
            self.book_img=book.image
            self.isbn=book.isbn
            self.gifter_name=current_gift.user.nickname
            current_user.beans-=1
            db.session.add(self)
