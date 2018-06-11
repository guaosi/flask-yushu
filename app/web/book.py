import json
from flask import jsonify, request, current_app, render_template, flash
from app.forms.book import SearchForm
from app.lib.helper import isIsbnOrKey
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from . import web
@web.route('/tests')
def test():
    r1={
        'name':'张三',
        'age':18
    }
    r2=10
    flash('this is the first message',category='error')
    flash('this is the second message',category='warn')
    return render_template('test2.html',data1=r1,r2=r2)
@web.route('/book/search')
def search():
    wtforms=SearchForm(request.args) #传入所有参数,会自动分配验证
    book = BookCollection()
    if wtforms.validate():  #开始进行验证，并且返回布尔值
        q=wtforms.q.data.strip() #从验证中获取数据
        page=wtforms.page.data

        is_isbn_or_key = isIsbnOrKey(q)
        yushuBook=YuShuBook()

        if is_isbn_or_key == 'isbn':
            yushuBook.isbnSearch(q)
        if is_isbn_or_key == 'key':
            yushuBook.keySearch(q,page)

        book.fill(yushuBook,q)
        # return json.dumps(book,default=lambda obj:obj.__dict__)
    else:
        flash('关键字错误，请重新输入关键字')
        # return jsonify(wtforms.errors) #返回所有错误信息
    return render_template('search_result.html',books=book)
@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushubook=YuShuBook()
    yushubook.isbnSearch(isbn)
    book=BookViewModel(yushubook.first)
    return render_template('book_detail.html',book=book,gifts=[],wishes=[])
