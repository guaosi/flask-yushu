from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.lib.email import send_mail
from app.models.base import db
from app.models.user import User
from . import web

@web.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('web.index'))
    wtform = RegisterForm(request.form)
    if request.method=='POST' and wtform.validate():
        with db.auto_commit():
            user=User()
            user.set_attr(wtform.data)
            # user.nickname=wtform.nickname.data
            # user.email=wtform.email.data
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html',form=wtform)


@web.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('web.index'))
    wtform=LoginForm(request.form)
    if request.method=='POST' and wtform.validate():
        user=User.query.filter_by(email=wtform.email.data).first()
        if user and user.check_password(wtform.password.data):
            login_user(user)
            url=request.args.get('next')
            if not url or not url.startswith('/'):
                url=url_for('web.index')
            return redirect(url)
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html',form=wtform)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    wtform=EmailForm(request.form)
    if request.method=='POST' and wtform.validate():
        user=User.query.filter_by(email=wtform.email.data).first_or_404()
        send_mail(wtform.email.data,'重置密码','email/reset_password.html',user=user,token=user.generate_token())
        return render_template('email_has_send.html')
    return render_template('auth/forget_password_request.html',form=wtform)

@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    wtform=ResetPasswordForm(request.form)
    if request.method=='POST' and wtform.validate():
        if User.reset_password(token,wtform.password1.data):
            flash('你的密码已经更新，请重新登陆')
            return redirect(url_for('web.login'))
        else:
            flash('密码重置失败')
    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))
