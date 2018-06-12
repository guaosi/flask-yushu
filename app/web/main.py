from . import web
@web.route('/')
def index():
    return 'this is index'


@web.route('/personal')
def personal_center():
    pass
