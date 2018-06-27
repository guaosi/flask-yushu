from flask import render_template

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web
from app.lib.Tests import n
@web.route('/')
def index():
    recent_gifts=Gift.recent()
    books=[BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html',recent=books)

@web.route('/personal')
def personal_center():
    return '这里是个人中心'
@web.route('/test')
def test():
    n.v=n.v+2
    return str(n.v)