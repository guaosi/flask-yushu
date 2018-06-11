# 初始化app
from flask import Flask
from app.models.base import db
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
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