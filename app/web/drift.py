from flask import flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import or_, desc

from app.forms.drift import DriftForm
from app.lib.email import send_mail
from app.models.drift import Drift
from app.models.gift import Gift
from app.view_models.user import UsersSummary
from . import web

@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    # 发起索要图书请求
    # 1.检查是不是自己的
    # 2.检查鱼豆是否大于1
    # 3.是否满足，成功索要两本书,必须成功送出一本书
    gift=Gift.query.get_or_404(gid)
    if gift.is_myself_gift(current_user.id):
        flash('这本书是你自己的^_^, 不能向自己索要书籍噢')
    if not current_user.can_send_drift():
        return render_template('not_enough_beans.html',beans=current_user.beans)
    wtform = DriftForm(request.form)
    # 步入正文
    if request.method=='POST' and wtform.validate():
        drift=Drift()
        drift.save_to_drift(wtform,gift)
        send_mail(gift.user.email,'有人想要您上传的图书: '+gift.book['title'],'email/get_gift.html',wisher=current_user,gift=gift)
        return redirect(url_for('web.pending'))
    viewmodel=UsersSummary(current_user)
    return render_template('drift.html',gifter=viewmodel.first,user_beans=current_user.beans,form=wtform)
@web.route('/pending')
def pending():
    drifts=Drift.query.filter(or_(Drift.requester_id==current_user.id,Drift.gifter_id==current_user.id),Drift.status==1).order_by(desc(Drift.create_time)).all()
    pass

@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
