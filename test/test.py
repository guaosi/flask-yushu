from flask import Flask, current_app

app=Flask(__name__)
app.config.from_object('app.secure')
with app.app_context():
    a=current_app
    config=a.config['HOST']
print(config)
# ctx=app.app_context()
# ctx.push()
# a=current_app
# config=a.config['HOST']
# ctx.pop()
class A():
    def __enter__(self):
        a=1
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else :
            print('no exception')
        a=2
        return False
try:
    with A() as a:
        b=2
        1/0
except Exception as ex:
    pass

