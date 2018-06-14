from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.models.base import db
from app.models.wish import Wish
from app.view_models.trade import MyTrades
from . import web


@web.route('/my/wish')
@login_required
def my_wish():
    uid=current_user.id
    wish_of_mine=Wish.get_user_wishes(uid)
    isbn_list=[wish.isbn for wish in wish_of_mine]
    gift_count=Wish.get_gift_counts(isbn_list)
    viewmodel=MyTrades(wish_of_mine,gift_count)
    return render_template('my_wish.html',wishes=viewmodel.trades)
@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish=Wish()
            wish.uid=current_user.id
            wish.isbn=isbn
            db.session.add(wish)
            flash('书籍加入心愿成功~')
    else:
        flash('这本书已经添加到你的赠送清单或者已经存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))

@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    wish=Wish.query.filter_by(uid=current_user.id,isbn=isbn,launched=False).first_or_404()
    with db.auto_commit():
        wish.delete()
        flash('您已经成功撤销礼物的心愿')
    return redirect(url_for('web.my_wish'))
