# 初始化app
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from app.models.base import db
# 初始化Loginmanager
login_manager = LoginManager()
mail=Mail()
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 注册flask-login
    login_manager.init_app(app)
    login_manager.login_view='web.login'
    login_manager.login_message='请先进行登陆'
    # 邮件注册
    mail.init_app(app)
    # 注册蓝图
    register_blueprint(app)
    # 注册SQLAlchemy
    db.init_app(app)
    # with app.app_context()
    db.create_all(app=app)
    return app

# 注册蓝图
def register_blueprint(app):
    # 注册book里web的蓝图
    from app.web import web
    app.register_blueprint(web)
def test():
    pass