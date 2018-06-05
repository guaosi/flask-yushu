from flask import jsonify, request
from app.forms.book import SearchForm
from helper import isIsbnOrKey
from yushu_book import YuShuBook
from . import web
@web.route('/book/search')
def search():
    wtforms=SearchForm(request.args) #传入所有参数,会自动分配验证
    if wtforms.validate():  #开始进行验证，并且返回布尔值
        q=wtforms.q.data.strip() #从验证中获取数据
        page=wtforms.page.data
        is_isbn_or_key = isIsbnOrKey(q)
        if is_isbn_or_key == 'isbn':
            result = YuShuBook.isbnSearch(q)
        if is_isbn_or_key == 'key':
            result = YuShuBook.keySearch(q)
        return jsonify(result)  # 将dict转为json输出
    else:
        return jsonify(wtforms.errors) #返回所有错误信息
