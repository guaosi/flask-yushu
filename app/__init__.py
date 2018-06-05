# 初始化app
from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 注册蓝图
    register_blueprint(app)
    return app
# 注册蓝图
def register_blueprint(app):
    # 注册book里web的蓝图
    from app.web import web
    print(id(web))
    app.register_blueprint(web)