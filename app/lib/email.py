from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail

def asyn_send_mail(app,msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass

def send_mail(to,subject,template,**kwargs):
    # msg=Message('测试邮件',sender='guaosi@vip.qq.com',body='test',recipients=['624249423@qq.com'])
    msg=Message(current_app.config['MAIL_SUBJECT_PREFIX']+' '+subject,sender=current_app.config['MAIL_USERNAME'],recipients=[to])
    msg.html=render_template(template,**kwargs)
    app=current_app._get_current_object()
    thread=Thread(target=asyn_send_mail,args=[app,msg])
    thread.start()