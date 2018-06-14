from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.lib.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.view_models.trade import MyTrades
from . import web


@web.route('/my/gifts')
@login_required
def my_gifts():
    gifts_of_mine=Gift.get_user_gifts(current_user.id)
    isbn_list=[gift.isbn for gift in gifts_of_mine]
    wish_list=Gift.get_wish_counts(isbn_list)
    viewmodel=MyTrades(gifts_of_mine,wish_list)
    return render_template('my_gifts.html',gifts=viewmodel.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift=Gift()
            gift.uid=current_user.id
            gift.isbn=isbn
            current_user.beans+=current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            flash('书籍赠送成功~')
    else:
        flash('这本书已经添加到你的赠送清单或者已经存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail',isbn=isbn))
@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    gift=Gift.query.filter_by(id=gid,uid=current_user.id,launched=False).first_or_404()
    drift=Drift.query.filter_by(isbn=gift.isbn,gift_id=gid,gifter_id=current_user.id,_pending=PendingStatus.Waiting.value).first()

    if drift:
        flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    else :
        with db.auto_commit():
            current_user.beans-=current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.delete()
            flash('您已经成功撤销书籍: 《'+gift.book['title']+'》的赠送')
    return redirect(url_for('web.my_gifts'))