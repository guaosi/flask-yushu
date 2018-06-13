from flask import current_app, render_template
from flask_mail import Message

from app import mail


def send_mail(to,subject,template,**kwargs):
    # msg=Message('测试邮件',sender='guaosi@vip.qq.com',body='test',recipients=['624249423@qq.com'])
    msg=Message(current_app.config['MAIL_SUBJECT_PREFIX']+' '+subject,sender=current_app.config['MAIL_USERNAME'],recipients=[to])
    msg.html=render_template(template,**kwargs)
    mail.send(msg)