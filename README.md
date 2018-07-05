Python+Flask 制作公益赠书平台-鱼书
===============

>  ~~🚀 暂时只能用于本地学习使用,未使用uWSGI待后面上线再更新补充~~

> 🚀 部署上线参考flask-movie  https://github.com/guaosi/flask-movie

> 🚀 留坑，过段时间下个分支将会补充API部分和小程序

## 特性

- 蓝图注册视图函数

- WTForms参数验证

- 编写viewModel处理原始数据

- Jinja2模板引擎

- 基于SQLAlchemy的CRUD

- 使用with的上下文特性自动开启事务

- flask-login处理登陆逻辑

- 使用多线程异步发送邮件

- 简单，开箱即用


> Python的运行环境要求3.6以上。


## 要求

| 依赖 | 说明 |
| -------- | -------- |
| Python| `>= 3.6` |
| Flask| `>= 1.0.2` |
| cymysql| `>= 0.9.10` |
| Flask-Login |`>= 0.4.1`|
| Flask-Mail |`>= 0.9.1`|
| Flask-SQLAlchemy  |`>= 2.3.2`|
| itsdangerous |`>= 0.24`|
| Jinja2 |`>= 2.10`|
| requests |`>= 2.18.4`|
| SQLAlchemy  |`>= 1.2.8`|
| urllib3 |`>= 1.22`|
| Werkzeug |`>= 0.14.1`|
| WTForms |`>= 2.2`|


## 注意

1. 数据库在运行fisher.py自动生成,请手动将每个数据表的引擎改为Innodb,默认为MyISAM,无事务功能。

2. 需要在app目录下创建secure.py文件。

3. **flask扩展需要自行安装**

4. ~~没有加入uWSCI,暂时最好只在本地学习使用~~

> 部署上线参考flask-movie  https://github.com/guaosi/flask-movie

5. API部分下个分支会加入

## 安装

1. 通过[Github](https://github.com/guaosi/flask-yushu),fork到自己的项目下
```
git clone git@github.com:<你的用户名>/flask-yushu.git
```
2. 在app目录下创建secure.py文件
```
DEBUG=True  #是否开启Dubug
HOST='0.0.0.0' #0.0.0.0表示访问权限为全网
PORT=80 #访问端口号

# mysql连接，比如 SQLALCHEMY_DATABASE_URI='mysql+cymysql://root:root@localhost:3306/fisher'
SQLALCHEMY_DATABASE_URI='mysql+cymysql://用户名:用户名@ip地址:mysql端口号/数据库名'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

# 设置key，比如 SECRET_KEY='guaosi'
SECRET_KEY=''
# Email 配置
MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'admin@guaosi.com'
MAIL_PASSWORD = '' #密码
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <admin@guaosi.com>'
```

## 相关依赖
最好在pipenv的虚拟环境中安装，避免全局污染
- flask
```
pipenv install flask
```
- requests
```
pip install requests
```
- WTforms
```
pip install wtforms
```
- SQLALChemy
```
pipenv install flask-sqlalchemy
```
- Jinja2
```
pip install Jinja2
```
- flask-login
```
pipenv install flask-login
```
- flask-mail
```
pipenv install flask-mail
```
## 运行
> `python fisher.py`

## 在项目中使用事务
已经使用with和yield对事务做了上下文处理，当进行数据库处理时，请在with下操作，发生错误时自动回滚
```
with db.auto_commit():
    # orm逻辑
    db.session.add(模型实例)
```

## 在项目中使用filter_by
已经重写filter_by方法，默认加入条件 status=1.
```
Gift.query.filter_by(id=gid).first_or_404()
#相当于
Gift.query.filter_by(id=gid,status=1).first_or_404()
```

## 在项目中构建ViewModel
推荐在渲染模板之前，创建ViewModel文件,将原始数据进行处理,具体参考 app/view_models/book.py 文件

## 在项目中发送邮件
直接调用发送邮件方法，已经默认多线程异步发送邮件
```
send_mail() #直接调用即可多线程异步发送邮件
```